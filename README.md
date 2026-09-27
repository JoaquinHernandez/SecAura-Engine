<div align="center">

# 🐉 SecAura-Engine

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![AI-Backend: AIAura](https://img.shields.io/badge/AI%20Engine-AIAura-blueviolet)](https://aiaura.me)
[![Security Pipeline](https://img.shields.io/badge/Pipeline-SAST%20%2B%20DAST%20%2B%20Remediation-orange)](#-system-architecture)

<p align="center">
  <strong>Autonomous Dual-Spectrum SAST + DAST Security Engine Powered by AIAura</strong>
</p>
__====-_  _-====__
                  _--^^^#####//      \\#####^^^--_
               _-^##########// (    ) \\##########^-_
              -############//  |\^^/|  \\############-
            _/############//   (@::@)   \\############\_
           /#############((     \\//     ))#############\
          -###############\\    (oo)    //###############-
         -#################\\  / VV \  //#################-
        -###################\\/      \//###################-
       _#/|##########/\######(   /\   )######/\##########|\#_
       |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
       `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
          `   `  `      `   / | |  | | \   '      '  '   '
                           (  | |  | |  )
                          __\ | |  | | /__
                         (____< |  | >____)
                               (____)
                     S E C A U R A   E N G I N E
              [ The Dragon of Autonomous Code Remediation ]

## 📌 Executive Overview

**SecAura-Engine** is a unified DevSecOps scanning and auto-remediation platform. It unifies static source security testing (SAST) and dynamic runtime analysis (DAST) into a single telemetry pipeline. 

When flaws or misconfigurations are discovered, SecAura extracts surrounding syntax context and queries the **AIAura** platform (`https://aiaura.me`) to synthesize functional, logic-preserving security patches directly into unified Git diffs.

---

## 🛡️ DAST Engine & Target Stack Matrix

To guarantee column layout stability across all browsers and screen widths, this matrix uses explicit structural column definitions with non-breaking whitespace.

<table>
  <thead>
    <tr>
      <th align="left" width="22%">Engine&nbsp;&amp;&nbsp;Target</th>
      <th align="center" width="16%">Pinned&nbsp;Release</th>
      <th align="left" width="22%">Primary&nbsp;Role</th>
      <th align="left" width="40%">Architecture&nbsp;&amp;&nbsp;Implementation&nbsp;Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>ZAP&nbsp;+&nbsp;AF</b></td>
      <td align="center"><code>2.17.0</code></td>
      <td>Web App DAST</td>
      <td>Automation Framework (<code>zap.yaml</code>) provides declarative, CI/CD-native active scans for OWASP Top 10 web injection vectors.</td>
    </tr>
    <tr>
      <td><b>ZAP Traditional + Client&nbsp;Spider</b></td>
      <td align="center"><i>Core&nbsp;Add-on</i></td>
      <td>Modern SPA Crawling</td>
      <td>Injects browser-side client scripts to construct dynamic DOM maps in modern frameworks (React, Vue, Angular) where legacy spiders fail.</td>
    </tr>
    <tr>
      <td><b>Nuclei</b></td>
      <td align="center"><code>3.11.1</code></td>
      <td>Fast Pattern Matching</td>
      <td>High-speed YAML templates targeting known CVEs, perimeter exposures, and infrastructure misconfigurations.</td>
    </tr>
    <tr>
      <td><b>Schemathesis</b></td>
      <td align="center"><code>4.24.3</code></td>
      <td>Property-Based API Fuzzing</td>
      <td>Derives fuzzing suites directly from OpenAPI / GraphQL / JSON schemas to catch 500-series panics, schema drift, and boundary errors.</td>
    </tr>
    <tr>
      <td><b>RESTler</b></td>
      <td align="center"><i>Source / Commit</i></td>
      <td>Stateful REST Fuzzing</td>
      <td>Microsoft stateful fuzzer built from an exact upstream commit; constructs dynamic dependency graphs across API endpoints.</td>
    </tr>
    <tr>
      <td><b>Playwright</b></td>
      <td align="center"><code>1.63.0</code></td>
      <td>Auth &amp; Session Driver</td>
      <td>Automates multi-step authenticated workflows (SSO/MFA) in sandboxed non-root browser sessions and routes traffic into ZAP.</td>
    </tr>
  </tbody>
</table>

---

## 🏗️ System Architecture

<pre><code>
                                [ Source Code / Git Repo ]
                                             |
                     +-----------------------+-----------------------+
                     |                                               |
                     v                                               v
         +-----------------------+                       +-----------------------+
         |     SAST PIPELINE     |                       |     DAST PIPELINE     |
         |  • Semgrep AST Rules  |                       |  • Nuclei 3.11.1      |
         |  • Language Linters   |                       |  • ZAP 2.17.0 (AF)    |
         |  • Secret Detection   |                       |  • Schemathesis 4.24  |
         +-----------+-----------+                       |  • RESTler & Playwright
                     |                                   +-----------+-----------+
                     |                                               |
                     +-----------------------+-----------------------+
                                             |
                                             v
                             +-------------------------------+
                             |    FINDING NORMALIZATION      |
                             |  • Deduplication Engine       |
                             |  • Unified SARIF/JSON Schema  |
                             |  • Context Window Extraction  |
                             +---------------+---------------+
                                             |
                                             v
                             +-------------------------------+
                             |        AIAURA ENGINE          |
                             |     (https://aiaura.me)       |
                             |  • Auth: User & API Key       |
                             |  • Semantic AST Logic Review  |
                             |  • Verified Patch Synthesizer |
                             +---------------+---------------+
                                             |
                                             v
                             +-------------------------------+
                             |      DEPLOYABLE OUTPUTS       |
                             |  • Rich CLI Diagnostic Table  |
                             |  • Unified Patch Diffs (.diff)|
                             |  • DefectDojo/CI Ingestion    |
                             +-------------------------------+
</code></pre>

---

## 📂 Project Structure

```text
secaura-engine/
│
├── config/
│   └── scan_policy.yaml         # Policy thresholds and scan exclusions
│
├── secaura/
│   ├── __init__.py
│   ├── aiaura_client.py         # AIAura API client & patch synthesizer
│   ├── sast_runner.py           # Static analysis engine (Semgrep / AST)
│   ├── dast_runner.py           # Dynamic scanning orchestrator (Nuclei / ZAP)
│   ├── normalizer.py            # Unified schema consolidation
│   └── reporter.py              # CLI and file reporting utilities
│
├── .env.example                 # Environment variable template
├── main.py                      # CLI entrypoint
├── requirements.txt             # Python runtime dependencies
└── README.md

🚀 Installation & Prerequisites
1. System Dependencies
SecAura orchestrates external binaries alongside its core Python framework:
# Ubuntu / Debian
sudo apt-get update && sudo apt-get install -y git curl python3-pip

# 1. Install Semgrep (Static Analysis)
pip install semgrep

# 2. Install Schemathesis (API Testing)
pip install schemathesis

# 3. Install Nuclei (ProjectDiscovery)
go install -v [github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest](https://github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest)
=== Starting SecAura Combined Scan ===
[*] Running SAST on: /workspace/project/src
[+] SAST complete. Found: 1 issue(s).
[*] Running DAST against: [https://staging.internal.net](https://staging.internal.net)
[+] DAST complete. Found: 0 issue(s).

                     Security Assessment Findings
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type  ┃ Rule / Check ID     ┃ Severity ┃ Location                    ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ SAST  │ sql-injection-param │ HIGH     │ src/db/users.py:42          │
└───────┴─────────────────────┴──────────┴─────────────────────────────┘

[*] Requesting automated remediations from AIAura...

Analyzing Finding #1: sql-injection-param in src/db/users.py
✔ Patch suggested by AIAura:
--- a/src/db/users.py
+++ b/src/db/users.py
@@ -39,5 +39,5 @@ def get_user_profile(user_id):
-    query = f"SELECT * FROM users WHERE id = '{user_id}'"
-    cursor.execute(query)
+    query = "SELECT * FROM users WHERE id = %s"
+    cursor.execute(query, (user_id,))
License
Distributed under the Apache 2.0 License. See LICENSE for complete terms.
