# 🥷🏻🧑🏻‍💻 Cybersecurity-Projects

## EduRankAI Cybersecurity Assessment

This repository contains my submissions for the EduRankAI Cybersecurity Internship Assessment. I have selected and completed Task 13 and Task 15 from the Assessment Task Catalogue, focusing on practical defensive tooling and secure identity management.

Repository Structure

Cybersecurity_assessment/
│
├── README.md
│
├── defensive_tool/                  # Task 13: Build a Small Defensive Security Tool
│   ├── scanner.py                   # Python script for local secret scanning
│   ├── test_cases.md                # Documented test cases and expected outcomes
│   ├── sample_output.txt            # Real execution output from a test scan
│   └── README.md                    # Setup and execution instructions
│
└── account_recovery/                # Task 15: Account Recovery: The Weakest Link
    ├── Risk_Analysis.md             # Security flaw assessment of the existing DOB/Email flow
    └── Redesigned_Flow.md           # Proposed secure, user-friendly recovery architecture


## Task Summaries

### Task 13: Build a Small Defensive Security Tool (Local Secret Scanner)

Objective: Create a practical tool to solve a benign security problem.
Solution: I built a Local Repository Secret Scanner in Python (scanner.py). The script recursively scans project directories and uses Regular Expressions to detect accidentally hardcoded secrets (such as AWS Access Keys, RSA Private Keys, and generic API tokens) before they are committed to version control. It is designed to ignore standard build directories (like node_modules or .git) to optimize performance and reduce false positives.

### Task 15: Account Recovery: The Weakest Link

Objective: Assess an insecure account recovery process and design a safer alternative.
Solution: I conducted a threat modeling exercise on the existing knowledge-based authentication (KBA) flow that relied on easily accessible public data (Date of Birth). To fix this, I designed a two-phase recovery architecture:

Automated Self-Service: Utilizing out-of-band (OOB) authentication (Magic Links) and secondary factors (TOTP/SMS).

Secure Assisted Recovery: A fallback path utilizing contextual identity verification combined with a mandatory 24-hour cooling-off period to thwart social engineering attempts.

## Evaluation Notes

All deliverables, including working code, test cases, and theoretical documentation, are fully contained within this repository. The scanner.py tool requires no external dependencies and runs on standard Python 3.x.
