ROUTES = [
    {"name": "Warangal-Uppal", "buses": 234, "fare": 50, "capacity": 50},
    {"name": "Secunderabad-MP", "buses": 55, "fare": 40, "capacity": 50},
]
TIME_SLOTS = ["Morning", "Midday", "Evening", "Night"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MAHALAXMI_RATIO = 0.4  # 40% free (can be varied)
MIN_SERVICE = {"Warangal-Uppal": 50, "Secunderabad-MP": 10}  # min buses per day
