# GhostMap

**GhostMap** es una herramienta de reconocimiento ofensivo en dos fases, creada para automatizar y acelerar procesos de escaneo durante auditorías, laboratorios de pentest y escenarios reales.

Utiliza `nmap` como núcleo para ejecutar:
- Un escaneo rápido de todos los puertos abiertos (Fase 1)
- Un análisis profundo de servicios, versiones y sistema operativo (Fase 2)

---

## 🧠 Características

- Banner estilo CLI personalizado
- Interfaz por línea de comandos con `argparse`
- Escaneo de puertos TCP abiertos con `nmap -sS -p-`
- Detección de servicios y versiones con `nmap -sCV`
- Código modular, limpio y extensible

---

## 🚀 Requisitos

- Python 3.x
- Nmap instalado y accesible desde el sistema

Para instalar Nmap en Kali Linux:

```bash
sudo apt update && sudo apt install nmap
```

---

## 💻 Uso

Cloná el repositorio o descargá el script:

```bash
git clone https://github.com/luisotero00/ghostmap.git
cd ghotmap
python3 ghotmap.py <IP o dominio objetivo>
```

Ejemplo:

```bash
python3 ghotmap.py 192.168.1.10
```

---

## 🔧 Instalación como comando global (opcional)

Hacé el script ejecutable:

```bash
chmod +x ghotmap.py
```

Movelo a una ruta del sistema:

```bash
sudo mv ghotmap.py /usr/local/bin/ghostmap
```

Ahora podés usarlo desde cualquier lugar con:

```bash
ghotmap 192.168.1.10
```

---

## 📁 Estructura del proyecto

```
ghostmap/
├── ghostmap.py
└── README.md
```

---

## 🧑‍💻 Autor

Creado por **erosennin420**  
Powered by Ghost Hack 🕶️

---

## ⚠️ Disclaimer

Esta herramienta fue desarrollada con fines educativos y de auditoría ética.  
**El uso no autorizado sobre sistemas que no te pertenecen puede constituir delito.**  
Usala bajo tu propia responsabilidad y siempre con permiso.
