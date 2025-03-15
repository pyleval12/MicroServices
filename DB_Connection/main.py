import db_users as dbu
import db_products as dbp



DATABASE_URL = "postgresql://myuser:mysecretpassword@localhost:5432/mydatabase"

result = dbu.create_table(DATABASE_URL)
# result2 = dbp.create_table(DATABASE_URL)

print(result)
# print(result2)