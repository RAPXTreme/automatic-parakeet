import requests

data = {
        "comments": "",
        "custemail": "rapxtreme@mail.ru",
        "custname": "Юсупов Тимур",
        "custtel": "8903264832",
        "delivery": "",
        "size": "medium",
        "topping": "cheese"
}
url = 'https://httpbin.org/post'

print(requests.post(url, data=data))