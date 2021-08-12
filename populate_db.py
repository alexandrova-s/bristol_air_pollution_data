import pandas as pd
import pymysql.cursors
import warnings
warnings.filterwarnings("ignore")

# TASK 3 b

# function to generate queries to insert to geolocation table
def create__geoinsert_query(params):
    sql_insert_GeoTab = ('INSERT INTO GeoLocation' +' ('+ str(', '.join(['SiteID','Latitude','Longitude','Location','DateStart','InstrumentType','DateEnd', 'Current']))+ ') VALUES '+ str(tuple(params))+';')
    sql_insert_GeoTab = sql_insert_GeoTab.replace('nan','NULL')
    return sql_insert_GeoTab

# function to generate queries to insert to measurement table
def create__measureinsert_query(params):
    sql_insert_MeasureTab = ('INSERT INTO measurement' +' ('+ str(', '.join(['DateTime', 'NOx', 'NO2', 'NO', 'FK_SiteId', 'PM10', 'NVPM10', 'VPM10', 'NVPM2_5', 'PM2_5', 'VPM2_5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'AirPressure']))+ ') VALUES ') + str(tuple(params))+';'
    sql_insert_MeasureTab = sql_insert_MeasureTab.replace('nan','NULL')
    return sql_insert_MeasureTab

#Connect to the database
con = pymysql.connect(host='localhost',
                             user='root',
                             password=None,
                             database='pollution-db',
                             cursorclass=pymysql.cursors.DictCursor)


# read file from task 1
df = pd.read_csv('result_df_air_quality.csv')


geoLoc = df[['SiteID','Latitude','Longitude','Location','DateStart','Instrument Type','DateEnd', 'Current']].drop_duplicates()     # dataframe to table geolocation
measurement = df.drop(columns=['Latitude','Longitude','Location','DateStart','Instrument Type','DateEnd','Current'])    # dataframe to table measurement

try:

    with con.cursor() as cur:

        # inserting to geolocation table
        for case in geoLoc.values:
            cur.execute(create__geoinsert_query(case))

        # #inserting to measurement table
        for case in measurement.values:
            cur.execute(create__measureinsert_query(case))

    con.commit()


finally:

    con.close()