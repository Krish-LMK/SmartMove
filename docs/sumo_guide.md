# SUMO guide for SmartMove (for Suyash and Trishen)

SUMO is a free traffic simulator. It reads a road network and a list of trips, moves every vehicle
second by second, and records how long each trip took. We use it to get **simulated car and bus travel
times on the corridor, before and after a scenario**.

Honest limit: our trip demand is an **assumption** (no real corridor counts), so results are simulated
projections, not measurements. Say so in the README and pitch.

## 1. Install (Prep days)
1. Download SUMO for Windows from https://sumo.dlr.de/docs/Downloads.php and run the installer.
2. Check it works: open a terminal and run `sumo --version`. If it is not found, restart VS Code or the computer.
3. Check the variable exists: `echo %SUMO_HOME%` (Windows cmd). If empty, set it to the SUMO install folder.

## 2. See a working simulation in 10 minutes (osmWebWizard)
1. Run `python "%SUMO_HOME%\tools\osmWebWizard.py"`. A map opens in your browser.
2. Zoom to the Curepipe - Port Louis corridor and select the area.
3. Tick "Car" and "Bus" (and "Public Transport" if offered), then click **Generate Scenario**.
4. SUMO-GUI opens. Press play and watch the cars move. This proves your install works.

osmWebWizard makes a folder with a network and random trips. Good for learning; for the project we
build the same thing by hand so the files are in the repo and repeatable (next steps).

## 3. Build the corridor network (Day 1)
Put files in the `sumo/` folder of the repo.

1. Download the OSM data for the corridor box (the same area as `CORRIDOR_BBOX` in `src/config.py`):
   ```
   curl -o sumo/corridor.osm "https://overpass-api.de/api/map?bbox=57.44,-20.34,57.55,-20.14"
   ```
   If this is refused as too large, use osmWebWizard to export the area instead.
2. Convert it to a SUMO network:
   ```
   netconvert --osm-files sumo/corridor.osm -o sumo/corridor.net.xml --geometry.remove --roundabouts.guess --ramps.guess --junctions.join --tls.guess-signals --tls.discard-simple --remove-edges.isolated --keep-edges.by-vclass passenger,bus
   ```
3. Open it to check: `netedit sumo/corridor.net.xml`. Look for broken or missing roads along the main route.

## 4. Create trips (Day 1)
Start simple, then make it zone-based.

1. **Quick start (random trips)** to prove the pipeline works:
   ```
   python "%SUMO_HOME%\tools\randomTrips.py" -n sumo/corridor.net.xml -o sumo/trips.trips.xml -r sumo/routes.rou.xml -e 3600 -p 2 --validate
   ```
2. **Real project version:** use Nikhil's `data/processed/zones.csv` (commuters per zone). Write trips from each
   zone's nearest road edge to the Port Louis edge, with the number of cars per hour taken from the table.
   Every demand number is an assumption: record it in `docs/assumptions.md`.

## 5. Run BEFORE and AFTER and save results
Create `sumo/before.sumocfg` pointing at the network and routes, then run:
```
sumo -c sumo/before.sumocfg --tripinfo-output outputs/before_tripinfo.xml
```
For the AFTER run, change one thing (for example, add a park-and-ride bus line or move demand from cars to
buses), save as `sumo/after.sumocfg`, and run:
```
sumo -c sumo/after.sumocfg --tripinfo-output outputs/after_tripinfo.xml
```
Then compare them:
```
python src/sumo_parse.py outputs/before_tripinfo.xml outputs/after_tripinfo.xml
```
The output says, for example, "Before -> after: 38.2 -> 31.5 min [SIMULATED]". Those numbers feed the
door-to-door model and the app.

## 6. Hand over to Trishen (Day 2)
Give Trishen the mean car travel time per zone for before and after. His model uses these instead of the assumed
1.3x / 1.6x / 2.0x slowdown. Record this in `docs/decisions.md`.

## Common problems
- **"sumo is not recognised":** restart VS Code; check SUMO's `bin` folder is on PATH.
- **Cars never arrive / simulation stops early:** the route may be impossible (one-way or disconnected road). Use `--validate` and check in netedit.
- **Huge network is slow:** keep only main roads (the `--keep-edges.by-vclass` option above) or shrink the box.
