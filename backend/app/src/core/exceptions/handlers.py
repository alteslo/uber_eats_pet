from jinja2.exceptions import TemplateNotFound


def route_error_handler(func):
    async def decorator(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except TemplateNotFound:
            return ''

    return decorator
