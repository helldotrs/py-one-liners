column_names  = ['name', 'salary', 'job']
db_rows       = [ ('Alice', 180000, 'data scientist'),
                  ('Bob', 89000, 'testter'),
                  ('Frank', 99000, 'ceo')]

db  = [dict(zip(column names, row)) for row in db_rows]

print(db)
