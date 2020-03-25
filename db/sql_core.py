from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime)
import os
from app.bridge_configs import *

# Database Config
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///bridge_1.0.db', echo=False)

metadata = MetaData(bind=engine)

recobrar_table = Table('Recobrar', metadata,
                       Column('opportunity', String(200), index=True),
                       Column('card_id', String(200)),
                       Column('customer_id', String(200)),
                       Column('amount', Integer),
                       Column('order_id', String(200)),
                       Column('charge_id', String(200)),
                       Column('result', String(200)),
                       Column('sf_transaction_id', String(200)),
                       Column('acquirer', String(200)),
                       Column('acquirer_code', String(200)),
                       Column('tid', String(200)),
                       Column('date', DateTime),
                       Column('last_update', DateTime)
                       )
metadata.create_all()
