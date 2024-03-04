from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

players = {
    1: {
        "name": "German Cano",
        "age": 35,
        "team": "Fluminense"
    },
    2: {
        "name": "John Kennedy",
        "age": 21,
        "team": "Fluminense"
    },
} 

class Player(BaseModel):
    name: str
    age: int
    team: str

@app.get("/")
def team():
    return {"message": players}

@app.get("/players/{id_player}")
def get_player(id_player:int):
    return {"message": players[id_player]}

@app.get("/players-name")
def get_player_name(name:str):
    for player_id in players:
        if players[player_id]["name"] == name :
            return players[player_id]
    return {"message": 'Jogador não encontrado'}

@app.post("/player-register/{id_player}")
def post_player(player_id: int, player: Player):
    if player_id in players:
        return { "Erro" : "Player registered before" }
    players[player_id] = player
    return players[player_id]

@app.delete("/player-excluded/{id_player}")
def exclude_player(player_id: int):
    if player_id not in players:
        return { "Erro" : "Player not registered" }
    del players[player_id]
    return {"Message" : "Player excluded succefull"}