nomePasta = 'C:/Users/lucas/Desktop/Python/Capitulo 13/dados/'
nomeArquivo = 'dicionario'

# criando a pasta que o arquivo de banco de dados será salvo
import os
os.makedirs(nomePasta,exist_ok=True)

# criando o arquivo de banco de dados
import shelve
db = shelve.open(f'{nomePasta}{nomeArquivo}','c',writeback=True)

# realizar o cadastro do dicionar caso nao exista
if 'alunos' not in db:
    db['alunos']  = {}

# funcao que cadastra aluno
def cadastrarAluno():
    os.system('cls')
    nome = input('Informe o nome do aluno: ')
    curso = input('Informe o nome do curso: ')

    # retorna a ultima matricula cadastrada e soma 1
    if db['alunos']:
        matricula = max(db['alunos']) + 1
    else:
        matricula =  1
    
    db['alunos'][matricula] = {'nome':nome, 'curso':curso}
    db.sync() # sincroniza com o banco salvando a linha
    print('Aluno cadastrado com sucesso.')
    os.system('pause')

def mostrarDados():
    os.system('cls')
    print('Matricula, Nome, Curso')
    print('-----------------------')

    for i in db['alunos']:
        nome = db['alunos'][i]['nome']
        curso = db['alunos'][i]['curso']
        print(f'{i}, {nome}, {curso}')
    
    os.system('pause')


def menu():
    while True:
        os.system('cls')
        print('\n\n--- Menu Principal ---')
        print('1. Cadastrar Aluno')
        print('2. Mostrar Dados')
        print('3. Sair')
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            cadastrarAluno()
        elif opcao == '2':
            mostrarDados()
        elif opcao == '3':
            db.close()
            break
        else:
            print('Opção invalida.')
            os.system('pause')


if __name__ == "__main__":
    menu()