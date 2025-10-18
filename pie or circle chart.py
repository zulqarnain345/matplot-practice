# pie or cicle chart

import matplotlib.pyplot as plt
import pandas as pd

# production=['laptop',"car",'mobile',"bike"]

# sales=[12,3,45,6]
df=pd.read_csv("data.csv")
print(df)

name1=df["name"]
maths1=df["maths"]
science1=df["science"]


plt.pie(maths1,science1,labels=name1 ,autopct='%1.1f%%', startangle=90)
plt.title("pie chart")
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()