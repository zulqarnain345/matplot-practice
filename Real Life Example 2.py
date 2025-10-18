# Real-Life Example
# Let’s say you want to track your daily study hours for one week:

import matplotlib.pyplot as plt

day=['mon','tue','wed','thursday','friday','sat','sun']
hours=[3,2,1,3,0,3,4]

plt.figure(facecolor="yellow")
plt.bar(day,hours,color="black")
plt.title("daily hours study")
plt.xlabel("days")
plt.ylabel("hours")

plt.show()