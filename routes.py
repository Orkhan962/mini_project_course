# routes.py
from typing import Tuple
import os

DATA_DIR = "./data"
ROUTES_FILE = os.path.join(DATA_DIR, "routes.txt")
VEHICLES_FILE = os.path.join(DATA_DIR, "vehicles.txt")

def routes_summary() -> Tuple[int, int]:
    """Bütün marşrutları və aktiv nəqliyyat vasitələrinə sahib marşrutları qaytarır"""
    total_routes = 0
    active_routes = 0
    route_status = {}

    if os.path.exists(VEHICLES_FILE):
        with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                route_id, status = parts[3], parts[4].lower()
                route_status.setdefault(route_id, []).append(status)

    if os.path.exists(ROUTES_FILE):
        with open(ROUTES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                route_id = line.split(",")[0]
                total_routes += 1
                if route_id in route_status and "active" in route_status[route_id]:
                    active_routes += 1

    return total_routes, active_routes

def add_route(route_id: str, name: str, start: str, end: str, distance: float) -> None:
    """Yeni marşrut əlavə edir"""
    # Marşrut ID artıq varsa
    if os.path.exists(ROUTES_FILE):
        with open(ROUTES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(route_id + ","):
                    print(f"Error: Route ID {route_id} already exists.")
                    return

    with open(ROUTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"{route_id},{name},{start},{end},{distance}\n")
    print(f"Route {route_id} added successfully.")
