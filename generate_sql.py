import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# TASK 3 a

# load file from task 1
df = pd.read_csv('bristol-air-quality-updated.csv')

geoLoc = df[['SiteID','Latitude','Longitude','Location','DateStart','Instrument Type','DateEnd', 'Current']].drop_duplicates()     # database to populate table geolocation

# # generating queries for table geolocation
with open('pollution_data.sql', 'w') as f:
    for _, row in geoLoc.iterrows():
        sql_insert_GeoTab = ('INSERT INTO GeoLocation' +' ('+ str(', '.join(['SiteID','Latitude','Longitude','Location','DateStart','InstrumentType','DateEnd', 'Current']))+ ') VALUES '+ str(tuple(row.values))+';\n')
        sql_insert_GeoTab = sql_insert_GeoTab.replace('nan','NULL')
        f.write(sql_insert_GeoTab)

measurement = df.drop(columns=['Latitude','Longitude','Location','DateStart','Instrument Type','DateEnd','Current'])     # database to populate table measurement

# generating queries for table measurement
with open('pollution_data.sql', 'a') as f:
    for index, row in measurement.iterrows():    
        sql_insert_MeasureTab = ('INSERT INTO measurement' +' ('+ str(', '.join(['DateTime', 'NOx', 'NO2', 'NO', 'FK_SiteId', 'PM10', 'NVPM10', 'VPM10', 'NVPM2_5', 'PM2_5', 'VPM2_5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'AirPressure']))+ ') VALUES ') + str(tuple(row.values))+';\n'
        sql_insert_MeasureTab = sql_insert_MeasureTab.replace('nan','NULL')
        f.write(sql_insert_MeasureTab)

f.close()