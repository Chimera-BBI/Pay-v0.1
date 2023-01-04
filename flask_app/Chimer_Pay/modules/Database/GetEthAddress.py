import asyncio
from flask import Flask, jsonify
import boto3
import psycopg2.pool

app = Flask(__name__)

# Create a connection pool
pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                         host='host',
                                         port='port',
                                         user='user',
                                         password='password',
                                         database='database')

@app.route('/postage/<int:id>', methods=['GET'])
async def get_postage(id):
  try:
    # Get a connection from the pool
    conn = pool.getconn()

    async with conn.cursor() as cursor:
      postgreSQL_select_Query = "select * from postage where id = %s"
      await cursor.execute(postgreSQL_select_Query, (id,))
      record = await cursor.fetchone()
      return jsonify({"id": record[0], "name": record[1], "cost": record[2]})

  except (Exception, psycopg2.Error) as error :
      print ("Error while fetching data from PostgreSQL", error)

  finally:
      # Return the connection to the pool
      if(conn):
          pool.putconn(conn)
          print("PostgreSQL connection returned to the pool")

if __name__ == '__main__':
    app.run(debug=True)