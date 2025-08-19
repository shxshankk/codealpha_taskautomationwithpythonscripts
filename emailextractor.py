import re
import sys
import os

def extract_emails(input_file, output_file):
    """
    Extracts all unique email addresses from input_file
    and saves them into output_file.
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found.")
        return

    # Step 1: Read input file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 2: Regex to capture email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    # Step 3: Save unique emails to output file
    unique_emails = sorted(set(emails))
    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"✅ Extracted {len(unique_emails)} unique emails to '{output_file}'.")

if __name__ == "__main__":
    # Usage: python main.py input.txt emails.txt
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_emails(input_file, output_file)
