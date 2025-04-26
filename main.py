from demand_forecasting import generate_demand
from optimization import optimize_allocation
from reporting import summary_report, plot_occupancy


def main():
    demand_df = generate_demand()
    results_df = optimize_allocation(demand_df)
    summary_report(results_df)
    plot_occupancy(results_df)

if __name__ == "__main__":
    main()
