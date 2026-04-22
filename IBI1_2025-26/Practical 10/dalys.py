import os                  # os: work with files and directories
import pandas as pd        # pandas（DataFrame）
import matplotlib.pyplot as plt  # matplotlib：draw plots and charts
import numpy as np         # numpy：mathematical operations and array handling

# os.chdir() ：Change the working Directory）
os.chdir("/Users/hyq-mac/Desktop/2026春夏学期资料/IBI/IBI1_2025-26/Practical 10")

# Optional inspection steps
# os.getcwd() :Get Current Working Directory
current_path = os.getcwd()
# os.listdir() :List all Directory under this working directory
files_in_dir = os.listdir()

# Read the CSV file as a DataFrame
# pd.read_csv() read file and convert to pandas DataFrame
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# check the head of the DataFrame to verify whether data is read successfully 
# DataFrame.head() view the first n rows of the DataFrame 
print("\nHead 5 of the data:")
print(dalys_data.head(5)) 

# check the info of the DataFrame
# DataFrame.info() View overall information such as column names, data types, and the number of non-null values of the DataFrame.
print("\n Overall Information:")
dalys_data.info()

# check DataFrame's statistical information
# DataFrame.describe() function meaning: calculate statistics for numeric columns (count, mean, std, min/max, quartiles)
print("\nData Statistics:")
print(dalys_data.describe())


# find 2019 countries that have the highest and lowest DALYs
# loc :DataFrame.loc[condition of column, columns to select]
# bool check：create a True/False list, True means the Year is 2019
year_2019_bool = dalys_data["Year"] == 2019
# year_2019_bool + ["Entity", "DALYs"]
data_2019 = dalys_data.loc[year_2019_bool, ["Entity", "DALYs"]]
data_2019 = data_2019.reset_index(drop=True)

# DataFrame.idxmax() find the maximum value's row index
# DataFrame.idxmin() find the minimum value's row index
max_daly_idx = data_2019["DALYs"].idxmax()  # return the row index
min_daly_idx = data_2019["DALYs"].idxmin()  
country_max = data_2019.iloc[max_daly_idx, 0]
country_min = data_2019.iloc[min_daly_idx, 0]

print("="*70)
print(f"highest: {country_max}")
print(f"lowest: {country_min}")
print("="*70)


# draw
country_bool = dalys_data["Entity"] == country_max  
country_data = dalys_data.loc[country_bool, ["Year", "DALYs"]]  

plt.figure(figsize=(8, 5), dpi=150)

plt.plot(country_data["Year"], country_data["DALYs"], 'b+', markersize=8, label=country_max)


plt.xlabel("Year", fontsize=11)
plt.ylabel("DALYs (Disability-Adjusted Life Years)", fontsize=11)
plt.title(f"DALYs Over Time: {country_max}", fontsize=13, fontweight="bold")
plt.xticks(rotation=-90)  
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 【Show 3rd & 4th columns for first 10 rows】
# iloc: access data by row/column index (Python counts from 0)
# Rows: first 10 rows → 0:10 (left-closed, 0-9 total 10 rows)
# Columns: 3rd=Year(index2), 4th=DALYs(index3) → 2:4
print("\n" + "="*70)
print("Required Task 1: 3rd & 4th columns (Year & DALYs) for first 10 rows")
first_10_year_daly = dalys_data.iloc[0:10, 2:4]
print(first_10_year_daly)

# Find the year with max DALYs in Afghanistan's first 10 years
# Boolean filter: get all Afghanistan data
afghanistan_bool = dalys_data["Entity"] == "Afghanistan"
afghanistan_data = dalys_data.loc[afghanistan_bool, ["Year", "DALYs"]]
# Get first 10 years of data
afghanistan_first_10 = afghanistan_data.iloc[0:10, :]
# Find max DALYs year
afghan_max_idx = afghanistan_first_10["DALYs"].idxmax()
afghan_max_year = afghanistan_first_10.loc[afghan_max_idx, "Year"]
# Comment for marking: Year with max DALYs in Afghanistan's first 10 years is afghan_max_year
print(f"\nYear with maximum DALYs in Afghanistan's first 10 years: {afghan_max_year}")
print("="*70)

