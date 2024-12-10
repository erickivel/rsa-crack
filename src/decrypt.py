from sympy import isprime, mod_inverse


def get_factors(n):
    """
    Obtém os fatores primos `p` e `q` de um número `n`.

    @param n: Número inteiro a ser fatorado.
    @return: Uma tupla contendo os fatores primos `p` e `q`, ou `(None, None)` se não for possível fatorar.
    """
    for i in range(2, 1024):
        if isprime(i) and n % i == 0:
            q = n // i
            if isprime(q):
                return i, q
    return None, None


def get_private_key(e, n):
    """
    Calcula a chave privada `d` utilizando os valores de `e` e `n`.

    @param e: Expoente público.
    @param n: Produto dos dois números primos `p` e `q`.
    @return: A chave privada `d`.
    """
    p, q = get_factors(n)
    if p is None or q is None:
        print("Não foi possível fatorar n.")
        exit()

    phi_n = (p - 1) * (q - 1)

    try:
        d = mod_inverse(e, phi_n)
    except ValueError:
        print(
            "Inverso modular não existe. Certifique-se de que 'e' é coprimo com phi(n)."
        )
        exit()
    return d


def decrypt(file_path, e, n):
    """
    Descriptografa os dados de um arquivo utilizando os valores de `e` e `n`.

    @param file_path: Caminho do arquivo a ser descriptografado.
    @param e: Expoente público.
    @param n: Produto dos dois números primos `p` e `q`.
    @return: Bytes descriptografados.
    """
    d = get_private_key(e, n)
    print("Chave privada: ", d)

    try:
        with open(file_path, "rb") as file:
            byte_data = file.read()
    except IOError:
        print(f"Não foi possível abrir o arquivo '{file_path}'")
        exit()

    # Divide os dados em bytes em blocos de 2 bytes
    ciphertexts = []
    for i in range(0, len(byte_data), 2):
        ciphertext = int.from_bytes(byte_data[i : i + 2], byteorder="big")
        ciphertexts.append(ciphertext)

    # Descriptografa cada inteiro
    plaintext_values = [pow(c, d, n) for c in ciphertexts]

    decrypted_bytes = bytearray(plaintext_values)

    return decrypted_bytes
