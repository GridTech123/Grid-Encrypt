from Tkinter import *

def encrypt():
    print '----------------------------------------------------------------------------'
    print e.get()
    labelText_str = e.get()
    length = len(labelText_str)
    print length
    clock = 1
    output = ''
    while clock < length + 1:
        letter = labelText_str[clock - 1:clock]
        #-
        if letter == 'q':
            output = output + '-1'
        if letter == 'w':
            output = output + '-2'
        if letter == 'e':
            output = output + '-3'
        if letter == 'r':
            output = output + '-4'
        if letter == 't':
            output = output + '-5'
        if letter == 'y':
            output = output + '-6'
        if letter == 'u':
            output = output + '-7'
        if letter == 'i':
            output = output + '-8'
        if letter == 'o':
            output = output + '-9'
        if letter == 'p':
            output = output + '-~'
        if letter == 'a':
            output = output + '-@'
        if letter == 's':
            output = output + '-#'
        if letter == 'd':
            output = output + '-$'
        if letter == 'f':
            output = output + '-%'
        if letter == 'g':
            output = output + '-^'
        if letter == 'h':
            output = output + '-&'
        if letter == 'j':
            output = output + '-*'
        if letter == 'k':
            output = output + '-('
        if letter == 'l':
            output = output + '-)'
        if letter == 'z':
            output = output + '-_'
        if letter == 'x':
            output = output + '-='
        if letter == 'c':
            output = output + '-+'
        if letter == 'v':
            output = output + '-['
        if letter == 'b':
            output = output + '-]'
        if letter == 'n':
            output = output + '-{'
        if letter == 'm':
            output = output + '-}'
        if letter == ' ':
            output = output + '-;'
        #!
        if letter == '@':
            output = output + '!1'
        if letter == '#':
            output = output + '!2'
        if letter == '$':
            output = output + '!3'
        if letter == '%':
            output = output + '!4'
        if letter == '^':
            output = output + '!5'
        if letter == '&':
            output = output + '!6'
        if letter == '*':
            output = output + '!7'
        if letter == '(':
            output = output + '!8'
        if letter == ')':
            output = output + '!9'
        if letter == '.':
            output = output + '!~'
        if letter == '/':
            output = output + '!@'
        if letter == '?':
            output = output + '!#'
        if letter == '[':
            output = output + '!_'
        if letter == ']':
            output = output + '!='
        if letter == '+':
            output = output + '!:'
        if letter == '-':
            output = output + '!;'
        #`
        if letter == 'Q':
            output = output + '`1'
        if letter == 'W':
            output = output + '`2'
        if letter == 'E':
            output = output + '`3'
        if letter == 'R':
            output = output + '`4'
        if letter == 'T':
            output = output + '`5'
        if letter == 'Y':
            output = output + '`6'
        if letter == 'U':
            output = output + '`7'
        if letter == 'I':
            output = output + '`8'
        if letter == 'O':
            output = output + '`9'
        if letter == 'P':
            output = output + '`~'
        if letter == 'A':
            output = output + '`@'
        if letter == 'S':
            output = output + '`#'
        if letter == 'D':
            output = output + '`$'
        if letter == 'F':
            output = output + '`%'
        if letter == 'G':
            output = output + '`^'
        if letter == 'H':
            output = output + '`&'
        if letter == 'J':
            output = output + '`*'
        if letter == 'K':
            output = output + '`('
        if letter == 'L':
            output = output + '`)'
        if letter == 'Z':
            output = output + '`_'
        if letter == 'X':
            output = output + '`='
        if letter == 'C':
            output = output + '`+'
        if letter == 'V':
            output = output + '`['
        if letter == 'B':
            output = output + '`]'
        if letter == 'N':
            output = output + '`{'
        if letter == 'M':
            output = output + '`}'
        clock = clock + 1
    else:
        print 'the encrypted code is: ',output

