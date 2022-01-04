nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""

    list_out = []
    for i in range(count):
        str_random = choice(nouns) + " " + choice(adverbs) + " " + choice(adjectives)
        list_out.append(str_random)
    return list_out


print(get_jokes(2))
print(get_jokes(10))





