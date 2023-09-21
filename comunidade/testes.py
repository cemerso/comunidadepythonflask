from comunidade import app, database
from comunidade.models import Post, Usuario
from flask_bcrypt import Bcrypt

#Criar o banco de dados, esse codigo abaixo será executado somente uma vez
# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Tom', email='tom@gmail.com', senha='123456')
#     database.session.add(usuario)
#     database.session.commit()
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     segundo_user = Usuario.query.filter_by(email='tomnovo@gmail.com').first()
#     print(segundo_user.senha)
#
#     #Como fazer para testar a senha:
#     bcrypt = Bcrypt()
#     senha = '123456'
#     senha_cript = bcrypt.generate_password_hash(senha)
#     print(bcrypt.check_password_hash(senha_cript, senha))
#     usuario_teste = Usuario.query.filter_by(email='tom@gmail.com').first()
#     print(usuario_teste.username)
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro post do Emerson', corpo='Esse site está ficando legal')
#     database.session.add(meu_post)
#     database.session.commit()
# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)
#     print(post.corpo)
#Limpar o banco de dados
# with app.app_context():
#     database.drop_all() #limpar
#     database.create_all() #Criar
def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
        print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return

    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []

while True:
    print('Lista de Tarefas: Listar, desfazer ou refazer')
    tarefa = input('Digite uma Tarefa ou Comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue

