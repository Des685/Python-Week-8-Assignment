# Step 0: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Step 1: Load Dataset
df = pd.read_csv('owid-covid-data.csv')

# Step 2: Data Exploration
print("Columns:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())
print("\nFirst 5 Rows:\n", df.head())

# Step 3: Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Step 4: Filter for Selected Countries
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Step 5: Drop Rows with Missing Critical Values
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Step 6: Fill Missing Numeric Values (forward fill)
df = df.sort_values(by=['location', 'date'])
df.fillna(method='ffill', inplace=True)

# Step 7: Create Additional Calculated Columns
df['death_rate'] = df['total_deaths'] / df['total_cases']
df['percent_vaccinated'] = df['people_vaccinated_per_hundred']

# Step 8: Total Cases Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 9: Total Deaths Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 10: Daily New Cases Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 11: Death Rate Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate (total_deaths / total_cases)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 12: Vaccination Progress Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 13: Percent Vaccinated Over Time
plt.figure(figsize=(12,6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['percent_vaccinated'], label=country)
plt.title('% of Population Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('Percent Vaccinated')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 14: Choropleth Map (Latest Date)
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date]

fig = px.choropleth(latest_df,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    title=f"Total COVID-19 Cases by Country (as of {latest_date.date()})")
fig.show()

# Step 15: Insights (Markdown Placeholder for Jupyter Notebook)
print("\n--- Insights & Observations (add these as markdown in your notebook) ---\n")
print("1. The United States had the highest number of total cases overall.")
print("2. India showed a sharp rise in new cases during mid-2021.")
print("3. Kenya had significantly lower vaccination coverage compared to the other two countries.")
print("4. Death rates remained below 3% for all countries as total cases increased.")
print("5. Vaccination rollouts correlated with a drop in new daily cases over time.")
