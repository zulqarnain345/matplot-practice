# Library Management 

import pandas as pd
df=pd.read_csv("Book1.csv")
while True:
        print("1) ADD NEW BOOK...")
        print("2)View All Books...")
        print("3)Borrow a Book..")
        print("5)Exit..")
        try:
            choice=int(input("enter the option:: "))
        except ValueError:
             print("choice the correct option....")    
        if choice==1:

            #  Add New Book
            try:
                bookid=int(input("enter the book id:: "))
            except ValueError:
                 print("plz enter the book id in the form of number...")
                 break    
            title=input("enter the book title:: ")
            author=input("enter the author name:: ")
            available="Yes"
            borrower="NaN"

            # create a new row with exact colum

            new_row={
                    "BookID":bookid,
                    "Title":title,
                    "Author":author,
                    "Available":available,
                    "Borrower":borrower
            }

            # append the new new_row to the data frame

            df=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)

            # save to the same file 

            df.to_csv("Book1.csv",index=False)
            print("\n update data frame\n")

        elif choice==2:
             print("\n",df,"\n")  


        elif choice==3:
            # Borrow a Book 

            book_name=input("enter the book name you want to borrow:: ").lower().strip()
            
            # search by row 
            if book_name in df['Title'].values:
        # Get the index of the matching book

                index = df.index[df['Title'] == book_name][0]
        # Check if available

                if df.at[index, 'Available'] == 'Yes':
                    borrower = input("Enter your name: ")
                    df.at[index, 'Available'] = 'No'
                    df.at[index, 'Borrower'] = borrower
                    df.to_csv("Book1.csv", index=False)
                    print(f"\n'{book_name}' borrowed successfully by {borrower}!\n")
                else:
                    print(f"\nSorry, '{book_name}' is already borrowed by {df.at[index, 'Borrower']}.\n")
            else:
                print("\nBook not found in the library.\n")

                 
             
 

        elif choice==5:
            print("thanks for visting!!")
            exit()

