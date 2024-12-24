import json

with open("proxies.txt", "r") as file:
    data = json.load(file)

proxies = data.get("proxies", [])
formatted_proxies = []

for proxy in proxies:
    if proxy.get("alive", False):
        protocol = proxy.get("protocol", "http")
        ip = proxy.get("ip", "unknown")
        port = proxy.get("port", "unknown")
        formatted_proxies.append(f"{protocol}://{ip}:{port}")

with open("proxies_cleaned.txt", "w") as f:
    f.write("\n".join(formatted_proxies))

print("Proxies guardados en 'proxies.txt'")
