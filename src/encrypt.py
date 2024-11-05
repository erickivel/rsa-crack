from sympy import isprime, mod_inverse


def generate_keys(p, q):
    # Calculate n
    n = p * q

    # Calculate phi(n)
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent e
    e = 65537  # Common choice for e in RSA

    # Ensure e and phi(n) are coprime
    if phi_n % e == 0:
        raise ValueError("e and phi(n) are not coprime. Choose different p and q.")

    # Calculate private key d
    d = mod_inverse(e, phi_n)

    return e, d, n


def encrypt_message(message, e, n):
    encrypted_bytes = bytearray()
    for byte in message:
        # Encrypt the byte using RSA: C = M^e mod n
        c = pow(byte, e, n)

        # Convert encrypted integer to bytes and extend to bytearray
        encrypted_bytes.extend(c.to_bytes((n.bit_length() + 7) // 8, byteorder="big"))

    return encrypted_bytes


def main():
    # Define prime numbers p and q (both should be prime)
    p = 53
    q = 59

    # Generate public and private keys
    e, d, n = generate_keys(p, q)
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d): {d}")

    # Input message
    message = input("Enter an ASCII message to encrypt: ")

    # Ensure message is ASCII
    try:
        message = message.encode("ascii")
    except UnicodeEncodeError:
        print("Message contains non-ASCII characters. Only ASCII is allowed.")
        return

    # Encrypt the message
    encrypted_bytes = encrypt_message(message, e, n)

    # Write encrypted bytes to a binary file
    with open("encrypted_message.bin", "wb") as file:
        file.write(encrypted_bytes)

    print("Message encrypted and saved to 'encrypted_message.bin'.")


if __name__ == "__main__":
    main()
