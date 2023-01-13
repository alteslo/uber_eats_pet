from fastapi import FastAPI

from backend.app.src.main_page.router import (main_page_css, main_page_img,
                                              main_page_js, main_page_router)

app = FastAPI()

app.include_router(main_page_router)

app.mount(path='/img', app=main_page_img, name='img')
app.mount(path='/css', app=main_page_css, name='css')
app.mount(path='/js', app=main_page_js, name='js')
