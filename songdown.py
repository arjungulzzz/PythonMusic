import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://dl2.faz2dl.in/mr-reese/single/june/Twenty%20One%20Pilots%20-%20Heathens%20-%20MP3%20320.mp3', preload_content=False)

with open('C:\\Users\\Arjun\\Downloads\\1.mp3', 'wb') as out:
    while True:
        data = r.read(chunk_size)
        if not data:
            break
        out.write(data)

r.release_conn()


import urllib.request
>>> urllib.request.urlretrieve('http://dl2.faz2dl.in/mr-reese/single/june/Twenty%20One%20Pilots%20-%20Heathens%20-%20MP3%20320.mp3','2.mp3')
