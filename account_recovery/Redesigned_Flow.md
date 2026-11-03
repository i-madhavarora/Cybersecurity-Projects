# Redesigned Account Recovery Flow

## Overview
To mitigate the risks of Account Takeover (ATO) while maintaining usability for legitimate users, the recovery process has been redesigned to eliminate Date of Birth (DOB) as a primary authenticator[cite: 6]. The new flow prioritizes a secure self-service model, reserving customer support for verified escalations.

## Phase 1: Automated Self-Service Recovery (Standard Path)
This path handles 90% of legitimate recovery requests without requiring human intervention, ensuring quick and secure access.

1. **Initiation:** The user requests a password reset by entering their registered email address.
2. **Out-of-Band (OOB) Link:** A time-bound (15-minute expiry) secure "Magic Link" or One-Time Password (OTP) is sent to the registered email. 
3. **Secondary Factor Verification:** Upon clicking the link, the user must provide a secondary verification factor established during account creation. Options include:
   * SMS OTP sent to the registered mobile number.
   * Time-based One-Time Password (TOTP) from an authenticator app.
   * Push notification to a trusted device where the user is currently logged in.

## Phase 2: Secure Assisted Recovery (Fallback Path)
If a user loses access to their secondary factor (e.g., lost phone), the request is routed to customer support with strict procedural safeguards.

1. **Contextual Identity Verification:** Instead of public PII like DOB, agents ask contextual questions that only the true account owner would know:
   * "What was the title of the last course you completed?"
   * "What are the last four digits of the credit card used for your recent subscription?"
   * "What month and year was this account created?"
2. **Mandatory Cooling-Off Period:** Once identity is contextually verified by the agent, the account is not reset immediately. A 24-hour hold is placed on the reset action.
3. **Active Notification:** During the 24-hour hold, automated alerts are sent to the user's original email and phone number stating: *"An account recovery process has been initiated. If this was not you, click here to cancel the request and lock down your account."*
4. **Execution:** If no cancellation occurs within 24 hours, the secure reset link is issued.

## Usability and Security Balance
* **Usability:** The automated flow provides instant access for the vast majority of users without making them wait in a support queue. 
* **Security:** The fallback path prevents social engineering by shifting from static, public data (DOB) to dynamic, contextual data, while the 24-hour delay completely neutralizes the urgency tactics typically used by attackers.