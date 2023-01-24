import traceback
from typing import Optional

from fastapi import status
from pydantic import BaseModel


class AppExceptionCase(Exception):
    def __init__(self, status_code: int, message: str, context: dict):
        self.exception_case = self.__class__.__name__
        self.message = message
        self.status_code = status_code
        self.context = context

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"message={self.message} - "
            + f"status_code={self.status_code} - "
            + f"context={self.context}>"
        )


class AppEcxeptionDB(Exception):
    def __init__(self, message, traceback):
        self.message = message
        self.traceback = traceback

    def __str__(self):
        return self.message


class ExceptionContent(BaseModel):
    app_exception: str
    context: Optional[dict]


class ExceptionResult(BaseModel):
    status_code: str
    message: str
    content: ExceptionContent


async def get_exception(exc: AppExceptionCase) -> dict:
    return ExceptionResult(
        status_code=exc.status_code,
        message=exc.message,
        content=ExceptionContent(
            app_exception=exc.exception_case, context=exc.context),
    ).dict()


class AppException(Exception):
    class CreateItemError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """
            Item creation failed
            """
            if not message:
                message = "Item creation failed"
            status_code = status.HTTP_409_CONFLICT
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class RouteError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}, status_code=None):
            if not message:
                message = "Route error"
            status_code = status_code or status.HTTP_500_INTERNAL_SERVER_ERROR
            AppExceptionCase.__init__(
                self,
                status_code=status_code,
                message=traceback.format_exc(),
                context=context,
            )

    class GetItemError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """
            Item not found
            """
            if not message:
                message = "Error occurred while receiving Item"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class GetListError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """
            Get List error
            """
            if not message:
                message = "Error occurred while receiving List"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class UpdateItemError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """
            Update Item error
            """
            if not message:
                message = "Element Update Failed"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class DeleteItemError(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """
            Delete Item error
            """
            if not message:
                message = "Element Delete Failed"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class ItemRequiresAuth(AppExceptionCase):
        """Item is not public and requires auth"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "Item is not public and requires auth"
            status_code = status.HTTP_401_UNAUTHORIZED
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class UserExist(AppExceptionCase):
        def __init__(self, message: str = "", context: dict = {}):
            """User already exists"""

            if not message:
                message = "User already exists"
            status_code = status.HTTP_409_CONFLICT
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class UserDisabled(AppExceptionCase):
        """User is disabled"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "User is disabled"
            status_code = status.HTTP_403_FORBIDDEN
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class UserNotExist(AppExceptionCase):
        """User not exists"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "User is not exists"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class UserNotAuthorized(AppExceptionCase):
        """User is not authorized"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "User is not authorized"
            status_code = status.HTTP_401_UNAUTHORIZED
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class ItemNotExist(AppExceptionCase):
        """Item is not exists"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "Item is not exists"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )

    class FileError(AppExceptionCase):
        """File operation error"""

        def __init__(self, message: str = "", context: dict = {}):
            if not message:
                message = "File operation error"
            status_code = status.HTTP_404_NOT_FOUND
            AppExceptionCase.__init__(
                self, status_code=status_code, message=message, context=context
            )
