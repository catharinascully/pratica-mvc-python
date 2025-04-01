from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.salvarTarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefas()
    return render_template("index.html", tarefas = tarefas, title='Minhas Tarefas')

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect(url_for('index'))

@app.route('/update/<int:idTarefa>', methods = ['GET', 'POST'])
def editar(idTarefa):
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(id = idTarefa, titulo = titulo, data_conclusao = data_conclusao)
        tarefa.atualizar_tarefa()
        return redirect(url_for('index'))

    tarefa_selecionada = Tarefa.buscar_tarefa(idTarefa)
    return render_template(
        'index.html',
        tarefa_selecionada = tarefa_selecionada,
        title = 'Editando tarefa | Minhas tarefas'
    )