import matplotlib.pyplot as plt

month=['jan','feb','march','april','may','june','july','aug']
expence=[1200,1400,1000,290,10002,12300,271,3782]

# bar chart

plt.bar(month,expence)
plt.title("expence chart of 8 months")
plt.xlabel('month')
plt.ylabel('expence')
plt.show()

# line chart

plt.plot(month,expence)
plt.title("line chart of 8 month expence")
plt.xlabel("month")
plt.ylabel("expence")
plt.show()