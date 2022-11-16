from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Rider(BaseModel):
    id: int
    naam: str
    leeftijd: int
    land: str
    ploeg: str

def Sorteer(lijst):
    lijst.sort(Rider(id))
    for i in lijst:
        print(i)
    return lijst


riders = []

riders.append(Rider(id=1, naam="Tadej Pogačar", leeftijd=24, land="Slovenië", ploeg="UAE Team Emirates"))
riders.append(Rider(id=2, naam="Wout van Aert", leeftijd=28, land="België", ploeg="Jumbo-Visma"))
riders.append(Rider(id=3, naam="Remco Evenepoel", leeftijd=22, land="België", ploeg="Soudal-Quickstep"))
riders.append(Rider(id=4, naam="Jonas Vingegaard", leeftijd=25, land="Denemarken", ploeg="Jumbo-Visma"))
riders.append(Rider(id=5, naam="Aleksandr Vlasov", leeftijd=26, land="Rusland", ploeg="BORA-Hansgrohe"))

@app.get("/")
async def root():
    return {"This is the home page"}

@app.get("/leaderboard")
async def get_leaderboard():
    topbord = Sorteer(riders)
    return {topbord}

@app.get("/riders")
async def get_riders():
    return {"riders": riders}

@app.post("/addrider/")
async def add_rider(riderid: int, ridernaam: str, riderleeftijd: int, riderland: str, riderploeg: str):
    riders.append(Rider(id=riderid, naam=ridernaam, leeftijd=riderleeftijd, land=riderland, ploeg=riderploeg))
    return {"riders": riders}
