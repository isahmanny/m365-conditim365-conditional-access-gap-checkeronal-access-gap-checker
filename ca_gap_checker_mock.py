"""
M365 Conditional Access Gap Checker - Mock Data Version
=========================================================
Portfolio demonstration tool for AltSchool Africa Cybersecurity.
Simulates Microsoft 365 sign-in log analysis, identifies logins that
bypassed or exposed gaps in Conditional Access policies, and generates
a professional HTML report with policy recommendations.

No Microsoft account or API credentials required.

Run:
    python ca_gap_checker_mock.py
"""

import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# MOCK SIGN-IN DATA
# ─────────────────────────────────────────────

MOCK_SIGNINS = [
    # ── HIGH RISK GAPS ─────────────────────────────────────────
    {
        "id": "s001",
        "userId": "u001",
        "userDisplayName": "Amina Yusuf",
        "userEmail": "amina.yusuf@contoso.onmicrosoft.com",
        "department": "Finance",
        "jobTitle": "Finance Manager",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "185.220.101.47",
        "location": {"city": "Moscow", "countryOrRegion": "RU"},
        "clientAppUsed": "Browser",
        "deviceCompliant": False,
        "deviceManaged": False,
        "mfaRequired": False,
        "mfaCompleted": False,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0)",
        "signInHour": 3,
        "isGuest": False,
        "riskLevel": "high",
        "status": {"errorCode": 0},
    },
    {
        "id": "s002",
        "userId": "u002",
        "userDisplayName": "Chidi Okafor",
        "userEmail": "chidi.okafor@contoso.onmicrosoft.com",
        "department": "IT",
        "jobTitle": "IT Administrator",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "103.75.190.12",
        "location": {"city": "Beijing", "countryOrRegion": "CN"},
        "clientAppUsed": "Microsoft Teams",
        "deviceCompliant": False,
        "deviceManaged": False,
        "mfaRequired": True,
        "mfaCompleted": False,
        "userAgent": "Mozilla/5.0 (Linux; Android)",
        "signInHour": 1,
        "isGuest": False,
        "riskLevel": "high",
        "status": {"errorCode": 0},
    },
    {
        "id": "s003",
        "userId": "u005",
        "userDisplayName": "External Vendor",
        "userEmail": "vendor@externalco.com",
        "department": "Guest",
        "jobTitle": "External Consultant",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "91.108.56.22",
        "location": {"city": "Lagos", "countryOrRegion": "NG"},
        "clientAppUsed": "SharePoint Online",
        "deviceCompliant": False,
        "deviceManaged": False,
        "mfaRequired": False,
        "mfaCompleted": False,
        "userAgent": "python-requests/2.31",
        "signInHour": 14,
        "isGuest": True,
        "riskLevel": "medium",
        "status": {"errorCode": 0},
    },

    # ── MEDIUM RISK GAPS ───────────────────────────────────────
    {
        "id": "s004",
        "userId": "u003",
        "userDisplayName": "Fatima Al-Hassan",
        "userEmail": "fatima.alhassan@contoso.onmicrosoft.com",
        "department": "Executive",
        "jobTitle": "CEO",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "197.210.54.101",
        "location": {"city": "Abuja", "countryOrRegion": "NG"},
        "clientAppUsed": "Outlook Mobile",
        "deviceCompliant": False,
        "deviceManaged": False,
        "mfaRequired": True,
        "mfaCompleted": True,
        "userAgent": "Outlook-iOS/3.40",
        "signInHour": 23,
        "isGuest": False,
        "riskLevel": "low",
        "status": {"errorCode": 0},
    },
    {
        "id": "s005",
        "userId": "u004",
        "userDisplayName": "James Okonkwo",
        "userEmail": "james.okonkwo@contoso.onmicrosoft.com",
        "department": "Sales",
        "jobTitle": "Sales Lead",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "41.58.99.34",
        "location": {"city": "Accra", "countryOrRegion": "GH"},
        "clientAppUsed": "Exchange Online",
        "deviceCompliant": True,
        "deviceManaged": True,
        "mfaRequired": False,
        "mfaCompleted": False,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0)",
        "signInHour": 10,
        "isGuest": False,
        "riskLevel": "medium",
        "status": {"errorCode": 0},
    },

    # ── LOW RISK / SECURE ──────────────────────────────────────
    {
        "id": "s006",
        "userId": "u006",
        "userDisplayName": "Michael Eze",
        "userEmail": "michael.eze@contoso.onmicrosoft.com",
        "department": "Engineering",
        "jobTitle": "Software Engineer",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "102.89.45.23",
        "location": {"city": "Abuja", "countryOrRegion": "NG"},
        "clientAppUsed": "Microsoft Teams",
        "deviceCompliant": True,
        "deviceManaged": True,
        "mfaRequired": True,
        "mfaCompleted": True,
        "userAgent": "Mozilla/5.0 (Windows NT 11.0)",
        "signInHour": 9,
        "isGuest": False,
        "riskLevel": "none",
        "status": {"errorCode": 0},
    },
    {
        "id": "s007",
        "userId": "u007",
        "userDisplayName": "Ngozi Ibrahim",
        "userEmail": "ngozi.ibrahim@contoso.onmicrosoft.com",
        "department": "Engineering",
        "jobTitle": "DevOps Engineer",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "105.112.10.88",
        "location": {"city": "Kano", "countryOrRegion": "NG"},
        "clientAppUsed": "Microsoft Teams",
        "deviceCompliant": True,
        "deviceManaged": True,
        "mfaRequired": True,
        "mfaCompleted": True,
        "userAgent": "Mozilla/5.0 (Macintosh)",
        "signInHour": 11,
        "isGuest": False,
        "riskLevel": "none",
        "status": {"errorCode": 0},
    },
    {
        "id": "s008",
        "userId": "u008",
        "userDisplayName": "Ahmed Musa",
        "userEmail": "ahmed.musa@contoso.onmicrosoft.com",
        "department": "Operations",
        "jobTitle": "Operations Manager",
        "createdDateTime": (datetime.datetime.utcnow() - datetime.timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ipAddress": "197.211.58.99",
        "location": {"city": "Abuja", "countryOrRegion": "NG"},
        "clientAppUsed": "Outlook",
        "deviceCompliant": True,
        "deviceManaged": True,
        "mfaRequired": True,
        "mfaCompleted": True,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0)",
        "signInHour": 8,
        "isGuest": False,
        "riskLevel": "none",
        "status": {"errorCode": 0},
    },
]

