import os
import re
import argparse

# Define regex patterns for common secrets
SECRET_PATTERNS = {
    "AWS Access Key": r"(?i)AKIA[0-9A-Z]{16}",
    "Generic API Key / Token": r"(?i)(?:api_key|secret|token|password)[^\n]{0,10}['\"]([a-zA-Z0-9\-_]{32,})['\"]",
    "RSA Private Key": r"-----BEGIN RSA PRIVATE KEY-----"
}

# Folders to skip during the scan to avoid massive outputs
IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__'}

def scan_file(filepath):
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, start=1):
                for secret_type, pattern in SECRET_PATTERNS.items():
                    if re.search(pattern, line):
                        findings.append((line_num, secret_type, line.strip()))
    except Exception:
        pass # Skip files that can't be read as text (like images/compiled binaries)
    return findings

def scan_directory(directory):
    print(f"Starting scan in: {directory}...\n" + "="*40)
    found_secrets = False

    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to skip ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            filepath = os.path.join(root, file)
            results = scan_file(filepath)
            
            if results:
                found_secrets = True
                print(f"🚨 ALERT in {filepath}:")
                for line_num, secret_type, snippet in results:
                    print(f"  Line {line_num}: [{secret_type}] -> {snippet[:60]}...")
                print("-" * 40)

    if not found_secrets:
        print("✅ No hardcoded secrets found. Repository looks clean!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple defensive tool to scan for hardcoded secrets.")
    parser.add_argument("path", help="Path to the directory to scan")
    args = parser.parse_args()
    
    if os.path.isdir(args.path):
        scan_directory(args.path)
    else:
        print("Invalid directory path provided.")