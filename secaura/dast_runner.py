import subprocess
import json
from typing import List, Dict, Any

class DASTScanner:
    def __init__(self, target_url: str):
        self.target_url = target_url

    def run(self) -> List[Dict[str, Any]]:
        findings = []
        cmd = [
            "nuclei",
            "-target", self.target_url,
            "-tags", "misconfig,exposure,cve",
            "-json-export", "/dev/stdout",
            "-silent"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            for line in result.stdout.strip().splitlines():
                if not line:
                    continue
                item = json.loads(line)
                findings.append({
                    "engine": "DAST-Nuclei",
                    "rule_id": item.get("template-id"),
                    "severity": item.get("info", {}).get("severity", "MEDIUM").upper(),
                    "description": item.get("info", {}).get("name"),
                    "target_url": item.get("matched-at"),
                    "file_path": None,
                    "line_number": None,
                    "code_context": item.get("extracted-results", "")
                })
        except FileNotFoundError:
            print("[!] Nuclei not installed or not in PATH. Skipping DAST.")
        except Exception as e:
            print(f"[!] Error running DAST: {e}")

        return findings
