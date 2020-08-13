#general
import pandas as pd
import os

#s3 python utility
import s3fs

#postgres python utility
import psycopg2 as pg
import pandas.io.sql as psql

#hdfs client python utility
from hdfs import InsecureClient

## Cloud data access: Pull sample of 2016 data from s3
#Note: s3fs automatically checks aws_access_key_id, aws_secret_access_key, and aws_session_token environment variables.

dfs3 = pd.read_csv('s3://seteam-files/mq/2016.csv', nrows=1000000)

## Legacy DB access: Pull sample of 2017 data from Postgres
#os.environ['user'] and os.environ['db_password'] stored in project env vars

dbname = 'postgres'

connection = pg.connect("host='10.10.0.5' dbname="+dbname+" user="+os.environ['user'])
dfpg = pd.read_sql_query('select * from import.airline_2017 limit 1000000',con=connection)
dfpg.columns = dfpg.columns.str.upper()

## Pull all 2018 from HDFS
#Connection string managed from within Domino Environment Variable os.environ['hdfs_conn']

client_hdfs = InsecureClient(os.environ['hdfs_conn'])
# ====== Reading files ======
with client_hdfs.read('/data/2018.csv', encoding = 'utf-8') as reader:
    dfhdfs = pd.read_csv(reader,nrows=1000000)

## Merge/join s3 & Postgres & HDFS
merged = pd.concat([dfs3,dfhdfs],axis=0, sort=False, ignore_index=True)
merged = pd.concat([merged,dfpg],axis=0, sort=False, ignore_index=True)
merged = merged.apply( pd.to_numeric, errors='ignore' )

## Export to a Domino Dataset
# provides shared, versioned, reproducible access to data
merged.to_csv(r'/domino/datasets/flight_data/airlines_2016_2017_2018.csv', index = None, header=True) 