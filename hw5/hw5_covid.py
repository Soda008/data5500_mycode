#Please see my 7 step instructions at the bottom to make sure this runs properly.
import cloudscraper  # pip install cloudscraper
import json
import os

# Create scraper to handle Cloudflare
scraper = cloudscraper.create_scraper()

# Load state/territory codes from a text file
try:
    with open("state_names.txt") as file:  # Make sure this file exists in the same folder
        state_list = [line.strip().lower() for line in file.readlines()]
except FileNotFoundError:
    print("File 'state_names.txt' not found.")
    exit()

# Ensure JSON output folder exists
json_folder = "json_states"
os.makedirs(json_folder, exist_ok=True)

# Class to store and calculate COVID statistics for a state
class CovidDataState:
    def __init__(self, state, covid_list):
        self.state = state
        self.covid_list = covid_list

    def calc_avg_cases(self):
        total_cases = sum(int(day.get("positiveIncrease", 0)) for day in self.covid_list)
        return round(total_cases / len(self.covid_list))

    def calc_max_day(self):
        max_day = max(self.covid_list, key=lambda day: int(day.get("positiveIncrease", 0)))
        return max_day["date"]

    def calc_no_cases(self):
        # Return the most recent day with 0 new cases
        for day in self.covid_list:
            if int(day.get("positiveIncrease", 0)) == 0:
                return day["date"]
        return "None"

    def calc_max_month(self):
        monthly_cases = {}
        for day in self.covid_list:
            date_str = str(day.get("date"))
            year = date_str[:4]
            month = date_str[4:6]
            key = f"{year}-{month}"
            monthly_cases[key] = monthly_cases.get(key, 0) + int(day.get("positiveIncrease", 0))
        max_key = max(monthly_cases, key=monthly_cases.get)
        year, month = max_key.split('-')
        month_name = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December'][int(month) - 1]
        return f"{month_name} {year}"

    def calc_min_month(self):
        monthly_cases = {}
        for day in self.covid_list:
            date_str = str(day.get("date"))
            year = date_str[:4]
            month = date_str[4:6]
            key = f"{year}-{month}"
            monthly_cases[key] = monthly_cases.get(key, 0) + int(day.get("positiveIncrease", 0))
        min_key = min(monthly_cases, key=monthly_cases.get)
        year, month = min_key.split('-')
        month_name = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December'][int(month) - 1]
        return f"{month_name} {year}"

# Loop through all states/territories
for state in state_list:
    url = f"https://api.covidtracking.com/v1/states/{state}/daily.json"
    response = scraper.get(url)
    covid_list = response.json()

    # Save JSON file for each state
    with open(os.path.join(json_folder, f"{state}.json"), "w") as json_file:
        json.dump(covid_list, json_file, indent=2)

    # Print statistics for this state
    print(f"\nCovid confirmed cases statistics\nState: {state.upper()}")
    state_obj = CovidDataState(state, covid_list)
    print("Average number of new daily confirmed cases:", state_obj.calc_avg_cases())
    print("Date with highest new number of covid cases:", state_obj.calc_max_day())
    print("Most recent date with no new covid cases:", state_obj.calc_no_cases())
    print("Month and Year with highest new number of covid cases:", state_obj.calc_max_month())
    print("Month and Year with lowest new number of covid cases:", state_obj.calc_min_month())



#If you want to run this code again, run the following code, step by step, in the terminal:
#1. Open the terminal in your VS Code environment.
#2. Navigate to the hw5 folder where the Python script is located:
    #cd /home/ubuntu/data5500_mycode/hw5
#3.Activate the Python virtual environment (so the required packages like cloudscraper are available):
    #source venv/bin/activate
        #After this, your terminal prompt should have (venv) at the beginning.
#4.Ensure the state_names.txt file exists in the same folder as the script. This file should contain all the state/territory codes, one per line, like:
#5.Run the Python script:
    #python hw5_covid.py
#6.Observe the output:
    #The terminal will display the COVID stats for each state.
    #JSON files for each state will be saved in json_states/ inside the hw5 folder.
#7.Optional – deactivate the virtual environment after running:
    #deactivate