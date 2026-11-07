# Impact and ethics note – SmartMove (prototype)

## Purpose
SmartMove explores how Metro Express use, carpooling and smarter routing could shorten travel on the Port Louis–Curepipe corridor.
It is a hackathon prototype (Tech Wave – AI Hackathon, Mauritius 2026, Track 5), not an operational service.

## Intended impact
- Shorter and more predictable peak-hour journeys for commuters from Curepipe, Vacoas-Phoenix, Quatre Bornes and Beau Bassin-Rose Hill, whose estimated number is 20,440–34,067 (assumption, `docs/assumptions.md` A10).
- Better use of Metro Express and of seats in private cars, which would reduce vehicles on the road. The Metro effect is estimated at 384–2,244 fewer vehicles over two peak hours, and it is unverified.
- Evidence for planners: scenarios can be compared under the same assumptions before anything is built.

## Honesty about data
- Real data: OpenStreetMap network, official fleet totals.
- Estimates and assumptions: peak flows, commuter numbers, Metro effect, car occupancy and SUMO demand. They are labelled as such everywhere.
- All before/after travel times are **SIMULATED** and shown as such. No synthetic data is presented as an observation.
- The demo is a prototype and says so.

## Privacy
- The prototype uses no real personal data and no real-time location data.
- A real carpooling service would need explicit consent, minimal collection of location and identity data, limited retention, and verification of drivers and riders. These are not built.
- The Google Maps API key was removed from the repository. Keys must be restricted and never committed.

## Fairness and safety
- Not all commuters live near a Metro station: stops such as Bagatelle, Réduit, Wooton and La Vigie have none nearby. Benefits may favour areas with access, so feeder services matter.
- Carpooling raises safety concerns, especially for women and night travel. A real service needs identity checks, ratings, trip sharing and a reporting route.
- Pricing, if added, should not make the option unaffordable for lower-income commuters.

## Limitations and risks
- Simulated demand is random, so results show relative effects, not exact predictions.
- Increased capacity can attract more vehicles over time (the 2025 fleet rose 5.1%), which could cancel gains.
- Results should support, not replace, official traffic studies and operator data.

## Open items before submission
Add the demo link, the video link and the final simulation results.
