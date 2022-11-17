from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Rider(BaseModel):
    id: int
    naam: str
    leeftijd: int
    land: str
    ploeg: str
    punten: int

riders = []

riders.append(Rider(id=1, naam="Tadej Pogačar", leeftijd=24, land="Slovenië", ploeg="UAE Team Emirates", punten=4839))
riders.append(Rider(id=2, naam="Wout van Aert", leeftijd=28, land="België", ploeg="Jumbo-Visma", punten=3722))
riders.append(Rider(id=3, naam="Remco Evenepoel", leeftijd=22, land="België", ploeg="Soudal-Quickstep", punten=3602))
riders.append(Rider(id=4, naam="Jonas Vingegaard", leeftijd=25, land="Denemarken", ploeg="Jumbo-Visma", punten=3317))
riders.append(Rider(id=5, naam="Aleksandr Vlasov", leeftijd=26, land="Rusland", ploeg="BORA-Hansgrohe", punten=2105))

@app.get("/")
async def root():
    return {"This is the home page"}

@app.get("/leaderboard")
async def sort_riders():
    riders.sort(key=lambda x: x.punten, reverse=True)
    return riders

@app.get("/riders")
async def get_riders():
    return riders

@app.get("/rider/{id}")
async def get_rider(id: int):
    for i in riders:
        if i.id == id:
            return i

@app.post("/addrider/")
async def add_rider(riderid: int, ridernaam: str, riderleeftijd: int, riderland: str, riderploeg: str, riderpunten: int):
    riders.append(Rider(id=riderid, naam=ridernaam, leeftijd=riderleeftijd, land=riderland, ploeg=riderploeg, punten=riderpunten))
    return  riders

@app.delete("/deleterider/")
async def delete_rider(riderid: int):
    for i in riders:
        if i.id == riderid:
            riders.remove(i)
    return riders

@app.put("/updaterider/")
async def update_rider(riderid: int, ridernaam: str, riderleeftijd: int, riderland: str, riderploeg: str, riderpunten: int):
    for i in riders:
        if i.id == riderid:
            i.naam = ridernaam
            i.leeftijd = riderleeftijd
            i.land = riderland
            i.ploeg = riderploeg
            i.punten = riderpunten
    return riders
