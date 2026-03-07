import pandas as pd
sale=pd.DataFrame({
    "no":[1,2,3],
    "product":["mobile","laptop","tv"],
    "sales":[50,60,80]

})
data=pd.DataFrame({
    "no":[1,2,3],
    "used":["student","engineers","parent"]

})
merged=pd.merge(sale,data,on="no")
print(merged)