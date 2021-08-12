import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# TASK 1 b
df = pd.read_csv('bristol-air-quality-updated.csv', sep=';')

pattern = {
            188 : 'AURN Bristol Centre',
            203 : 'Brislington Depot',
            206 : 'Rupert Street',
            209 : 'IKEA M32',
            213 : 'Old Market',
            215 : 'Parson Street School',
            228 : 'Temple Meads Station',
            270 : 'Wells Road',
            271 : 'Trailer Portway P&R',
            375 : 'Newfoundland Road Police Station',
            395 : "Shiner's Garage",
            452 : 'AURN St Pauls',
            447 : 'Bath Road',
            459 : 'Cheltenham Road \ Station Road',
            463 : 'Fishponds Road',
            481 : 'CREATE Centre Roof',
            500 : 'Temple Way',
            501 : 'Colston Avenue'
        }


# finding wrong and mismatched SiteIds
listOfUnexpectedSiteIDs = list(set(df['SiteID'].unique())-set(pattern.keys()))
duds = []

for i in listOfUnexpectedSiteIDs:
    duds = duds + df.index[(df['SiteID'].astype(str)==str(i))].tolist()
for k,v in pattern.items():
    if not df[(df['SiteID']==k) & (df['Location'].astype(str)!=v)].empty:
        duds = duds + df.index[(df['SiteID']==k) & (df['Location'].astype(str)!=v)].tolist()

# Printing dud records
print('Dud records: ')
df['SiteID'] = df['SiteID'].astype(pd.Int64Dtype()) # preventing changing dtype

for dud in duds:
    print(df['SiteID'][dud], ' did not match ', df['Location'][dud], ' at line ', dud)

# printing amount of lines to be removed because od SiteID
print(len(duds), ' lines found in total.')
        
# drop dud records
df.drop(index = duds, inplace=True)

# replacing geo_piont_2d with seperate variables: latitude and longitude to have one information in one column
df[['Latitude','Longitude']] = df['geo_point_2d'].str.split(",", expand=True)
df.drop(columns='geo_point_2d',inplace=True)

# changing format of dates in dataset to format default in SQL
df['DateStart'] = df['DateStart'].astype('datetime64[ns]').dt.strftime('%Y-%m-%d %H:%M:%S')
df['DateEnd'] = df['DateEnd'].astype('datetime64[ns]').dt.strftime('%Y-%m-%d %H:%M:%S')
df['Date Time'] = df['Date Time'].astype('datetime64[ns]').dt.strftime('%Y-%m-%d %H:%M:%S')

# printing amount of lines after removing data before 1 Jan 2010 and wrong SiteIDs
index = df.index
numberOfRows_updated = len(index)
print('There are ', numberOfRows_updated, ' rows in cleaned file bristol-air-quality-updated.csv.')


# writing result file
df.to_csv('bristol-air-quality-updated.csv',index=False)