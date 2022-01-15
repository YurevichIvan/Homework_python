tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Абракадабра', 'Конь']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

from itertools import zip_longest, islice

def check_gen(tutors: list, klasses: list):


    for tutor, klas in zip_longest(tutors, klasses):
            yield tutor, klas



generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration


