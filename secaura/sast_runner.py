import subprocess
import json
import os
from typing import List, Dict, Any

class SASTScanner:
    def __init__(self, target_dir: str):
        self.target_dir = os.path.abspath(target_dir)

    def run(self) -> List[Dict[str, Any]]:
        findings = []
        # Runs Semgrep using security audit rules with JSON output
        cmd = [
            "semgrep", "scan",
            "--config", "auto",
            "--json",
            self.target_dir
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if not result.stdout:
                return findings

            data = json.loads(result.stdout)
            for item in data.get("results", []):
                findings.append({
                    "engine": "SAST-Semgrep",
                    "rule_id": item.get("check_id"),
                    "severity": item.get("extra", {}).get("severity", "MEDIUM"),
                    "description": item.get("extra", {}).get("message"),
                    "file_path": item.get("path"),
                    "line_number": item.get("start", {}).get("line"),
                    "end_line": item.get("end", {}).get("line"),
                    "code_context": item.get("extra", {}).get("lines", "")
                })
        except FileNotFoundError:
            print("[!] Semgrep is not installed or not in PATH. Skipping SAST.")
        except json.JSONDecodeError:
            print("[!] Failed to parse Semgrep output.")
        
        return findings