def decrypt():
    print '----------------------------------------------------------------------------'
    print e.get()
    labelText_str = e.get()
    length = len(labelText_str)
    print length
    clock = 1
    output = ''
    while clock < length + 1:
        letter = labelText_str[clock - 1:clock]
        if letter == '-':
            if labelText_str[clock:clock + 1] == '1':
                output = output + 'q'
            if labelText_str[clock:clock + 1] == '2':
                output = output + 'w'
            if labelText_str[clock:clock + 1] == '3':
                output = output + 'e'
            if labelText_str[clock:clock + 1] == '4':
                output = output + 'r'
            if labelText_str[clock:clock + 1] == '5':
                output = output + 't'
            if labelText_str[clock:clock + 1] == '6':
                output = output + 'y'
            if labelText_str[clock:clock + 1] == '7':
                output = output + 'u'
            if labelText_str[clock:clock + 1] == '8':
                output = output + 'i'
            if labelText_str[clock:clock + 1] == '9':
                output = output + 'o'
            if labelText_str[clock:clock + 1] == '!':
                output = output + 'p'
            if labelText_str[clock:clock + 1] == '@':
                output = output + 'a'
            if labelText_str[clock:clock + 1] == '#':
                output = output + 's'
            if labelText_str[clock:clock + 1] == '$':
                output = output + 'd'
            if labelText_str[clock:clock + 1] == '%':
                output = output + 'f'
            if labelText_str[clock:clock + 1] == '^':
                output = output + 'g'
            if labelText_str[clock:clock + 1] == '&':
                output = output + 'h'
            if labelText_str[clock:clock + 1] == '*':
                output = output + 'j'
            if labelText_str[clock:clock + 1] == '(':
                output = output + 'k'
            if labelText_str[clock:clock + 1] == ')':
                output = output + 'l'
            if labelText_str[clock:clock + 1] == '_':
                output = output + 'z'
            if labelText_str[clock:clock + 1] == '=':
                output = output + 'x'
            if labelText_str[clock:clock + 1] == '+':
                output = output + 'c'
            if labelText_str[clock:clock + 1] == '[':
                output = output + 'v'
            if labelText_str[clock:clock + 1] == ']':
                output = output + 'b'
            if labelText_str[clock:clock + 1] == '{':
                output = output + 'n'
            if labelText_str[clock:clock + 1] == '}':
                output = output + 'm'
            if labelText_str[clock:clock + 1] == ';':
                output = output + ' '
        if letter == '!':
            if labelText_str[clock:clock + 1] == '1':
                output = output + '@'
            if labelText_str[clock:clock + 1] == '2':
                output = output + '#'
            if labelText_str[clock:clock + 1] == '3':
                output = output + '$'
            if labelText_str[clock:clock + 1] == '4':
                output = output + '%'
            if labelText_str[clock:clock + 1] == '5':
                output = output + '^'
            if labelText_str[clock:clock + 1] == '6':
                output = output + '&'
            if labelText_str[clock:clock + 1] == '7':
                output = output + '*'
            if labelText_str[clock:clock + 1] == '8':
                output = output + '('
            if labelText_str[clock:clock + 1] == '9':
                output = output + ')'
            if labelText_str[clock:clock + 1] == '~':
                output = output + '.'
            if labelText_str[clock:clock + 1] == '@':
                output = output + '/'
            if labelText_str[clock:clock + 1] == '#':
                output = output + '?'
            if labelText_str[clock:clock + 1] == '_':
                output = output + '['
            if labelText_str[clock:clock + 1] == '=':
                output = output + ']'
            if labelText_str[clock:clock + 1] == ':':
                output = output + '+'
            if labelText_str[clock:clock + 1] == ';':
                output = output + '-'
        if letter == '`':
            if labelText_str[clock:clock + 1] == '1':
                output = output + 'Q'
            if labelText_str[clock:clock + 1] == '2':
                output = output + 'W'
            if labelText_str[clock:clock + 1] == '3':
                output = output + 'E'
            if labelText_str[clock:clock + 1] == '4':
                output = output + 'R'
            if labelText_str[clock:clock + 1] == '5':
                output = output + 'T'
            if labelText_str[clock:clock + 1] == '6':
                output = output + 'Y'
            if labelText_str[clock:clock + 1] == '7':
                output = output + 'U'
            if labelText_str[clock:clock + 1] == '8':
                output = output + 'I'
            if labelText_str[clock:clock + 1] == '9':
                output = output + 'O'
            if labelText_str[clock:clock + 1] == '!':
                output = output + 'P'
            if labelText_str[clock:clock + 1] == '@':
                output = output + 'A'
            if labelText_str[clock:clock + 1] == '#':
                output = output + 'S'
            if labelText_str[clock:clock + 1] == '$':
                output = output + 'D'
            if labelText_str[clock:clock + 1] == '%':
                output = output + 'F'
            if labelText_str[clock:clock + 1] == '^':
                output = output + 'G'
            if labelText_str[clock:clock + 1] == '&':
                output = output + 'H'
            if labelText_str[clock:clock + 1] == '*':
                output = output + 'J'
            if labelText_str[clock:clock + 1] == '(':
                output = output + 'K'
            if labelText_str[clock:clock + 1] == ')':
                output = output + 'L'
            if labelText_str[clock:clock + 1] == '_':
                output = output + 'Z'
            if labelText_str[clock:clock + 1] == '=':
                output = output + 'X'
            if labelText_str[clock:clock + 1] == '+':
                output = output + 'C'
            if labelText_str[clock:clock + 1] == '[':
                output = output + 'V'
            if labelText_str[clock:clock + 1] == ']':
                output = output + 'B'
            if labelText_str[clock:clock + 1] == '{':
                output = output + 'N'
            if labelText_str[clock:clock + 1] == '}':
                output = output + 'M'
        clock = clock + 1
    else:
        print 'The decrypted text it: ',output
    

def generate():
    v_int = v.get()
    if v_int == 1:
        encrypt()
    elif v_int == 2:
        decrypt()
    else:
        print 'choose one'

app = Tk()
app.title('Grid Encrypt')
app.geometry('500x250')

labelText = StringVar()
labelText.set('Enter Text to Encrypt or Decrypt:')
label1 = Label(app, textvariable = labelText, height = 4)
label1.pack()

e = Entry(app, width = 70)
e.pack()

v = IntVar()

Radiobutton(app, text="Encrypt", variable=v, value=1).pack(anchor=W)
Radiobutton(app, text="Decrypt", variable=v, value=2).pack(anchor=W)

logbutton = Button(app, text = 'Generate', width = 60, command = generate)
logbutton.pack(padx = 15, pady = 15)

app.mainloop()