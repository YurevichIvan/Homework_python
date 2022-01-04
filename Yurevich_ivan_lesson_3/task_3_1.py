def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """


    str_out = { 'zero': '"ноль"',
                'one': '"один"',
               'two':'"два"',
               'three': '"три"',
               'four': '"четыре"',
               'five': '"пять"',
               'six': '"шесть"',
               'seven': '"семь"',
               'eight': '"восемь"',
               'nine': '"девять"',
               'ten': '"десять"'
            }
    if value in str_out:
        return str(str_out[value])
    else:
        return None


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("o"))