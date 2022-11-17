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
- DELETE /deleterider/?riderid={riderid} => Verwijdert de rider uit de lijst door middel van zijn ID
- PUT /updaterider/?riderid={riderid}&ridernaam={ridernaam}&riderleeftijd={riderleeftijd}&riderland=riderland}&riderploeg={riderploeg}&riderpunten={riderpunten}
  
  => Update een rider, heeft alle info nodig

## Screenshots

### GET /riders
![image](https://user-images.githubusercontent.com/55507726/202534491-b46166cb-1994-4776-9818-a3d9ee4bf1f4.png)

### GET /leaderboard
![image](https://user-images.githubusercontent.com/55507726/202574581-3da588b3-3dd4-4ddb-9e44-bc4247f52357.png)

### GET /rider/{riderid}
![image](https://user-images.githubusercontent.com/55507726/202574689-9c0fb467-43d2-4b54-ae74-828ca43b931b.png)

### POST /addrider/?riderid={riderid}&ridernaam={ridernaam}&riderleeftijd={riderleeftijd}&riderland=riderland}&riderploeg={riderploeg}&riderpunten={riderpunten}
![image](https://user-images.githubusercontent.com/55507726/202575446-6e49fb0a-b016-4c71-a647-6153d97d3e75.png)

### DELETE /deleterider/?riderid={riderid}
![image](https://user-images.githubusercontent.com/55507726/202575631-dcf1de92-abe3-4b73-9016-d7cd0dae2154.png)

### PUT /updaterider/?riderid={riderid}&ridernaam={ridernaam}&riderleeftijd={riderleeftijd}&riderland=riderland}&riderploeg={riderploeg}&riderpunten={riderpunten}
![image](https://user-images.githubusercontent.com/55507726/202576162-f1f878cf-02cc-44f1-a8c9-bcf96585d6a8.png)


## Links

- Link naar hosted API: https://main-service-siebevr.cloud.okteto.net/
- Link naar Front-end repository: https://github.com/SiebeVR/basisproject_frontend
- Link naar hosted Front-end: https://siebevr.github.io/basisproject_frontend/
