import duckdb
conn = duckdb.connect()
conn.sql("""
ATTACH 's3://location'
AS dataframe_db(READ_ONLY)
""")

conn.sql("SELECT * 
         FROM dataframe_db 
         LIMIT 4")

         
#PYTHON EXAMPLE
