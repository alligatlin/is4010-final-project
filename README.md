Markdown
# Marketing Spend Analyzer

## What it does
The Marketing Spend Analyzer is a command-line interface (CLI) tool designed for marketing professionals to audit expenditure reports. It processes CSV files containing marketing expenses and generates a summary report including total expenditure and a breakdown of costs by category (e.g., Social Media, Events, Email).

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/alligatlin/is4010-final-project.git
Navigate to the project directory:

Bash
cd is4010-final-project
Install dependencies:
This project uses pytest for the automated test suite.

Bash
pip3 install -r requirements.txt
Usage
To run the analyzer, pass the path of your CSV expense file as an argument:

Bash
python3 main.py data.csv
Examples
Example 1: Standard Marketing Audit

Input (data.csv):

Code snippet
date,category,description,amount
2026-04-01,Social Media,Instagram Ads,150.00
2026-04-10,Events,Graeter's Pop-up,300.00
Run command:

Bash
python3 main.py data.csv
Expected Output:

Plaintext
--- Marketing Spend Report ---
Total Expenditure: $450.00
------------------------------
Events         : $300.00
Social Media   : $150.00
------------------------------
Example 2: Error Handling (Missing File)

If you attempt to run a file that does not exist, the program handles it gracefully:

Run command:

Bash
python3 main.py missing_file.csv
Expected Output:

Plaintext
Error: File 'missing_file.csv' not found.
Known Limitations
Currently supports .csv format only.

Input files must include headers for amount and category.