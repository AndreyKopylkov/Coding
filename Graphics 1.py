import matplotlib.pyplot as plt

lineN = []
with open("Data.txt") as file:
    for line in file:
        lineN.append([float(x) for x in line.split()])
        print(lineN)

fig = plt.figure()   # Создание объекта Figure
plt.scatter(lineN[0], lineN[1])
plt.show()
