import time

start = time.clock()
i = 1 + 1
elapsed = (time.clock() - start)
print(elapsed)

start = time.time()
k = 23456789*6758757987654
elapsed = (time.time() - start)
print(elapsed, "время работы программы без задержки")

#По непонятным причинам время работы программы ровняется нулю, вне зависимости от сложности вычислеслений
# Фиксится задержкой через:

start = time.time()
k = 23456789*6758757987654
time.sleep(5)
elapsed = (time.time() - start)
print(elapsed, "с задержкой")
