import parser
import re

def main():
    read = open("emails.txt", "r")
    text = read.read()
    read.close()

    email = re.findall(r'[\w\"\'\.\@]*[\w\"\'\.]+@[\w\.]+\.[\w\.]+[\w]+', text)

    print(email)

if __name__ == "__main__":
    main()

