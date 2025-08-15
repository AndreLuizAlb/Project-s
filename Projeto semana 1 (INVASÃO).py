import random

import time

# Configurações iniciais

estacas_disponiveis = 2

lenhador = 4

minerador = 10

ferreiro = 10

plantacoes = 7  # nova variável para contar plantações


print("Início do dia... - projeto semana 1 (parte 2):18")

time.sleep(1)

investidas = random.randint(2, 3)


for i in range(investidas):

    print(f"\nInvestida {i+1} - projeto semana 1 (parte 2):27")


    goblins = random.randint(2, 5)

    print(f"{goblins} goblins estão atacando! - projeto semana 1 (parte 2):32")

    time.sleep(1)

    for j in range(goblins):

        print(f"\nGoblin #{j+1} está tentando atravessar! - projeto semana 1 (parte 2):38")

        time.sleep(1)

        if estacas_disponiveis > 0:

            chance = random.randint(1, 100)

            if chance >= 31:

                print(f"Estaca bloqueou o goblin! (porcentagem = {chance}) - projeto semana 1 (parte 2):48")

            else:

                estacas_disponiveis -= 1

                print(f"Estaca destruída! Goblin conseguiu passar! (porcentagem = {chance}) - projeto semana 1 (parte 2):54")

                time.sleep(1)

                escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()

                if escolha == "s":

                    print("Você enfrentou o goblin! - projeto semana 1 (parte 2):62")

                else:

                    print("Goblin atacou os moradores! - projeto semana 1 (parte 2):66")

                    queima = random.randint(1, 100)

                    if queima <= 5:

                        print("VOCÊ PERDEU UMA PLANTAÇÃO! - projeto semana 1 (parte 2):72")

                        plantacoes -= 1

                    else:

                        print("1 dano causado aos moradores. - projeto semana 1 (parte 2):78")

                        lenhador -= 1

                        minerador -= 1

                        ferreiro -= 1

        else:

            print(f"Sem estacas! Goblin passou direto! (porcentagem = {chance}) - projeto semana 1 (parte 2):88")

            escolha = input("Você quer enfrentar o goblin? (s/n): ").strip().lower()

            if escolha == "s":

                print("Você enfrentou o goblin! - projeto semana 1 (parte 2):94")

            else:

                print("Goblin atacou os moradores! - projeto semana 1 (parte 2):98")

                queima = random.randint(1, 100)

                if queima <= 5:

                    print("VOCÊ PERDEU UMA PLANTAÇÃO! - projeto semana 1 (parte 2):104")

                    plantacoes -= 1

                else:

                    lenhador - 1

                    minerador - 1

                    ferreiro - 1

                    print("1 dano causado aos moradores. - projeto semana 1 (parte 2):116")


# Fim do dia

print(f"\nFim do dia. - projeto semana 1 (parte 2):121")

print(f"Estacas restantes: {estacas_disponiveis} - projeto semana 1 (parte 2):123")

print(f"Vida do lenhador {lenhador} - projeto semana 1 (parte 2):125")

print(f"vida do minerador {minerador} - projeto semana 1 (parte 2):127")

print(f"vida do ferreiro {ferreiro} - projeto semana 1 (parte 2):129")

print(f"Plantações restantes: {plantacoes} - projeto semana 1 (parte 2):131")
