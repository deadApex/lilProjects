class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False) -> None:
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        if self.comendo == False:
            self.comendo = True
            print(f'{self.nome} está comendo...\n')
        else:
            self.comendo = False
            print(f'{self.nome} já está comendo...')