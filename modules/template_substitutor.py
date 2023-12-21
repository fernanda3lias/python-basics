# Creating template for replacing variables in texts
# doc: https://docs.python.org/3/library/string.html#template-strings
import json
import locale
import string
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'template.txt'
locale.setlocale(locale.LC_ALL, '')

def change_currency(number: float) -> str:
    brl = "R$" + locale.currency(number, symbol=False, grouping=True)
    return brl

date = datetime(2022, 12, 21)
data = dict(
    name = "Charles",
    value = change_currency(1_600_000),
    date = date.strftime('%d/%m/%Y'),
    company = 'Ferrari',
    phone = '+1 161 616 1616'
)

class MyTemplate(string.Template):
    delimiter = '%'

with open(FILE_PATH, 'r') as file:
    text = file.read()
    template = MyTemplate(text)
    # substitute: replaces but raises errors if curly braces are missing;
    # safe_substitute: replaces without raising errors.
    print(template.substitute(data))