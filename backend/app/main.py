from requests import get
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Codeforces Dashboard API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

API_URL = "https://codeforces.com/api/user.info"

db = {}
handles = ["bzznx", "yosrtati", "tourist"]

def get_info(handle):
    response = get(API_URL, params={"handles": handle})

    data = response.json()

    if data["status"] == "OK":
        return data["result"][0]



def update_db():
    for handle in handles:
        info = get_info(handle)
        db[handle] = {
            "handle": info["handle"],
            "rating": info.get("rating"),
            "maxRating": info.get("maxRating"),
        }
    

def add_handle(handle):
    if handle not in handles:
        handles.append(handle)
        update_db()
    

@app.get("/api/users")
def get_users(db=db):
    update_db()
    return list(db.values())

