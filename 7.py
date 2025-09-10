# 7. Avançado

# Geradores podem ajudar você a escrever código "preguiçoso"
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Um gerador cria valores conforme necessário.
# Ao invés de gerar e retornar todos os valores de uma só vez ele cria um em
# cada interação. Isto significa que valores maiores que 15 não serão
# processados em double_numbers.
# Nós usamos um sublinhado ao final do nome das variáveis quando queremos usar
# um nome que normalmente colide com uma palavra reservada do python.
range_ = range(1, 900000000)
# Multiplica por 2 todos os números até encontrar um resultado >= 30
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break


# Decoradores
# Neste exemplo beg encapsula say
# beg irá chamar say. Se say_please é verdade então ele irá mudar a mensagem
# retornada
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Por favor! Eu sou pobre :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Você me paga uma cerveja?"
    return msg, say_please


print(say())                # Você me paga uma cerveja?
print(say(say_please=True)) # Você me paga uma cerveja? Por favor! Eu sou pobre :(