# ─────────────────────────────────────────────
# RISK & POLICY DEFINITIONS
# ─────────────────────────────────────────────
RISKY_COUNTRIES      = {"RU", "CN", "KP", "IR", "SY", "CU"}
BUSINESS_HOURS_START = 7
BUSINESS_HOURS_END   = 20
SUSPICIOUS_AGENTS    = ["python-requests", "curl", "go-http-client", "scrapy", "axios"]

POLICY_RECOMMENDATIONS = {
    "no_mfa":              "Create CA Policy: Require MFA for All Users — applies to all cloud apps.",
    "risky_country":       "Create CA Policy: Block sign-ins from high-risk countries (RU, CN, KP, IR).",
    "non_compliant_device":"Create CA Policy: Require compliant device — blocks unmanaged endpoints.",
    "outside_hours":       "Create CA Policy: Restrict sign-ins to business hours (07:00–20:00).",
    "suspicious_agent":    "Create CA Policy: Block legacy/automated clients via user agent filtering.",
    "guest_no_mfa":        "Create CA Policy: Require MFA for Guest and External Users.",
    "high_risk_signin":    "Enable Identity Protection: Auto-block or require MFA on high-risk sign-ins.",
}


# ─────────────────────────────────────────────
# GAP ANALYSIS
# ─────────────────────────────────────────────
def analyse_gaps(signin: dict) -> tuple[str, list[str], list[str]]:
    gaps         = []
    policies     = []

    # MFA not completed
    if not signin.get("mfaCompleted"):
        gaps.append("MFA not enforced on this sign-in")
        policies.append(POLICY_RECOMMENDATIONS["no_mfa"])

    # Risky country
    country = (signin.get("location") or {}).get("countryOrRegion", "")
    if country in RISKY_COUNTRIES:
        gaps.append(f"Sign-in from high-risk country: {country}")
        policies.append(POLICY_RECOMMENDATIONS["risky_country"])

    # Non-compliant device
    if not signin.get("deviceCompliant"):
        gaps.append("Non-compliant/unmanaged device allowed")
        policies.append(POLICY_RECOMMENDATIONS["non_compliant_device"])

    # Outside business hours
    hour = signin.get("signInHour", 12)
    if hour < BUSINESS_HOURS_START or hour > BUSINESS_HOURS_END:
        gaps.append(f"Sign-in outside business hours ({hour:02d}:00 UTC)")
        policies.append(POLICY_RECOMMENDATIONS["outside_hours"])

    # Suspicious user agent
    agent = signin.get("userAgent", "").lower()
    for sa in SUSPICIOUS_AGENTS:
        if sa in agent:
            gaps.append(f"Suspicious client detected: {signin.get('userAgent')}")
            policies.append(POLICY_RECOMMENDATIONS["suspicious_agent"])
            break

    # Guest with no MFA
    if signin.get("isGuest") and not signin.get("mfaCompleted"):
        gaps.append("Guest user signed in without MFA")
        policies.append(POLICY_RECOMMENDATIONS["guest_no_mfa"])

    # High risk sign-in level
    if signin.get("riskLevel") in {"high", "medium"}:
        gaps.append(f"Microsoft risk detection: {signin.get('riskLevel').upper()} risk sign-in")
        policies.append(POLICY_RECOMMENDATIONS["high_risk_signin"])

    # Deduplicate policies
    policies = list(dict.fromkeys(policies))

    if len(gaps) >= 3:
        return "HIGH", gaps, policies
    elif len(gaps) >= 1:
        return "MEDIUM", gaps, policies
    else:
        return "LOW", gaps, policies


