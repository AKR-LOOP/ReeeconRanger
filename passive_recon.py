import subprocess
from rich.console import Console

console = Console()

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True)
        return result.strip()
    except subprocess.CalledProcessError:
        return ""

def passive_recon(target):
    data = {}
    
    console.print(f"[yellow]WHOIS Lookup for {target}[/yellow]")
    data["whois"] = run_command(f"whois {target}")

    console.print(f"[yellow]DNS Records for {target}[/yellow]")
    data["dns_records"] = run_command(f"dig {target} ANY +noall +answer")

    console.print(f"[yellow]Reverse DNS Lookup for {target}[/yellow]")
    data["reverse_dns"] = run_command(f"dig -x {target} +short")

    console.print(f"[yellow]Traceroute to {target}[/yellow]")
    data["traceroute"] = run_command(f"traceroute {target}")

    return data
