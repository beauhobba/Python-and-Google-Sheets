
from sheets import GoogleSheet


def main():
    sheet = GoogleSheet()
    sheet.sendData("beau", "Hobba", "hobbabeau@gmail.com", "04x1x1x1")
    


if __name__ == "__main__":
    main()