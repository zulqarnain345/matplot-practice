# Student Marks Analyzer 

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("111.csv")

# sum of all subjects

df['TotalMarks']=df[['Math','Science','English','Computer','Physics']].sum(axis=1)

# average of the class
average_of_class=df['TotalMarks'].mean().round(2)
print(f"the average of the class is {average_of_class}")
 
top_3=df.nlargest(3,'TotalMarks')
top_3_least=df.nsmallest(3,'TotalMarks')

# top students in subjects and least students gets marks in subjects

top_3_maths=df.nlargest(3,"Math")
top_3_least_maths=df.nsmallest(3,"Math")

def get_colors(subject):
    top = df.nlargest(3, subject)
    bottom = df.nsmallest(3, subject)
    colors = []
    for name in df['Name']:
        if name in top['Name'].values:
            colors.append('green')      
        elif name in bottom['Name'].values:
            colors.append('red')        
        else:
            colors.append('skyblue')   
    return colors 
# graph of the total marks and the student which score higher then average mark by line
plt.bar(df['Name'],df['TotalMarks'],color=get_colors('TotalMarks'))
plt.title("TOTAL MARKS")
plt.xlabel("MARKS")
plt.ylabel("NAMES")
plt.axhline(y=average_of_class,color="black",linestyle="--",linewidth=2,label="average")
plt.grid(True,linestyle="--",alpha=0.5)
plt.legend()
plt.show()


# chart of subject maths 

subjects = ['Math', 'Science', 'English', 'Computer', 'Physics']
for subject in subjects:
    avg = df[subject].mean().round(2)
    plt.bar(df['Name'],df[subject],color=get_colors(subject))
    plt.axhline(y=avg,color="black",linestyle="--",linewidth=2,label="average of maths")
    plt.title(f"{subject} SUBJECT CHART")
    plt.xlabel("NAMES")
    plt.ylabel("MARKS")
    plt.grid(True,linestyle="--",alpha=0.5)
    plt.legend()
    plt.show()


# line chart of total marks

plt.plot(df['Name'],df['TotalMarks'],color="red",marker='o')
plt.axhline(y=average_of_class,color="black",linestyle="--",linewidth=2,label="average")
plt.title("line chart of total marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.legend()
plt.grid(True,linestyle="--",alpha=0.2)
plt.show()


# line charts for all the subject also

subjects=['Math','Science','English','Computer','Physics']

for subject in subjects:
    avg=df[subject].mean().round(2)
    plt.plot(df['Name'],df[subject],color="red",marker="o")
    plt.axhline(y=avg,color="black",linestyle="--",linewidth=2,label="average")
    plt.title(f"LINE CHARTS FOR {subject}")
    plt.xlabel("NAME")
    plt.ylabel("MARKS")
    plt.legend()
    plt.grid(True,linestyle="--",alpha=0.2)
    plt.show()




# attendance report

short_attendance=df[(df['Attendance']>8)]
print(f"\n these students have short attendance\n{short_attendance}")


# pie chart

plt.pie(df['Attendance'],labels=df['Name'],autopct='%1.1f%%',startangle=90)
plt.show()


# persantage of total marks

df['Persantage']=(df['TotalMarks']*100)/500

df['Rank'] = df['TotalMarks'].rank(ascending=False).astype(int)

# grade

def grade(Persantage):
    if Persantage>90:
        return "A+"
    elif Persantage>80:
        return "A"
    elif Persantage>70:
        return "B+"
    elif Persantage>60:
        return "B"
    elif Persantage>50:
        return "C"
    elif Persantage>40:
        return "D"
    else:
        return "F"
    
df["Grade"]=df['Persantage'].apply(grade)   
 
# sorting the marks
sort=df.sort_values(by='TotalMarks',ascending=False).reset_index(drop=True)
print(sort)

# garde distribution
grade_counts = df['Grade'].value_counts()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Grade Distribution")
plt.show()


# horizantal bar chart of top 3 students

top_5 = df.nlargest(3, 'TotalMarks')
plt.barh(top_5['Name'], top_5['TotalMarks'], color='green')
plt.title("Top 3 Students by Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Students")
plt.gca().invert_yaxis()
plt.show()

# horizantal bar chart of least 3 students
least_3=df.nsmallest(3,'TotalMarks')
plt.barh(least_3['Name'],least_3['TotalMarks'],color="red")
plt.title("least 3 students by total marks")
plt.xlabel("TOTAL MARKS")
plt.ylabel("STUDENTS")
plt.gca().invert_yaxis()
plt.show()


#Attendance vs Performance Scatter Plot

plt.scatter(df['Attendance'], df['TotalMarks'], color='purple', s=100, edgecolors='black')
plt.title("Attendance vs Performance")
plt.xlabel("Attendance (Days)")
plt.ylabel("Total Marks")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# search and show the results of that student 
search_data=input("enter the name of the student you want to search the result")
data=df.loc[df['Name']==search_data]
print(data.value[0])


# Save the final analyzed dataset

df.to_csv("update.csv")
print("data save in to update file")

# Save All Charts Automatically
plt.savefig(f"{subjects}_chart.png")

