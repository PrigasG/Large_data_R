import duckdb
conn = duckdb.connect()
conn.sql("""
ATTACH 's3://location'
AS dataframe_db(READ_ONLY)
""")

#PYTHON EXAMPLE
