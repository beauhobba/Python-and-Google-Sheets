import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet():
    def __init__(self):
        scope = ['https://www.googleapis.com/auth/drive']
        
        creds = ServiceAccountCredentials.from_json_keyfile_name('token.json', scope)
        client = gspread.authorize(creds)
        
        # The name of your Spreadsheet
        sheet = client.open('Test Spreadsheet')
        
        # The name of your sheets
        self.contacts = sheet.worksheet('Contacts')
        self.contacts2 = sheet.worksheet('Contacts2')
        
    def getRowLength(self):
        # gets the length of all values within a column 
        return len(self.contacts.get_all_values())
    
    def sendData(self, first, last, email, phone):
        # sends the data to the spreadsheet
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
        
        # inserts the data (py arrays -> spreadsheet rows)
        self.contacts.insert_row(contacts, id_num+1)
        self.contacts2.insert_row(contacts2, id_num+1)