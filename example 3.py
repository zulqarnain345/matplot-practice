import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")

average_math=df['maths'].mean()
print(average_math)
maths1=df['maths']
name1=df['name']
# bar chart of maths marks
above_avg = df[df['maths'] > average_math]
below_avg = df[df['maths'] <= average_math]
plt.scatter(above_avg['name'], above_avg['maths'], color='green', s=100, label='Above Average')
plt.scatter(below_avg['name'], below_avg['maths'], color='red', s=100, label='Below Average')

plt.axhline(y=average_math, color='red', linestyle='--', label=f'Average = {average_math:.2f}')

plt.bar(name1,maths1)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()

print(df)
