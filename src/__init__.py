from src.message import CustomMessage
from src.icon import Icons
from src.schedule import Schedule
from src.notification import Notification

if __name__ == "__main__":
    sc = Schedule()
    # sc.refresh_schedule()
    print(sc.fajr())