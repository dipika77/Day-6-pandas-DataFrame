#Pandas Series and DataFrames

#instructions
'''Import pandas as pd.
Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
key 'country' and value names.
key 'drives_right' and value dr.
key 'cars_per_cap' and value cpc.
Use pd.DataFrame() to turn your dict into a DataFrame called cars.
Print out cars and see how beautiful it is.'''

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


#instructions
''' import CSV files you still need the pandas package: import it as pd.
Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
Print out cars. Does everything look OK?'''

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)



#instructions
'''Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame.
Use double square brackets to print out a DataFrame with both the country and drives_right
columns of cars, in this order.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])



#instructions
'''select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth observation, corresponding to row indexes
3, 4 and 5, and print them out.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])



#instructions
'''Use loc or iloc to select the observation corresponding to Japan as a Series.
The label of this row is JPN, the index is 2. Make sure to print the resulting Series.
Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. 
You can find out about the labels/indexes of these rows by inspecting cars. Make sure
to print the resulting DataFrame.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])


#instructions
'''Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns
country and drives_right.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])


# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])



#instructions
'''Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars['drives_right'])

# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[['cars_per_cap', 'drives_right']])


#Adding columns

#instructions
'''Add a new column to homelessness, named total, containing the sum of the individuals
and family_members columns.
Add another column to homelessness, named p_homeless, containing the proportion of the 
total homeless population to the total population in each state state_pop.'''

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_homeless col as proportion of total homeless population to the state population
homelessness["p_homeless"] = homelessness["total"]/homelessness["state_pop"]

# See the result
print(homelessness)


#instructions
'''Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals per 
ten thousand people in each state, using state_pop for state population.
Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt.
Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result. Look at the result.'''

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)



#summary statistics
#instructions
'''Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
Print information about the columns in sales.
Print the mean of the weekly_sales column.
Print the median of the weekly_sales column.'''

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())


#instructions
'''Print the maximum of the date column.
Print the minimum of the date column.'''

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())


#instructions
'''Use the custom iqr function defined for you along with .agg() to 
print the IQR of the temperature_c column of sales.
Update the column selection to use the custom iqr function with .agg()
to print the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.
Update the aggregation functions called by .agg(): include iqr and np.median in that order.'''

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))


# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))



#instructions
'''Sort the rows of sales_1_1 by the date column in ascending order.
Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.'''

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])



#Dropping duplicates

#instructions
'''Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, saving as holiday_dates.
Select the date column of holiday_dates, and print.'''

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset = ["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset =["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset = "date")

# Print date col of holiday_dates
print(holiday_dates["date"])


#instructions
'''Count the number of stores of each store type in store_types.
Count the proportion of stores of each store type in store_types.
Count the number of stores of each department in store_depts, sorting the counts in descending order.
Count the proportion of stores of each department in store_depts, sorting the proportions in descending order.'''

# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts["department"].value_counts(sort = True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)


#Grouped Summary Statistics
#instructions
'''Calculate the total weekly_sales over the whole dataset.
Subset for type "A" stores, and calculate their total weekly sales.
Do the same for type "B" and type "C" stores.
Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type.'''

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)



#instructions
'''Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.'''

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type =  sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)


#instructions
'''Group sales by "type" and "is_holiday", take the sum of weekly_sales, and store as sales_by_type_is_holiday.'''

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type","is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)


#instructions
'''Import numpy with the alias np.
Get the min, max, mean, and median of weekly_sales for each store type using .groupby() and .agg(). Store this as sales_stats. Make sure to use numpy functions!
Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l for each store type. Store this as unemp_fuel_stats.'''

# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]] .agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


#pivot table

#instructions
'''Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.
Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.'''

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type")

# Print mean_sales_by_type
print(mean_sales_by_type)


# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales", index = "type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)


# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values = "weekly_sales", index = "type", columns = "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)



#instructions
'''Print the mean weekly_sales by department and type, filling in any missing values with 0.
Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.'''

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value = 0, margins = True))

