import re

def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    re_mail = re.compile(r'^(\w+)\@((\w+\.\w+$)|(\w+\.\w+\.\w+$))')
    if re_mail.match(email) is None:
        raise ValueError(f'wrong email: {email}')
    else:
        mail_list = re_mail.findall(email)
        return {'username': mail_list[0][0], 'domain': mail_list[0][1]}



if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    #email_parse('someone@geekbrainsru')

