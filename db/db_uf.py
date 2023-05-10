
from sqlalchemy.orm.session import Session

from schemas import UfBase
from db.models import DbUF
from datetime import date

def create_uf(db:Session, request:UfBase):
    new_uf_value = DbUF(
        value = request.value,
        date=request.date,
    )
    db.add(new_uf_value)
    db.commit()
    db.refresh(new_uf_value)
    return new_uf_value


def get_uf(db:Session,date:date ):
    return db.query(DbUF).filter(DbUF.date == date).first()


