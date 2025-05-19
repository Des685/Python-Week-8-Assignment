# COVID-19 Data Analysis Project

## Overview

This project is a Python-based data analysis of COVID-19 data, using libraries like pandas, matplotlib, seaborn, and plotly. The script performs an exploratory analysis, focusing on trends in total cases, deaths, new cases, death rates, and vaccination progress for selected countries (Kenya, India, and the United States).  It also includes a choropleth map visualizing total cases by country.

## Features

* **Data Loading and Cleaning**: Loads data from a CSV file ('owid-covid-data.csv'), handles missing values, and filters data for specific countries.
* **Data Exploration**: Provides initial data overview, including column information and missing value counts.
* **Time Series Analysis**: Generates time series plots to visualize COVID-19 trends over time.
* **Choropleth Map**: Creates an interactive map showing the global distribution of total COVID-19 cases.
* **Key Metrics Calculation**: Computes important metrics like death rate and vaccination percentage.
* **Interactive Visualizations**: Uses plotly for interactive plots, allowing for better data exploration.

## Prerequisites

Before running the script, ensure you have the following installed:

* Python (version 3.6 or later)
* pandas
* matplotlib
* seaborn
* plotly

You can install the required packages using pip:

```bash
pip install pandas matplotlib seaborn plotly
How to UseDownload the Data: Download the 'owid-covid-data.csv' file from a reliable source (Our World in Data is a good option) and save it in the same directory as the Python script.Run the Script: Execute the Python script (e.g., main.py) in your Python environment.python main.py
View the Results: The script will:Print initial data exploration information to the console.Generate several plots showing COVID-19 trends. These plots will be displayed in your default web browser.Code DescriptionThe Python script consists of the following functions:load_and_clean_data(filename='owid-covid-data.csv'):Loads COVID-19 data from a CSV file.Handles potential FileNotFoundError.Converts the 'date' column to datetime.Filters data for Kenya, India, and the United States.Drops rows with missing 'total_cases' and 'total_deaths'.Fills missing numeric values using forward fill.Returns the cleaned DataFrame.create_plots(df):Calculates 'death_rate' and 'percent_vaccinated'.Generates interactive time series plots for:Total casesTotal deathsDaily new casesDeath rateTotal vaccinationsPercentage of population vaccinatedCreates a choropleth map of total COVID-19 cases on the latest date.Displays all plots.main():Calls load_and_clean_data() to load and preprocess the data.Calls create_plots() to generate and display the visualizations.Prints placeholder insights and observations to the console.Data SourceThe script uses COVID-19 data from the 'Our World in Data' dataset.  You can find the most up-to-date data here:Our World in Data: https://ourworldindata.org/coronavirus-source-dataInsights and ObservationsThe script provides a placeholder for insights and observations.  Here's what the script currently prints:--- Insights & Observations ---

1.  The United States had the highest number of total cases overall.
2.  India showed a sharp rise in new cases during mid-2021.
3.  Kenya had significantly lower vaccination coverage compared to the other two countries.
4.  Death rates remained below 3% for all countries as total cases increased.
5.  Vaccination rollouts correlated with a drop in new daily cases over time.
