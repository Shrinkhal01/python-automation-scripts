import json
import datetime

def generate_report(data):
    filename = f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
