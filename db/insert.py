from db.sql_core import engine, recobrar_table
import datetime as dt


def insert_recobrar(opportunity, card_id, customer_id, amount, order_id,
                    charge_id, result, sf_transaction_id,
                    acquirer, acquirer_message, tid, date):
    conn = engine.connect()
    ins = recobrar_table.insert()
    new_success = ins.values(opportunity=opportunity,
                             card_id=card_id,
                             customer_id=customer_id,
                             amount=amount,
                             order_id=order_id,
                             charge_id=charge_id,
                             result=result,
                             sf_transaction_id=sf_transaction_id,
                             acquirer=acquirer,
                             acquirer_code=acquirer_message,
                             tid=tid,
                             date=date,
                             last_update=dt.datetime.now())
    conn.execute(new_success)
    conn.close()
