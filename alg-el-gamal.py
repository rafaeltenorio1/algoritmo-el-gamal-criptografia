# Geração de Chaves
def geracao_chaves(grupo, gerador, sk):

    # Definindo a chave privada escolhida pelo usuário e realizando o modulo do grupo no final
    chave_privada = sk % grupo

    # Definindo a chave publica baseada na chave privada e realizando o modulo do grupo no final
    chave_publica = (gerador ** chave_privada) % grupo

    return chave_privada, chave_publica

# Criptografia
def criptografar(mensagem, chave_publica, grupo, gerador, r):
    # Definindo o alpha baseado no gerador e no r, realizando o modulo do grupo no final
    alpha = (gerador ** r) % grupo

    # Definindo o beta baseado na mensagem, chave publica e r, realizando o modulo do grupo no final
    beta = (mensagem * (chave_publica ** r)) % grupo

    return alpha, beta

# Descriptografia
def descriptografar(cifra, chave_privada):  

    alpha, beta = cifra

    s = (alpha ** chave_privada) % grupo
    
    # Calcular a inversa multiplicativa de s
    s_inverso = pow(s, -1, grupo)
    
    # Recuperar a mensagem original
    mensagem = (beta * s_inverso) % grupo
    
    return mensagem

if __name__ == "__main__":

    grupo = 73
    gerador = 2
    sk = 7 

    mensagem = 64
    r = 17

    # Geração de chaves
    chave_privada, chave_publica = geracao_chaves(grupo, gerador, sk)
    print("Chave Privada:", chave_privada)
    print("\nChave Pública:", chave_publica)

    # Criptografia
    cifra = criptografar(mensagem, chave_publica, grupo, gerador, r)
    print("\nMensagem Criptografada:", cifra)

    # Descriptografia
    mensagem_decifrada = descriptografar(cifra, chave_privada)
    print("\nMensagem Decifrada:", mensagem_decifrada)