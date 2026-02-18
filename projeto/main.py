# Chama a função do arquivo funcao.py
import funcao
funcao.hello_world()

# Chama direto a função sem precisar do prefixo
from funcao import hello_world
hello_world()

# Importando o módulo inteiro
import modulos.funcao
modulos.funcao.hello_world()

# Importando apenas a função
from modulos.funcao import hello_world
hello_world()