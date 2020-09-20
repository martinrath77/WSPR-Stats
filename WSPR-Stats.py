import pandas as pd

datafile = 'data/wsprspots-2020-07.csv.zip'
datafile = '9v1rm.csv'

rows = 5000000
total_rows = 0
my_rows = 0
martin_df = pd.DataFrame()
for df in pd.read_csv(datafile,chunksize=rows):
    df.columns = ['SpotID','Timestamp','Reporter','Reporter_Grid','SNR','Frequency','DX_Call','DX_Grid','Power','Drift','Distance','Azimuth','Band','Version','Code']

    total_rows = total_rows + len(df.index)

    df_9v1rm = df[df['Reporter'] == '9V1RM']
    # print(df.to_string())
    print((df_9v1rm['DX_Call'].unique()).sort())
    print('Unique Stations',len(df_9v1rm['DX_Call'].unique()))
    print('Active Bands',df_9v1rm['Band'].unique())
    print('Total Reports:',len(df_9v1rm.index))
    my_rows = my_rows + len(df_9v1rm.index)
    martin_df = pd.concat([df_9v1rm, martin_df], ignore_index=True)


print(my_rows)
print(total_rows)
# martin_df.to_csv('9v1rm.csv',index=False,header=True)
print(martin_df.describe())