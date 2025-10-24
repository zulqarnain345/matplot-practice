import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sale.csv")

# total price of products

df['Total']=df['Quantity']*df['Price']

print(df)
# total revenue generated
total_revenue_generated=df['Total'].sum(axis=0)
print(f"\nthe total revenue generated is {total_revenue_generated}\n")

# Category with Highest Revenue
category_revenue=df.groupby("Category")['Total'].sum()
highest_category=category_revenue.idxmax()
print(f"\nthe highest category is ::{highest_category}\n")

# top 3 products that earned the most money.

top_3=df.nlargest(3,'Total')
print(f"\nthe top 3 products earned the most money is\n{top_3}\n")

# sort by the total

sort=df.sort_values(by="Total",ascending=False).reset_index(drop=True)
print(sort)


# bar chart

plt.bar(df['Category'],df['Total'],color="blue")
plt.axhline(df["Total"].mean(),color="black",linestyle="--",linewidth=2,label="average")
plt.title("bar char of total ")
plt.xlabel("category")
plt.ylabel("total")
plt.grid(True,alpha=0.5,linestyle="--")
plt.legend()
plt.show()

# each product’s total

plt.bar(category_revenue.index,category_revenue.values,color="red")
plt.grid(True,linestyle="--",alpha=0.5)
plt.title("revensu by category")
plt.xlabel("category revenue by product name")
plt.legend()
plt.show()
# pie chart
plt.plot(df['Category'],df["Total"],color="black",marker='o')
plt.show()


# Save the final DataFram

df.to_csv("update.csv",index=True)
print("update sucessfullt!!")