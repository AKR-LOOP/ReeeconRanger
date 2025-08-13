#!/usr/bin/env python3
import argparse
from rich.console import Console
from rr_utils import ensure_tool, save_json
from passive_recon import passive_recon
from active_recon import active_recon

console = Console()

def main():
    parser = argparse.ArgumentParser(description="ReconRanger - Passive & Active Recon Tool")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("--passive", action="store_true", help="Run passive reconnaissance only")
    parser.add_argument("--active", action="store_true", help="Run active reconnaissance only")
    parser.add_argument("--output", help="Save output to JSON file")
    args = parser.parse_args()

    ensure_tool("nmap")
    ensure_tool("whois")
    ensure_tool("dig")

    results = {}

    if args.passive or (not args.passive and not args.active):
        console.print("\n[cyan][*] Running Passive Reconnaissance...[/cyan]")
        results["passive"] = passive_recon(args.target)

    if args.active or (not args.passive and not args.active):
        console.print("\n[cyan][*] Running Active Reconnaissance...[/cyan]")
        results["active"] = active_recon(args.target)

    if args.output:
        save_json(results, args.output)

if __name__ == "__main__":
    main()
