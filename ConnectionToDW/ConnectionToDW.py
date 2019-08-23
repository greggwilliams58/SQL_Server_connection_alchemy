
import pyodbc
import sqlalchemy
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import inspect
import pprint as pp
import time


def main():
    print(sqlalchemy.__version__)
    
    engine = sqlalchemy.create_engine('mssql+pyodbc://AZORRDWSC01/ORR_DW?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes')
    conn = engine.connect()

    inspector = inspect(engine)

    print(inspector.get_table_names())

    start = time.time()

    #stmt = 'SELECT * FROM [ORR_DW].[NETL].[factt_206_rollingstock]'
    stmt = """SELECT TOP (1000) [Lennon_ID]
      ,[source_item_id]
      ,[status_id]
      ,[Date of Settlement]
      ,[Date key]
      ,[Quarter]
      ,[Carrier Profit Centre Code]
      ,[Carrier Profit Centre Desc]
      ,[Carrier Subdivision Code]
      ,[Carrier Subdivision Desc]
      ,[Service Code]
      ,[Service Desc]
      ,[Sector_Franchise Combo]
      ,[Sector_Franchise]
      ,[train_operating_company_key]
      ,[Product Code]
      ,[Product Level 1 Code]
      ,[Ordinary/Season Ticket]
      ,[Ticket Type]
      ,[Ticket Class]
      ,[Reduced/Full/Other Ticket]
      ,[Lennon Adjusted Earnings (Sterling)]
      ,[Lennon Operating Miles]
      ,[Lennon Operating KM]
      ,[Operating Journeys]
      ,[route_key]
      ,[ticket_type_key]
  FROM [ORR_DW].[ORR].[factt_205_lennon_ch1]"""
 

    df = pd.read_sql(stmt,conn)
    print(df)



    end = time.time()
    print(f"the code needed {end-start} seconds")

if __name__ == '__main__':
    main()