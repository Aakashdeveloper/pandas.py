import pandas as pd;
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

first_db = {'Day':[1,2,3,4,5,6], "User":[1000,5000,6000,500,400,1000], "Bounce_rate":[1020,2050,3300,1200,1000,7007]}

df = pd.DataFrame(first_db)

df.set_index("Day", inplace=True)

df.plot()
plt.show()
