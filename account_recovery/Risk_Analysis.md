# Risk Analysis: Account Recovery Vulnerabilities

## Current Workflow Assessment
The existing account recovery process relies solely on verifying a user's Date of Birth (DOB) and registered email address via customer support. This represents a critical vulnerability in the identity verification pipeline, prioritizing basic usability over standard security practices.

## Identified Security Risks

* **Easily Attainable PII (Open Source Intelligence):** A Date of Birth is not a secret; it is publicly discoverable data. Attackers can easily scrape this information from social media profiles, public records, or previous data breaches.
* **Email Spoofing and Compromise:** If an attacker has already compromised the user's email account, they effectively own the recovery process. Furthermore, bad actors can spoof sender addresses to trick customer support agents into processing a reset without actually logging into the registered email.
* **Susceptibility to Social Engineering:** Customer support agents are prime targets for social engineering. An attacker armed with the user's email and DOB can impersonate the victim over a phone call or live chat, manufacturing a sense of urgency to bypass further scrutiny.
* **Lack of Out-of-Band (OOB) Authentication:** The current model fails to verify possession of a trusted device or secondary channel. It relies purely on "knowledge-based authentication" (KBA), which is widely considered deprecated by modern security frameworks.

## Threat Modeling Matrix

| Threat Vector | Likelihood | Business Impact | Vulnerability Source |
| :--- | :--- | :--- | :--- |
| **Targeted Account Takeover (ATO)** | High | Severe | Publicly accessible DOB |
| **Social Engineering of Support Staff** | High | High | Over-reliance on human verification |
| **Unauthorized Data Access** | High | Severe | Lack of secondary verification factors |

## Conclusion on Current State
Using DOB and an email address as the sole gates for account recovery makes the platform highly vulnerable to Account Takeover (ATO) attacks. These verification factors act as public identifiers rather than secure authenticators, breaking the core principle of verifying identity through something the user *owns* or uniquely *knows*.