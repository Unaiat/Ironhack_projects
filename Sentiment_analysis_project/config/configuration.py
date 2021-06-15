import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()


passw = os.getenv("pass_sql")
dbName= "The_simpsons"

#Me conecto con la base de datos

connectionData=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)


