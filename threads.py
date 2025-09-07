from threading import Thread


class Task1(Thread):
  def run(self):
    for i in range(1000):
      print("Task1")

class Task2(Thread):
  def run(self):
    for i in range(1000):
      print("Task2")



