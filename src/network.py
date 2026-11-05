"""Download the corridor road network from OpenStreetMap and save a map + summary table.

Run from the project root, with your virtual environment active:

    python src/network.py

Needs an internet connection. Outputs:
    data/processed/corridor_roads.graphml   (the road network, for later code)
    data/processed/corridor_edges.csv       (one row per road segment)
    outputs/corridor_map.html               (open in a browser to check the area)

Data: (c) OpenStreetMap contributors, ODbL licence. Cite this in the README.
"""
import os
import sys

import folium
import osmnx as ox

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config  # noqa: E402


def as_text(value):
    """OSM tags can be lists (a road with two names). Turn anything into plain text."""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return "" if value is None else str(value)


def main():
    os.makedirs(config.DATA_PROCESSED, exist_ok=True)
    os.makedirs(config.OUTPUTS, exist_ok=True)

    print("Downloading main roads from OpenStreetMap (can take a minute)...")
    graph = ox.graph_from_bbox(config.CORRIDOR_BBOX, custom_filter=config.MAIN_ROAD_FILTER)
    graph = ox.add_edge_speeds(graph)        # fills missing speeds with typical values (an ASSUMPTION)
    graph = ox.add_edge_travel_times(graph)  # free-flow travel time in seconds

    nodes, edges = ox.graph_to_gdfs(graph)
    print(f"Nodes (junctions): {len(nodes)}   Edges (road segments): {len(edges)}")

    table = edges.reset_index()[["u", "v", "name", "highway", "length", "maxspeed", "speed_kph", "travel_time"]].copy()
    for col in ["name", "highway", "maxspeed"]:
        table[col] = table[col].map(as_text)
    table.to_csv(os.path.join(config.DATA_PROCESSED, "corridor_edges.csv"), index=False)

    print("\nRoad length by type (km):")
    print((table.groupby("highway")["length"].sum() / 1000).round(1).sort_values(ascending=False).to_string())
    print("\nSegments with no maxspeed tag in OSM:", int((table["maxspeed"] == "").sum()), "of", len(table))

    ox.save_graphml(graph, os.path.join(config.DATA_PROCESSED, "corridor_roads.graphml"))

    # Map for checking the area by eye.
    centre = [(config.CORRIDOR_BBOX[1] + config.CORRIDOR_BBOX[3]) / 2, (config.CORRIDOR_BBOX[0] + config.CORRIDOR_BBOX[2]) / 2]
    fmap = folium.Map(location=centre, zoom_start=12, tiles="OpenStreetMap")

    lines = edges.reset_index()
    for _, row in lines.iterrows():
        coords = [(lat, lon) for lon, lat in row["geometry"].coords]
        folium.PolyLine(coords, weight=2, color="#1F4E78", tooltip=as_text(row["name"]) or as_text(row["highway"])).add_to(fmap)

    for name, (lat, lon) in config.ZONES.items():
        folium.Marker([lat, lon], popup=name, tooltip=name, icon=folium.Icon(color="green")).add_to(fmap)
    dest_name, (dlat, dlon) = config.DESTINATION
    folium.Marker([dlat, dlon], popup=dest_name, tooltip=dest_name, icon=folium.Icon(color="red")).add_to(fmap)

    out_map = os.path.join(config.OUTPUTS, "corridor_map.html")
    fmap.save(out_map)
    print(f"\nSaved map to {out_map}. Open it in your browser and check the zone markers sit where they should.")


if __name__ == "__main__":
    main()
