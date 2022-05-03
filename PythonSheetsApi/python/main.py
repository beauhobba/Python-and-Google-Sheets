import requests

if __name__ == "__main__":
    response = requests.get("https://script.google.com/macros/s/AKfycbzyUhavz3jcQKVw4WJhPpDxOcalrUeFTeINMO2NGou64oaxRCnEjnB_ZnChe643vZCkpA/exec", params="id=1") 
    print(response.json())
