import requests

link = 'https://script.google.com/macros/s/AKfycbySVUHWo1FKAGh-LVwgr_H80YdcStCGqr1qFzwld7qk8yeiJQ_GJE2Mm8ehRW0ErOUpwQ/exec'

def print_response(requests_link, params):
    response = requests.get(requests_link, params=params).json()
    print(response)
    

def send_response(requests_link, params):
    response = requests.post(requests_link, params=params).text
    print(response)
    


if __name__ == "__main__":
    send_response(link, {'id':'10', 'first':'ppp', 'last':'tttt','phone':'xxx','email':'hobbabeau@gmail.com'})

    
    print_response(link, {'task': "getNames", 'filter': 'pp'})
    
    
    
    


