import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="$Enn3nK1"
)

pointer = db.cursor()

# pointer.execute("CREATE DATABASE flaskProject")

pointer.execute("SHOW DATABASES")
for db in pointer:
    print(db)