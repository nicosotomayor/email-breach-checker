#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import hashlib
import pyfiglet
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ===============================
# Banner con ASCII ART
# ===============================
def show_banner():
    banner = pyfiglet.figlet_format("BreachChecker")
    print(Fore.CYAN + banner)
    print(Fore.RED + "⚠️  Warning: Use responsibly. The creator is not liable for illegal use.")
    print(Fore.YELLOW + "🔗 Powered by Have I Been Pwned API")
    print("-" * 70)

# ===============================
# Función para verificar email
# ===============================
def check_email(email):
    # Demo con hash SHA1 para simular API (HIBP real requiere API key)
    sha1 = hashlib.sha1(email.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        print(Fore.RED + "[-] Error al conectarse con la API")
        return

    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            print(Fore.RED + f"❌ {email} aparece en filtraciones ({count} veces).")
            return
    print(Fore.GREEN + f"✅ {email} no aparece en filtraciones conocidas.")

# ===============================
# Main
# ===============================
if __name__ == "__main__":
    show_banner()
    print(Fore.CYAN + "[*] Email Breach Checker iniciado...\n")

    email = input("📧 Ingresá el email a verificar: ")
    check_email(email)
