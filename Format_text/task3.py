# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

with open("text.txt", 'r', encoding="utf-8") as f:
    data = f.readlines()
    data_upd = []
    count = int(input("Input number more than 35: "))
    if count > 35:
        pass
    else:
        print("Input correct number")

    for line in data:
        line = line.rstrip()
        c = count
        while len(line) != 1:
            if len(line) > c:
                if line[c] != ' ':
                    c -= 1
                else:
                    data_upd.append(line[:c].rstrip())
                    line = line.replace(line[:c + 1], '')
                    c = count
            else:
                data_upd.append(' ' + line.rstrip() + ' ')
                line = ' '
    del data

    output = []
    for text in data_upd:
        space_index = [index for index, char in enumerate(text) if char == ' ']
        i = 0
        while True:
            if len(text) < count:
                text = text[:space_index[i]] + ' ' + text[space_index[i]:]
                space_index = space_index[:i]+list(map(lambda x: x+1, space_index[i:]))
                i += 1
                if i + 1 > len(space_index):
                    i = 0
            else:
                break
        output.append(text + '\n')

    del data_upd
    with open("test_out.txt", 'w', encoding = "utf-8") as file_out:
        for txt in output:
            file_out.write(txt)
        print("File successfully wrote")