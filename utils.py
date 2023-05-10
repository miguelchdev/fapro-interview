from bs4 import BeautifulSoup
from typing import  Union
import requests
import logging
from datetime import date

def get_uf_from_sii(date: date) -> requests.Response:
    response = requests.get(f"https://www.sii.cl/valores_y_fechas/uf/uf{date.year}.htm")
    response.raise_for_status()
    return response

def extract_value_from_response(date:date, response:requests.Response) -> float:
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("div", {"id": "mes_all"}).find("tbody")
    day_rows = table.find_all("tr")
    day_row = day_rows[date.day - 1].findChildren()
    value = day_row[date.month].get_text().replace(".", "").replace(",", ".")
    return value