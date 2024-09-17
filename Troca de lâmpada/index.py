def verificar_lampada():
    while True:
        estado = input("A lâmpada está queimada? (sim/não): ").lower()
        if estado in ["sim", "não"]:
            return estado == "sim"
        else:
            print("Entrada inválida. Por favor, responda com 'sim' ou 'não'.")

def desligar_energia():
    print("Desligando o interruptor para evitar choques elétricos...")

def obter_lampada_nova():
    print("Pegando uma lâmpada nova e compatível com o soquete...")

def esperar_esfriar():
    print("Esperando a lâmpada antiga esfriar...")

def remover_lampada_antiga():
    print("Removendo a lâmpada queimada do soquete...")

def instalar_lampada_nova():
    print("Instalando a nova lâmpada no soquete...")

def ligar_energia():
    print("Ligando o interruptor...")

def testar_lampada():
    while True:
        funcionamento = input("A nova lâmpada está funcionando? (sim/não): ").lower()
        if funcionamento in ["sim", "não"]:
            if funcionamento == "sim":
                print("Lâmpada trocada com sucesso!")
            else:
                print("Pode haver um problema com a nova lâmpada ou a instalação.")
            break
        else:
            print("Entrada inválida. Por favor, responda com 'sim' ou 'não'.")

def trocar_lampada():
    if verificar_lampada():
        desligar_energia()
        obter_lampada_nova()
        esperar_esfriar()
        remover_lampada_antiga()
        instalar_lampada_nova()
        ligar_energia()
        testar_lampada()
    else:
        print("A lâmpada está funcionando normalmente, não é necessário trocar.")

# Executar o código
trocar_lampada()
