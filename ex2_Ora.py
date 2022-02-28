import cx_Oracle


def info(conn):
    print(f"Oracle Server Version: {conn.version}")
    print(f"User: {conn.username}")
    print(f"Autocommit: {conn.autocommit}")
    print(f"Encoding: {conn.encoding}")
    print(f"cx_Oracle Client Version: {cx_Oracle.version}")
    print('Hello')


def main():

    conn = None
    try:
        conn = cx_Oracle.connect("user1","password123","rds-oracle.czp3j8qn36vx.us-west-2.rds.amazonaws.com:1521/ORACLEDB")
        info(conn)
        c = conn.cursor()
        for row in c.execute('select sid ,status from v$session'):
           print(row)
    except cx_Oracle.DatabaseError as err:
        print(err)
        print(f"ORA Code: {err.args[0].code}")
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()