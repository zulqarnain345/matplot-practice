import matplotlib.pyplot as plt

student=['ali','zara','hassan','ahmed']
marks=[1,2,10,4]

# bar chart
# plt.bar(student,marks)
# plt.title(" bar student data chart")
# plt.ylabel("marks")
# plt.xlabel('students')
# plt.show()

# Horizontal Bar Chart (If you want the bars to go sideways (horizontal), use barh())

plt.barh(student,marks)
plt.title("horizontal bar chart")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()


# line chart 

plt.plot(student,marks ,color="darkred" ,marker=0,linestyle='--',linewidth=2)
plt.title("line chart")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()
