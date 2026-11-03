# SmartMove – Port Louis–Curepipe Corridor Simulator

> **Status:** prototype built for Tech Wave – AI Hackathon Mauritius 2026 (Track 5: Traffic and Metro Express optimisation).
> This is a research prototype. It is **not** an official planning or timetable tool.

## The problem
Congestion on the Port Louis–Curepipe corridor costs commuters hours every day. We test **scenarios**
(feeder buses, park-and-ride, Metro headway changes) and estimate their effect on **door-to-door travel time**.

## Approach (summary)
1. Split the corridor into origin zones, all travelling to Port Louis.
2. Estimate door-to-door time per mode (car, bus, Metro, feeder/park-and-ride).
3. Model how commuters may switch mode when times change (mode-choice model).
4. Search over scenarios to find the best option (optimiser).
5. Show before/after results in a Streamlit app with a map.

See `docs/assumptions.md` for every assumption and `docs/decisions.md` for the decision log.

## Measured vs simulated – read this first
| Item | Status |
|---|---|
| Road network, stops, free-flow car times | Real (OpenStreetMap) |
| Metro and bus headways, journey times | Published timetables, to be verified (see `docs/data_audit.md`) |
| Peak congestion slowdown | **Scenario parameter** (run at several values), not a measurement |
| Zone commuter demand | Census-based where available, otherwise **assumption** |
| Mode-choice parameters | **Assumptions**, shown with sensitivity ranges |
| "After" travel times | **Simulated projections**, depend on the assumptions above |

No synthetic dataset is presented as observed data.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Repository layout
```
data/raw/                 original downloads (never edited)
data/processed/           cleaned tables
src/                      model code
app/                      Streamlit demo
notebooks/                data audit and exploration
docs/                     assumptions, data audit, decisions, submission checklist
outputs/                  charts and result tables
```

## Data sources
Listed with access date and licence in `docs/data_audit.md`. Every dataset, model and API used must appear there.

## Team
Mihivar Luchoomun,
Trishen Naidoo,
Suyash Balluck,
Nikhil Gopaul.

## Limitations
To be completed with final results. Draft limits: peak slowdown is a scenario parameter, assumed behaviour parameters,
no real-time data, corridor-level (not junction-level) congestion.
