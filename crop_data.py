import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# TASK 1 a

#read file
df = pd.read_csv('bristol-air-quality-data.csv', sep=';')
df = df.convert_dtypes()

# print amount of lines in input file
print("The file bristol-air-quality-data.csv" + " has " + str(len(df.index)) + " lines.")

# change date variables to datetime
df['Date Time'] = pd.to_datetime(df['Date Time'],infer_datetime_format=True)
df['DateStart'] = pd.to_datetime(df['DateStart'],infer_datetime_format=True)
df['DateEnd'] = pd.to_datetime(df['DateEnd'],infer_datetime_format=True)

# drop data before 1 Jan 2020
df = df[~(df['Date Time']<pd.to_datetime("1/1/2010  0:00:0 AM", utc=True))]

# writing updated file
df.to_csv("bristol-air-quality-updated.csv", sep=';', index=0)

# print amount of lines in updated file
print("The bristol-air-quality-updated.csv" + " has " + str(len(df.index)) + " lines.")