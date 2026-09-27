import os
import requests
from typing import Dict, Any, Optional

class AIAuraClient:
    def __init__(self, base_url: Optional[str] = None, user: Optional[str] = None, api_key: Optional[str] = None):
        self.base_url = (base_url or os.getenv("AIAURA_BASE_URL", "https://aiaura.me/api/v1")).rstrip("/")
        self.user = user or os.getenv("AIAURA_USER")
        self.api_key = api_key or os.getenv("AIAURA_API_KEY")

        if not self.user or not self.api_key:
            raise ValueError("Missing AIAura credentials: AIAURA_USER and AIAURA_API_KEY must be set.")

        self.session = requests.Session()
        self.session.headers.update({
            "X-Aura-User": self.user,
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "SecAura-Scanner/1.0"
        })

    def request_remediation(self, finding: Dict[str, Any], source_code: str) -> Dict[str, Any]:
        """
        Submits the identified flaw and code context to AIAura for an automated patch.
        """
        payload = {
            "finding": {
                "rule_id": finding.get("rule_id"),
                "severity": finding.get("severity"),
                "description": finding.get("description"),
                "file_path": finding.get("file_path"),
                "line_number": finding.get("line_number")
            },
            "source_snippet": source_code,
            "instruction": "Fix the detected security vulnerability while preserving business logic."
        }

        try:
            # Adjust the endpoint path to match your specific AIAura routing (e.g., /chat/completions or /remediate)
            response = self.session.post(f"{self.base_url}/remediate", json=payload, timeout=45)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e),
                "remediated_code": None,
                "explanation": "Failed to communicate with AIAura."
            }
