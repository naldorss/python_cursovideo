# Declaração de classe
class Gafanhoto: 
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Método de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    # Declaração de objetos

g1 = Gafanhoto() # Criando um objeto da classe Gafanhoto
g1.nome = "João"
g1.idade = 20
print(g1.mensagem())