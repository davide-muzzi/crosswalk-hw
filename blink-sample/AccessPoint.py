from utime import sleep
import socket
import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="bowler", password="geheimespw123")

print("Access Point aktiv")
print("SSID:", ap.config("essid"))
print("IP-Adresse:", ap.ifconfig()[0])

# Create and bind socket to port 80
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
addr = ('0.0.0.0', 80)
s.bind(addr)
s.listen(5)
print("Listening on", addr)

value = 0;
while True:
    conn, client_addr = s.accept()
    print("Client connected from", client_addr)
    request = conn.recv(1024).decode()
    print("Request:", request)
    # Process the request to update LED status
    if "GET" in request:
            response_body = """<!DOCTYPE html>
                <html lang="de">
                <head>
                    <title>Traffic</title>
                </head>
                <body>
                    <h1>Light</h1>
                    <p>Value: """ + str(value) + """</p>
                </body>
                </html>
                            """
            value += 1

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + response_body
    conn.send(response.encode())
    conn.close()