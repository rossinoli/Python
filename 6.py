# 6. Módulos

# Você pode importar módulos
import math
print(math.sqrt(16))  # => 4.0

# Você pode importar apenas funções específicas de um módulo
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# Você pode importar todas as funções de um módulo para o namespace atual
# Atenção: isso não é recomendado
from math import *

# Você pode encurtar o nome dos módulos
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Módulos python são apenas arquivos python comuns. Você
# pode escrever os seus, e importá-los. O nome do
# módulo é o mesmo nome do arquivo.

# Você pode procurar que atributos e funções definem um módulo.
import math
dir(math)