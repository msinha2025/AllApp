from datetime import datetime
import pytz

def show_times():
    timezones = {
        "IST": "Asia/Kolkata",
        "EST": "America/New_York",
        "CST": "America/Chicago",
        "UTC": "UTC"
    }
    now_utc = datetime.now(pytz.utc)
    for name, tz_str in timezones.items():
        tz = pytz.timezone(tz_str)
        local_time = now_utc.astimezone(tz)
        print(f"{name}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    show_times()