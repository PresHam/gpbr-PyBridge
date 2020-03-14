from sqlalchemy import select, column, and_
from db.sql_core import engine, recobrar_table
import datetime as dt


def salesforce_to_insert():
    conn = engine.connect()
    # today = str(dt.datetime.today()).split(' ')[0]
    s = select([recobrar_table]).where(and_(recobrar_table.c.sf_transaction_id == None,
                                            recobrar_table.c.result == 'paid',
                                            recobrar_table.c.sf_input == None
                                            ))
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    print(result)
    return result


def label_transactions():
    conn = engine.connect()
    s = select([recobrar_table]).where(recobrar_table.c.date > '2020-03%')
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    return result

