import pandas as pd
class StandardNormalization:
  def standardscalar(self,d):
    for i in d.columns:
      mean=d[i].mean()
      sd=d[i].std()      
      d[i]=(d[i]-mean)/sd     
    return d
data=pd.DataFrame([[20000,30],[25000,32],[30000,35],[37000,37]],columns=['Salary','Age'])
print("\nUtsukta Khatri Roll No:23321")
print("\nOriginal Data is")
print(data)
s=StandardNormalization()
df=s.standardscalar(data)
print("\nNormalized Data is")
print(df)