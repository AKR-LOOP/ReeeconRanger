# ReconRanger 🕵️‍♂️
A Python-based reconnaissance tool for Red Teaming, supporting both passive and active recon.  
No APIs. No browser automation. 100% CLI-based.

---

## 🚀 Features
- **Passive Recon:**
  - WHOIS Lookup
  - DNS Records
  - Reverse DNS
  - Traceroute
- **Active Recon:**
  - Nmap SYN Scan (-sS)
  - Service & Version Detection (-sV)
  - OS Detection (-O)
  - Vulnerability Scan (nmap --script vuln)

---

## 📦 Installation
bash
git clone https://github.com/YOUR_USERNAME/ReconRanger.git
cd ReconRanger
pip install -r requirements.txt


⚡ Usage
bash
Copy
Edit
python3 reconranger.py <target> [--passive] [--active] [--output results.json]
Examples:

bash
Copy
Edit
python3 reconranger.py example.com --passive
python3 reconranger.py example.com --active
python3 reconranger.py example.com --output scan.json
