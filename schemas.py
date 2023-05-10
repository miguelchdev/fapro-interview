from pydantic import BaseModel

from datetime import date

class UfBase(BaseModel):
    date:date
    value:float 
    class Config():
        orm_mode = True