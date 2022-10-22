import pandas as pd
header_list = ['IP-cím']
df = pd.read_csv('ip.txt', names=header_list)
print("Adatsorok az állományban: ", len(df.index) )

documentAddressesCount = 0      
itAccessoriesCount = 0          
localAddresssesCount = 0        

for index, row in df.iterrows():
    actualRow = (row['IP-cím'])
    if (actualRow.startswith('fc') or actualRow.startswith('fd')):
        localAddresssesCount += 1
    else:
        if actualRow.startswith('2001:0e'):
            itAccessoriesCount += 1
        else:
            if actualRow.startswith('2001:0db8'):
                documentAddressesCount += 1

print("Dokumentációs címek száma: ", documentAddressesCount )
print("IT eszközöknek kiosztott globális címek száma: ", itAccessoriesCount )
print("Eszközöknek kiosztott helyi egyedi címek száma: ", localAddresssesCount )
