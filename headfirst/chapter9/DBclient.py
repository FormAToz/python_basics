from DBcm import UseDatabase

db_config = {'database': 'hf_py', 'user': 'hfuser', 'password': '123', 'host': 'localhost', 'port': 5432}

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

with UseDatabase(db_config) as cursor:
    cursor.execute(describe_table_sql)
    print(cursor.fetchall())
