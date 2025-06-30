# VulnScanner 🔍

**VulnScanner** is a lightweight, Python-based vulnerability scanner that:
- Scans common ports on a target IP/domain
- Grabs banners from open ports (e.g., SSH, FTP, HTTP)
- Fetches HTTP headers from live web servers
- Saves scan results in clean JSON format

---

## 💡 Features

- 🔎 Open port detection (e.g. 22, 80, 443...)
- 📡 Banner grabbing (reveals server info)
- 🌐 HTTP header inspection (via requests)
- 📁 Output reports as JSON files

---

## 🚀 Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/MTS-27/VulnScanner.git
cd VulnScanner
