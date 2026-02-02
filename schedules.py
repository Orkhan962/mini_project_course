# schedules.py
from typing import Tuple
import os

DATA_DIR = "./data"
SCHEDULES_FILE = os.path.join(DATA_DIR, "schedules.txt")
VEHICLES_FILE = os.path.join(DATA_DIR, "vehicles.txt")
DRIVERS_FILE = os.path.join(DATA_DIR, "drivers.txt")
ROUTES_FILE = os.path.join(DATA_DIR, "routes.txt")

def schedule_summary() -> Tuple[int, int]:
    """Cədvəllərin ümumi sayını və texniki baxımda olan vasitələrdən istifadə edənləri qaytarır"""
    maintenance_vehicle_ids = set()
    if os.path.exists(VEHICLES_FILE):
        with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) < 5:
                    continue
                vehicle_id, status = parts[0], parts[4].lower()
                if status == "maintenance":
                    maintenance_vehicle_ids.add(vehicle_id)

    total_schedules = maintenance_schedules = 0
    if os.path.exists(SCHEDULES_FILE):
        with open(SCHEDULES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) < 2:
                    continue
                total_schedules += 1
                vehicle_id = parts[1]
                if vehicle_id in maintenance_vehicle_ids:
                    maintenance_schedules += 1

    return total_schedules, maintenance_schedules

def add_schedule(schedule_id: str, vehicle_id: str, driver_id: str, start_time: str, end_time: str) -> None:
    """Yeni cədvəl əlavə edir"""
    # Fayllar mövcuddurmu
    for file_path, name in [(SCHEDULES_FILE, "Schedules"), (VEHICLES_FILE, "Vehicles"), (DRIVERS_FILE, "Drivers")]:
        if not os.path.exists(file_path):
            print(f"Error: {name} file not found.")
            return

    # Nəqliyyat vasitəsi texniki baxımda olmamalıdır
    vehicle_found = False
    with open(VEHICLES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == vehicle_id:
                vehicle_found = True
                if parts[4].lower() == "maintenance":
                    print(f"Error: Vehicle {vehicle_id} is under maintenance.")
                    return
                break
    if not vehicle_found:
        print(f"Error: Vehicle {vehicle_id} does not exist.")
        return

    # Sürücü mövcuddurmu
    driver_found = False
    with open(DRIVERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(driver_id + ","):
                driver_found = True
                break
    if not driver_found:
        print(f"Error: Driver {driver_id} does not exist.")
        return

    # Cədvəl ID mövcuddurmu
    if os.path.exists(SCHEDULES_FILE):
        with open(SCHEDULES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(schedule_id + ","):
                    print(f"Error: Schedule {schedule_id} already exists.")
                    return

    with open(SCHEDULES_FILE, "a", encoding="utf-8") as f:
        f.write(f"{schedule_id},{vehicle_id},{driver_id},{start_time},{end_time}\n")

    print(f"Schedule {schedule_id} added successfully.")
