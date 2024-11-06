import json
from ics import Calendar, Event
from datetime import datetime
import pytz

# Load events from JSON file
with open("events.json", "r") as file:
    events_data = json.load(file)

# Initialize the calendar
cal = Calendar()

# Define the CET timezone
cet = pytz.timezone("Europe/Zurich")

# Add events to the calendar
for event_data in events_data:
    event = Event()
    event.name = event_data["title"]
    
    # Parse start and end times with CET timezone
    start = cet.localize(datetime.strptime(event_data["start"], "%Y-%m-%d %H:%M"))
    end = cet.localize(datetime.strptime(event_data["end"], "%Y-%m-%d %H:%M"))
    
    event.begin = start
    event.end = end
    event.location = event_data["location"]
    cal.events.add(event)

# Save to an .ics file
with open("Calendrier_2024_2025.ics", "w") as f:
    f.writelines(cal)
