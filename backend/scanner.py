# backend/scanner.py

from scapy.all import ARP, Ether, srp
import socket
import ipaddress

def obtener_rango_ip_local() -> str:
    """
    Detecta automáticamente el rango de red local (ej. '192.168.1.0/24').
    """
    try:
        # Método robusto para obtener la IP local real
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()

        red = ipaddress.IPv4Network(ip_local + "/24", strict=False)
        return str(red)
    except Exception as e:
        print(f"[ERROR] No se pudo detectar la IP local: {e}")
        return "192.168.1.0/24"  # fallback seguro

def escanear_red(rango_ip: str = None) -> list[dict]:
    """
    Escanea la red usando ARP y devuelve lista de dispositivos {"ip", "mac"}.
    """
    if rango_ip is None:
        rango_ip = obtener_rango_ip_local()

    try:
        paquete = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rango_ip)
        resultado = srp(paquete, timeout=2, verbose=0)[0]

        dispositivos = []
        for _, recibido in resultado:
            dispositivos.append({
                "ip": recibido.psrc,
                "mac": recibido.hwsrc
            })

        return dispositivos
    except Exception as e:
        print(f"[ERROR] al escanear red: {e}")
        return []
