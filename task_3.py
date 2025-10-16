# Задание 3
# Функция оптимизирована под малые массивы черех сортировку вставками и проверкой на наличие одного элемента
# например втроенная Timsort sorted()
# использует на языке C проверки и менее оптимизирована для малых массивов
# Timsort уже содержит все необходимые оптимизации и является лучшим решением 
# при сортировке данных от 20 элементов 
# (проверено тестовым путём. Может от 20 до 30 элементов отличаться)

def fasted_sort(some_list):
  n = len(some_list)

  if n <= 1:
    return some_list

  if n <= 20:
    return _insertion_sort(some_list)

  return sorted(some_list)

def _insertion_sort(arr):
  res = list(arr)

  for i in range(1, len(res)):
    checking_data = res[i]
    j = i -1
    while j >= 0 and res[j] > checking_data:
      res[j + 1] = res[j]
      j -= 1
    res[j + 1] = checking_data
  return res
