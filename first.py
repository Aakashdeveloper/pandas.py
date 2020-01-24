import pandas as pd;

first_db = {'Day':[1,2,3,4,5,6], "User":[1000,5000,6000,500,400,1000], "Bounce_rate":[20,50,33,12,10,77]}

df = pd.DataFrame(first_db)

print(df)