# Test Cases for Secret Scanner

## Test Case 1: Clean Repository
* **Input:** A folder containing standard code files with no hardcoded credentials.
* **Expected Result:** Script completes successfully and outputs "✅ No hardcoded secrets found. Repository looks clean!"
* **Pass/Fail:** Pass.

## Test Case 2: Hardcoded AWS Key
* **Input:** A `config.js` file containing the line `const aws_key = "AKIAIOSFODNN7EXAMPLE";`
* **Expected Result:** Script triggers an alert, flags "AWS Access Key", and prints the file path and line number.
* **Pass/Fail:** Pass.

## Test Case 3: Ignored Directories
* **Input:** A `node_modules` folder containing dummy files with text that matches the regex patterns.
* **Expected Result:** Script ignores the folder entirely and does not flag the dummy files, saving processing time.
* **Pass/Fail:** Pass.