import sipfullproxy as sip
import socket
import socketserver
import sys
import time as t
import logging 

if __name__ == "__main__":   

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info("SERVER ON -> " + t.strftime("%a, %d %b %Y %H:%M:%S ", t.localtime()))
    hostname = socket.gethostname()
    logging.info("SERVER HOSTNAME -> " + hostname)
    ipaddress = socket.gethostbyname(hostname)

    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)

    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sip.PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sip.PORT)
    
    server = socketserver.UDPServer((sip.HOST, sip.PORT), sip.UDPHandler)

    server.serve_forever()