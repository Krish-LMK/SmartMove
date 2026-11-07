# SmartMove – Port Louis–Curepipe Corridor

> **Status: prototype** built for the Tech Wave – AI Hackathon, Mauritius 2026 (Track 5: Traffic and Metro Express optimisation).
> It is a research prototype, **not** an official planning or timetable tool.

## The problem
The Port Louis–Curepipe corridor (M1 and the Metro Express line) is congested at peak hours, and there is no official
vehicle count for the route. SmartMove tests **scenarios** (Metro Express use, carpooling, feeder services) and estimates
their effect on **travel time**.

## What is in this repository
| Part | Folder | What it does |
|---|---|---|
| Web app (front end) | `web/` | SmartMove interface: ride request, carpool, smart routes |
| Traffic simulation | `sumo/` | SUMO networks and demand built from OpenStreetMap; before/after runs |
| Analysis code | `src/`, `scripts/` | Corridor settings, network download, SUMO result parser, setup check |
| Documentation | `docs/` | Assumptions, data audit, decision log, impact and ethics note, source report |
| Results | `outputs/` | Summary tables and charts from the simulation runs |

## Measured, official, assumed or simulated – read this first
| Item | Status |
|---|---|
| Road network and stops | Real (OpenStreetMap) |
| Fleet totals | Official (Statistics Mauritius), quoted in `docs/sources/` |
| Peak flow and commuter numbers | **Estimates** from the project data report, not official counts |
| Traffic demand inside SUMO | **Assumption** (random trips, fixed seeds) |
| Before/after travel times | **SIMULATED**, they depend on the assumptions above |

No synthetic data is presented as an observation. Every assumption is listed in `docs/assumptions.md`.

## SUMO simulation
Details and run commands are in [`sumo/README.md`](sumo/README.md).
**Current status:** two small test networks (central Port Louis and Ébène–Réduit) are in the repository. One baseline run (Port Louis) has completed; before/after results are not yet published.
Results will appear in `outputs/` and be labelled SIMULATED.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_setup.py
```
SUMO is installed separately: <https://sumo.dlr.de/docs/Downloads.php>. Set the `SUMO_HOME` environment variable.

## Running the web app
`web/index.html` is a static page. Open it in a browser, or run `python -m http.server` inside `web/` and visit
`http://localhost:8000`. The map needs a Google Maps API key: replace `YOUR_API_KEY` in `web/index.html`
with your own key (restrict it to your own domains; never commit a real key).

## Repository layout
```
web/          SmartMove web front end (index.html)
sumo/         SUMO scenarios, one folder per area (see sumo/README.md)
src/          model and parsing code
scripts/      helper scripts (setup check)
outputs/      result tables and charts
docs/         assumptions, data audit, decisions, impact and ethics, sources/
data/         raw/ (original downloads, git-ignored) and processed/ (cleaned tables)
```

## Data sources
Listed in `docs/data_audit.md`. The corridor traffic report is in `docs/sources/`.

## Team
Mihivar Luchoomun, Trishen Naidoo, Suyash Balluck, Nikhil Gopaul.

## Limitations
- Traffic demand in SUMO is assumed, so simulated times show relative effects, not exact prediction.
- No real-time data and no official vehicle count for the route in 2024–26.
- The commuter and Metro effect figures are estimates with wide low–high ranges.
- See `docs/impact_and_ethics.md` for the ethics note.

## Licence
MIT, see `LICENSE`.
