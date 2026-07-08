import csv
from datetime import datetime
import database


def generate_report(filename=None):
    """Export all registered participants to a CSV file."""
    participants = database.view_participants()

    if filename is None:
        filename = f"participant_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Email"])
        for row in participants:
            writer.writerow(row)

    print(f"Report generated: {filename} ({len(participants)} participants)")
    return filename


if __name__ == "__main__":
    generate_report()
