from fastapi import APIRouter, HTTPException, Path
from typing import Annotated
from fastapi import status, Depends
from db.database import get_db
from schemas import UfBase
from datetime import date
from pydantic import condate
from sqlalchemy.orm import Session
from db import db_uf
from utils import get_uf_from_sii, extract_value_from_response
from requests.exceptions import ConnectionError
import logging

router = APIRouter(prefix="/uf", tags=["uf"])


@router.get(
    "/{date}",
    status_code=200,
    response_model=UfBase,
    description="Gets the value of the UF for a given date",
)
def get_uf(
    uf_date: Annotated[
        condate(ge=date(2013, 1, 1)),
        Path(alias="date", description="Date to find UF value"),
    ],
    db: Session = Depends(get_db),
):
    # finds the value of the uf for the given date in the database
    uf_value = db_uf.get_uf(db, uf_date)

    if uf_value:
        return uf_value
    try:
        # Makes a request to SII to obtain all uf values for the year
        response = get_uf_from_sii(uf_date)

        # Extracts value from html response
        value = extract_value_from_response(uf_date, response)

        # Coverts value to float
        value = float(value)

        # Stores uf value in database for future requests
        uf_value = db_uf.create_uf(db, UfBase(value=value, date=uf_date))

        return uf_value
    except AttributeError as error:
        logging.error(error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f" Unable to extract UF value for response",
        )
    except ConnectionError as error:
        logging.error(error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f" Unable to connect to 'https://www.sii.cl/'",
        )
    except Exception as error:
        logging.error(error)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UF value for {uf_date} not found",
        )
