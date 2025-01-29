import pyaes
import os

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"

try:
    # Abrir o arquivo criptografado
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Chave de criptografia (deve ser idêntica à usada na criptografia)
    key = b"testeransomware"  # 16 bytes
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypted_data = aes.decrypt(encrypted_data)

    # Salvar o arquivo descriptografado
    decrypted_file_name = encrypted_file_name.replace(".ransomwaretroll", "")
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Arquivo '{encrypted_file_name}' descriptografado com sucesso como '{decrypted_file_name}'.")

    # Remover o arquivo criptografado (opcional)
    os.remove(encrypted_file_name)
except FileNotFoundError:
    print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")
