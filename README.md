# VulnScanner 🔍

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/MTS-27/VulnScanner)
![Repo Size](https://img.shields.io/github/repo-size/MTS-27/VulnScanner)
![Last Commit](https://img.shields.io/github/last-commit/MTS-27/VulnScanner)
[![Star this repo](https://img.shields.io/github/stars/MTS-27/VulnScanner?style=social)](https://github.com/MTS-27/VulnScanner)

---

## ⚠️ Disclaimer

This tool is for **educational and ethical hacking use only.**  
⚠️ Always get permission before scanning systems you don’t own or control.

---

## 📄 Overview

**VulnScanner** is a lightweight Python-based vulnerability scanner that:
- Scans common ports (e.g. 22, 80, 443)
- Grabs service banners
- Fetches HTTP headers
- Saves results as a clean JSON report

---

## 🚀 Features

- Open port detection
- Banner grabbing
- HTTP header analysis
- JSON report generation

---

## 🛠 How to Use

```bash
git clone https://github.com/MTS-27/VulnScanner.git
cd VulnScanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python scanner.py

```
## When prompted, enter a domain or IP like:
```bash
scanme.nmap.org
```

Built with 💻 by MTS-27
Feel free to fork, star, or contribute!



