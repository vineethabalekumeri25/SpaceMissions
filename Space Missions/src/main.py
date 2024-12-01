from data_loader import load_data
from data_analysis import analyze_launches_per_year, analyze_cost_per_year
from utils import save_summary_to_file
import matplotlib.pyplot as plt
from visualizations import plot_launches_per_year, plot_cost_per_year
import os

# Define the output directory path
OUTPUT_DIR = 'output'

# Check if the output directory exists, if not create it
try:
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Directory '{OUTPUT_DIR}' created successfully.")
    else:
        print(f"Directory '{OUTPUT_DIR}' already exists.")
except Exception as e:
    print(f"Error creating directory: {e}")

def main():
    # Load the data
    df = load_data("D:/PyCharmProjects/Space Missions/data/mission_launches.csv")

    # Save the mission details as a CSV file in the output directory
    output_file_path = os.path.join(OUTPUT_DIR, 'mission_details.csv')
    df.to_csv(output_file_path, index=False)
    print(f"Mission details saved to: {output_file_path}")

    # Analyze launches per year
    launches_per_year = analyze_launches_per_year(df)
    print("Launches per year:\n", launches_per_year)

    # Plot the launches per year
    """
    Plot the number of launches per year.
    """
    # Analyze cost per year
    mean_cost_per_year = analyze_cost_per_year(df)
    print("Average mission cost per year:\n", mean_cost_per_year)

    """
    Plot the number of launches per year and plot the average cost of missions per year.
    """
    plot_launches_per_year(launches_per_year)
    plot_cost_per_year(mean_cost_per_year)

    # Save analysis summary
    summary = (
        "Space Missions Analysis Summary\n"
        f"Total Launches: {len(df)}\n"
        f"Unique Years: {len(launches_per_year)}\n"
        f"Launches Per Year:\n{launches_per_year}\n"
        f"Average Cost Per Year:\n{mean_cost_per_year}\n"
        "Notes:\n"
        "- Data includes space missions from the loaded dataset.\n"
        "- Launches per year provide a historical trend of space missions.\n"
        "- Average cost per year calculated in USD (converted from the 'Price' column).\n"
        "- Any missing or invalid values were handled during data cleaning.\n"
    )
    save_summary_to_file(summary, os.path.join(OUTPUT_DIR, 'analysis_summary.txt'))

if __name__ == "__main__":
    main()