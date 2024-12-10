import sys
import os

from decrypt import decrypt


def get_file_path():
    """
    Obtém o caminho absoluto do arquivo a partir dos argumentos da linha de comando.

    @return: O caminho absoluto do arquivo.
    """
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        absolute_file_path = os.path.abspath(input_file_path)
        return absolute_file_path
    else:
        print(
            "Nenhum caminho de arquivo fornecido. Uso: python3 main.py <caminho_do_arquivo>"
        )
        exit()


def main():
    """
    Função principal que executa o fluxo do programa:
    1. Obtém o caminho do arquivo.
    2. Solicita os valores de `e` e `n` do usuário.
    3. Descriptografa os dados do arquivo utilizando a função `decrypt`.
    4. Escreve os bytes descriptografados em um arquivo de saída.
    5. Converte os bytes para uma string UTF-8 e imprime a mensagem descriptografada.
    """
    file_path = get_file_path()
    e = int(input("Digite o valor de e: "))
    n = int(input("Digite o valor de n: "))

    decrypted_bytes = decrypt(file_path, e, n)

    with open("plain.txt", "wb") as file:
        file.write(decrypted_bytes)

    decrypted_message = decrypted_bytes.decode("utf-8", errors="ignore")
    print("Mensagem descriptografada:", decrypted_message)


main()
