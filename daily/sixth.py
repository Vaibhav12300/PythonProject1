import pandas as pd
data={'A':[1,2,3],'B':[4,5,6]}
df=pd.DataFrame(data)
print(df)
#print("\n addition \n",df+5.2)
# print("\n subtraction \n",df-5)
# print("\n multiplication \n",df*5)
df['C']=df['A']+df['B']
print(df)
#-----------------------------------------------------------
import pandas as pd
df1=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
df2=pd.DataFrame({'A':[10,20,30],'B':[50,60,70]},index=[0,1,2])
print(df1)
print(df2)
print("\n Addition of 2 dataframes\n",df1+df2)
print("\n Subtraction of 2 dataframes\n",df1-df2)
print("\n Division of 2 dataframes\n",df1/df2)
#------------------------------------------------------------------
import pandas as pd
one=pd.DataFrame({
    'Name':['A1','A2','A3','A4','A5'],
    'subject':['sub1','sub2','sub3','sub4','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
two=pd.DataFrame({
'Name':['B1','B2','B3','B4','B5'],
    'subject':['sub2','sub4','sub3','sub6','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
res=pd.concat([one,two])
print(res)
#----------------------------------------------------------
import pandas as pd
one=pd.DataFrame({
    'Name':['A1','A2','A3','A4','A5'],
    'subject':['sub1','sub2','sub3','sub4','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
two=pd.DataFrame({
'Name':['B1','B2','B3','B4','B5'],
    'subject':['sub2','sub4','sub3','sub6','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
res=pd.concat([one,two],keys=['a','b'])
print(res)
#--------------------------------------------------------
import pandas as pd
one=pd.DataFrame({
    'Name':['A1','A2','A3','A4','A5'],
    'subject':['sub1','sub2','sub3','sub4','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
two=pd.DataFrame({
'Name':['B1','B2','B3','B4','B5'],
    'subject':['sub2','sub4','sub3','sub6','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
res=pd.concat([one,two],keys=['a','b'],ignore_index=True)
print(res)
#--------------------------------------------------------------
import pandas as pd
one=pd.DataFrame({
    'Name':['A1','A2','A3','A4','A5'],
    'subject':['sub1','sub2','sub3','sub4','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
two=pd.DataFrame({
'Name':['B1','B2','B3','B4','B5'],
    'subject':['sub2','sub4','sub3','sub6','sub5'],
    'marks':[89,80,79,97,88]},
    index=[1,2,3,4,5])
res=pd.concat([one,two],axis=1)
print(res)
#---------------------------------------------------------------
import pandas as pd
left=pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['A1','A2','A3','A4','A5'],
    'subject':['sub1','sub2','sub3','sub4','sub5'],
},
    index=[1,2,3,4,5])
right=pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['B1','B2','B3','B4','B5'],
    'subject':['sub2','sub4','sub3','sub6','sub5'],
},
    index=[1,2,3,4,5])
res=left.merge(right,on='id')
print(res)
#-------------------------------------------------------------
import pandas as pd
left=pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['A1','A2','A3','A4','A5'],
    'subject_id':['sub1','sub2','sub3','sub4','sub5'],
},
    index=[1,2,3,4,5])
right=pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['B1','B2','B3','B4','B5'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
},
    index=[1,2,3,4,5])
res=left.merge(right,on='id'and'subject_id')
print(res)