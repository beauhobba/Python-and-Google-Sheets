import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet():
    def __init__(self):
        scope = ['https://www.googleapis.com/auth/drive']
        
        creds = ServiceAccountCredentials.from_json_keyfile_name('token.json', scope)
        client = gspread.authorize(creds)
        
        sheet = client.open('Test Spreadsheet')
        self.contacts = sheet.worksheet('Contacts')
        self.contacts2 = sheet.worksheet('Contacts2')
        
    def getRowLength(self):
        return len(self.contacts.get_all_values())
    
    def sendData(self, first, last, email, phone):
        contacts = []
        contacts2 = []
        
        id_num = self.getRowLength()
        
        contacts.append(id_num)
        contacts.append(first)
        contacts.append(last)
        contacts.append(email)
        
        contacts2.append(id_num)
        contacts2.append(first)
        contacts2.append(last)
        contacts2.append(phone)
        
        self.contacts.insert_row(contacts, id_num+1)
        self.contacts2.insert_row(contacts2, id_num+1)