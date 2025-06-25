"""
Módulo analisador.py

Implementa o analisador léxico para códigos em Pascal.
Reconhece tokens como palavras reservadas, identificadores, números, strings,
operadores e delimitadores.
Pode ser utilizado como módulo em aplicações Flask ou scripts de linha de comando.
"""

RESERVADAS = {
    # Tipos
    'integer': 'TIPO',
    'real': 'TIPO',
    'boolean': 'TIPO',
    'char': 'TIPO',
    'string': 'TIPO',

    # Entrada/Saída
    'read': 'LEITURA',
    'readln': 'LEITURA',
    'write': 'ESCRITA',
    'writeln': 'ESCRITA',

    # Condicionais
    'if': 'CONDICIONAL',
    'then': 'CONDICIONAL',
    'else': 'CONDICIONAL',
    'case': 'CONDICIONAL',

    # Laços
    'for': 'LACO',
    'to': 'LACO',
    'downto': 'LACO',
    'do': 'LACO',
    'while': 'LACO',
    'repeat': 'LACO',
    'until': 'LACO',

    # Estrutura de programa
    'program': 'PROGRAMA',
    'begin': 'BLOCO',
    'end': 'BLOCO',
    'var': 'DECLARACAO',
    'const': 'DECLARACAO',
    'procedure': 'SUBPROGRAMA',
    'function': 'SUBPROGRAMA',

    # Outros
    'and': 'LOGICO',
    'or': 'LOGICO',
    'not': 'LOGICO',
    'div': 'ARITMETICO',
    'mod': 'ARITMETICO',
    'with': 'OUTRO',
    'of': 'OUTRO',
    'array': 'TIPO',
    'record': 'TIPO',
    'type': 'DECLARACAO',
    'nil': 'OUTRO',
    'goto': 'OUTRO',
    'label': 'OUTRO'
}

OPERADORES = {'+', '-', '*', '/', '=', '>', '<'}
OPERADORES_RELACIONAIS = {'>=', '<=', '<>', '>' , '<', '='}
DELIMITADORES = {';', '(', ')', ',', '.', ':'}

def is_letter(c):
    """Retorna True se o caractere for uma letra."""
    return c.isalpha()

def is_digit(c):
    """Retorna True se o caractere for um dígito."""
    return c.isdigit()

def le_token(code, pos):
    """
    Lê o próximo token a partir da posição 'pos' no código.
    Retorna uma tupla (tipo, lexema, nova_pos).
    """
    while pos < len(code) and code[pos].isspace():
        pos += 1
    if pos >= len(code):
        return ('EOF', '', pos)

    c = code[pos]

    # Strings entre aspas simples ou duplas
    if c in ('"', "'"):
        aspas = c
        start = pos
        pos += 1
        while pos < len(code) and code[pos] != aspas:
            pos += 1
        if pos < len(code) and code[pos] == aspas:
            pos += 1
            return ('Nstring', code[start:pos], pos)
        return ('TOKEN_DESCONHECIDO', code[start:], len(code))

    # Identificadores e palavras reservadas
    if is_letter(c):
        start = pos
        while pos < len(code) and (is_letter(code[pos]) or is_digit(code[pos])):
            pos += 1
        lexema = code[start:pos]
        token_type = RESERVADAS.get(lexema.lower(), 'ID')
        return (token_type, lexema, pos)

    # Números inteiros e reais
    if is_digit(c):
        start = pos
        while pos < len(code) and is_digit(code[pos]):
            pos += 1
        if pos < len(code) and code[pos] == '.':
            pos += 1
            if pos < len(code) and is_digit(code[pos]):
                while pos < len(code) and is_digit(code[pos]):
                    pos += 1
                return ('Nreal', code[start:pos], pos)
            return ('TOKEN_DESCONHECIDO', code[start:pos], pos)
        return ('Nint', code[start:pos], pos)

    # Operadores relacionais compostos
    if c in {'<', '>'}:
        if pos+1 < len(code):
            next_c = code[pos+1]
            if c == '<' and next_c == '>':
                return ('OP', '<>', pos+2)
            if next_c == '=':
                return ('OP', c + '=', pos+2)
        return ('OP', c, pos+1)

    # Atribuição
    if c == ':' and pos+1 < len(code) and code[pos+1] == '=':
        return ('ATRIB', ':=', pos+2)

    # Operadores simples
    if c in OPERADORES:
        return ('OP', c, pos+1)

    # Delimitadores
    if c in DELIMITADORES:
        return ('DELIM', c, pos+1)

    # Token desconhecido
    return ('TOKEN_DESCONHECIDO', c, pos+1)

def analyze_code(code):
    """
    Analisa todo o código fonte e retorna uma lista de tokens.
    Cada token é uma tupla (tipo, lexema).
    """
    pos = 0
    tokens = []
    while True:
        token_type, lexema, pos = le_token(code, pos)
        tokens.append((token_type, lexema))
        if token_type == 'EOF':
            break
    return tokens
