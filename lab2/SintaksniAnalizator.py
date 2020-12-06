import sys

line_position = 0
line_count = 0
space_count = 0

err_positions = []
output_list = []


def program():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<program>')
    space_count += 1
    lista_naredbi()


def lista_naredbi():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<lista_naredbi>')
    space_count += 1
    if line_position >= line_count or lines[line_position].split()[0] == 'KR_AZ':
        output_list.append(' ' * space_count + '$')
    elif lines[line_position].split()[0] == 'IDN' or lines[line_position].split()[0] == 'KR_ZA':
        naredba()
        lista_naredbi()
    else:
        err_positions.append(line_position)
    space_count -= 1


def naredba():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<naredba>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] == 'IDN':
        naredba_pridruzivanja()
    elif line_position < line_count and lines[line_position].split()[0] == 'KR_ZA':
        za_petlja()
    else:
        err_positions.append(line_position)
    space_count -= 1


def naredba_pridruzivanja():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<naredba_pridruzivanja>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] == 'IDN':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        if line_position < line_count and lines[line_position].split()[0] == 'OP_PRIDRUZI':
            output_list.append(' ' * space_count + lines[line_position])
            line_position += 1
            E()
        else:
            err_positions.append(line_position)
    else:
        err_positions.append(line_position)
    space_count -= 1


def za_petlja():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<za_petlja>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] == 'KR_ZA':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        if line_position < line_count and lines[line_position].split()[0] == 'IDN':
            output_list.append(' ' * space_count + lines[line_position])
            line_position += 1
            if line_position < line_count and lines[line_position].split()[0] == 'KR_OD':
                output_list.append(' ' * space_count + lines[line_position])
                line_position += 1
                E()
                if line_position < line_count and lines[line_position].split()[0] == 'KR_DO':
                    output_list.append(' ' * space_count +
                                       lines[line_position])
                    line_position += 1
                    E()
                    lista_naredbi()
                    if line_position < line_count and lines[line_position].split()[0] == 'KR_AZ':
                        output_list.append(
                            ' ' * space_count + lines[line_position])
                        line_position += 1
                    else:
                        err_positions.append(line_position)
                else:
                    err_positions.append(line_position)
            else:
                err_positions.append(line_position)
        else:
            err_positions.append(line_position)
    else:
        err_positions.append(line_position)
    space_count -= 1


def E():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<E>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] in ['IDN', 'BROJ', 'OP_PLUS', 'OP_MINUS', 'L_ZAGRADA']:
        T()
        E_lista()
    else:
        err_positions.append(line_position)
    space_count -= 1


def E_lista():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<E_lista>')
    space_count += 1
    if line_position >= line_count or lines[line_position].split()[0] in ['IDN', 'KR_ZA', 'KR_DO', 'KR_AZ', 'D_ZAGRADA']:
        output_list.append(' ' * space_count + '$')
    elif line_position < line_count and lines[line_position].split()[0] == 'OP_PLUS':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        E()
    elif line_position < line_count and lines[line_position].split()[0] == 'OP_MINUS':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        E()
    else:
        err_positions.append(line_position)
    space_count -= 1


def T():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<T>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] in ['IDN', 'BROJ', 'OP_PLUS', 'OP_MINUS', 'L_ZAGRADA']:
        P()
        T_lista()
    else:
        err_positions.append(line_position)
    space_count -= 1


def T_lista():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<T_lista>')
    space_count += 1
    if line_position >= line_count or lines[line_position].split()[0] in ['IDN', 'KR_ZA', 'KR_DO', 'KR_AZ', 'OP_PLUS', 'OP_MINUS', 'D_ZAGRADA']:
        output_list.append(' ' * space_count + '$')
    elif lines[line_position].split()[0] == 'OP_PUTA':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        T()
    elif lines[line_position].split()[0] == 'OP_DIJELI':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        T()
    else:
        err_positions.append(line_position)
    space_count -= 1


def P():
    global line_position, line_count, space_count
    output_list.append(' ' * space_count + '<P>')
    space_count += 1
    if line_position < line_count and lines[line_position].split()[0] == 'OP_PLUS':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        P()
    elif line_position < line_count and lines[line_position].split()[0] == 'OP_MINUS':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        P()
    elif line_position < line_count and lines[line_position].split()[0] == 'L_ZAGRADA':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
        E()
        if line_position < line_count and lines[line_position].split()[0] == 'D_ZAGRADA':
            output_list.append(' ' * space_count + lines[line_position])
            line_position += 1
        else:
            err_positions.append(line_position)
    elif line_position < line_count and lines[line_position].split()[0] == 'IDN':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
    elif line_position < line_count and lines[line_position].split()[0] == 'BROJ':
        output_list.append(' ' * space_count + lines[line_position])
        line_position += 1
    else:
        err_positions.append(line_position)
    space_count -= 1


all_text = sys.stdin.readlines()
lines = []
for line in all_text:
    lines.append(line.strip())
    line_count += 1

program()

if len(err_positions):
    if err_positions[0] == line_count:
        print('err kraj')
    else:
        print('err ' + lines[err_positions[0]])
else:
    for line in output_list:
        print(line)
