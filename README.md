# Guia de Uso: Criptografia e Descriptografia com RSA

Este repositório contém dois programas Python que implementam as funções de criptografia e descriptografia usando o algoritmo RSA. O guia abaixo explica como utilizar os códigos para criptografar e descriptografar mensagens.

## Requisitos

Antes de executar os códigos, assegure-se de que o seguinte está instalado:

- Python 3.7 ou superior.
- Biblioteca `sympy` (pode ser instalada com `pip install sympy`).

## Estrutura do Repositório

Os arquivos principais são:

- **encrypt.py**: Contém as funções para gerar chaves e criptografar mensagens.
- **decrypt.py**: Contém as funções para descriptografar mensagens.
- **main.py**: Contém a função main que lê o arquivo criptografado e o descriptografa.

---

## Como Criptografar uma Mensagem

### Passo 1: Execute o script de criptografia

Para criptografar uma mensagem, execute o arquivo `encrypt.py`. Ele gera chaves RSA e criptografa uma mensagem fornecida pelo usuário.

```bash
python encrypt.py
```

### Passo 2: Insira uma mensagem UTF-8

O programa solicitará o valor de `p`, `q`, `e` e uma mensagem UTF-8 para criptografar. Digite a mensagem desejada e pressione Enter.

### Resultado

- Uma chave pública (`e`, `n`) e uma chave privada (`d`, `n`) serão geradas e exibidas no terminal.
- A mensagem será criptografada e salva no arquivo `encrypted_message.bin`.

Exemplo de saída:

```
Digite o valor de p: 61 
Digite o valor de q: 67
Digite o valor de e: 17
Chave Pública (e, n): (17, 4087)
Chave Privada (d, n): (233, 4087)
Digite uma mensagem para criptografar: Olá, Mundo!
Mensagem criptografada e salva em 'encrypted_message.bin'.
```

---

## Como Descriptografar uma Mensagem

### Passo 1: Certifique-se de que o arquivo criptografado existe

Assegure-se de que o arquivo `encrypted_message.bin` gerado na etapa de criptografia está no mesmo diretório do script de descriptografia (na raiz do projeto).

### Passo 2: Execute o script de descriptografia

Para descriptografar a mensagem, execute o arquivo `main.py`.

```bash
python main.py <caminho_para_arquivo_criptografado>
```

Substitua `<caminho_para_arquivo_criptografado>` pelo caminho do arquivo `encrypted_message.bin`. O programa também solicitará os valores de `e` e `n` usados na criptografia.

### Passo 3: Insira os valores de `e` e `n`

Insira os valores de `e` e `n` exibidos durante o processo de criptografia.

### Resultado

- A mensagem descriptografada será exibida no terminal.
- Os bytes descriptografados serão salvos no arquivo `plain.txt`.

Exemplo de saída:

```
Digite o valor de e: 65537
Digite o valor de n: 3127
Mensagem descriptografada: Olá, Mundo!
```

---

## Observações Importantes

- **Apenas caracteres UTF-8**: A mensagem de entrada deve conter apenas caracteres UTF-8.
- **Erros comuns**: Certifique-se de fornecer os valores corretos de `e` e `n` durante a descriptografia para evitar erros.
