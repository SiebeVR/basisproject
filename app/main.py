from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Rider(BaseModel):
    naam: str
    leeftijd: int
    land: str
    ploeg: str
    geboortedatum: str
    gewicht: int
    lengte: int
    punten: int
    
riders = []

riders.append(Rider(naam="Tadej Pogačar", leeftijd=24, land="Slovenië", ploeg="UAE Team Emirates", geboortedatum="21/09/1998", gewicht=66, lengte=176, punten=4839))
riders.append(Rider(naam="Wout van Aert", leeftijd=28, land="België", ploeg="Jumbo-Visma", geboortedatum="15/09/1994", gewicht=78, lengte=190, punten=3722))
riders.append(Rider(naam="Remco Evenepoel", leeftijd=22, land="België", ploeg="Soudal-Quickstep", geboortedatum="25/01/2000", gewicht=63, lengte=171, punten=3602))
riders.append(Rider(naam="Jonas Vingegaard", leeftijd=25, land="Denemarken", ploeg="Jumbo-Visma", geboortedatum="10-12-1996", gewicht=60, lengte=175,punten=3317))
riders.append(Rider(naam="Aleksandr Vlasov", leeftijd=26, land="Rusland", ploeg="BORA-Hansgrohe", geboortedatum="23-04-1996", gewicht=68, lengte=186,punten=2105))


@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("/riders")
async def get_riders():
    return riders