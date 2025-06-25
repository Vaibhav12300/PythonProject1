import pandas
a=[10,20,30,40]
s=pandas.Series(a)
print(s)
print(type(s))
#---------------------------------------------------
import pandas as pd
data_set = {'fruits': ["Apple", "Orange", "Mango"],
            'passings': [3, 7, 2]
            }
mydata= pd.DataFrame(data_set)
print(mydata)

#----------------------------------------------------
import pandas as pd
print(pd.__version__)
#---------------------------------------------------
import pandas as pd
a=[10,20,30,40]
s=pd.Series(a,index={'a','b','c','d'})
print(s['a'])
print(type(s))
#--------------------------------------------------
import pandas as pd
qmarks= {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(qmarks,index=["day1","day2"])
print(myvar)
#---------------------------------------------------
import pandas as pd
ps=pd.Series([2,4,6,8,10])
print(ps)
print(type(ps))
print("convert pandas series to python list")
print(ps.tolist())
print(type(ps.tolist()))
#----------------------------------------------------
import pandas as pd
data={
"qmarks":[420,380,390],"duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)

#-------------------------------------------------------
import pandas as pd
data={
"qmarks":[420,380,390],"duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar.loc[0])
#---------------------------------------------------------
import pandas as pd
data={
"qmarks":[420,380,390],"duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar.loc[[0,1]])
#------------------------------------------------------------
import pandas as pd
data={
"qmarks":[420,380,390],"duration":[50,40,45]
}
myvar = pd.DataFrame(data,index=["day1", "day2", "day3"])
print(myvar)
#-------------------------------------------------------------
import pandas as pd
data={
"qmarks":[420,380,390],"duration":[50,40,45]
}
myvar = pd.DataFrame(data,index=["day1", "day2", "day3"])
print(myvar.loc["day2"])
#------------------------------------------------------------
import pandas as pd
df = pd.DataFrame({
    'Name': ['Abc', 'Bcd', 'Pqr', 'Xyz'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]},
    index=['r1', 'r2', 'r3', 'r4'])
print(df)
print()
df.index = [100, 200, 300, 400]
print(df)
#--------------------------------------------------------------
import pandas as pd
df = pd.DataFrame({
    'Name': ['Abc', 'Bcd', 'Pqr', 'Xyz'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]},
    index=['r1', 'r2', 'r3', 'r4'])
result = df.columns
print(result)
#-------------------------------------------------------------
import pandas as pd
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']],
columns=['col1', 'col2'])
result=df.iloc[1:3,:]
print(df)
print()
print(result)
#--------------------------------------------------------------------
import pandas as pd
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']],columns=['col1', 'col2'],
index=['r1','r2','r3','r4'])
print(df)
result=df.loc['r1':'r3','col1']
print(result)
#--------------------------------------------------------------------
import pandas as pd
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9,]}
df=pd.DataFrame(data)
col_A=df.loc[:,'A']
print(col_A)
cols_AB=df.loc[:,'A':'B']
print(cols_AB)
#---------------------------------------------------------------------
import pandas as pd
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']],
                  columns=['col1','col2'])
print(df)
df.iloc[1:3,1]=['x','y']
print(df)
#----------------------------------------------------------------------
import pandas as pd
df=pd.DataFrame({'A':[1,2,3,4,5],'B':[4,5,6,7,8],
                 'C':[9,10,11,12,0]},index=['r1','r2','r3','r4','r5'])
print(df)
result = df[df["C"] != 0]
print(result)


