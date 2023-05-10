from db.database import Base
from  sqlalchemy import Column
from  sqlalchemy.sql.sqltypes import Integer,Float, Date




class DbUF(Base):
    __tablename__ = "uf_values"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    value = Column(Float)