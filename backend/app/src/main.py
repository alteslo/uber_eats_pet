from fastapi import FastAPI
from backend.app.src.main_page.router import main_page_router

app = FastAPI()

app.include_router(main_page_router)
