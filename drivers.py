# drivers.py
from typing import List, Tuple
import os

DATA_DIR = "./data"
DRIVERS_FILE = os.path.join(DATA_DIR, "drivers.txt")
VEHICLES_FILE = os.path.join(DATA_DIR, "vehicles.txt")

def driver_workload_summary() -> Tuple[int, List[Tuple[str, str, float, str]]]:
    """Bütün sürücüləri və 8 saatdan çox işləyən sürücüləri qaytarır"""
    total_drivers = 0
    overtime_drivers: List[Tuple[str, str, float, str]] = []

    if not os.path.exists(DRIVERS_FILE):
        return 0, overtime_drivers

    with open(DRIVERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            driver_id, name, vehicle_id, hours = parts[0], parts[1], parts[3], float(parts[4])
            total_drivers += 1
            if hours > 8:
                overtime_drivers.append((driver_id, name, hours, vehicle_id))

    return total_drivers, overtime_drivers

def assign_driver_to_vehicle(driver_id: str, vehicle_id: str) -> None:
    """Sürücünü nəqliyyat vasitəsinə təyin edir"""
    if not os.path.exists(DRIVERS_FILE):
        print("Error: Drivers file not found.")
        return
    if not os.path.exists(VEHICLES_FILE):
        print("Error: Vehicles file not found.")
        return

    # Nəqliyyat vasitəsi mövcuddurmu və texniki baxımda deyil?
    vehicle_status = None
    with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == vehicle_id:
                vehicle_status = parts[4].lower()
                break
    if vehicle_status is None:
        print(f"Error: Vehicle {vehicle_id} does not exist.")
        return
    if vehicle_status == "maintenance":
        print(f"Error: Vehicle {vehicle_id} is under maintenance.")
        return

    # Sürücünü tap və təyin et
    updated_lines = []
    driver_found = False
    with open(DRIVERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == driver_id:
                driver_found = True
                parts[3] = vehicle_id
            updated_lines.append(",".join(parts) + "\n")

    if not driver_found:
        print(f"Error: Driver {driver_id} not found.")
        return

    with open(DRIVERS_FILE, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print(f"Driver {driver_id} assigned to vehicle {vehicle_id}.")
