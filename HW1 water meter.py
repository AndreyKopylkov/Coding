minute = int(input("Введите длительность приёма душа в минутах: "))
if minute > 0:
    liter = minute * 6
    bottle = liter * 2
    print ("За ", minute, " минут вы израсхоовали ", liter, " литров воды или ", bottle, " бутылок")
elif minute == 0:
    print ("Советую принять душ ещё раз")
else:
    print ("Советую впредь не пользоваться машиной времени")
#
