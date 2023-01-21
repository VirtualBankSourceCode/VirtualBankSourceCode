# Something I will write someday --- after losing data twice

# Summary Glossary
# .mean()
# .median()
# .min()
# .max()
# .agg()
# .cumsum()
# .cummax()
# var.sort_values("column_name")
# var.drop_duplicates(subset="column_name") OR var.value_counts(subset=["column 1","column 2"])
# var.value_counts(sort=True)   
#
#
#


"""
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())
"""

#Exemplo de Function agregada
#.agg() method
"""
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))
"""

#A list of functions
#.
"""
# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))"""
### Will printout: (Arg defined in DataCamp DBT)
###      temperature_c  fuel_price_usd_per_l  unemployment
#iqr            16.583                 0.073         0.565
#median         16.967                 0.743         8.099
#

#Filtering Columns Manipulation
#
# Sort sales_1_1 by date
#sales_1_1 = sales_1_1.sort_values("date")
# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
#sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
# Get the cumulative max of weekly_sales, add as cum_max_sales col
#sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
