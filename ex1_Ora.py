import cx_Oracle


def info(conn):
    print(f"Oracle Server Version: {conn.version}")
    print(f"User: {conn.username}")
    print(f"Autocommit: {conn.autocommit}")
    print(f"Encoding: {conn.encoding}")
    print(f"cx_Oracle Client Version: {cx_Oracle.version}")


def main():

    conn = None
    try:
        conn = cx_Oracle.connect(
            "user1", "password123", "rds-oracle.czp3j8qn36vx.us-west-2.rds.amazonaws.com:1521/ORACLEDB", encoding="UTF-8"
        )
        info(conn)
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