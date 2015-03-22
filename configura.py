#! /usr/bin/env python3

import os
from datetime import date
from string import printable, Template

# Solicitação de dados dos usuários
print('''
Quatro (4) dados são necessários para configurar seu caderno digital:

 * Autor (seu nome)
 * E-mail (seu endereço de e-mail)
 * Projeto (título do projeto)
 * Versão (versão do projeto)
''')

autor = input('Qual seu nome completo?\n')
email = input('Qual seu endereço de e-mail?\n')
projeto = input('Qual o título de seu projeto?\n')
versao = input('Qual a versão de seu projeto?\n')

ano = date.today().year
editor = autor
liberacao = versao

arq_conf_sphinx = os.path.join('_modelos', 'conf.py')
arq_conf_git = os.path.join('_modelos', 'gitconfig.ini')
arq_conf_index = os.path.join('_modelos', 'index.rst')

modelo_sphinx = open(arq_conf_sphinx).read()
modelo_git = open(arq_conf_git).read()
modelo_index = open(arq_conf_index).read()

contexto = {
    'ano': ano,
    'autor': autor,
    'editor': editor,
    'liberacao': liberacao,
    'projeto': projeto,
    'versao': versao,
    }

conf_sphinx = open(os.path.join('fonte', 'conf.py'), 'w')
tmpl_sphinx = Template(modelo_sphinx)
conf_sphinx.write(tmpl_sphinx.substitute(**contexto))
# http://stackoverflow.com/questions/5952344/how-do-i-format-a-string-using-a-dictionary-in-python-3-x
conf_sphinx.close()

arq_git = os.path.join(os.path.expanduser('~'), '.gitconfig')
if not os.path.exists(arq_git):
    conf_git = open(arq_git, 'w')
    tmpl_git = Template(modelo_git)
    conf_git.write(tmpl_git.substitute(**contexto))
    conf_git.close()

conf_index = open(os.path.join('fonte', 'index.rst'), 'w')
tmpl_index = Template(modelo_index)
caracteres_nao_ascii = [caracter for caracter in projeto if not caracter in printable]
contexto['marcador_titulo'] = '='*(len(projeto)+len(caracteres_nao_ascii))
conf_index.write(tmpl_index.substitute(**contexto))
# http://stackoverflow.com/questions/5952344/how-do-i-format-a-string-using-a-dictionary-in-python-3-x
conf_index.close()


# Variáveis extraídas do arquivo de configuração de modelo
# Comando executado a partir do *vim*:
#   egrep -o '\{[a-z]+\}' fonte/conf.py | sort -u
#
# {ano}
# {autor}
# {editor}
# {liberacao
# {projeto}
# {versao}
