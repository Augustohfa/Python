# Encapsulamento (modificadores de acesso: public, protected, private)
# python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#       (sem uderline) = public
#               pode ser usado em qualquer lugar
# _      (um underline) = protected
#               não DEVE ser usado fora da classe
#               ou de suas sub classes
# __       (dois underlines ou __) = private
#               "name mangling" (desfiguração de nomes) em Python
#               só DEVE ser usado na classe em que foi
#               declarado.
#
# Classes
class Foo:
    def __init__(self):
        self.public = 'This is public'
        self._protected = 'This is protected'
        self.__private = 'This is private to __init__ function'

    def public_method(self):
        return 'Public method'

    def _protected_method(self):
        print(self.__private)
        return 'Protected method'

# Objetos


f = Foo()

# Code

print(f._protected)
print(f._protected_method())
