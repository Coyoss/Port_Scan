import socket

def scan_ports(host, ports):
    print(f"🔍 Escaneando {host}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)  
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"✅ Porta {port} aberta")
            else:
                print(f"❌ Porta {port} fechada")
        except Exception as e:
            print(f"Erro na porta {port}: {e}")
        finally:
            sock.close()

host = "127.0.0.1"  #IP que sera verificado
ports = range(80, 246)  # Aqui e colocado as portas que deseja verificar
scan_ports(host, ports) #Teste em acao
