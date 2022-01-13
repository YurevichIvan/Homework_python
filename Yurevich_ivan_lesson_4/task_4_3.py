from requests import get
import decimal
import datetime

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates_adv(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю
    @rtype: object
    """
    code = code.upper()

    response = get(URL)
    #if response.status_code == 200: # Можно раскоментировать для проверки запроса.
        #print('Запрос успешен')
    #else:
        #print(f'Запрос не успешен: {response.status_code}')

    content = response.content.decode(encoding=response.encoding) # приводим содержимое ответа сервера к строковому виду,
    # может есть способ проще? чтоб понять как это сделать было потрачено очень много времени)
    counter = 0

    date_value = content.split('<ValCurs Date="')[1][:10]
    day, month, year = date_value.split('.')
    date_res = datetime.date(int(year), int(month), int(day))

    for i in content.split('<CharCode>')[1:]:
        charcode = i[:3]
        value = ((i.split('<Value>')[1:][0]).split('</Value>')[0]).split(',')
        result_value = round(decimal.Decimal('.'.join(value)) * 1,2)
        if code == charcode:
            return float(result_value), date_res


kurs, date_value = currency_rates_adv("usd")
empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)



