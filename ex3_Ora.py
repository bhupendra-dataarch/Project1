import cx_Oracle
import logging

logging.basicConfig(filename='ex3_oracle.log',level=logging.DEBUG,format='%(levelname)s - %(asctime)s - %(message)s')
logging.info('STart Program for Ex3 Oracle Data fetch')

sql = """ select sid,status from v$session where status = :STATUS"""


try:
		conn = cx_Oracle.connect("user1","password123","rds-oracle.czp3j8qn36vx.us-west-2.rds.amazonaws.com:1521/ORACLEDB")

		print(f"Database Version  {conn.version}")
		print(f"Database User ' {conn.username}")
		print('Hello')

except Exception as err:
#except cx_Oracle.DatabaseError as err:
		print('Execption occured while creating the connection with Database Error', err)
		#print('Error Message ..', err.message)
else:
		cur = conn.cursor()
		result = cur.execute(sql , STATUS='ACTIVE')
		#result = cur.fetchall()

		for row in result:
			print(row)		

		
finally:
		cur.close()
		conn.close()
		logging.info('Program Extecuted Successfully')

