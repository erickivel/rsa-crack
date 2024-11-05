import sys
import os
from sympy import isprime, mod_inverse


def get_factors(n):
    for i in range(2, 1024):
        if isprime(i) and n % i == 0:
            q = n // i
            if isprime(q):
                return i, q
    return None, None


def get_private_key(e, n):
    p, q = get_factors(n)
    if p is None or q is None:
        print("It was not possible to factor n.")
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


def decrypt(file_path, d, n):
    try:
        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            byte_data = file.read()
            print("byte_data", byte_data)
    except IOError:
        print(f"Não foi possível abrir o arquivo '{file_path}'")
        exit()

    # Split byte_data into 2-byte chunks
    ciphertexts = [
        int.from_bytes(byte_data[i : i + 2], byteorder="big")
        for i in range(0, len(byte_data), 2)
    ]
    print("ciphertexts", ciphertexts)

    # Decrypt each integer
    plaintext_values = [pow(c, d, n) for c in ciphertexts]
    print("plaintext_values", plaintext_values)

    # Convert decrypted values back to bytes
    decrypted_bytes = bytearray(plaintext_values)

    print(decrypted_bytes)

    return decrypted_bytes


def get_file_path():
    """Gets the absolute file path from command-line arguments."""
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        absolute_file_path = os.path.abspath(input_file_path)
        return absolute_file_path
    else:
        print("No file path provided. Usage: python3 main.py <file_path>")
        exit()


def main():
    file_path = get_file_path()
    e = int(input("Digite o valor de e: "))
    n = int(input("Digite o valor de n: "))

    d = get_private_key(e, n)
    print("Chave privada: ", d)

    decrypted_bytes = decrypt(file_path, d, n)

    print("Decrypted bytes:", decrypted_bytes)

    with open("out.txt", "wb") as file:
        file.write(decrypted_bytes)

    # Convert to ASCII string and print
    decrypted_message = decrypted_bytes.decode(
        "utf-8", errors="ignore"
    )  # Ignore errors for invalid bytes
    print("Decrypted message:", decrypted_message)


main()
