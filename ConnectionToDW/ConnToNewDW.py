
import pyodbc
import sqlalchemy
import urllib
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import inspect
import pprint as pp


def main():
    print(sqlalchemy.__version__)
    
    engine = sqlalchemy.create_engine('mssql+pyodbc://AZORRDWSC01/ORR_DW?driver=SQL+Server+Native+Client+11.0?trusted_connection=yes')
    conn = engine.connect()

    inspector = inspect(engine)

    print(inspector.get_table_names())

    stmt = 'SELECT * FROM [ORR_DW].[NETL].[factt_206_rollingstock]'

    results = conn.execute(stmt).fetchall()

    print(f"results are {type(results)}")
    for line in results:
        print(f"each line from results is {type(line)}")
        pp.pprint(line)


if __name__ == '__main__':
    main()