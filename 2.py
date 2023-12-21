import socket
from urllib.parse import urlparse

domen = urlparse('https://vk.com/@haccking1-poluchenie-informacii-o-domene-s-pomoschu-python-chast-1').netloc


def get_ip(d):
    return f"IP - {socket.gethostbyname(d)}"


print(f"Domen - {domen}")
print(get_ip(domen))
