import json
import hashlib
import sqlite3

path = 'database_hash2.db'
try:
    with open(path) as database:
        data = sqlite3.connect(path)
except:
    print('missing file')


c = data.cursor()
c.execute("select * from users")
print(c.fetchone())

# # Create table
c.execute('''CREATE TABLE users
             (username_hash varchar, password_hash varchar)''')

# # Insert a row of data

var1 = hashlib.sha256('0'.encode('utf-8')).hexdigest()
print(var1)
var2 = hashlib.sha256('p'.encode('utf-8')).hexdigest()
print(var2)
c.execute("INSERT INTO users VALUES (?, ?)", (var1, var2))

# # Save (commit) the changes
# conn.commit()
# c.execute("select * from users")
# print(c.fetchall())

# conn.close()

# json_path = 'data_hash.txt'

# with open(json_path, 'w') as out_json_cache:
#     json.dump(data_hash, out_json_cache)

