# 5. Classes

# Nós usamos o operador "class" para ter uma classe
class Human:

    # Um atributo de classe. Ele é compartilhado por todas as instâncias dessa
    # classe.
    species = "H. sapiens"

    # Construtor básico, é chamado quando esta classe é instanciada.
    # Note que dois sublinhados no início e no final de uma identificados
    # significa objetos ou atributos que são usados pelo python mas vivem em
    # um namespace controlado pelo usuário. Métodos (ou objetos ou atributos)
    # como: __init__, __str__, __repr__, etc. são chamados métodos mágicos (ou
    # algumas vezes chamados métodos dunder - "double underscore")
    # Você não deve usar nomes assim por sua vontade.
    def __init__(self, name):
        @ Atribui o argumento ao atributo da  instância
        self.name = name

    # Um método de instância. Todos os métodos tem "self" como primeiro
    # argumento
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

    # Um método de classe é compartilhado por todas as instâncias
    # Eles são chamados com a classe requisitante como primeiro argumento
    @classmethod
    def get_species(cls):
        return cls.species

    # Um método estático é chamado sem uma referência a classe ou instância
    @staticmethod
    def grunt():
        return "*grunt*"


# Instancie uma classe
i = Human(name="Ian")
print(i.say("oi"))     # imprime "Ian: oi"

j = Human("Joel")
print(j.say("olá"))  # imprime "Joel: olá"

# Chama nosso método de classe
i.get_species()  # => "H. sapiens"

# Altera um atributo compartilhado
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# Chama o método estático
Human.grunt()    # => "*grunt*"
