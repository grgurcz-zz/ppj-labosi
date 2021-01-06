import sys

lines = []
line_count = 0
err_positions = []
output_list = []
pos = 0
popis_varijabli = [dict()]
dubina = 0
a = dict()


def program():
    global dubina, popis_varijabli, output_list, err_positions
    if pos == line_count:
        return
    if lines[pos][0] == 'KR_ZA':
        popis_varijabli.append(dict())
        dubina += 1
    elif lines[pos][0] == 'IDN':
        ime_var = lines[pos][2]
        broj_retka = lines[pos][1]
        if lines[pos - 1][0] == 'KR_ZA':
            popis_varijabli[dubina][ime_var] = broj_retka
        elif lines[pos + 1][0] == 'OP_PRIDRUZI':
            nasao = 0
            for i in range(dubina, -1, -1):
                if ime_var in popis_varijabli[i].keys():
                    nasao = 1
                    break
            if not nasao:
                popis_varijabli[dubina][ime_var] = broj_retka
        else:
            nasao = 0
            for i in range(dubina, -1, -1):
                if ime_var in popis_varijabli[i].keys():
                    if popis_varijabli[i][ime_var] == broj_retka:
                        break
                    output_list.append(
                        broj_retka + ' ' + popis_varijabli[i][ime_var] + ' ' + ime_var)
                    nasao = 1
                    break
            if not nasao:
                err_positions.append(broj_retka + ' ' + ime_var)
                return
    elif lines[pos][0] == 'KR_AZ':
        popis_varijabli.pop()
        dubina -= 1


all_text = sys.stdin.readlines()
for line in all_text:
    lines.append(line.strip().split())
    line_count += 1
lines.append('')

while pos < line_count and not len(err_positions):
    program()
    pos += 1

for i in output_list:
    print(i)
if len(err_positions):
    print('err' + ' ' + err_positions[0])
