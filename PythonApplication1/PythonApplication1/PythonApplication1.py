import pandas as pd
header_list = ['Ip-cím']
df = pd.read_csv('ip.txt', names = header_list)

print('Adatsorok az állományban: ', len(df.index))
