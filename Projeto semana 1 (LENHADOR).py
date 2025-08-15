import random

vida = 10
arvores = 0

for hora in range(3): # 3 horas
    print(f"\nHora {hora+1}: O lenhador cortou uma árvore. - projeto semana 1 (LENHADOR):7")
    print("O goblin apareceu! - projeto semana 1 (LENHADOR):8")
    acao = input("Você escolheu que o lenhador iria correr ou lutar? ").lower()

    if acao == "correr":
        if random.random() < 0.5:
            print("O lenhador correu, mas não conseguiu levar a árvore! - projeto semana 1 (LENHADOR):13")
        else:
            arvores += 1
            print("O lenhador correu e conseguiu levar a arvore. - projeto semana 1 (LENHADOR):16")
    elif acao == "lutar":
        vida -= 2
        arvores += 1
        print("O lenhador lutou e levou 2 de dano. Vida restante: - projeto semana 1 (LENHADOR):20", vida)
    else:
        vida = 0
        print("Ação inválida! ele fica parado e o goblin o ataca, tirando toda a vida dele, resultando em morte imediata!! - projeto semana 1 (LENHADOR):23")
        print("O Lenhador morreu! - projeto semana 1 (LENHADOR):24")
        break

    if vida <= 0:
        print("O Lenhador morreu! - projeto semana 1 (LENHADOR):28")
        break

# Calculo das estacas
estacas = 0
for i in range(arvores):
    estacas += random.randint(5, 7)

print(f"\nFim do dia. Árvores coletadas: {arvores}, Vida restante: {vida} - projeto semana 1 (LENHADOR):36")
print(f"Você conseguiu {estacas} estacas no total. - projeto semana 1 (LENHADOR):37")
