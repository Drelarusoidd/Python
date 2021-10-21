with open("text.txt", 'r', encoding="utf-8") as f:
    data = f.readlines()
    data_upd = []
    count = int(input("Input number more than 35: "))
    if count > 35:
        for line in data:
            line = line.rstrip()
            c = count
            while len(line) != 1:
                if len(line) > c:
                    if line[c] != ' ':
                        c -= 1
                    else:
                        data_upd.append(line[:c])
                        line = line.replace(line[:c + 1], '')
                        c = count
                else:
                    data_upd.append(line.rstrip() + ' ')
                    line = ' '
        del data

        output = []
        for text in data_upd:
            space_index = [index for index, char in enumerate(text) if char == ' ']
            i = 0
            while True:
                if len(text) < count and len(space_index) > 0:
                    text = text[:space_index[i]] + ' ' + text[space_index[i]:]
                    space_index = space_index[:i] + [x + 1 for x in space_index[i:]]
                    i += 1
                    if i + 1 > len(space_index):
                        i = 0
                else:
                    output.append(text + '\n')
                    break

        del data_upd
        with open("test_out.txt", 'w', encoding = "utf-8") as file_out:
            for txt in output:
                file_out.write(txt)
            print("File successfully wrote")
    else:
        print("Input correct number")