# SecAura-EngineEnterprise Hybrid SAST + DAST Security Engine Powered by AIAura Autonomous RemediationPlaintext                        __====-_  _-====__
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
Executive OverviewSecAura-Engine is a unified security scanning and remediation framework. It coordinates static source analysis (SAST) and dynamic runtime analysis (DAST) into a consolidated, normalized finding pipeline.When vulnerabilities or misconfigurations are discovered, SecAura extracts the relevant code context and queries the AIAura platform ([https://aiaura.me](https://aiaura.me)) using secure user authentication to synthesize verified code fixes, contextual explanations, and production-ready patch diffs.Complete DAST Toolchain MatrixSecAura integrates a production-grade DAST testing suite designed to cover traditional web flaws, modern SPAs, and complex API architectures:EngineRelease TargetCore Function & JustificationZAP + Automation Framework2.17.0Core Web Application DAST. The Automation Framework (zap.yaml) ensures declarative, CI/CD-native scans for classic OWASP Top 10 web injection vectors.ZAP Traditional + Client SpiderCore ExtensionDiscovery & Modern SPA Crawling. Uses DOM-based injection via browser automation to execute client-side JavaScript, solving SPA crawling limitations.Nuclei3.11.1Ultra-fast protocol-level rule matching for known exposures, CVE checks, and misconfigurations.Schemathesis4.24.3Property-based contract testing directly derived from OpenAPI, GraphQL, and JSON schemas to uncover 500-series panics and boundary drift.RESTlerMicrosoft CoreStateful REST API fuzzing. Constructs dynamic dependency graphs across endpoints (e.g., resource creation $\rightarrow$ token exchange $\rightarrow$ deletion).Playwright1.63.0Seed crawler & synthetic user journey execution. Drives authenticated headless workflows and proxies browser traffic directly through ZAP.System ArchitecturePlaintext                                [ Source Code / Git Repo ]
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
                             |  • Common SARIF/JSON Schema   |
                             |  • Context Window Extraction  |
                             +---------------+---------------+
                                             |
                                             v
                             +-------------------------------+
                             |        AIAURA ENGINE          |
                             |     (https://aiaura.me)       |
                             |  • Auth: AIAura User & Key    |
                             |  • Semantic Code Analysis     |
                             |  • Business-Logic Preservation|
                             +---------------+---------------+
                                             |
                                             v
                             +-------------------------------+
                             |      DEPLOYABLE OUTPUTS       |
                             |  • Rich CLI Summary Table     |
                             |  • Unified Patch Diffs (.diff)|
                             |  • DefectDojo/CI Ingestion    |
                             +-------------------------------+
Project LayoutPlaintextsecaura-engine/
├── config/
│   └── scan_policy.yaml     # Policy limits, thresholds, and exclusions
├── secaura/
│   ├── __init__.py
│   ├── aiaura_client.py     # AIAura API integration and prompt scaffolding
│   ├── dast_runner.py       # DAST executor (Nuclei, ZAP, Schemathesis)
│   ├── normalizer.py        # Maps tool outputs to unified schema
│   ├── reporter.py          # Formats CLI tables and patch diffs
│   └── sast_runner.py       # SAST executor (Semgrep / AST scanners)
├── .env.example             # Configuration variables
├── main.py                  # CLI Orchestrator
├── requirements.txt         # Core Python dependencies
└── README.md
Installation & Setup1. System DependenciesSecAura-Engine coordinates external engines alongside its core Python framework.Bash# Ubuntu / Debian
sudo apt-get update && sudo apt-get install -y git curl python3-pip

# Install Semgrep (SAST)
pip install semgrep

# Install Nuclei (DAST Engine)
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Install Schemathesis (API Fuzzing)
pip install schemathesis
2. Clone the RepositoryBashgit clone https://github.com/your-org/secaura-engine.git
cd secaura-engine
3. Python Virtual EnvironmentBashpython3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
4. ConfigurationCopy the example environment template and configure your AIAura credentials:Bashcp .env.example .env
Edit .env:Ini, TOMLAIAURA_BASE_URL="https://aiaura.me/api/v1"
AIAURA_USER="your_username"
AIAURA_API_KEY="your_api_key_here"
Core UsageFull Hybrid Scan with Auto-RemediationRun static checks against a codebase, trigger dynamic tests against a live endpoint, and generate patches via AIAura:Bashpython main.py --src ./src --url https://staging.internal.net --remediate
SAST-Only ScanRun local pattern analysis and generate remediation diffs without launching network services:Bashpython main.py --src ./src --remediate
DAST-Only ScanTarget an active deployment or staging instance for dynamic testing:Bashpython main.py --url https://staging.internal.net
Remediation Output ExampleDuring execution, SecAura aggregates all findings into a structured terminal view and prints the AIAura remediation patch:Plaintext=== Starting SecAura Combined Scan ===
[*] Running SAST on: /workspace/project/src
[+] SAST complete. Found: 1 issue(s).
[*] Running DAST against: https://staging.internal.net
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
Diff--- a/src/db/users.py
+++ b/src/db/users.py
@@ -39,5 +39,5 @@ def get_user_profile(user_id):
-    query = f"SELECT * FROM users WHERE id = '{user_id}'"
-    cursor.execute(query)
+    query = "SELECT * FROM users WHERE id = %s"
+    cursor.execute(query, (user_id,))
Policy Configuration (config/scan_policy.yaml)YAMLsast:
  exclude_paths:
    - "tests/"
    - "node_modules/"
    - "vendor/"
  minimum_severity: "MEDIUM"

dast:
  rate_limit: 150
  timeout_seconds: 15
  nuclei_tags:
    - "misconfig"
    - "exposure"
    - "cve"

remediation:
  context_window_lines: 15
  auto_generate_diff: true
LicenseDistributed under the Apache 2.0 License. See LICENSE for details.
