# Assumptions register

Every number the model uses that is NOT measured or officially published goes here.
Judges will ask. Each row needs a source or the label "assumption" and a sensitivity range.

| ID | Parameter | Value | Type (official / measured / assumption) | Source or reason | Sensitivity range |
|---|---|---|---|---|---|
| A1 | Metro station-to-station time, Curepipe–Port Louis | 52 min (excludes walking and waiting) | estimate (project data report, Table 8) | `docs/sources/` report; verify against operator | |
| A2 | Metro peak headway | TBD | official | verify | |
| A3 | Car free-flow speed per segment | TBD | OSM distance + assumed limits | | |
| A4 | Congestion slowdown (peak/off-peak) | scenarios 1.3x / 1.6x / 2.0x | assumption (scenario parameter) | no published corridor figure found; refine from studies or manual map-app read-off if available | 1.3x–2.0x |
| A7 | Peak windows | 07:00–09:00 and 16:00–18:00 | published (press report) | expat.com congestion article | |
| A8 | Bus headway Curepipe–Port Louis | about 15 min, about 45 min journey | published (third-party, NTC) | mauritius-bus.com, verify | |
| A9 | Metro headway | 10 min, 06:00–19:00 | official, page may be dated | mauritiusmetroexpress.mu, verify | |
| A10 | Commuters to Port Louis from four zones (Curepipe, Vacoas-Phoenix, Quatre Bornes, Beau Bassin-Rose Hill) | 20,440 / 27,253 / 34,067 (low / mid / high) | assumption | Report Table 14: population × 40% employed × 15/20/25% working in Port Louis | low–high |
| A11 | Mode-choice (logit) coefficients | TBD | assumption | literature | wide range |
| A5 | Value of waiting time vs in-vehicle time | TBD | assumption | literature | |
| A6 | Park-and-ride capacity | TBD | assumption | | |
| A12 | Peak flow Curepipe→Port Louis 07–09, Port Louis→Curepipe 16–18 | 7,484 / 10,523 / 11,092 and 9,010 / 11,585 / 12,211 (low / mid / high) | estimate | Report Table 5; no official vehicle count for the route in 2024–26 | low–high |
| A13 | Vehicles removed from the road by Metro Express over 2 h | 384 / 1,111 / 2,244 (3.6% / 10.6% / 21.3% of mid flow) | estimate, unverified | Report; the 2025 fleet rise of 36,356 vehicles (5.1%) may absorb the freed space | low–high |
| A14 | Car occupancy | 1.2 / 1.4 / 1.6 persons per car | assumption | Report | 1.2–1.6 |
| A15 | SUMO traffic demand | random trips, 1 h, seeds 42–45 (`sumo/*/build.bat`) | assumption | SUMO `randomTrips.py` | rerun with other seeds and densities |
