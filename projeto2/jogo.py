#Personagem 
#Heroi
#Inimigo
import random

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        #Dano por nivel            nivel * 2           nivel * 4          
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        #Super = Referencia o metodo que vai ser utilizado da classe PAI(Principal), no caso, PERSONAGEM
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() *8)#Dano aumentado
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} usou a Habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
        

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"


class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Flash", vida=100, nivel=5, habilidade="Volta ao mundo")
        self.inimigo = Inimigo(nome="Savitar", vida=100, nivel=5, tipo="Velocista")
        
    def iniciar_batalha(self):
        """Fazer gestão da batalha em turno"""
        print("Iniciando Batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("\nPressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida, escolha novamente!")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê perdeu a batalha!")

            

#Instancia do jogo e inciar batalha
jogo = Jogo()
jogo.iniciar_batalha()         

