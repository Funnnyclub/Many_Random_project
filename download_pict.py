import requests
respose = requests.get("https://cs13.pikabu.ru/post_img/2023/03/30/11/168020128218477952.webp")
with open(file='pikabu.webp', mode = "wb") as file:
    file.write(respose.content)