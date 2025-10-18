# histogram chart
import matplotlib.pyplot as plt

marks=[1,2,3,4,5,6,7,11,234,2,343,12,35,2,1,35,6,1000000]

plt.hist(marks,bins=5)
plt.title("histogram chart")
plt.xlabel("numbers")
plt.ylabel("marks")
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()