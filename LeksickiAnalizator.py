import sys

keywords = ['za', 'az', 'od', 'do']
operators = ['+', '-', '/', '*', '=']

def processKR(lineNum, word):
    print('KR_' + word.upper() + ' ' + str(lineNum) + ' ' + word)

def processLZ(lineNum):
    print('L_ZAGRADA ' + str(lineNum) + ' (')

def processDZ(lineNum):
    print('D_ZAGRADA ' + str(lineNum) + ' )')

def processOP(lineNum, word):
    sol = ''
    if word == '+':
        sol += 'OP_PLUS'
    elif word == '-':
        sol += 'OP_MINUS'
    elif word == '*':
        sol += 'OP_PUTA'
    elif word == '/':
        sol += 'OP_DIJELI'
    elif word == '=':
        sol += 'OP_PRIDRUZI'
    sol += ' ' + str(lineNum) + ' ' + word
    print(sol)

def processWORD(lineNum, word):
    num = ''
    for letter in word:
        if not letter.isnumeric():
            word = word.replace(num, '', 1)
            break
        else:
            num += letter
    if num:
        print('BROJ ' + str(lineNum) + ' ' + num)
    if num != word:
        print('IDN ' + str(lineNum) + ' ' + word)

def processCOMBO(lineNum, word):
    newWord = ''
    for letter in word:
        if not letter.isalnum():
            if newWord:
                processWORD(lineNum, newWord)
            newWord = ''
            if letter == '(':
                processLZ(lineNum)
            if letter == ')':
                processDZ(lineNum)
            if letter in operators:
                processOP(lineNum, letter)
        else:
            newWord += letter
    if newWord:
        processWORD(lineNum, newWord)
#input
allText = sys.stdin.readlines()
lines = []
for line in allText:
    lines.append(line.strip())

#line processing
lineCount = 1
for line in lines:
    words = line.split()
    for word in words:
        if '//' in word:
            break
        if word in keywords:
            processKR(lineCount, word)
        else:
            processCOMBO(lineCount, word)
    lineCount += 1
