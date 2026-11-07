# Decision log

| Date | Decision | Reason | Owner |
|---|---|---|---|
| 2026-11-03 | Track 5 chosen | Team assigned/selected | Lead |
| 2026-11-03 | Direction (proposed, awaiting team confirmation): corridor door-to-door scenario simulator + scenario optimiser | No corridor traffic dataset found; brief asks for before/after simulation | Lead |
| 2026-11-03 | No deep learning | No training data; not defensible | Lead |
| 2026-11-03 | No field measurements (protocol removed); use published timetables + OSM; peak slowdown as scenario parameter until a better data source is found | Field timing is impractical for the team; Track 5 may not use synthetic data as observations | Lead |
| 2026-11-03 | Project name: SmartMove | Used for the repository and web app | Team |
| 2026-11-05 | SUMO is required for the before/after simulation | Track 5 brief expects a simulation; before/after times must be labelled SIMULATED | Lead |
| 2026-11-05 | No emails to Metro Express or NLTA | Work from published data and the project data report | Lead |
| 2026-11-07 | Repository reorganised: `sumo/` for scenarios, `web/` for the front end, API key removed | Presentable submission; key was public | Lead |
