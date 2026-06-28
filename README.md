# M365 Conditional Access Gap Checker

A white-hat Python security tool that analyses Microsoft 365 sign-in 
logs and detects gaps in Conditional Access policies — logins that 
bypassed security controls and should have been blocked.

## What It Detects
- MFA not enforced on sign-in
- Logins from high-risk countries (RU, CN, KP, IR)
- Non-compliant or unmanaged devices allowed
- Sign-ins outside business hours (07:00–20:00 UTC)
- Suspicious automated clients (python-requests, curl)
- Guest users accessing resources without MFA
- High/Medium risk sign-ins not blocked by Identity Protection

## Risk Scoring
| Level | Triggers |
|-------|----------|
| HIGH | 3+ policy gaps |
| MEDIUM | 1–2 policy gaps |
| LOW | No gaps detected |

## Policy Recommendations Generated
| Gap | Recommended CA Policy |
|-----|----------------------|
| No MFA | Require MFA for All Users |
| Risky country | Block high-risk country sign-ins |
| Non-compliant device | Require compliant device |
| After-hours access | Restrict to business hours |
| Suspicious client | Block legacy/automated clients |
| Guest no MFA | Require MFA for guests |
| High risk sign-in | Enable Identity Protection auto-block |

## Tools Used
- Python 3.12
- Microsoft Graph API (architecture)
- HTML/CSS Dashboard

## Project Context
Built as part of AltSchool Africa Cybersecurity programme.
Covers: Conditional Access, Zero Trust Architecture, Identity Security.
