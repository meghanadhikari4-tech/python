import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.DataFrame({
    "subject":[1,2,3,4],
    "marks":[90,65,78,56]
})
X=data[["marks"]]
Y=data["subject"]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
model=LinearRegression()
model.fit(X_train,Y_train)
prediction=model.predict([[6]])
print(prediction)
plt.scatter(X,Y,color="blue")
plt.plot(X,model.predict(X),color="red")
plt.xlabel("marks")
plt.ylabel("subject")
plt.show()
