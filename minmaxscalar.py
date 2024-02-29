import pandas as pd
class MinMaxNorm:
  def scale(self,d):
    for i in d.columns:
      min=d[i].min()
      max=d[i].max()
      d[i]=(d[i]-min)/(max-min)
    return d
data=pd.DataFrame([[20000,30],[25000,32],[30000,35],[37000,37]],columns=['Salary','Age'])
print("Original Data")
print(data)
s=MinMaxNorm()
print("\nScaled Data")
df=s.scale(data)
print(df)