from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.api import routes_health
from app.api import routes_chat
from app.api import routes_documents
from app.api import routes_auth

from app.db.__init__db import init_db
from fastapi import Depends
from app.auth.auth_middleware import get_current_user
 







app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
def startup():
    init_db()




templates = Jinja2Templates(directory="app/frontend")

app.mount(
    "/static",
    StaticFiles(directory="app/frontend"),
    name="static"
)




@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/chat-ui", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse(
        "chat.html",
        {"request": request}
    )



app.include_router(
    routes_health.router,
    prefix=settings.API_V1_STR
)

app.include_router(
    routes_chat.router,
    prefix="/chat"
)

app.include_router(
    routes_documents.router,
    prefix="/files"
)

app.include_router(
    routes_auth.router,
    prefix="/auth"
)