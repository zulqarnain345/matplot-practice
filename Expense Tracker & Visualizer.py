import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("project 2.csv")
category_expense = df.groupby("Category", as_index=False)["Amount"].sum()

while True:
    print("1)ADD NEW DETAIL..")
    print("2)JUST CHECK THE DATA")
    print("3)Category wise Bar Chart")
    print("4)EXIT..")

    try:
        choice=int(input("enter the option in the form of numbers 1,2... "))
    except ValueError:
        print("choice the correct option...")
        continue
    if (choice==1):
        # add the new row..
        date = input("Enter the date: ")
        category = input("Enter the category: ")
        while True:
            try:
                amount = int(input("Enter the amount: "))
                break
            except Exception:
                print("plz enter the number not text....")

        description = input("Enter the description: ")

        # Create a new row with exact column names (match your CSV)
        new_row = {
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description
        }

        # Append the new row to the DataFrame
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        # Save back to the same CSV (optional)
        df.to_csv("project 2.csv", index=False)
        print("\nUpdated DataFrame:\n")


    elif choice==2:

        print(df)

        # total expense in 10 days 
        total_expense = df['Amount'].sum()
        print(f"\nThe total expense in 10 days is: {total_expense}\n")

        # bar chart of amount and date 
        plt.bar(df["Date"],df["Amount"],color="red")
        plt.axhline(df['Amount'].mean(),color="black",linestyle="--",linewidth=2,label="average")
        plt.title("bar chart which show the expence")
        plt.xlabel("date")
        plt.ylabel("amount")
        plt.grid(True,linestyle='--',alpha=0.5)
        plt.legend()
        plt.show() 


        
        print(category_expense) 


        plt.figure(figsize=(7,7))  

        plt.pie(category_expense["Amount"],labels=category_expense["Category"],autopct="%1.1f%%",startangle=90,pctdistance=0.75)
        plt.title("pie chart of expence ")
        plt.axis("equal")  
        plt.tight_layout()
        plt.show()

    # Category-wise Bar Chart
    elif choice==3:
        plt.bar(category_expense['Category'],category_expense["Amount"],color="greem")
        plt.axhline(category_expense['Amount'].mean(),color="red",label='Average',linestyle='--',linewidth=2)
        plt.grid(True,linestyle="--",alpha=0.5)
        plt.legend()
        plt.title("Category-wise Bar Chart")
        plt.xlabel("Category")
        plt.xticks(rotation=45)
        plt.ylabel("Amount")
        plt.show()
        

    elif choice==4:
        print("thanks for visting!!")
        exit()
        break
    


        



        


