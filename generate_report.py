from datetime import datetime

FILES = ["drivers.txt", "routes.txt", "schedules.txt", "vehicles.txt"]

def count_records(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len([line for line in f if line.strip()])

def routes_summary():
    total_routes = 0
    routes_with_active_vehicles = 0
    with open("routes.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                total_routes += 1
                routes_with_active_vehicles += 1
    return total_routes, routes_with_active_vehicles

def generate_report():
    today = datetime.now().strftime("%Y-%m-%d")
    with open("generate_report.txt", "w", encoding="utf-8") as report:
        report.write("DAILY OPERATIONS REPORT\n")
        report.write(f"Generated on: {today}\n")
        report.write("-" * 33 + "\n\n")
        for file in FILES:
            report.write(f"{file}: {count_records(file)} records\n")
        total, active = routes_summary()
        report.write("\nROUTES SUMMARY\n")
        report.write(f"Total routes: {total}\n")
        report.write(f"Routes with active vehicles: {active}\n")

if __name__ == "__main__":
    generate_report()
    print("generate_report.txt yaradıldı ✅")

