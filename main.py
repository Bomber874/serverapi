from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import json
from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    text: str
    is_published: bool

app = FastAPI()
origins = [
    "http://193.164.16.150",
    "http://193.164.16.150:8000"
    "http://193.164.16.150:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/realese/")
async def create_post(info):
    return info

@app.get("/info")
def info():
    with sqlite3.connect("/home/gameserver/server/garrysmod/sv.db") as con:
        cur = con.cursor()
        users = cur.execute('SELECT * FROM bomb_killsinfo ORDER BY npc_kills DESC LIMIT 5').fetchall()
        return users

@app.get("/ammoinfo")
def arsenalinfo():
    with sqlite3.connect("/home/gameserver/server/garrysmod/sv.db") as con:
        cur = con.cursor()
        users = cur.execute('SELECT * FROM bomb_arsenalinfo ORDER BY cnt DESC LIMIT 5').fetchall()
        return users
        
@app.get("/allinfo")
def allinfo():
    with sqlite3.connect("/home/gameserver/server/garrysmod/sv.db") as con:
        cur = con.cursor()
        users_ammo = cur.execute('SELECT * FROM bomb_arsenalinfo ORDER BY cnt DESC LIMIT 5').fetchall()
        users_kills = cur.execute('SELECT * FROM bomb_killsinfo ORDER BY npc_kills DESC LIMIT 5').fetchall()
        
        
        return {'ammo': users_ammo, 'kills':users_kills}