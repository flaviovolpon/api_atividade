from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Volpon', idade=40)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Flávio').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flávio').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Volpon').first()
    pessoa.delete()

def consulta():
    pessoas = Pessoas.query.all()
    for i in pessoas:
        print(i.id)
        print(i.nome)
        print(i.idade)

    pessoa = Pessoas.query.filter_by(nome='Flávio').first()

    print(pessoa.nome)

if __name__ == '__main__':
    # insere_pessoas()
    altera_pessoa()
    consulta()