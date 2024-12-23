import pandas as pd

# Read csv file
data = pd.read_csv("covid_cases_stats.csv")
df = pd.read_csv("covid_safety_measures.csv")
# Handel Nan values
data = data.fillna(0)
#Task 1
print("Task 1:Ratio of recovered patients over total cases for given country.")


def display_recovered_ratio(_a):
    #get the country from covid_case
    country_name = data[data["country"] == _a]
    if country_name.empty:
        print("country name not found")
    else:
        #get total_cases & total_recovered data of the country
        total_cases = country_name.iloc[0]['total_cases']
        total_recovered = country_name.iloc[0]['total_recovered']
        recover_ratio = total_recovered / total_cases
        print("Recovered/total ratio is:{:.2f}".format(recover_ratio))


a = input("Enter the Name of country:").title()
display_recovered_ratio(a)
#Task 2
print("Task 2:For a given safety measure, display the average death rate around the globe")


def average_death_rate(_b):
    # check for the safety_measure in measure
    safety_measure = df[df["measure"] == _b]
    if safety_measure.empty:
        print(f"No data found for {_b}")
    else:
        #get the unique country names of that measure
        countries = safety_measure['country'].unique()
        total_death = []
        # get the country data from covid_cases
        for country in countries:
            country_name = data[data["country"] == country]
            if not country_name.empty:
                death = country_name[['total_deaths', 'total_cases']].iloc[0].tolist()
                if death[0] > 0:
                    total_death.append(death)

        total_deaths = 0
        total_cases = 0
        for death_rate in total_death:
            total_deaths += death_rate[0]
            total_cases += death_rate[1]
        if total_cases > 0:
            avg_death_rate = (total_deaths / total_cases) * 100
            num_countries = len(total_death)
            print(f"{avg_death_rate:.2f}% Average death rate found in {num_countries}")
        else:
            print(f"No data found for {safety_measure}")


measure = input("Enter safety measure:").capitalize()
average_death_rate(measure)
#Task 3
print("Task 3:Display the efficiencies of 5 mostly adopted safety measures.")


def display_efficiencies():
    # get measure column
    measure_data = df["measure"]
    # search for top 5 measures
    top_safety_measure = measure_data.value_counts().head(5)
    #print(top_safety_measure)
    measure = top_safety_measure.index.tolist()
    #print(measure)
    country_names = {}
    safety_efficiencies = []
    #loop trough each measure and get country name
    for i in measure:
        measures = df[df["measure"] == i]
        name = measures["country"].unique()
        # safe the countries in dic
        country_names[i] = list(name)
    #print(country_names)
    #loop trough each measure
    for safety_measure in measure:
        total_recovered = 0
        total_cases = 0
        # check for the countries name for each measure and get names
        if safety_measure in country_names:
            countries = country_names.get(safety_measure)
            #check for countries in covid case file
            for n in countries:
                country_data = data[data["country"] == n]
                if not country_data.empty:
                    #get the data of recovered and total cases
                    recovered, cases = country_data[["total_recovered", "total_cases"]].iloc[0]
                    total_recovered += recovered
                    total_cases += cases
                    """print(recovered)
                    print(cases)"""

            if total_cases > 0:
                efficiency = (total_recovered / total_cases)
                safety_efficiencies.append((safety_measure, efficiency))

    for measures, efficiency in safety_efficiencies:
        print(f"{measures},{efficiency:.2f}")


display_efficiencies()
