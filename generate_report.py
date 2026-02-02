# generate_report.py
from datetime import datetime
import os
from vehicles import vehicles_summary
from drivers import driver_workload_summary
from routes import routes_summary
from schedules import schedule_summary

REPORT_DIR = "./reports"
os.makedirs(REPORT_DIR, exist_ok=True)
report_file = os.path.join(REPORT_DIR, "generate_report.txt")

DATA_FILES = ["drivers.txt", "routes.txt", "schedules.txt", "vehicles.txt"]

def count_records(filename: str) -> int:
    with open(os.path.join("./data", filename), "r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())

def generate_report() -> None:
    now = datetime.now()
    timestamp = str(now)

    with open(report_file, "w", encoding="utf-8") as report:
        report.write("DAILY OPERATIONS REPORT\n")
        report.write(f"Generated on: {timestamp}\n")
        report.write("-" * 33 + "\n\n")

        for file in DATA_FILES:
            report.write(f"{file}: {count_records(file)} records\n")

        total, active, maintenance, maintenance_list = vehicles_summary()
        report.write("\nVEHICLES STATUS\n")
        report.write(f"Total vehicles: {total}\n")
        report.write(f"Active vehicles: {active}\n")
        report.write(f"Vehicles under maintenance: {maintenance}\n")
        for v_id, v_type, route_id in maintenance_list:
            report.write(f"- {v_id} ({v_type}) – Route {route_id}\n")

        total_routes, active_routes = routes_summary()
        report.write("\nROUTES SUMMARY\n")
        report.write(f"Total routes: {total_routes}\n")
        report.write(f"Routes with active vehicles: {active_routes}\n")

        total_drivers, overtime_drivers = driver_workload_summary()
        report.write("\nDRIVER WORKLOAD\n")
        report.write(f"Total drivers: {total_drivers}\n")
        if overtime_drivers:
            report.write("Drivers with overtime:\n")
            for d_id, name, hours, vehicle_id in overtime_drivers:
                report.write(f"- {d_id} {name} – {hours} hours (Vehicle {vehicle_id})\n")

        total_schedules, maintenance_schedules = schedule_summary()
        report.write("\nSCHEDULE SUMMARY\n")
        report.write(f"Total scheduled trips: {total_schedules}\n")
        report.write(f"Schedules using vehicles under maintenance: {maintenance_schedules}\n")

    print(f"{report_file} yaradıldı ✅")

if __name__ == "__main__":
    generate_report()
