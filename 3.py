# 3. Controle de fluxo e iteráveis

# Iniciemos um variável
some_var = 5

# Aqui está uma expressão if. Indentação é significante em python!
# imprime "somevar é menor que10"
if some_var > 10:
    print("some_var é absolutamente maior que 10.")
elif some_var < 10:    # Esta cláusula elif é opcional.
    print("some_var é menor que 10.")
else:                  # Isto também é opcional.
    print("some_var é, de fato, 10.")

"""
Laços for iteram sobre listas
imprime:
    cachorro é um mamífero
    gato é um mamífero
    rato é um mamífero
"""

for animal in ["cachorro", "gato", "rato"]:
    # Você pode usar format() para interpolar strings formatadas
    print("{} é um mamífero".format(animal))


"""
"range(número)" retorna um iterável de números
de zero até o número escolhido
imprime:
    0
    1
    2
    3
"""

for i in range(4):
    print(i)


"""
"range(menor, maior)" gera um iterável de números
começando pelo menor até o maior
imprime:
    4
    5
    6
    7
"""

for i in range(4, 8):
    print(i)


"""
"range(menor, maior, passo)" retorna um iterável de números
começando pelo menor número até o maior númeno, pulando de
passo em passo. Se o passo não for indicado, o valor padrão é um.
imprime:
    4
    6
"""

for i in range(4, 8, 2):
    print(i)


"""

Laços while executam até que a condição não seja mais válida.
imprime:
    0
    1
    2
    3
"""

x = 0
while x < 4:
    print(x)
    x += 1  # Maneira mais curta para for x = x + 1

# Lide com exceções com um bloco try/except
try:
    # Use "raise" para gerar um erro
    raise IndexError("Isto é um erro de índice")
except IndexError as e:
    pass                 # Pass é um não-operador. Normalmente você usa algum código de recuperação aqui.
except (TypeError, NameError):
    pass                 # Varias exceções podem ser gerenciadas, se necessário.
else:                    # Cláusula opcional para o bloco try/except. Deve estar após todos os blocos de exceção.
    print("Tudo certo!")   # Executa apenas se o código em try não gera exceção
finally:                 #  Sempre é executado
    print("Nós podemos fazer o código de limpeza aqui.")

# Ao invés de try/finally para limpeza você pode usar a cláusula with
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Python provê uma abstração fundamental chamada Iterável.
# Um iterável é um objeto que pode ser tratado como uma sequência.
# O objeto retornou a função range, um iterável.

filled_dict = {"um": 1, "dois": 2, "três": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => range(1,10). Esse é um objeto que implementa nossa interface iterável.

# Nós podemos percorrê-la.
for i in our_iterable:
    print(i)  # Imprime um, dois, três

# Mas não podemos acessar os elementos pelo seu índice.
our_iterable[1]  # Gera um TypeError

# Um iterável é um objeto que sabe como criar um iterador.
our_iterator = iter(our_iterable)

# Nosso iterador é um objeto que pode lembrar o estado enquanto nós o percorremos.
# Nós acessamos o próximo objeto com "next()".
next(our_iterator)  # => "um"

# Ele mantém o estado enquanto nós o percorremos.
next(our_iterator)  # => "dois"
next(our_iterator)  # => "três"

# Após o iterador retornar todos os seus dados, ele gera a exceção StopIterator
next(our_iterator)  # Gera StopIteration

# Você pode capturar todos os elementos de um iterador aplicando list() nele.
list(filled_dict.keys())  # => Retorna ["um", "dois", "três"]