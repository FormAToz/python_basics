import psycopg2

conn = psycopg2.connect(database='hf_py', user='hfuser', password='123', host='localhost', port=5432)
cursor = conn.cursor()

show_all_tables_sql = """
SELECT relname FROM pg_class 
WHERE relkind='r' 
AND relname !~ '^(pg_|sql_)'
"""
describe_table_sql = """
SELECT column_name, is_nullable, data_type, character_maximum_length FROM information_schema.columns 
WHERE table_schema = 'public' 
AND table_name = 'log' 
ORDER BY ordinal_position
"""

insert_sql = """
INSERT INTO log (phrase, letters, ip, browser_string, results)
VALUES (%s, %s, %s, %s, %s)
"""
select_all_sql = """
SELECT * FROM log
"""

cursor.execute(insert_sql, ('hitch-hiker', 'xyz', '127.0.0.1', 'Chrome', 'set()'))
cursor.execute(insert_sql, ('hitch-hiker', 'xyz', '127.0.0.1', 'Chrome', 'set()'))
conn.commit()

cursor.execute(select_all_sql)
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
