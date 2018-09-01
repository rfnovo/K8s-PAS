'''
Created on Jan 10, 2017

@author: hanif
'''

import os
import json
import pymysql


if 'VCAP_SERVICES' in os.environ:
   mysql_service = json.loads(os.environ['VCAP_SERVICES'])['cleardb'][0]
   credentials = mysql_service['credentials']
else:
   credentials = dict(hostname=os.environ['MYSQL_DB_HOST'], username=os.environ['MYSQL_DB_USER'], password=os.environ['MYSQL_USER_PASSWORD'], name=os.environ['MYSQL_DB_NAME'])


class Database:
    def connect(self):
        return pymysql.connect(credentials['hostname'],credentials['username'],credentials['password'],credentials['name'])

    def initialize(self):
        con = Database.connect(self)
        cursor = con.cursor()

	#IsDBOK = cursor.execute("SELECT table_name FROM information_schema.tables where table_schema='appdb' AND table_name='phone_book';")
        #if IsDBOK == 0:
        #    print ("initdb")

        #cursor.execute("CREATE TABLE IF NOT EXISTS `phone_book` (`id` int(5) NOT NULL,`name` varchar(255) NOT NULL,`phone` varchar(50) NOT NULL,`address` varchar(255) NOT NULL) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;")
        cursor.execute("CREATE TABLE IF NOT EXISTS phone_book (id int(5) NOT NULL AUTO_INCREMENT,name varchar(255) NOT NULL,phone varchar(50) NOT NULL,address varchar(255) NOT NULL,PRIMARY KEY (id)) DEFAULT CHARSET=latin1;")

        con.close()


    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
