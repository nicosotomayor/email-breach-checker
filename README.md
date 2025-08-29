# 📧 Email Breach Checker  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

Herramienta en **Python** que permite verificar si un correo electrónico aparece en filtraciones de datos conocidas, utilizando la API de [Have I Been Pwned](https://haveibeenpwned.com).  

---

## ✨ Características
- 🔎 Verifica si un email fue filtrado en brechas de seguridad.  
- ⚡ Respuesta rápida con la API de HIBP.  
- 🎨 Interfaz en consola con colores y banner ASCII.  
- 🐍 Código simple en Python 3.  

---

## 🚀 Instalación en Kali Linux

Clonar el repositorio y entrar en la carpeta:

```bash
git clone https://github.com/nicosotomayor/email-breach-checker.git
cd email-breach-checker
Instalar dependencias con apt:

bash
Copiar código
sudo apt update
sudo apt install python3-requests python3-colorama python3-pyfiglet -y
▶️ Uso
Ejecutar el script:

bash
Copiar código
python3 src/email_checker.py
Ejemplo de entrada:

text
Copiar código
📧 Ingresá el email a verificar: test@example.com
📋 Ejemplo de salida
text
Copiar código
██████╗ ██████╗ ███████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║
██████╔╝██████╔╝█████╗  ███████║██║     ███████║
██╔═══╝ ██╔══██╗██╔══╝  ██╔══██║██║     ██╔══██║
██║     ██║  ██║███████╗██║  ██║╚██████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

⚠️  Warning: Use responsibly. The creator is not liable for illegal use.
🔗 Powered by Have I Been Pwned API
----------------------------------------------------------------------

[*] Email Breach Checker iniciado...

📧 Ingresá el email a verificar: test@example.com
✅ test@example.com no aparece en filtraciones conocidas.
📜 Licencia
Este proyecto está bajo la licencia MIT – ver el archivo LICENSE para más detalles.
