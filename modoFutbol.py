import requests

# Ponemos los identificadores de Telegram
claves = {}
with open("tokens.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea and "=" in linea:
            key, value = linea.split("=", 1)
            claves[key.strip()] = value.strip()

# Asignar variables a partir del diccionario
API_TOKEN = str(claves.get("API_TOKEN", 0))
ZONE_ID = claves.get("ZONE_ID", "")

# Lista de nombres de registros que NO quieres modificar
EXCLUIR = [
    "minecraft.robotcgb.org",
    "ssh.robotcgb.org",
    "wire.robotcgb.org"
]

# Cabeceras
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Obtener lista de registros DNS
url_dns = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
response = requests.get(url_dns, headers=headers)
data = response.json()

if not data["success"]:
    print("Error al obtener registros DNS:", data)
    exit()

# Cambiar proxy a "DNS only" salvo los excluidos
for record in data["result"]:
    nombre = record["name"]
    
    if nombre in EXCLUIR:
        print(f"⏭ Registro {nombre} excluido, no se modifica.")
        continue

    if record["proxied"]:  # Solo modificar si está con proxy
        dns_id = record["id"]
        update_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{dns_id}"
        payload = {
            "type": record["type"],
            "name": record["name"],
            "content": record["content"],
            "ttl": record["ttl"],
            "proxied": False
        }
        update_response = requests.put(update_url, headers=headers, json=payload)
        update_data = update_response.json()
        if update_data["success"]:
            print(f"Registro {nombre} actualizado a DNS only")
        else:
            print(f"Error al actualizar {nombre}: {update_data}")
