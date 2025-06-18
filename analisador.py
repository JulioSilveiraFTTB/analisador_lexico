from utils.cores import Cores
from utils.prints import Print

RESERVADAS = {
    'integer': 'TIPO',
    'real': 'TIPO',
    'boolean': 'TIPO',
    'read': 'LEITURA',
    'readln': 'LEITURA',
    'write': 'ESCRITA',
    'writeln': 'ESCRITA',
    'if': 'CONDICIONAL'
}

OPERADORES = {'+', '-', '*', '/', '='}
DELIMITADORES = {';', '(', ')', ',', '.'}

def is_letter(c):
    return c.isalpha()

def is_digit(c):
    return c.isdigit()

def le_token(code, pos):
    while pos < len(code) and code[pos].isspace():
        pos += 1
    if pos >= len(code):
        return ('EOF', '', pos)

    c = code[pos]

    if is_letter(c):
        start = pos
        while pos < len(code) and (is_letter(code[pos]) or is_digit(code[pos])):
            pos += 1
        lexema = code[start:pos]
        type = RESERVADAS.get(lexema.lower(), 'ID')
        return (type, lexema, pos)

    if is_digit(c):
        start = pos
        while pos < len(code) and is_digit(code[pos]):
            pos += 1
        if pos < len(code) and code[pos] == '.':
            pos += 1
            if pos < len(code) and is_digit(code[pos]):
                while pos < len(code) and is_digit(code[pos]):
                    pos += 1
                return ('NREAL', code[start:pos], pos)
            else:
                return ('TOKEN_DESCONHECIDO', code[start:pos], pos)
        else:
            return ('NINT', code[start:pos], pos)

    if c == ':' and pos+1 < len(code) and code[pos+1] == '=':
        return ('ATRIB', ':=', pos+2)

    if c in OPERADORES:
        return ('OP', c, pos+1)

    if c in DELIMITADORES:
        return ('DELIM', c, pos+1)

    return ('TOKEN_DESCONHECIDO', c, pos+1)

def analyze_code(code):
    pos = 0
    tokens = []
    while True:
        type, lexema, pos = le_token(code, pos)
        tokens.append((type, lexema))
        if type == 'EOF':
            break
    return tokens

if __name__ == "__main__":
    with open('codigo.txt', encoding='utf-8') as f:
        code = f.read()
    tokens = analyze_code(code)

    Print.print_banner()
    Print.print_table(tokens)
    Print.print_footer(tokens)
    input(Print.cor_token('DELIM') + "Pressione Enter para sair..." + Cores.ENDC)
