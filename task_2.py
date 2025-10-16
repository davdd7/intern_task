# Задание 2

# Реализовал самый простой функционал без проверок на ошибки, только главное
# При запуске отслеживает результат за определенное количество циклов
# Можно организовать ограничение очереди

from types import new_class
from typing import List
import random
import time
from collections import deque

class FIFOList:
  def __init__(self):
    self.list_data = []

  def put_data(self, some_data):
    self.list_data.append(some_data)

  def get_data(self):
    if self.is_empty:
      return
    return self.list_data.pop(0)

  def is_empty(self):
    return len(self.list_data) == 0


class FIFODeque:
  def __init__(self):
    self.deq_list = deque()
  
  def put_data(self, some_data):
    self.deq_list.append(some_data)

  def get_data(self):
    if self.is_empty():
      return
    return self.deq_list.popleft

  def is_empty(self):
    return len(self.deq_list) == 0

def test_fifo():
  op = 100000

  fifo_l = FIFOList()
  fifo_d = FIFODeque()

  started_time_l = time.time()

  for i in range(op):
    if random.random() > 0.4 or fifo_l.is_empty():
      fifo_l.put_data(i)
    else:
      fifo_l.get_data()
  
  delta_l = time.time() - started_time_l

  print("FIFO List time: {:.4}".format(delta_l))

  started_time_d = time.time()

  for i in range(op):
    if random.random() > 0.4 or fifo_d.is_empty():
      fifo_d.put_data(i)
    else:
      fifo_d.get_data()

  delta_d = time.time() - started_time_d
  
  print("FIFO Deque time: {:.4}".format(delta_d))

  if delta_d > delta_l:
    print(
      "Реализация на списках быстрее "
      "коллекции deque за {} операций на {:.4} сек".format(
        op,
        delta_d - delta_l
      )
    )
  else:
    print(
      "Реализация на коллекции deque быстрее "
      "списков за {} операций на {:.4} сек".format(
        op,
        delta_l - delta_d
      )
    )



if __name__ == "__main__":
  test_fifo()
