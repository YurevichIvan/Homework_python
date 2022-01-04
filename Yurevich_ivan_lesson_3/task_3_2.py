def num_translate_adv(value: str) -> str:
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
    elif value.istitle() == True and value.lower() in str_out:
        return str(str_out[value.lower()].title())
    else:
        return None


print(num_translate_adv("One"))
print(num_translate_adv("one"))
print(num_translate_adv("o"))