# 【Boolean filter for Zimbabwe's all-year data】
# loc: access data by column name + row condition
print("\n" + "="*70)
print("Required Task 2: Zimbabwe's all-year DALYs data")
# Boolean filter: True when Entity is Zimbabwe
zimbabwe_bool = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[zimbabwe_bool, ["Year", "DALYs"]]
print(zimbabwe_data.head())

# Get first and last year of Zimbabwe's data
zimbabwe_first_year = zimbabwe_data["Year"].min()
zimbabwe_last_year = zimbabwe_data["Year"].max()
# Comment for marking: First year of Zimbabwe's data is zimbabwe_first_year, last year is zimbabwe_last_year
print(f"\nFirst year of Zimbabwe's DALYs data: {zimbabwe_first_year}")
print(f"Last year of Zimbabwe's DALYs data: {zimbabwe_last_year}")
print("="*70)

# 【Code for question.txt】
# Question: What is the distribution of DALYs across all countries in 2019?
print("\n" + "="*70)
print("Required Task 3: 2019 DALYs distribution across all countries")
# Plot histogram (same style as your original plot)
plt.figure(figsize=(8, 5), dpi=150)
plt.hist(data_2019["DALYs"], bins=20, color="#2E86AB", edgecolor="black", alpha=0.7)
plt.xlabel("DALYs Value", fontsize=11)
plt.ylabel("Number of Countries", fontsize=11)
plt.title("DALYs Distribution Across All Countries (2019)", fontsize=13, fontweight="bold")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Simple statistics for result discussion
daly_2019_mean = data_2019["DALYs"].mean()
daly_2019_median = data_2019["DALYs"].median()
print(f"2019 Global DALYs Mean: {daly_2019_mean:.2f}")
print(f"2019 Global DALYs Median: {daly_2019_median:.2f}")
print("="*70)

# 【Extra Custom Function】
# Match your coding style: clear English comments, use loc/iloc/plot as you did
# Function: Plot DALYs trend for any country, return key statistics
def plot_country_daly_trend(dalys_df, country_name):
    """
    Extra function: Plot DALYs time trend for a single country, return core statistics
    Parameters:
        dalys_df: full DALYs dataframe (your dalys_data)
        country_name: name of the target country (string, e.g. "China")
    Returns:
        stats_dict: dictionary with mean/max/min DALYs and corresponding years
    """
    # Boolean filter to get target country data (same as your code logic)
    country_filter = dalys_df["Entity"] == country_name
    country_full_data = dalys_df.loc[country_filter, ["Year", "DALYs"]]
    
    # Handle no data case
    if country_full_data.empty:
        print(f"Warning: No data found for {country_name}")
        return None
    
    # Calculate core statistics
    daly_mean = country_full_data["DALYs"].mean()
    daly_max = country_full_data["DALYs"].max()
    daly_min = country_full_data["DALYs"].min()
    year_max = country_full_data.loc[country_full_data["DALYs"].idxmax(), "Year"]
    year_min = country_full_data.loc[country_full_data["DALYs"].idxmin(), "Year"]
    
    # Plot with the EXACT same style as your original code
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(country_full_data["Year"], country_full_data["DALYs"], 'bo', markersize=6, label=country_name)
    plt.xlabel("Year", fontsize=11)
    plt.ylabel("DALYs (Disability-Adjusted Life Years)", fontsize=11)
    plt.title(f"DALYs Over Time: {country_name}", fontsize=13, fontweight="bold")
    plt.xticks(rotation=-90)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Return statistics as a structured dictionary
    stats_dict = {
        "country": country_name,
        "mean_daly": round(daly_mean, 2),
        "max_daly": round(daly_max, 2),
        "year_of_max_daly": year_max,
        "min_daly": round(daly_min, 2),
        "year_of_min_daly": year_min
    }
    return stats_dict

# Example of using the extra function 
print("\n" + "="*70)
print("Extra Function Example: China's DALYs Analysis Result")
china_daly_stats = plot_country_daly_trend(dalys_data, "China")
print(china_daly_stats)
print("="*70)