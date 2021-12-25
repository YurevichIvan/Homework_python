duration = int(input('Введите количество секунд:'))
s = duration
m = s / 60
h = s / 3600
d = s / 86400
if duration <= 59:
    print(s, 'сек')
elif 60 <= duration <= 3599:
    print(int(m), 'мин', s % 60, 'сек' )
elif 3600 <= duration <= 86399:
    print(int(h), 'час', int(m) % 60, 'мин', int(s) % 60,'сек' )
else:
    print(int(d), 'дн', int(h) % 24, 'час', int(m) % 60, 'мин', int(s) % 60, 'сек' )
