import pandas as pd;


first_db = {'Day':[1,2,3,4,5,6], "User":[1000,5000,6000,500,400,1000], "Bounce_rate":[1020,2050,3300,1200,1000,7007]}

df = pd.DataFrame(first_db)

df = df.rename(columns={"User":"Visitors"})

print(df)
