# 2. Variáveis e coleções

# Python tem uma função print
print("Eu sou o Python. Prazer em conhecer!")  # => Eu sou o Python. Prazer em conhecer!

# Por padrão a função print também imprime o caractere de nova linha ao final.
# Use o argumento opcional end para mudar o caractere final.
print("Olá, Mundo", end="!")  # => Olá, Mundo!

# Forma simples para capturar dados de entrada via console
input_string_var = input("Digite alguma coisa: ") # Retorna o que foi digitado em uma string
# Observação: Em versões antigas do Python, o método input() era chamado raw_input()

# Não é necessário declarar variáveis antes de iniciá-las
# É uma convenção usar letras_minúsculas_com_sublinhados
alguma_variavel = 5
alguma_variavel  # => 5

# Acessar uma variável que não tenha sido inicializada gera uma exceção.
# Veja Controle de Fluxo para aprender mais sobre tratamento de exceções.
alguma_variavel_nao_inicializada  # Gera a exceção NameError

# Listas armazenam sequências
li = []

# Você pode iniciar uma lista com valores
outra_li = [4, 5, 6]

# Adicione conteúdo ao fim da lista com append
li.append(1)    # li agora é [1]
li.append(2)    # li agora é [1, 2]
li.append(4)    # li agora é [1, 2, 4]
li.append(3)    # li agora é [1, 2, 4, 3]

# Remova do final da lista com pop
li.pop()        # => 3 e agora li é [1, 2, 4]

# Vamos colocá-lo lá novamente!
li.append(3)    # li agora é [1, 2, 4, 3] novamente.

# Acesse uma lista da mesma forma que você faz com um array
li[0]   # => 1

# Acessando o último elemento
li[-1]  # => 3

# Acessar além dos limites gera um IndexError
li[4]  # Gera o IndexError

# Você pode acessar vários elementos com a sintaxe de limites
# Inclusivo para o primeiro termo, exclusivo para o segundo
li[1:3]   # => [2, 4]
# Omitindo o final
li[2:]    # => [4, 3]
# Omitindo o início
li[:3]    # => [1, 2, 4]
# Selecione cada segunda entrada
li[::2]   # => [1, 4]
# Tenha uma cópia em ordem invertida da lista
li[::-1]  # => [3, 4, 2, 1]
# Use qualquer combinação dessas para indicar limites complexos
# li[inicio:fim:passo]

# Faça uma cópia profunda de um nível usando limites
li2 = li[:]  # => li2 = [1, 2, 4, 3] mas (li2 is li) resultará em False.

# Apague elementos específicos da lista com "del"
del li[2]  # li agora é [1, 2, 3]
 
# Você pode somar listas
# Observação: valores em li e other_li não são modificados.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatene listas com "extend()"
li.extend(other_li)  # Agora li é [1, 2, 3, 4, 5, 6]

# Verifique se algo existe na lista com "in"
1 in li  # => True

# Examine  tamanho com "len()"
len(li)  # => 6

# Tuplas são como l istas, mas imutáveis.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Gera um TypeError

# Observe que uma tupla de tamanho um precisa ter uma vírgula depois do
# último elemento mas tuplas de outros tamanhos, mesmo vazias, não precisa,.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# Você pode realizar com tuplas a maior parte das operações que faz com listas
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# Você pode desmembrar tuplas (ou listas) em variáveis.
a, b, c = (1, 2, 3)  # a é 1, b é 2 e c é 3

# Por padrão, tuplas são criadas se você não coloca parêntesis.
d, e, f = 4, 5, 6

# Veja como é fácil permutar dois valores
e, d = d, e  # d é 5, e é 4

# Dicionários armazenam mapeamentos
empty_dict = {}

# Aqui está um dicionário preenchido na definição da referência
filled_dict = {"um": 1, "dois": 2, "três": 3}

# Observe que chaves para dicionários devem ser tipos imutáveis. Isto é para
# assegurar que a chave pode ser convertida para uma valor hash constante para
# buscas rápidas.
# Tipos imutáveis incluem inteiros, flotas, strings e tuplas.
invalid_dict = {[1,2,3]: "123"}  # => Gera um TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Já os valores, podem ser de qualquer tipo.

# Acesse valores com []
filled_dict["um"]  # => 1

# Acesse todas as chaves como um iterável com "keys()". É necessário encapsular
# a chamada com um list() para transformá-las em uma lista. Falaremos sobre isso
# mais adiante. Observe que a ordem de uma chave de dicionário não é garantida.
# Por isso, os resultados aqui apresentados podem não ser exatamente como os
# aqui apresentados.
list(filled_dict.keys())  # => ["três", "dois", "um"]

# Acesse todos os valores de um iterável com "values()". Novamente, é
# necessário encapsular ele com list() para não termos um iterável, e sim os
# valores. Observe que, como foi dito acima, a ordem dos elementos não é
# garantida.
list(filled_dict.values())  # => [3, 2, 1]

# Verifique a existência de chaves em um dicionário com "in"
"um" in filled_dict  # => True
1 in filled_dict      # => False

# Acessar uma chave inexistente gera um KeyError
filled_dict["quatro"]  # KeyError

# Use o método "get()" para evitar um KeyError
filled_dict.get("um")      # => 1
filled_dict.get("quatro")     # => None

# O método get permite um parâmetro padrão para quando não existir a chave
filled_dict.get("um", 4)   # => 1
filled_dict.get("quatro", 4)  # => 4

# "setdefault()" insere em dicionário apenas se a dada chave não existir
filled_dict.setdefault("cinco", 5)  # filled_dict["cinco"] tem valor 5
filled_dict.setdefault("cinco", 6)  # filled_dict["cinco"] continua 5

# Inserindo em um dicionário
filled_dict.update({"quatro":4})  # => {"um": 1, "dois": 2, "três": 3, "quatro": 4}
#filled_dict["quatro"] = 4        #outra forma de inserir em um dicionário

# Remova chaves de um dicionário com del
del filled_dict["um"]  # Remove a chave "um" de filled_dict

# Armazenamento em sets... bem, são conjuntos
empty_set = set()

# Inicializa um set com alguns valores. Sim, ele parece um dicionário. Desculpe.
some_set = {1, 1, 2, 2, 3, 4}  # some_set agora é {1, 2, 3, 4}

# Da mesma forma que chaves em um dicionário, elementos de um set devem ser
# imutáveis.
invalid_set = {[1], 1}  # => Gera um TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Pode definir novas variáveis para um conjunto
filled_set = some_set

# Inclua mais um item no set
filled_set.add(5)  # filled_set agora é {1, 2, 3, 4, 5}

# Faça interseção de conjuntos com &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Faça união de conjuntos com |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Faça a diferença entre conjuntos com -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Verifique a existência em um conjunto com in
2 in filled_set   # => True
10 in filled_set  # => False


