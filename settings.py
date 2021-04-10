from sqlalchemy import create_engine

engine = create_engine('sqlite:///shop.db', echo = False)
