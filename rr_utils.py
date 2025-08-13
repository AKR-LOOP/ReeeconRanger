import json
import shutil
import sys
from rich.console import Console

console = Console()

def ensure_tool(tool_name):
    if shutil.which(tool_name) is None:
        console.print(f"[red][ERROR][/red] Required tool '{tool_name}' is not installed.")
        sys.exit(1)

def save_json(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        console.print(f"[green]Results saved to {filename}[/green]")
    except Exception as e:
        console.print(f"[red][ERROR][/red] Could not save JSON: {e}")
