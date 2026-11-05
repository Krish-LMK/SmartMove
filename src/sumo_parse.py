"""Read a SUMO tripinfo file and print travel-time statistics.

    python src/sumo_parse.py outputs/before_tripinfo.xml
    python src/sumo_parse.py outputs/before_tripinfo.xml outputs/after_tripinfo.xml

Each file is the --tripinfo-output of one SUMO run. With two files it prints the before/after change.
"""
import sys
import xml.etree.ElementTree as ET


def read_trips(path):
    """Return a list of (duration_s, time_loss_s) for every finished trip."""
    trips = []
    for trip in ET.parse(path).getroot().iter("tripinfo"):
        trips.append((float(trip.get("duration")), float(trip.get("timeLoss"))))
    return trips


def summarise(trips):
    n = len(trips)
    if n == 0:
        return {"trips": 0, "mean_min": 0.0, "mean_delay_min": 0.0}
    return {
        "trips": n,
        "mean_min": sum(t[0] for t in trips) / n / 60,
        "mean_delay_min": sum(t[1] for t in trips) / n / 60,
    }


def main(paths):
    results = []
    for path in paths:
        stats = summarise(read_trips(path))
        results.append(stats)
        print(f"{path}: {stats['trips']} trips, mean travel time {stats['mean_min']:.1f} min, "
              f"mean time lost to congestion {stats['mean_delay_min']:.1f} min")
    if len(results) == 2 and results[0]["trips"] and results[1]["trips"]:
        before, after = results
        change = after["mean_min"] - before["mean_min"]
        pct = 100 * change / before["mean_min"]
        print(f"\nBefore -> after: {before['mean_min']:.1f} -> {after['mean_min']:.1f} min "
              f"({change:+.1f} min, {pct:+.0f}%)  [SIMULATED]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:3])
