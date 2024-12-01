import time
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "output"

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def plot_launches_per_year(launches_per_year):
    """
    Plot launches per year.
    """
    filename = os.path.join(OUTPUT_DIR, 'launches_per_year.png')
    plt.figure(figsize=(9, 6))
    launches_per_year.plot(kind='bar', color='darkblue')
    plt.title('Space Mission Launches Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Launches')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    plt.close()
    print(f"Launches per year plot saved at {filename}")

def plot_cost_per_year(cost_per_year):
    """
    Plot average cost of missions per year.
    """
    filename = os.path.join(OUTPUT_DIR, 'cost_per_year.png')
    plt.figure(figsize=(9, 6))
    cost_per_year.plot(kind='line', marker='o', color='darkblue')
    plt.title('Average Mission Cost Per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Cost (in million USD)')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    plt.close()
    print(f"Cost per year plot saved at {filename}")