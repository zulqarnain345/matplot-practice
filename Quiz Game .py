# Quiz Game
import random 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("quiz.csv")
Question1=df['Question'].tolist()
random.shuffle(Question1)
print(Question1)
