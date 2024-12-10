from sympy import mod_inverse


def generate_keys(p, q, e):
    """
    Gera as chaves pública e privada para o algoritmo RSA.

    @param p: Um número primo.
    @param q: Outro número primo.
    @return: Uma tupla contendo o expoente público `e`, a chave privada `d` e `n`.
    """
    n = p * q

    phi_n = (p - 1) * (q - 1)

    if phi_n % e == 0:
        raise ValueError(
            "e e phi(n) não são coprimos. Escolha valores diferentes para p e q."
        )

    d = mod_inverse(e, phi_n)

    return e, d, n


def encrypt_message(message, e, n):
    """
    Criptografa uma mensagem usando RSA.

    @param message: Mensagem em bytes a ser criptografada.
    @param e: Expoente público.
    @param n: Produto dos números primos `p` e `q`.
    @return: Um bytearray contendo os bytes criptografados.
    """
    encrypted_bytes = bytearray()
    for byte in message:
        # Criptografa o byte usando RSA: C = M^e mod n
        c = pow(byte, e, n)

        # Converte o inteiro criptografado para bytes e adiciona ao bytearray
        encrypted_bytes.extend(c.to_bytes((n.bit_length() + 7) // 8, byteorder="big"))

    return encrypted_bytes


def main():
    """
    Função principal que executa o fluxo do programa:
    1. Define os números primos p e q.
    2. Gera as chaves pública e privada.
    3. Solicita uma mensagem UTF-8 do usuário.
    4. Criptografa a mensagem.
    5. Salva os bytes criptografados em um arquivo binário.
    """
    # Define os números primos p e q (ambos devem ser primos)

    p = int(input("Digite o valor de p: "))
    q = int(input("Digite o valor de q: "))
    e = int(input("Digite o valor de e: "))

    e, d, n = generate_keys(p, q, e)
    print(f"Chave Pública (e, n): ({e}, {n})")
    print(f"Chave Privada (d, n): ({d}, {n})")

    message = input("Digite uma mensagem para criptografar: ")

    try:
        message = message.encode("utf-8")
    except UnicodeEncodeError:
        print(
            "A mensagem contém caracteres que não são UTF-8. Apenas caracteres UTF-8 são permitidos."
        )
        return

    encrypted_bytes = encrypt_message(message, e, n)

    with open("encrypted_message.bin", "wb") as file:
        file.write(encrypted_bytes)

    print("Mensagem criptografada e salva em 'encrypted_message.bin'.")


if __name__ == "__main__":
    main()
