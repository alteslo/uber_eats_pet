from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.app.src.core.exceptions.handlers import route_error_handler
from jinja2.exceptions import TemplateNotFound

templates = Jinja2Templates(directory="frontend/html/")
main_page_router = APIRouter()


main_page_img = StaticFiles(directory="frontend/img/")
main_page_css = StaticFiles(directory="frontend/css/")
main_page_js = StaticFiles(directory="frontend/js/")


@main_page_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    response = templates.TemplateResponse(
        name='index.html',
        context={"request": request}
    )
    # try:
    #     response = templates.TemplateResponse(
    #         name='index.html',
    #         context={"request": request}
    #     )
    # except TemplateNotFound:
    #     print('JDNJNDKNVSKNDKVJNSDKJNV')
    return response
