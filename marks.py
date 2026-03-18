from sklearn.linear_model import LinearRegression
X=[[1],[2],[3],[4],[5]]
y=[30,40,50,80,90]
model=LinearRegression()
model.fit(X,y)
hour=float(input("enter how many hours you studied: "))
predicted_marks=model.predict([[hour]])
print(f"based on your hours {hour} you may score {predicted_marks}")
print(predicted_marks)
from sklearn.linear_model import LogisticRegression
X=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]
model=LogisticRegression()
model.fit(X,y)
hour=float(input("enter how many hours hou studied: "))
result=model.predict([[hour]])
if result==1:
    print(f"based on {result} you are likely too pass")
else:
    print(f"based on {result} you are likely to fail")
from sklearn.neighbors import KNeighborsClassifier
X=[
    [100,5],
    [150,6],
    [200,7],
    [250,8],
    [300,9],
    [350,9.5]
]
#0=litchi #1=mango
y=[0,0,0,1,1,1]
model=KNeighborsClassifier()
model.fit(X,y)
weight=float(input("enter the value in grams:"))
height=float(input("enter the value in cm:"))
prediction=model.predict([[weight,height]])
if prediction==0:
    print(f"based on {prediction} it is likely an litchi")
else:
    print(f"based on {prediction} it is likely an mango")
    
