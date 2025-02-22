print("***************")
print("Bem vindo ao Jogo de Adivinhação!")
print("***************")

numero_secret0 = 42

chute_str = input("Digite o seu número:")
print("Voçê digitou:", chute_str)
chute = int (chute_str)

if( numero_sereto == chute):
    print("Você acertou!")
    else:
        print("Você errou!")
        print("Fim de jogo")