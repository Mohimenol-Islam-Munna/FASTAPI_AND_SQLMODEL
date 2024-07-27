from sqlalchemy import create_engine, text

# create engine
engine = create_engine("sqlite:///sqlite_db.db", echo=True)

# connect engine 
with engine.connect() as connection:
    result = connection.execute(text('select "hello world"'))

    print(result.all())



