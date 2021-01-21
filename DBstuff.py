import os
from dotenv import load_dotenv
import sshtunnel
import pymysql as mysql

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DATABASE')
SSH_USER = os.getenv('SSH_USER')
SSH_PASSWORD = os.getenv('SSH_PASSWORD')
SSH_PATH = os.getenv('SSH_PATH')

class DBstuff:
    def dbquotequery(query, quotenumber=None, newquote=None):
        sshtunnel.SSH_TIMEOUT = 5.0
        sshtunnel.TUNNEL_TIMEOUT = 5.0
        with sshtunnel.SSHTunnelForwarder(
                (DB_HOST, 21098),
                ssh_username=SSH_USER,
                ssh_password=SSH_PASSWORD,
                ssh_private_key=SSH_PATH,
                remote_bind_address=('127.0.0.1', 3306)
        ) as tunnel:
            db = mysql.connect(
                user=DB_USER,
                passwd=DB_PASSWORD,
                host='127.0.0.1',
                port=tunnel.local_bind_port,
                db=DATABASE
            )
            cursor = db.cursor()
            if quotenumber == None and newquote == None:
                cursor.execute(query)
                completedQuery = cursor.fetchall()
                db.close()
                tunnel.close()
                return completedQuery
            elif newquote != None:
                cursor.execute(query, newquote)
                db.commit()
                newquotenumber = cursor.lastrowid
                db.close()
                tunnel.close()
                return newquotenumber
            else:
                cursor.execute(query, (quotenumber,))
                completedQuery = cursor.fetchall()
                db.commit()
                db.close()
                tunnel.close()
                return completedQuery

    def dbjokequery(query):
        sshtunnel.SSH_TIMEOUT = 5.0
        sshtunnel.TUNNEL_TIMEOUT = 5.0
        with sshtunnel.SSHTunnelForwarder(
                (DB_HOST, 21098),
                ssh_username=SSH_USER,
                ssh_password=SSH_PASSWORD,
                ssh_private_key=SSH_PATH,
                remote_bind_address=('127.0.0.1', 3306)
        ) as tunnel:
            db = mysql.connect(
                user=DB_USER,
                passwd=DB_PASSWORD,
                host='127.0.0.1',
                port=tunnel.local_bind_port,
                db=DATABASE
            )
            cursor = db.cursor()
            cursor.execute(query)
            completedQuery = cursor.fetchall()
            db.close()
            tunnel.close()
            return completedQuery