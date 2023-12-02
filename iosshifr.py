import pyAesCrypt

password = input("Введите пароль от  программы")

#enrypt
pyAesCrypt.encryptFile("pass.txt", "dats.txt.aes", password)