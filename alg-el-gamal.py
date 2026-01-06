
# Geração de Chaves
def geracao_chaves(grupo, gerador):
    chave_privada = grupo
    chave_publica = gerador ** chave_privada
    return chave_privada, chave_publica

# Criptografia
def criptografar(mensagem, chave_publica, grupo, gerador):
    r = 18
    alfa = gerador ** r
    beta = mensagem * (chave_publica ** r)
    return alfa, beta

# Descriptografia
def descriptografar(cifra, chave_privada):  
    alfa, beta = cifra
    mensagem = beta / (alfa ** chave_privada)
    return mensagem

if __name__ == "__main__":

    grupo = 73
    gerador = 9

    # Geração de chaves
    chave_privada, chave_publica = geracao_chaves(grupo, gerador)
    print("Chave Privada:", chave_privada)
    print("\nChave Pública:", chave_publica)

    mensagem = 46

    # Criptografia
    cifra = criptografar(mensagem, chave_publica, grupo, gerador)
    print("\nMensagem Criptografada:", cifra)

    # Descriptografia
    mensagem_decifrada = descriptografar(cifra, chave_privada)
    print("\nMensagem Decifrada:", mensagem_decifrada)

    # Verificação
    assert mensagem == mensagem_decifrada, "A mensagem decifrada não corresponde à original!"