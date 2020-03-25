from sqlalchemy import update, and_
from db.sql_core import engine, recobrar_table


def update_salesforce(order_id, sf_transaction_id):
    conn = engine.connect()
    u = update(recobrar_table). \
        where(recobrar_table.c.order_id == order_id). \
         values(sf_transaction_id=sf_transaction_id)

    result = conn.execute(u)
    conn.close()
    print('Update Attempt')
    return result
