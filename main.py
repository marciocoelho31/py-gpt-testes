from gerador_casos_uso import *
from gerador_cenarios_teste import *
from gerador_script_teste import *
from tools import *

def main():
    pedido_usuario = input("Digite um caso de uso: ")

    caso_uso = gerar_caso_uso(pedido_usuario, MODELO_GPT_3_5)
    print("\nCaso de Uso NAO REFINADO:\n", caso_uso)

    caso_uso = gerar_caso_uso(pedido_usuario, MODELO_REFINADO)
    print("\nCaso de Uso REFINADO:\n", caso_uso)

    # cenario_teste = gerar_cenario_teste(caso_uso)
    # print("\nCenário de teste:\n", cenario_teste)

    # script_teste = gerar_script_teste(caso_uso, cenario_teste)
    # print("\nScript de teste:\n", script_teste)

    # salva("script_temp_ia.py", script_teste)

if __name__ == "__main__":
    main()