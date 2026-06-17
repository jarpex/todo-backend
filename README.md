> [!NOTE]
> This repository represents a completed project stable since 2025. All subsequent commits are strictly limited to documentation updates and cosmetic formatting.

# Secure FastAPI Backend (SSDLC Reference)

The backend API for a task management application with a custom Svelte frontend. This repository serves as a reference implementation of a secured RESTful API built entirely around SSDLC (Secure Software Development Life Cycle) processes and a Shift-Left DevSecOps pipeline.

## Tech Stack

- **Core:** Python 3.13 (Alpine), FastAPI, Uvicorn
- **Database:** PostgreSQL, SQLAlchemy, Alembic
- **Validation & Config:** Pydantic v2, Pydantic Settings
- **Auth & Crypto:** Python-jose (JWT), Passlib (Bcrypt)

## Architecture & Network Topology

The application and database run in an isolated K3s cluster with zero public ports exposed. The infrastructure is segmented using the following network topology:

```text
[ Web Traffic ]
       │
       ▼
┌──────────────┐
│  Cloudflare  │       –   (WAF, SSL Termination, DDoS Protection)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Nginx VPS   │       –   (Reverse Proxy)
└──────┬───────┘
       │
  [ OpenVPN ]          –   (Secure Tunnel)
       │
       ▼
┌──────────────┐
│  Router/FW   │       –   (Edge Firewall)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Isolated     │
│ Server VLAN  │ ───► [ K3s Cluster ] ───► [ Isolated PostgreSQL ]
└──────────────┘
```

- Secret Management: HashiCorp Vault integration. Credentials are dynamically injected into Kubernetes Secrets at runtime rather than stored in env variables or code.

- Validation: Strict input validation and response serialization via Pydantic schemas.
  Threat Model & Target Assets
  The security controls and CI/CD gates in this repository are explicitly designed to protect the following assets against specific threat vectors:
  Protected Assets

- User Data: Authentication credentials (hashed passwords, JWTs) and user task metadata.

- Infrastructure Configuration: CI/CD variables, HashiCorp Vault access tokens, and Kubernetes cluster configurations.

- Supply Chain: Third-party Python dependencies (pip) and base container images.
  Mitigated Threat Vectors

- External Attacks: Network-layer threats including automated vulnerability scanners, injection attacks (SQLi, XSS), broken authentication mechanisms, and API privilege escalation.

- Internal/Insider Threats: Unauthorized modification of source code, CI/CD pipeline compromise, environment variable tampering, and unauthorized container escape/access within the K3s cluster.

## DevSecOps Pipeline (GitHub Actions)

The CI/CD workflow runs on self-hosted K3s runners and enforces the SSDLC Shift-Left security model:

```text
Code Change ➔ Git Commit ➔ GitHub Actions (Self-hosted K3s)
                                      │
    ┌─────────────────────────────────┴────────────────────────────────┐
    ▼                                 ▼                                ▼
SCA (Dependabot)               SAST (CodeQL & Semgrep Job)     Vault Secret Injection
    │                                 │                                │
    └─────────────────────────────────┼────────────────────────────────┘
                                      ▼
                             Kaniko (Daemonless Build)
                                      │
                                      ▼
                             K3s Deployment (Internal)
                                      │
                                      ▼
                             DAST (OWASP ZAP Job)
                                      │
                                      ▼
                        SARIF Export ➔ GitHub Security Dashboard
```

1. Vault Integration: Dynamically fetches secrets and injects K8s secrets at runtime.
2. SAST: Semgrep (run as an isolated K3s Job) and GitHub CodeQL. Pipeline exits with an error on critical findings to block vulnerable code from merging.
3. SCA: Daily CVE monitoring via GitHub Dependabot to eliminate supply chain vulnerabilities.
4. Build: Kaniko (daemonless container builds inside K3s) pushing to a local registry, minimizing host infrastructure attack surface.
5. DAST: OWASP ZAP (K3s Job) scanning internal cluster URLs to assess raw application logic by bypassing external WAF (Cloudflare).
6. Triage: Reports are aggregated into SARIF format and uploaded to the GitHub Security Dashboard.

## Related Repositories

- [ssdlc-svelte-frontend](https://github.com/jarpex/ssdlc-svelte-frontend) — Svelte + TypeScript frontend featuring the same DevSecOps infrastructure and innovative UX workflow.
