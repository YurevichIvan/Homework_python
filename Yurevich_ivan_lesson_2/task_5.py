from random import uniform
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»
def transfer_list_in_str(list_in: list) -> str:
  price_1 = []
  for i in my_list:
      price_1.append(str(int(i)) + ' руб. ' + str(round(i * 100))[-2::] + ' коп.,')
  return price_1

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
print()

#B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
def sort_prices(list_in: list) -> list:
    return my_list.sort()

print(*my_list, 'ID =', id(my_list))
result_2 = sort_prices(my_list)
print(*my_list, 'ID =', id(my_list))
print()

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
def sort_price_adv(list_in: list) -> list:
  """Создаёт новый список и возвращает список с элементами по убыванию"""
  list_out = sorted(my_list)[::-1]
  return list_out
result_3 = sort_price_adv(my_list)
print(*result_3)
print()


#D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
def check_five_max_elements(list_in: list) -> list:
  """Проверяет элементы входного списка вещественных чисел и возвращает
      список из ПЯТИ максимальных значений"""
  list_out = sorted(my_list)[::-1]
  return list_out[:5]

result_4 = check_five_max_elements(my_list)
print(*result_4)









