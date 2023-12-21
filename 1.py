import requests

link = 'https://ftis-conf.mephi.ru/content/public/uploads/files/trebovaniya_doklad_0.pdf'


def save(link):
    r = requests.get(link, allow_redirects=True)
    open("Tayna.pdf", "wb").write(r.content)


save(link)
