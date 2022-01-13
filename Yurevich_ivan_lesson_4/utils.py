from requests import get
import decimal


URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(code: str) -> float:
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
    for i in content.split('<CharCode>')[1:]:
        charcode = i[:3]
        value = ((i.split('<Value>')[1:][0]).split('</Value>')[0]).split(',')
        result_value = round(decimal.Decimal('.'.join(value)) * 1, 2)
        if code == charcode:
            return float(result_value)

if __name__ == '__main__':
    # пример использования
    currency_rates('EUR')
