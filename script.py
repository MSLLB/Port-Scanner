import socket


target=input("***Enter an ip address*** -->")
def portattack(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Crée un nouveau socket pour envoyer des requêtes.
        """
        socket.AF_INET → Utilise IPv4 (si c'était AF_INET6, ce serait IPv6).
        socket.SOCK_STREAM → Utilise le protocole TCP (connexion stable)."""
        
        sock.connect((target,port))#sock.connect() attend un tuple (IP, PORT)
        sock.close()  # Ferme la connexion après le test
        return True
    

    except:
        return False
    

print(f"\n🔍 Scanning {target}...\n")
for port in [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389]:#liste des port les plus utilisés
    res=portattack(port)
    if res:
        print("port{} is open".format(port))
    else:
        print("port {} is close".format(port))    
