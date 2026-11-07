# Data audit

Fill one row per source. Record the access date and licence. Never invent or fill gaps silently.

| Source | URL | What we need | Found? | Format | Licence | Quality notes | Owner |
|---|---|---|---|---|---|---|---|
| National Open Data Portal | https://data.govmu.org | traffic counts, bus data | Not confirmed | | | Search manually | |
| Statistics Mauritius | https://statsmauritius.govmu.org | vehicles, road transport stats | Yes (annual/half-yearly, island-wide) | PDF | | No corridor flows | |
| OpenStreetMap | https://www.openstreetmap.org | roads, Metro, bus stops | Yes | OSM/Overpass | ODbL | Check completeness | |
| Metro Express | https://mauritiusmetroexpress.mu | stations, timetable, fares | To verify | web | | Sources disagree on station count | |
| NLTA / bus timetables | | bus routes and headways | No official feed found | | | Not used; bus stop order taken from public stop lists, unconfirmed | |
| Port Louis to Curepipe: Peak Traffic and Metro Express Data Report (N. Gopaul, 5 Nov 2026) | `docs/sources/` | fleet, peak flow, commuters, journey times | Yes | PDF | Team document | Contains estimates and assumptions, labelled in the report | Nikhil |
| SUMO / osmWebWizard 1.28.0 | https://sumo.dlr.de | traffic simulation | Yes | software | EPL-2.0 | Demand is random (assumption) | Suyash |

## Decision on data requests
No data requests were sent to Metro Express Ltd or the NLTA. The project works from published figures and the project data report.
