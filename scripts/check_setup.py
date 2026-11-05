"""Run this first on every team member's computer.

    python scripts/check_setup.py

It checks your Python version and that every package SmartMove needs can be imported.
"""
import importlib
import sys

PACKAGES = ["pandas", "numpy", "sklearn", "matplotlib", "plotly", "streamlit", "folium", "osmnx"]

print(f"Python version: {sys.version.split()[0]}")
if sys.version_info < (3, 10):
    print("  PROBLEM: use Python 3.10 or newer (3.11 or 3.12 is best).")

missing = []
for name in PACKAGES:
    try:
        module = importlib.import_module(name)
        print(f"  OK       {name} {getattr(module, '__version__', '')}")
    except ImportError:
        print(f"  MISSING  {name}")
        missing.append(name)

if missing:
    print("\nSome packages are missing. With your virtual environment active, run:")
    print("  pip install -r requirements.txt")
else:
    print("\nAll packages found. You are ready.")
