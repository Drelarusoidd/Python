# Реализовать текстовый вывод текущего времени + текстовый вывод времени, введённого с консоли.
# Для получения текущего времени использовать модуль datetime.

# min < 30: столько-то минут следующего часа
# min == 30: половина такого-то
# min > 30 and min < 45 столько-то минут следующего часа
# min >= 45 без min такого-то

from datetime import*
t = str(datetime.now())
t = t.split(' ')
t = t[1].split('.')
t = t[0].split(':')
hour, minut = int(t[0]), int(t[1])

hour_dict = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого", 7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одинадцатого", 12: "двенадцатого", 13: "первого", 14: "второго", 15: "третьего", 16: "четвертого", 17: "пятого", 18: "шестого", 19: "седьмого", 20: "восьмого", 21: "девятого", 22: "десятого", 23: "одинадцатого", 24: "двенадцатого"}
minut_dict_1 = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят"}
minut_dict_2 = {0: "ноль", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}

if minut < 30 and (hour != 00):
    if 0 <= minut < 20:
        if 4 < minut < 20 or minut == 0: 
            print(f"{minut_dict_2[minut]} минут {hour_dict[hour+1]}")
        elif 1 < minut < 5:
            print(f"{minut_dict_2[minut]} минуты {hour_dict[hour + 1]}")
        else:
            print(f"{minut_dict_2[minut]} минута {hour_dict[hour + 1]}")
    else:
        if minut % 10 == 1:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минута {hour_dict[hour + 1]}")
        elif 1 < minut % 10 < 5:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минуты {hour_dict[hour + 1]}")
        elif minut % 10 == 0:
            print(f"{minut_dict_1[minut//10]} минут {hour_dict[hour + 1]}")
        else:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минут {hour_dict[hour + 1]}")

elif minut == 30:
    print(f"половина {hour_dict[hour]}")

elif minut > 30 and minut < 45:
    if minut % 10 == 1:
        print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минута {hour_dict[hour + 1]}")
    elif 1 < minut % 10 < 5:
        print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минуты {hour_dict[hour + 1]}")
    elif minut % 10 == 0:
        print(f"{minut_dict_1[minut//10]} минут {hour_dict[hour + 1]}")
    else:
        print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минут {hour_dict[hour + 1]}")

elif minut >= 45:
    if minut % 10 == 0:
        print(f"{minut_dict_1[minut//10]} {hour_dict[hour]}")
    else:
        print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} {hour_dict[hour]}")

elif minut == 00 and hour == 00 or hour == 24 and minut == 00:
    print("полночь")

