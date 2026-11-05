"""Shared settings for SmartMove. Everyone imports from here so numbers live in ONE place.

Anything marked APPROXIMATE must be checked on OpenStreetMap before it is used in results,
and every change should be recorded in docs/assumptions.md.
"""

# Bounding box of the Port Louis - Curepipe corridor, in decimal degrees (APPROXIMATE).
# Order follows OSMnx 2.x: (west, south, east, north).
CORRIDOR_BBOX = (57.44, -20.34, 57.55, -20.14)

# Only keep the main road types so the network stays small and fast.
# (motorway = M1/M2, trunk/primary/secondary = main roads.)
MAIN_ROAD_FILTER = '["highway"~"motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link"]'

# Origin zones, all travelling to Port Louis. (latitude, longitude) are APPROXIMATE town centres:
# check each point on openstreetmap.org and adjust.
ZONES = {
    "Curepipe": (-20.3180, 57.5260),
    "Vacoas-Phoenix": (-20.2985, 57.4783),
    "Quatre Bornes": (-20.2650, 57.4790),
    "Rose Hill-Beau Bassin": (-20.2390, 57.4700),
    "Ebene": (-20.2450, 57.4900),
}
DESTINATION = ("Port Louis", (-20.1609, 57.5012))

# Peak windows reported in the press (see docs/assumptions.md, A7).
PEAK_MORNING = ("07:00", "09:00")
PEAK_EVENING = ("16:00", "18:00")

# Congestion slowdown scenarios used until SUMO gives us real simulated car times (A4).
SLOWDOWN_SCENARIOS = [1.3, 1.6, 2.0]

# Folder names (relative to the project root).
DATA_RAW = "data/raw"
DATA_PROCESSED = "data/processed"
OUTPUTS = "outputs"
