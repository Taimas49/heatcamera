import psycopg2
from congif import host, user, password, db_name, port

temperature = 99
connection = None
cursor = None

con = psycopg2.connect(
            host = "localhost",
            database="face_temperature",
            user = "postgres",
            password = "assasin007")

#connect to the db 

#cursor 
cur = con.cursor()

cur.execute("insert into temp (temperature) values (5)"  )

#execute query
cur.execute("select temperature from temp")

rows = cur.fetchall()

# for r in rows:
#     print (f"id {r[0]} name {r[1]}")

#commit the transcation 
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()
