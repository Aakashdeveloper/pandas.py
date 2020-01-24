import pandas as pd;

country = pd.read_csv('API_ILO_country_YU.csv')

country.to_html('data.html')