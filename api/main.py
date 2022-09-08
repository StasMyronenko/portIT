from fastapi import FastAPI, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from configuration.utils import get_current_user
from projects.projects_router import project_router
from auth.auth_router import router as auth_router
from configuration.db import engine, SessionLocal, no_sql_db
import admin as admin_models
from users.models import User
from site_data.site_data_app import app as site_app

from dotenv import load_dotenv

# TODO make something with admin panel - it don't work on frontend(in postman it works, so problem in front)
app = FastAPI()

admin = Admin(app, engine, base_url="/admin")
admin.add_view(admin_models.ProjectView)
admin.add_view(admin_models.UserView)

origins = [
    # "http://localhost",
    # "http://localhost:8080",
    # "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

site_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Connect it to router site (but firstly create this router
@site_app.middleware("http")
async def no_sql_db_middleware(request: Request, call_next):
    response = Response("Server error. NoSQL Problems", status_code=500)
    try:
        request.state.site_data_db = no_sql_db
        response = await call_next(request)
    except BaseException as e:
        print(e)
    return response

app.mount("/site_app", site_app)

app.include_router(project_router, prefix="/projects")
app.include_router(auth_router, prefix="/auth")


@app.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
