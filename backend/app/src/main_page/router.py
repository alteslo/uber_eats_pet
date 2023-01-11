from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

main_page_router = APIRouter()


main_page_router.mount(
    "/", StaticFiles(directory="frontend/html/", html=True), name="index")