# ─────────────────────────────────────────────
# HTML REPORT
# ─────────────────────────────────────────────
def generate_report(signins_with_gaps: list[dict]) -> str:
    now    = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    high   = [s for s in signins_with_gaps if s["risk"] == "HIGH"]
    medium = [s for s in signins_with_gaps if s["risk"] == "MEDIUM"]
    low    = [s for s in signins_with_gaps if s["risk"] == "LOW"]

    total_gaps = sum(len(s["gaps"]) for s in signins_with_gaps)

    def badge(risk):
        colors = {"HIGH": "#dc2626", "MEDIUM": "#d97706", "LOW": "#16a34a"}
        return f'<span class="badge" style="background:{colors[risk]}">{risk}</span>'

    def rows(lst):
        if not lst:
            return '<tr><td colspan="7" class="empty">No sign-ins in this category.</td></tr>'
        out = ""
        for item in lst:
            s   = item["signin"]
            loc = s.get("location") or {}
            out += f"""
            <tr>
              <td><strong>{s.get('userDisplayName','—')}</strong><br>
                  <small>{s.get('userEmail','')}</small><br>
                  <small class="dept">{s.get('department','')} — {s.get('jobTitle','')}</small></td>
              <td class="mono">{s.get('createdDateTime','—')[:16].replace('T',' ')}</td>
              <td class="mono">{s.get('ipAddress','—')}<br>
                  <small>{loc.get('city','—')}, {loc.get('countryOrRegion','—')}</small></td>
              <td>{s.get('clientAppUsed','—')}</td>
              <td>{badge(item['risk'])}</td>
              <td class="gaps">{'<br>'.join(['⚠ ' + g for g in item['gaps']]) if item['gaps'] else '—'}</td>
              <td class="policy">{'<br>'.join(['→ ' + p for p in item['policies']]) if item['policies'] else '—'}</td>
            </tr>"""
        return out

    def section(title, emoji, lst):
        return f"""
        <section>
          <h2>{emoji} {title} <span class="count">({len(lst)})</span></h2>
          <div class="table-wrap">
            <table>
              <thead><tr>
                <th>User</th><th>Sign-in Time</th><th>IP / Location</th>
                <th>Client App</th><th>Risk</th><th>CA Gaps Detected</th><th>Policy Recommendation</th>
              </tr></thead>
              <tbody>{rows(lst)}</tbody>
            </table>
          </div>
        </section>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>M365 Conditional Access Gap Report</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
  *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:'Inter',sans-serif;background:#0a0f1e;color:#e2e8f0;min-height:100vh;padding:2rem 2.5rem}}

  header{{margin-bottom:2.5rem;padding-bottom:1.5rem;border-bottom:1px solid #1e293b}}
  .header-top{{display:flex;align-items:center;gap:1rem;margin-bottom:0.5rem}}
  .logo{{width:42px;height:42px;background:linear-gradient(135deg,#8b5cf6,#06b6d4);border-radius:10px;
         display:flex;align-items:center;justify-content:center;font-size:1.3rem}}
  header h1{{font-size:1.6rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em}}
  .meta{{font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#475569}}
  .meta span{{margin-right:1.5rem}}
  .mock-badge{{display:inline-block;background:#1e3a5f;color:#60a5fa;border:1px solid #2563eb;
               padding:0.2rem 0.6rem;border-radius:4px;font-size:0.65rem;font-weight:600;
               letter-spacing:0.08em;margin-left:0.75rem;vertical-align:middle}}

  .stats{{display:grid;grid-template-columns:repeat(6,1fr);gap:1rem;margin-bottom:2.5rem}}
  .card{{background:#0f172a;border:1px solid #1e293b;border-radius:12px;padding:1.1rem 1.2rem}}
  .card .label{{font-size:0.68rem;color:#64748b;text-transform:uppercase;letter-spacing:0.1em;font-weight:600}}
  .card .val{{font-size:1.8rem;font-weight:700;margin-top:0.3rem;font-family:'JetBrains Mono',monospace}}
  .card.total  .val{{color:#818cf8}}
  .card.high   .val{{color:#f87171}}
  .card.medium .val{{color:#fbbf24}}
  .card.low    .val{{color:#4ade80}}
  .card.gaps   .val{{color:#f87171}}
  .card.policies .val{{color:#38bdf8}}

  section{{margin-bottom:2.5rem}}
  section h2{{font-size:0.95rem;font-weight:600;color:#94a3b8;margin-bottom:0.75rem;
              display:flex;align-items:center;gap:0.4rem}}
  .count{{color:#475569;font-weight:400}}

  .table-wrap{{overflow-x:auto;border-radius:10px;border:1px solid #1e293b}}
  table{{width:100%;border-collapse:collapse;font-size:0.78rem}}
  thead th{{background:#0f172a;color:#475569;font-weight:600;text-transform:uppercase;
            letter-spacing:0.07em;font-size:0.65rem;padding:0.8rem 1rem;
            text-align:left;border-bottom:1px solid #1e293b}}
  tbody tr{{border-bottom:1px solid #0f172a;transition:background 0.12s}}
  tbody tr:hover{{background:#0f172a}}
  tbody tr:last-child{{border-bottom:none}}
  tbody td{{padding:0.75rem 1rem;color:#cbd5e1;vertical-align:top;line-height:1.7}}
  tbody td small{{color:#475569;font-size:0.7rem}}
  .dept{{color:#334155}}
  .mono{{font-family:'JetBrains Mono',monospace;font-size:0.73rem}}
  .gaps{{color:#fca5a5;font-size:0.76rem;line-height:1.8}}
  .policy{{color:#7dd3fc;font-size:0.74rem;line-height:1.8}}
  .empty{{text-align:center;color:#334155;padding:1.5rem!important}}

  .badge{{display:inline-block;padding:0.2rem 0.55rem;border-radius:4px;font-size:0.65rem;
          font-weight:700;letter-spacing:0.08em;color:#fff;font-family:'JetBrains Mono',monospace}}

  footer{{text-align:center;color:#334155;font-size:0.72rem;margin-top:3rem;
          font-family:'JetBrains Mono',monospace;padding-top:1.5rem;border-top:1px solid #1e293b}}
</style>
</head>
<body>

<header>
  <div class="header-top">
    <div class="logo">🛡</div>
    <h1>M365 Conditional Access Gap Report <span class="mock-badge">SIMULATED DATA</span></h1>
  </div>
  <div class="meta">
    <span>Generated: {now}</span>
    <span>Tool: ca_gap_checker_mock.py</span>
    <span>Tenant: contoso.onmicrosoft.com</span>
    <span>Sign-ins analysed: {len(signins_with_gaps)}</span>
  </div>
</header>

<div class="stats">
  <div class="card total">
    <div class="label">Sign-ins</div>
    <div class="val">{len(signins_with_gaps)}</div>
  </div>
  <div class="card high">
    <div class="label">High Risk</div>
    <div class="val">{len(high)}</div>
  </div>
  <div class="card medium">
    <div class="label">Medium Risk</div>
    <div class="val">{len(medium)}</div>
  </div>
  <div class="card low">
    <div class="label">Secure</div>
    <div class="val">{len(low)}</div>
  </div>
  <div class="card gaps">
    <div class="label">Total Gaps</div>
    <div class="val">{total_gaps}</div>
  </div>
  <div class="card policies">
    <div class="label">Policies Needed</div>
    <div class="val">{len(set(p for s in signins_with_gaps for p in s['policies']))}</div>
  </div>
</div>

{section("High Risk — Immediate Policy Action Required", "🔴", high)}
{section("Medium Risk — Policy Gaps Detected", "🟡", medium)}
{section("Secure Sign-ins — No Gaps Detected", "🟢", low)}

<footer>
  ca_gap_checker_mock.py &nbsp;|&nbsp; AltSchool Africa Cybersecurity Portfolio &nbsp;|&nbsp;
  White-hat defensive security tool &nbsp;|&nbsp; {now}
</footer>

</body>
</html>"""


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    print("\n╔══════════════════════════════════════════╗")
    print("║  M365 Conditional Access Gap Checker v1.0 ║")
    print("║  AltSchool Cybersecurity Portfolio        ║")
    print("╚══════════════════════════════════════════╝\n")

    print("[1/3] Loading simulated M365 sign-in logs...")
    print(f"      {len(MOCK_SIGNINS)} sign-in events loaded.\n")

    print("[2/3] Analysing sign-ins for Conditional Access gaps...")
    signins_with_gaps = []
    for s in MOCK_SIGNINS:
        risk, gaps, policies = analyse_gaps(s)
        signins_with_gaps.append({
            "signin": s, "risk": risk,
            "gaps": gaps, "policies": policies
        })

    high   = [x for x in signins_with_gaps if x["risk"] == "HIGH"]
    medium = [x for x in signins_with_gaps if x["risk"] == "MEDIUM"]
    low    = [x for x in signins_with_gaps if x["risk"] == "LOW"]
    total_gaps = sum(len(x["gaps"]) for x in signins_with_gaps)

    print(f"      🔴 HIGH:         {len(high)}")
    print(f"      🟡 MEDIUM:       {len(medium)}")
    print(f"      🟢 SECURE:       {len(low)}")
    print(f"      ⚠️  Total Gaps:   {total_gaps}\n")

    print("─" * 70)
    print(" CONDITIONAL ACCESS GAPS DETECTED:")
    print("─" * 70)
    for item in high + medium:
        s = item["signin"]
        loc = s.get("location") or {}
        print(f"\n  [{item['risk']}] {s.get('userDisplayName','?')} — "
              f"{loc.get('city','?')}, {loc.get('countryOrRegion','?')}")
        print(f"         {s.get('jobTitle','?')} | {s.get('department','?')}")
        for g in item["gaps"]:
            print(f"         ⚠ {g}")
        print(f"         Recommended Policies:")
        for p in item["policies"]:
            print(f"           → {p}")
    print("─" * 70)

    print(f"\n[3/3] Generating HTML report...")
    html = generate_report(signins_with_gaps)
    out  = Path("ca_gap_report.html")
    out.write_text(html, encoding="utf-8")
    print(f"      ✓ Report saved → {out.resolve()}\n")
    print("  Open ca_gap_report.html in your browser to view the dashboard.")
    print()


if __name__ == "__main__":
    main()
