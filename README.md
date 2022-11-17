# Basisproject API-Development
> Basisproject voor het vak API-Development
> gemaakt door Siebe Van Rompay R0804405

## Inhoud

* [Project Thema](#project-thema)
* [Methods](#Methods)
* [Screenshots](#Screenshots)
* [Links](#Links)


## Project Thema

- Het thema van dit project is wielrennen.
- Het wielrenseizoen is afgelopen dus nu zijn alle punten van de renners bekend.


## Methods

- GET /riders => Lijst van alle riders met info
- GET /leaderboard => Leaderboard van de renners (Hoogste punten eerst)
- GET /rider/{riderid} => opvragen van specifieke rider door middel van zijn ID
- POST /addrider/?riderid={riderid}&ridernaam={ridernaam}&riderleeftijd={riderleeftijd}&riderland=riderland}&riderploeg={riderploeg}&riderpunten={riderpunten}
  => Voegt rider toe aan lijst van riders, heeft alle info nodig, mag niet bestaande nummer/naam zijn
- DELETE /deleterider/{riderid} => Verwijdert de rider uit de lijst door middel van zijn ID
- PUT /updaterider/?riderid={riderid}&ridernaam={ridernaam}&riderleeftijd={riderleeftijd}&riderland=riderland}&riderploeg={riderploeg}&riderpunten={riderpunten}
  => Update een rider, heeft alle info nodig

## Screenshots

- Get /riders
![image](https://user-images.githubusercontent.com/55507726/202534491-b46166cb-1994-4776-9818-a3d9ee4bf1f4.png)

- Get /leaderboard

## Links

- Link naar hosted API: https://main-service-siebevr.cloud.okteto.net/
- Link naar Front-end repository: https://github.com/SiebeVR/basisproject_frontend
- Link naar hosted Front-end: https://siebevr.github.io/basisproject_frontend/
