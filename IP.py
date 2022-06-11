import socket

def ip():
    host = input("Введите адресс сайта")
    try:
        return f"Host: {host}\n IP:{socket.gethostbyname(host)}"
    except socket.gaierror as error:
        return f"Не корректные данные:{error}"
def main():
    print(ip())

if __name__ == '__main__':
    main()