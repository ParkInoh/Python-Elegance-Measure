import ply.lex as lex

class PythonLexer(object) :
    reserved = {    
        'None' : 'NONE',        #reserved words
        'and' : 'AND',
        'as' : 'AS',
        'assert' : 'ASSERT',
        'async' : 'ASYNC',
        'await' : 'AWAIT',
        'break' : 'BREAK',
        'class' : 'CLASS',
        'continue' : 'CONTINUE',
        'def' : 'DEF',
        'del' : 'DEL',
        'elif' : 'ELIF',
        'else' : 'ELSE',
        'except' : 'EXCEPT',
        'finally' : 'FINALLY',
        'for' : 'FOR',
        'from' : 'FROM',
        'global' : 'GLOBAL',
        'if' : 'IF',
        'import' : 'IMPORT',
        'in' : 'IN',
        'is' : 'IS',
        'lambda' : 'LAMBDA',
        'nonlocal' : 'NONLOCAL',
        'not' : 'NOT',
        'or' : 'OR',
        'pass' : 'PASS',
        'raise' : 'RAISE',
        'return' : 'RETURN',
        'try' : 'TRY',
        'while' : 'WHILE',
        'with' : 'WITH',
        'yield' : 'YIELD',
        'abs' : 'ABS',          #built in functions
        'aiter' : 'AITER',
        'all' : 'ALL',
        'any' : 'ANY',
        'anext' : 'ANEXT',
        'ascii' : 'ASCII',
        'bin' : 'BIN',
        'bool' : 'BOOL',
        'breakpoint' : 'BREAKPOINT',
        'bytearray' : 'BYTEARRAY',
        'bytes' : 'BYTES',
        'callable' : 'CALLABLE',
        'chr' : 'CHR',
        'classmethod' : 'CLASSMETHOD',
        'complie' : 'COMPLIE',
        'complex' : 'COMPLEX',
        'delattr' : 'DELATTR',
        'dict' : 'DICT',
        'dir' : 'DIR',
        'divmod' : 'DIVMOD',
        'enumerate' : 'ENUMERATE',
        'eval' : 'EVAL',
        'exec' : 'EXEC',
        'filter' : 'FILTER',
        'float' : 'FLOAT',
        'format' : 'FORMAT',
        'frozenset' : 'FROZENSET',
        'getattr' : 'GETATTR',
        'globals' : 'GLOBALS',
        'hasattr' : 'HASATTR',
        'hash' : 'HASH',
        'help' : 'HELP',
        'hex' : 'HEX',
        'id' : 'ID',
        'input' : 'INPUT',
        'int' : 'INT',
        'isinstance' : 'ISINSTANCE',
        'issubclass' : 'ISSUBCLASS',
        'iter' : 'ITER',
        'len' : 'LEN',
        'list' : 'LIST',
        'locals' : 'LOCALS',
        'map' : 'MAP',
        'max' : 'MAX',
        'memoryview' : 'MEMORYVIEW',
        'min' : 'MIN',
        'next' : 'NEXT',
        'object' : 'OBJECT',
        'oct' : 'OCT',
        'open' : 'OPEN',
        'ord' : 'ORD',
        'pow' : 'POW',
        'print' : 'PRINT',
        'property' : 'PROPERTY',
        'range' : 'RANGE',
        'repr' : 'REPR',
        'reversed' : 'REVERSED',
        'round' : 'ROUND',
        'set' : 'SET',
        'setattr' : 'SETATTR',
        'slice' : 'SLICE',
        'sorted' : 'SORTED',
        'staticmethod' : 'STATICMETHOD',
        'str' : 'STR',
        'sum' : 'SUM',
        'super' : 'SUPER',
        'tuple' : 'TUPLE',
        'type' : 'TYPE',
        'vars' : 'VARS',
        'zip' : 'ZIP',
        '__import__' : '__IMPORT__',
    }
    
    tokens = [
        'NAME',
        'FUNCTION',
        'INTEGER',
        'FLOATNUM',
        'COMPLEXNUM',
        'BOOLEAN',
        'STRING',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'MODULUS',
        'FLOORDIVISION',
        'EXPONENT',
        'GREATER',
        'LESS',
        'GREATEREQUAL',
        'LESSEQUAL',
        'EQUAL',
        'NOTEQUAL',
        'LPAREN',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'LBRACKET',
        'RBRACKET',
        'COMMA',
        'DOT',
        'COLON',
        'ASSIGNMENT',
        'UNDERBAR',
        'TRIPLEDOT',
        'BLANK',
        'INDENT',
        'NEWLINE',
    ] + list(reserved.values())

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULUS = r'%'
    t_FLOORDIVISION = r'//'
    t_EXPONENT = r'\*\*'
    t_GREATER = r'>'
    t_LESS = r'<'
    t_GREATEREQUAL = r'>='
    t_LESSEQUAL = r'<='
    t_EQUAL = r'=='
    t_NOTEQUAL = r'!='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_COMMA = r','
    t_DOT = r'\.'
    t_COLON = r':'
    t_ASSIGNMENT = r'='
    t_UNDERBAR = r'_'
    t_TRIPLEDOT = r'\.{3}'
    t_BLANK = r'[  \t\v\r\f]'   #Since there are two types of spaces, they are added separately.

    t_ignore_COMMENT = r'\#.*'

    def t_COMPLEXNUM(self, t):
        r'([+-]?(0|[1-9]\d*)\.\d+([eE][+-]?(0|[1-9]\d*))?)?[+-]?(0|[1-9]\d*)\.\d+([eE][+-]?(0|[1-9]\d*))?j'
        return t

    def t_FLOATNUM(self, t):
        r'[+-]?(0|[1-9]\d*)\.\d+([eE][+-]?(0|[1-9]\d*))?'
        return t

    def t_INTEGER(self, t):
        r'[+-]?(0|[1-9]\d*)'
        return t
    
    def t_STRING(self, t):
        r'[fr]?(\'\'\'[^(\"\"\")]*\'\'\'|\"\"\"[^(\"\"\")]*\"\"\"|\'[^\']*\'|\"[^\"]*\")'
        return t

    def t_BOOLEAN(self, t):
        r'(True|False)'
        return t

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while(True):
            tok = self.lexer.token()
            if(not tok):
                break
            print(tok)

    def tokenize(self, data):
        self.lexer.input(data)
        python_tokens = []

        newline_flag = False
        
        while(True):
            tok = self.lexer.token()
            if(not tok):
                break
            if(tok.type == 'NEWLINE'):
                newline_flag = True
            if(tok.type == 'BLANK' and newline_flag == False):
                continue
            if(tok.type != 'NEWLINE' and tok.type != 'BLANK' and newline_flag == True):
                newline_flag = False
            python_tokens.append(tok)

        functions = []
        for i in range(len(python_tokens)):
            if(python_tokens[i].type == 'DEF' and python_tokens[i+1].type == 'NAME'):
                python_tokens[i+1].type = 'FUNCTION'
                functions.append(python_tokens[i+1].value)
                continue
            if(python_tokens[i].type == 'NAME' and python_tokens[i].value in functions):
                python_tokens[i].type = 'FUNCTION'
                continue

        return python_tokens

    def tokenize_indent(self, data):
        python_tokens = self.tokenize(data)
        indent_tokens = []

        indent_flag = False

        for tok in python_tokens:
            if(tok.type == 'BLANK' and indent_flag == False):
                tok.type = 'INDENT'
                indent_flag = True
                indent_tokens.append(tok)
            elif(tok.type == 'BLANK' and indent_flag == True):
                indent_tokens[-1].value += tok.value
            else:
                indent_flag = False
                indent_tokens.append(tok)

        return indent_tokens
