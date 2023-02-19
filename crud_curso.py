import mysql.connector
import locale
from base import sql
from flask import Flask, render_template, request
app = Flask(__name__)

# URL: localhost:5000
@app.route('/')
def menu():
  return render_template('menu.html')

# URL: localhost:5000/formincluir
@app.route('/formincluir')
def formIncluir():
  return render_template('formIncluir.html')

@app.route('/incluir', methods=['POST'])
def incluir():
  # Recuperando dados do formulário de formIncluir()
  sigla    = request.form['sigla']
  nome     = request.form['nome']
  data     = request.form['Data de abertura']
  numero   = request.form['Numero total de Créditos']
  ementa   = request.form['Ementa']

  # Incluindo dados no SGBD
  mysql = sql.SQL("root", "root", "test")
  comando = "INSERT INTO tb_curso(sigla_curso, nme_curso, data_abertura,numero_total_creditos, ementa) VALUES (%s, %s, %s, %s, %s);"
  if mysql.executar(comando, [sigla,nome, data,numero ,ementa ]):
      msg=" O curso " + nome + " cadastrado com sucesso!"
  else:
      msg="Falha na inclusão do curso."

  return render_template('incluir.html', msg=msg)
