import pandas as pd

df = pd.read_csv("covid_safety_measures.csv")
data = pd.read_csv("covid_cases_stats.csv")
data = data.fillna(0)
"""print(data.head())
print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns:{data.shape[1]}")

print("Columns:", data.columns)
print(data.describe())
print(data.info())"""
#Task #1
print("Task 1")
country_name = input("Enter the Name of country:").title()
matching_country = data[data["country"] == country_name]
if matching_country.empty:
    print("Country not found")
else:
    total_cases = matching_country.iloc[0]['total_cases']
    total_recovered = matching_country.iloc[0]['total_recovered']
    recover_ratio = total_recovered / total_cases
    print("Recovered/total ratio:{:.2f}".format(recover_ratio))

#Task #2
print("Task 2")
"""avg_death_rate = data["total_deaths"].dropna().iloc[:220].mean()
print("Death Average found around the globe:{:.2f}".format(avg_death_rate))"""

measures = input("Enter a safety measure:").capitalize()
safety_measure = df[df["measure"] == measures]
if safety_measure.empty:
    print(f"No security measure found for the {safety_measure}.")
else:
    countries = safety_measure["country"].unique()
    death = []
    for country in countries:
        country_data = data[data["country"] == country]
        if not country_data.empty:
            total_death = country_data[["total_deaths", "total_cases"]].iloc[0].tolist()
            if total_death[0] > 0:
                death.append(total_death)
    total_deaths = 0
    total_cases = 0
    for rate in death:
        total_deaths += rate[0]
        total_cases += rate[1]
    if total_cases > 0:
        avg_death_rate = (total_deaths / total_cases) * 100
        num_countries = len(death)
        print(f"{avg_death_rate:.2f}% death average found in {num_countries} countries.")
    else:
        print("No data found")

#Task 3
print("Task 3")
column_data = df["measure"]
top_safety_measure = column_data.value_counts().head(5)
measure = top_safety_measure.index.tolist()
country_names = {}
safety_efficiencies = []
#get values for each and store in dic
for i in measure:
    measures = df[df["measure"] == i]
    name = measures["country"].unique()
    country_names[i] = list(name)
for safety_measure in measure:
    total_recovered = 0
    total_cases = 0
    if safety_measure in country_names:
        countries = country_names.get(safety_measure)
        for n in countries:
            country_data = data[data["country"] == n]
            if not country_data.empty:
                recovered, cases = country_data[["total_recovered", "total_cases"]].iloc[0]
                total_recovered += recovered
                total_cases += cases
        if total_cases > 0:
            efficiency = (total_recovered / total_cases)
            safety_efficiencies.append((safety_measure, efficiency))
for measure, efficiency in safety_efficiencies:
    print(f"{measure},{efficiency:.2f}")