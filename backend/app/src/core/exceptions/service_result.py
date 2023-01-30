import inspect

from fastapi import HTTPException

from backend.app.src.core.exceptions.app_exceptions import (AppExceptionCase,
                                                            get_exception)
from backend.app.src.core.logging.logging import logger


class ServiceResult(object):
    def __init__(self, arg):
        if isinstance(arg, AppExceptionCase):
            self.success = False
            self.exception_case = arg.exception_case
            self.status_code = arg.status_code
        else:
            self.success = True
            self.exception_case = None
            self.status_code = None
        self.value = arg

    def __str__(self):
        if self.success:
            return "[Success]"
        return f'[Exception] "{self.exception_case}"'

    def __repr__(self):
        if self.success:
            return "<ServiceResult Success>"
        return f"<ServiceResult AppException {self.exception_case}>"

    def __enter__(self):
        return self.value

    def __exit__(self, *kwargs):
        pass


async def caller_info() -> str:
    info = inspect.getframeinfo(inspect.stack()[2][0])
    return f"{info.filename}:{info.function}:{info.lineno}"


async def handle_result(result: ServiceResult):
    if not result.success:
        with result as exception:
            error = await caller_info()
            logger.error(f"{exception} | caller={error}")
            raise HTTPException(
                status_code=exception.status_code,
                detail=await get_exception(exception)
            )
    with result as result:
        return result
