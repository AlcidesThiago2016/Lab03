# -*- coding: utf-8 -*-

# Import
import random

# Board (Tabuleiro)
board = ['''

>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
0   |
    |
    |
    |
=========''', '''

+---+
|   |
0   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 0   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Metodo Construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Metodo para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Metodo para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Metodo para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Metodo para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Metodo para checar o status do game e imprimir na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras Erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras Corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# Função para ler uma palavra de forma aleatória do banco palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminando, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuario
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame Over! Você Perdeu.')
        print('A Palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
