import io
import sys
import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from vars import hostname, serverPort, miCanal, client_id, secret

hostName = hostname()
serverPort = serverPort()
miCanal = miCanal()
client_id = client_id()
secret = secret()
token = ""
user_id = ""
listado = ""



class MyServer(BaseHTTPRequestHandler):
    def do_GET(self): #OBTENGO EL TOKEN
        url = "https://id.twitch.tv/oauth2/token"
        payload = dict(client_id=client_id, client_secret=secret, grant_type='client_credentials', scope='user_follows_edit')
        res = requests.post(url, data=payload)

        token = json.loads(res.text)['access_token']

        #BUSCO EL USUARIO
        url = "https://api.twitch.tv/helix/search/channels?query="+miCanal
        headers = {
            'Authorization': 'Bearer '+token,
            'Client-Id': client_id
        }

        response = requests.request("GET", url, headers=headers)

        for canal in json.loads(response.text.encode('utf8'))['data']:
            if canal['broadcaster_login'] == miCanal:
                user_id = canal['id']


        #BUSCO LOS FOLLOWERS
        url = "https://api.twitch.tv/helix/users/follows?to_id="+ user_id + "&first=100"
        headers = {  
            'Authorization': 'Bearer '+token,
            'Client-Id': client_id
        }

        response = requests.request("GET", url, headers=headers)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html lang=\"es\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Minerva</title></head>", "utf-8"))
        self.wfile.write(bytes("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC\" crossorigin=\"anonymous\">", "utf-8"))
        self.wfile.write(bytes("<body><div class=\"container\"><div class=\"list-group\">", "utf-8"))     
        for follower in json.loads(response.text)['data']:
            self.wfile.write(bytes("<a href=\"#\" class=\"list-group-item list-group-item-action\" aria-current=\"true\"><div class=\"d-flex w-100 justify-content-between\"><h5 class=\"mb-1\">"+follower['from_name']+"</h5><small>3 days ago</small></div><p class=\"mb-1\">Some placeholder content in a paragraph.</p><small>And some small print.</small></a><br>", "utf-8"))
        self.wfile.write(bytes("</div></div></body>", "utf-8"))
        self.wfile.write(bytes("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM\" crossorigin=\"anonymous\"></script>", "utf-8"))
        self.wfile.write(bytes("</html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")