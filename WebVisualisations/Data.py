import pandas as pd
from sqlalchemy import false

# Read in the csv file 
df = pd.read_csv('resources/city_data.csv')

# Save to html file
df.to_html('data.html', index=false)

# Assign to string
table = df.to_html()

print(table)