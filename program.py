import time
from plyer import notification

def notify_water_reminder():
    title = "Hydration Reminder"
    message = "Time to drink water!"
    notification.notify(
        title=title,
        message=message,
        app_name='Water Reminder',
        timeout=10  # seconds
    )

def main():
    while True:
        notify_water_reminder()
        time.sleep(2700)  # 2700 seconds = 45 minutes

if __name__ == "__main__":
    main()
