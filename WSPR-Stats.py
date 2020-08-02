import pandas as pd

datafile = 'data/wsprspots-2020-08.csv.zip'
df = pd.read_csv(datafile)
df.columns = ['SpotID','Timestamp','Reporter','Reporter_Grid','SNR','Frequency','DX_Call','DX_Grid','Power','Drift','Distance','Azimuth','Band','Version','Code']
print(df.info())
# print(df.describe())
# print(df.head(10))
# print(df.tail(10))

print('Unique Stations',len(df['DX_Call'].unique()))
print('Active Bands',df['Band'].unique())
print('Total Reports:',len(df.index))

df_9v1rm = df[df['Reporter'] == '9V1RM']
# print(df.to_string())
print(df_9v1rm['DX_Call'].unique())
print('Unique Stations',len(df_9v1rm['DX_Call'].unique()))
print('Active Bands',df_9v1rm['Band'].unique())
print('Total Reports:',len(df_9v1rm.index))