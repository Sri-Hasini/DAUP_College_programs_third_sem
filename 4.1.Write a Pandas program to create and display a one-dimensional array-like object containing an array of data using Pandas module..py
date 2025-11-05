# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
data = [18,45,7,33,17,333]
series = pd.Series(data)
print(series)
