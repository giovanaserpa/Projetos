#Jogo da Velha em python

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))


def verificar_vitoria(tabuleiro, jogador):
# Verifica linhas
    for i in range(3):
       if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
           return True
# Verifica colunas
    for i in range(3):
       if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
           return True
       
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
              return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
              return True
    return False


tabuleiro = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]
jogador_atual = "X"

for _ in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")
    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos % 3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já ocupada. Tente novamente.")
        continue
    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual} venceu!")
        break

    if jogador_atual == "O":
        jogador_atual = "X"
    else:
        jogador_atual = "O"