import subprocess
from rich.console import Console

console = Console()

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True)
        return result.strip()
    except subprocess.CalledProcessError:
        return ""

def active_recon(target):
    data = {}

    console.print(f"[yellow]Scanning top 1000 ports on {target}[/yellow]")
    data["nmap_top_1000"] = run_command(f"nmap -sS -sV -O {target}")

    console.print(f"[yellow]Running Aggressive Scan on {target}[/yellow]")
    data["nmap_aggressive"] = run_command(f"nmap -A {target}")

    console.print(f"[yellow]Running Vulnerability Scripts on {target}[/yellow]")
    data["nmap_vuln"] = run_command(f"nmap --script vuln {target}")

    return data
