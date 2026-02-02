# vehicles.py
from typing import List, Tuple
import os

DATA_DIR = "./data"
VEHICLES_FILE = os.path.join(DATA_DIR, "vehicles.txt")
ROUTES_FILE = os.path.join(DATA_DIR, "routes.txt")

def vehicles_summary() -> Tuple[int, int, int, List[Tuple[str, str, str]]]:
    """Bütün nəqliyyat vasitələrinin statusunu qaytarır"""
    total = active = maintenance = 0
    maintenance_list: List[Tuple[str, str, str]] = []

    if not os.path.exists(VEHICLES_FILE):
        return 0, 0, 0, maintenance_list

    with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            vehicle_id, vehicle_type, route_id, status = parts[0], parts[1], parts[3], parts[4].lower()
            total += 1
            if status == "active":
                active += 1
            elif status == "maintenance":
                maintenance += 1
                maintenance_list.append((vehicle_id, vehicle_type, route_id))

    return total, active, maintenance, maintenance_list

def assign_vehicle_to_route(vehicle_id: str, new_route_id: str) -> None:
    """Nəqliyyat vasitəsini yeni marşruta təyin edir"""
    # Fayllar mövcuddurmu
    if not os.path.exists(VEHICLES_FILE):
        print("Error: Vehicles file not found.")
        return
    if not os.path.exists(ROUTES_FILE):
        print("Error: Routes file not found.")
        return

    # Yeni marşrut mövcuddurmu
    route_exists = False
    with open(ROUTES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(new_route_id + ","):
                route_exists = True
                break
    if not route_exists:
        print(f"Error: Route {new_route_id} does not exist.")
        return

    updated_lines = []
    vehicle_found = False
    with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == vehicle_id:
                vehicle_found = True
                if parts[4].lower() == "maintenance":
                    print(f"Error: Vehicle {vehicle_id} is under maintenance.")
                    return
                parts[3] = new_route_id
            updated_lines.append(",".join(parts) + "\n")

    if not vehicle_found:
        print(f"Error: Vehicle {vehicle_id} not found.")
        return

    with open(VEHICLES_FILE, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print(f"Vehicle {vehicle_id} assigned to route {new_route_id}.")
