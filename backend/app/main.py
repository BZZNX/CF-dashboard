from requests import get
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db, get_saved_users, update_db, add_handle
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException



app = FastAPI(
    title="Codeforces Dashboard API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

API_URL = "https://codeforces.com/api/user.info"

init_db()


def get_info(handles):
    response = get(
        API_URL,
        params={"handles": ";".join(handles)},
    )

    return response.json()["result"]



@app.get("/api/users")
def get_users():
    saved_users = get_saved_users()
    handles = [user["handle"] for user in saved_users]

    infos = get_info(handles)

    for handle, info in zip(handles, infos):
        update_db(
            handle,
            info.get("rating"),
            info.get("maxRating"),
        )

    return get_saved_users()

class NewUser(BaseModel):
    handle: str


@app.post("/api/users")
def add_user(user: NewUser):
    handle = user.handle.strip()

    data = get(API_URL, params={"handles": handle}).json()
    if data["status"] != "OK":
        raise HTTPException(status_code=404, detail="Codeforces handle not found")

    info = data["result"][0]
    add_handle(info["handle"])
    update_db(info["handle"], info.get("rating"), info.get("maxRating"))

    return get_saved_users()