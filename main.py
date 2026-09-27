import os
import argparse
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from secaura.sast_runner import SASTScanner
from secaura.dast_runner import DASTScanner
from secaura.aiaura_client import AIAuraClient

console = Console()

def extract_file_context(file_path: str, start_line: int, window: int = 15) -> str:
    """Reads surrounding source lines for accurate AI context."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    start = max(0, start_line - window)
    end = min(len(lines), start_line + window)
    return "".join(lines[start:end])

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="SecAura: Dual SAST/DAST + AIAura Remediation Engine")
    parser.add_argument("--src", type=str, help="Path to source code for SAST", default=".")
    parser.add_argument("--url", type=str, help="Target URL for dynamic DAST scanning", default=None)
    parser.add_argument("--remediate", action="store_true", help="Send findings to AIAura for patches")
    args = parser.parse_args()

    console.print("[bold blue]=== Starting SecAura Combined Scan ===[/bold blue]")

    all_findings = []

    # 1. Run SAST
    if args.src:
        console.print(f"[*] Running SAST on: [cyan]{args.src}[/cyan]")
        sast = SASTScanner(target_dir=args.src)
        sast_results = sast.run()
        all_findings.extend(sast_results)
        console.print(f"[+] SAST complete. Found: {len(sast_results)} issue(s).")

    # 2. Run DAST
    if args.url:
        console.print(f"[*] Running DAST against: [cyan]{args.url}[/cyan]")
        dast = DASTScanner(target_url=args.url)
        dast_results = dast.run()
        all_findings.extend(dast_results)
        console.print(f"[+] DAST complete. Found: {len(dast_results)} issue(s).")

    # Display Findings Table
    table = Table(title="Security Assessment Findings")
    table.add_column("Type", style="cyan")
    table.add_column("Rule / CVE", style="magenta")
    table.add_column("Severity", style="bold red")
    table.add_column("Location", style="green")

    for f in all_findings:
        loc = f"{f['file_path']}:{f['line_number']}" if f.get("file_path") else f.get("target_url", "N/A")
        table.add_row(f["engine"], f["rule_id"], f["severity"], loc)

    console.print(table)

    # 3. AI Remediation via AIAura
    if args.remediate and all_findings:
        console.print("\n[bold yellow][*] Requesting automated remediations from AIAura...[/bold yellow]")
        client = AIAuraClient()

        for idx, finding in enumerate(all_findings, 1):
            if not finding.get("file_path"):
                console.print(f"[-] Skipping remediation for non-code finding: {finding['rule_id']}")
                continue

            console.print(f"\n[cyan]Analyzing Finding #{idx}: {finding['rule_id']} in {finding['file_path']}[/cyan]")
            context = extract_file_context(finding["file_path"], finding["line_number"])
            
            patch_data = client.request_remediation(finding, context)
            
            if patch_data.get("remediated_code"):
                console.print(f"[bold green]✔ Patch suggested by AIAura:[/bold green]")
                console.print(patch_data["remediated_code"])
            else:
                console.print(f"[red]Could not generate patch: {patch_data.get('error', 'Unknown error')}[/red]")

if __name__ == "__main__":
    main()
