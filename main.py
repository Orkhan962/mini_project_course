# main.py
import os
from datetime import datetime

from routes import routes_summary, add_route
from vehicles import vehicles_summary, assign_vehicle_to_route
from drivers import driver_workload_summary, assign_driver_to_vehicle
from schedules import schedule_summary, add_schedule
from generate_report import generate_report

DATA_DIR = "./data"
REPORT_DIR = "./reports"
os.makedirs(REPORT_DIR, exist_ok=True)
report_file = os.path.join(REPORT_DIR, "generate_report.txt")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("\nPress Enter to return to menu...")


def view_routes():
    path = os.path.join(DATA_DIR, "routes.txt")
    print("\n--- ROUTES ---")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    print(f"{parts[0]} | {parts[1]} | {parts[2]} -> {parts[3]} | {parts[4]} km")
    else:
        print("No routes found.")
    pause()


def view_vehicles():
    path = os.path.join(DATA_DIR, "vehicles.txt")
    print("\n--- VEHICLES ---")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    print(f"{parts[0]} | {parts[1]} | Capacity: {parts[2]} | Route: {parts[3]} | Status: {parts[4]}")
    else:
        print("No vehicles found.")
    pause()


def view_drivers():
    path = os.path.join(DATA_DIR, "drivers.txt")
    print("\n--- DRIVERS ---")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    print(f"{parts[0]} | {parts[1]} | Vehicle: {parts[3]} | Hours: {parts[4]}")
    else:
        print("No drivers found.")
    pause()


def view_schedules():
    path = os.path.join(DATA_DIR, "schedules.txt")
    print("\n--- SCHEDULES ---")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    print(f"{parts[0]} | Vehicle: {parts[1]} | Driver: {parts[2]} | {parts[3]} -> {parts[4]}")
    else:
        print("No schedules found.")
    pause()


def menu():
    while True:
        clear_screen()
        print("====================================")
        print("PUBLIC TRANSPORT OPERATIONS SYSTEM")
        print("====================================")
        print("1. View routes")
        print("2. View vehicles")
        print("3. View drivers")
        print("4. View schedules")
        print("5. Add new route")
        print("6. Assign vehicle to route")
        print("7. Assign driver to vehicle")
        print("8. Create schedule")
        print("9. Generate daily report")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_routes()
        elif choice == "2":
            view_vehicles()
        elif choice == "3":
            view_drivers()
        elif choice == "4":
            view_schedules()
        elif choice == "5":
            route_id = input("Route ID: ").strip()
            name = input("Route Name: ").strip()
            start = input("Start Stop: ").strip()
            end = input("End Stop: ").strip()
            distance = input("Distance (km): ").strip()
            try:
                distance = float(distance)
                add_route(route_id, name, start, end, distance)
            except ValueError:
                print("Error: Distance must be a number.")
            pause()
        elif choice == "6":
            vehicle_id = input("Vehicle ID: ").strip()
            route_id = input("New Route ID: ").strip()
            assign_vehicle_to_route(vehicle_id, route_id)
            pause()
        elif choice == "7":
            driver_id = input("Driver ID: ").strip()
            vehicle_id = input("Vehicle ID: ").strip()
            assign_driver_to_vehicle(driver_id, vehicle_id)
            pause()
        elif choice == "8":
            schedule_id = input("Schedule ID: ").strip()
            vehicle_id = input("Vehicle ID: ").strip()
            driver_id = input("Driver ID: ").strip()
            start_time = input("Start Time: ").strip()
            end_time = input("End Time: ").strip()
            add_schedule(schedule_id, vehicle_id, driver_id, start_time, end_time)
            pause()
        elif choice == "9":
            generate_report()
            pause()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
            pause()


if __name__ == "__main__":
    menu()
