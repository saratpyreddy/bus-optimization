import pandas as pd
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpInteger, value
from .config import ROUTES, TIME_SLOTS, DAYS, MIN_SERVICE

def optimize_allocation(demand_df):
    results = []
    for day in DAYS:
        for route in ROUTES:
            route_name = route["name"]
            buses_avail = route["buses"]
            fare = route["fare"]
            capacity = route["capacity"]

            prob = LpProblem(f"Bus_Allocation_{route_name}_{day}", LpMaximize)
            alloc = {}
            paid_seats = {}
            free_seats = {}

            for slot in TIME_SLOTS:
                key = (slot)
                alloc[slot] = LpVariable(f"buses_{slot}", 0, buses_avail, cat=LpInteger)
                paid_seats[slot] = LpVariable(f"paid_{slot}", 0, None, cat=LpInteger)
                free_seats[slot] = LpVariable(f"free_{slot}", 0, None, cat=LpInteger)

                slot_demand = demand_df[
                    (demand_df.route == route_name) & (demand_df.day == day) & (demand_df.slot == slot)
                ].iloc[0]

                # Constraints
                prob += paid_seats[slot] + free_seats[slot] <= alloc[slot] * capacity
                prob += paid_seats[slot] <= slot_demand["paid_demand"]
                prob += free_seats[slot] >= slot_demand["mahalaxmi_demand"]

            # Fleet and minimum service constraints
            prob += lpSum([alloc[slot] for slot in TIME_SLOTS]) <= buses_avail
            prob += lpSum([alloc[slot] for slot in TIME_SLOTS]) >= MIN_SERVICE[route_name]

            # Objective: maximize revenue (sum of paid seats * fare)
            prob += lpSum([paid_seats[slot] * fare for slot in TIME_SLOTS])

            prob.solve()

            for slot in TIME_SLOTS:
                results.append({
                    "day": day,
                    "route": route_name,
                    "slot": slot,
                    "buses_allocated": int(alloc[slot].varValue),
                    "paid_seats": int(paid_seats[slot].varValue),
                    "free_seats": int(free_seats[slot].varValue),
                    "revenue": int(paid_seats[slot].varValue) * fare
                })
    return pd.DataFrame(results)
