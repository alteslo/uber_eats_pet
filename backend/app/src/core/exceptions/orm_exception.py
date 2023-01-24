import sys
import traceback

from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from backend.app.src.core.exceptions.app_exceptions import (AppEcxeptionDB,
                                                            AppException,
                                                            AppExceptionCase)
from backend.app.src.core.exceptions.service_result import ServiceResult


def crud_error_handler(func):
    async def decorator(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except (
            AppEcxeptionDB,
            AppException.UserNotAuthorized,
            AppException.ItemNotExist,
            ValueError,
        ) as error:
            raise error
        except Exception as error:
            _, _, tb = sys.exc_info()
            raise AppEcxeptionDB(
                message=str(error),
                traceback=str(traceback.format_exc()),
            )

    return decorator


def service_error_handler(throw_error_type):
    def wrapper(func):
        async def decorator(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            # except AppException as error:
            except AppExceptionCase as error:
                raise error
            except AppEcxeptionDB as error:
                raise throw_error_type(
                    context={"error": str(error), "traceback": error.traceback}
                )
            except Exception as error:
                raise throw_error_type(
                    context={
                        "error": str(error),
                        "traceback": str(traceback.format_exc()),
                    }
                )

        return decorator

    return wrapper


def route_error_handler(func):
    async def decorator(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except RequestValidationError as error:
            return ServiceResult(
                AppException.RouteError(
                    context={"error": str(error)},
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            )
        except AppException as error:
            return ServiceResult(error)
        except Exception as error:
            return ServiceResult(AppException.RouteError(context={"error": str(error)}))

    return decorator


async def wrap_errors(request, call_next):
    try:
        response = await call_next(request)
    except RequestValidationError as error:
        return error_response(
            AppException.RouteError(
                context={"error": str(error)}, status_code=status.HTTP_400_BAD_REQUEST
            )
        )
    except AppExceptionCase as error:
        return error_response(error)
    except Exception as error:
        return error_response(AppException.RouteError(context={"error": str(error)}))
    return response


def error_response(exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "exception_case": exc.exception_case,
            "message": exc.message,
            "context": exc.context,
        },
    )
