import pandas as pd
# Q1: Convert a list of date strings into a timeseries
date_list = ['2024-01-01', '2024-01-02', '2024-01-03']
date_series = pd.to_datetime(pd.Series(date_list))
data = pd.DataFrame({'Date': date_series, 'Marks': [10, 20, 30]})
data.set_index('Date', inplace=True)
print("Question 1 - Timeseries DataFrame:")
print(data)
#----------------------------------------------------------------------------
# Q2: Merge two DataFrames on common column 'ID'
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Amit', 'Rahul', 'Priya', 'Anjali']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Score': [78, 85, 90, 95]
})

inner_join = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Join Result:")
print(inner_join)

left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join Result:")
print(left_join)

right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join Result:")
print(right_join)

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')
index_join = df1_index.join(df2_index, how='right')
print("\nIndex-based Join using join():")
print(index_join)

df3 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Class': ['A', 'B', 'A'],
    'Student': ['Amit', 'Rahul', 'Priya']
})

df4 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Class': ['A', 'B', 'B'],
    'Marks': [88, 75, 82]
})

multi_key_merge = pd.merge(df3, df4, on=['ID', 'Class'], how='inner')
print("\nMerge on Multiple Keys:")
print(multi_key_merge)

#------------------------------------------------------------------------
# Q3: Concatenating and then merging
df_a = pd.DataFrame({'ID': [1, 2], 'Student': ['Amit', 'Rahul']})
df_b = pd.DataFrame({'ID': [3, 4], 'Student': ['Priya', 'Anjali']})
df_c = pd.DataFrame({'ID': [1, 2, 3, 4], 'Marks': [78, 82, 90, 85]})

combined = pd.concat([df_a, df_b], ignore_index=True)
final_merge = pd.merge(combined, df_c, on='ID')
print("\nFinal Result after Concatenation and Merge:")
print(final_merge)

# Last part: Difference between join() and merge()
print("\nDifference between df.join() and pd.merge():")
print("- df.join() joins on index, while pd.merge() joins on columns.")
print("- df.join() is simple for index-based joins.")
print("- pd.merge() is more flexible and used for column-based joins and multiple keys.")
