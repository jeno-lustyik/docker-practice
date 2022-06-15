import pandas as pd
from sqlalchemy import create_engine


def create_db():
    try:
        engine = create_engine("sqlite:///student.db")
        conn = engine.connect()

        df = pd.read_csv("source.csv")

        df.to_sql("source", conn, if_exists='replace')
        conn.close()
        return 0
    except:
        return 1


def get_students():
    try:
        engine = create_engine("sqlite:///student.db")
        conn = engine.connect()

        df = pd.read_sql_query("SELECT * FROM source", conn)
        conn.close()
        df_dict = df.to_dict()
        return df_dict

    except:

        return {"ERROR": "No table found"}


def get_name(email):
    try:
        engine = create_engine("sqlite:///student.db")
        conn = engine.connect()

        df = pd.read_sql_query("SELECT name FROM source WHERE email='{}'".format(email), conn)
        conn.close()
        return df.to_dict()

    except:

        return {"ERROR": "No table found"}


create_db()
