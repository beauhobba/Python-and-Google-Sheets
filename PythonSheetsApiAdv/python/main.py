import requests

link = 'https://script.google.com/macros/s/AKfycbzMGIai3fC6ZDyHeviTVuJVpRgtgpEdgrO7C1GBBbjrsNTZ8lrHjCMbkMw6A_gv_OgKgQ/exec'

def print_response(requests_link, params):
    response = requests.get(requests_link, params=params).json()
    print(response)
    


if __name__ == "__main__":
    print_response(link, {'task': "getFirstName", 'id': '1'})
    print_response(link, {'task': "getNames"})
    print_response(link, {'task': "getNamesfirst"})
    
    print_response(link, {'task': "getNames", 'filter': 'Be'})

