# -*- coding: utf-8 -*-
"""Q03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bdXg-FYlN0aHi_wKRefXQzW_po2-7vLJ
"""

data = input()
initial = data[0]
count = 0
predecessor = data[0]

for datum in data:
  if datum != predecessor:
    predecessor = datum
    if datum != initial:
      count += 1

print(count)