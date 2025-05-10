import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv(r'C:\Users\Mokitha\OneDrive\Desktop\Data Science\Task 1\world_bank_population.csv')

# Step 2: Explore first few rows (optional)
print(df.head())

# Step 3: Pick the latest population column
# (You can adjust year based on your file, e.g., '2022' or '2021')
latest_year = '2022'  # Change this to match your dataset's latest year column

# Step 4: Drop rows with missing population data
df_clean = df[['Country Name', latest_year]].dropna()

# Step 5: Convert population column to numeric (safe)
df_clean[latest_year] = pd.to_numeric(df_clean[latest_year], errors='coerce')

# Step 6: Get top 10 countries by population
top10 = df_clean.sort_values(by=latest_year, ascending=False).head(10)

# Print top 10 countries by population
print("\nTop 10 countries by population:")
print(top10)

# Step 7: Plot - Bar chart for top 10 countries by population
plt.figure(figsize=(12,6))
sns.barplot(x=top10['Country Name'], y=top10[latest_year], palette='viridis')
plt.xticks(rotation=45)
plt.title(f'Top 10 Countries by Population in {latest_year}')
plt.xlabel('Country')
plt.ylabel('Population')
plt.tight_layout()
plt.show()

# Step 8: Plot - Pie chart for the proportion of population in the top 10 countries
plt.figure(figsize=(8, 8))
plt.pie(top10[latest_year], labels=top10['Country Name'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(top10)))
plt.title(f'Population Proportion of Top 10 Countries in {latest_year}')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Step 9: Statistical summary of the population data
population_summary = df_clean[latest_year].describe()
print("\nStatistical summary of population data:")
print(population_summary)

# Step 10: Get the bottom 10 countries by population
bottom10 = df_clean.sort_values(by=latest_year).head(10)

# Print bottom 10 countries by population
print("\nBottom 10 countries by population:")
print(bottom10)

# Step 11: Plot - Bar chart for bottom 10 countries by population
plt.figure(figsize=(12,6))
sns.barplot(x=bottom10['Country Name'], y=bottom10[latest_year], palette='magma')
plt.xticks(rotation=45)
plt.title(f'Bottom 10 Countries by Population in {latest_year}')
plt.xlabel('Country')
plt.ylabel('Population')
plt.tight_layout()
plt.show()

# Step 12: Plot - Histogram for population distribution across all countries
plt.figure(figsize=(12,6))
sns.histplot(df_clean[latest_year], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title(f'Population Distribution of All Countries in {latest_year}')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


