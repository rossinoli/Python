# 4. Funções

# Use "def" para criar novas funções.
def add(x, y):
    print("x é {} e y é {}".format(x, y))
    return x + y  # Retorne valores com a cláusula return

# Chamando funções com parâmetros
add(5, 6)  # => imprime "x é 5 e y é 6" e retorna 11

# Outro meio de chamar funções é com argumentos nomeados
add(y=6, x=5)  # Argumentos nomeados podem aparecer em qualquer ordem.

# Você pode definir funções que pegam um número variável de argumentos
# posicionais
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# Você pode definir funções que pegam um número variável de argumentos nomeados
# também
def keyword_args(**kwargs):
    return kwargs

# Vamos chamá-lo para ver o que acontece
keyword_args(peh="grande", lago="ness")  # => {"peh": "grande", "lago": "ness"}

# Você pode fazer ambos simultaneamente, se você quiser
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) imprime:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Quando chamar funções, você pode fazer o oposto de args/kwargs!
# Use * para expandir tuplas e use ** para expandir dicionários!
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalente a foo(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalente a foo(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalente a foo(1, 2, 3, 4, a=3, b=4)

# Retornando múltiplos valores (com atribuição de tuplas)
def swap(x, y):
    return y, x  # Retorna múltiplos valores como uma tupla sem os parêntesis.
                 # (Observação: os parêntesis foram excluídos mas podem estar
                 # presentes)
x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Novamente, os parêntesis foram excluídos mas podem estar presentes.

# Escopo de função
x = 5

def setX(num):
    # A variável local x não é a mesma variável global x
    x = num    # => 43
    print (x)  # => 43

def setGlobalX(num):
    global x
    print (x)  # => 5
    x = num    # variável global x agora é 6
    print (x)  # => 6

setX(43)
setGlobalX(6)

# Python tem funções de primeira classe
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# Também existem as funções anônimas
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# TODO - Fix for iterables
# Existem funções internas de alta ordem
map(add_10, [1, 2, 3])          # => [11, 12, 13]
map(max, [1, 2, 3], [4, 2, 1])  # => [4, 2, 3]

filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

# Nós podemos usar compreensão de lista para interessantes mapas e filtros
# Compreensão de lista armazena a saída como uma lista que pode ser uma lista
# aninhada
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]
