import numpy as np
import pandas as pd
from .config import ROUTES, TIME_SLOTS, DAYS, MAHALAXMI_RATIO

def generate_demand(seed=42):
    np.random.seed(seed)
    data = []
    for route in ROUTES:
        for day in DAYS:
            for slot in TIME_SLOTS:
                total = np.random.randint(500, 1200)  # total demand per slot
                mahalaxmi = int(total * MAHALAXMI_RATIO)
                paid = total - mahalaxmi
                data.append({
                    "route": route["name"],
                    "day": day,
                    "slot": slot,
                    "paid_demand": paid,
                    "mahalaxmi_demand": mahalaxmi
                })
    return pd.DataFrame(data)
