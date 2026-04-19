import csv
import argparse
import sys

def calculate_stats(rows):
    """Processes rows to find total and category totals."""
    total = 0
    categories = {}
    for row in rows:
        # Convert string amount to float for math
        amount = float(row.get('amount', 0))
        total += amount
        cat = row.get('category', 'Uncategorized')
        categories[cat] = categories.get(cat, 0) + amount
    return total, categories

def main():
    parser = argparse.ArgumentParser(description="Marketing Spend Analyzer")
    parser.add_argument("filename", help="Path to the expenses CSV")
    args = parser.parse_args()

    try:
        with open(args.filename, mode='r', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))
            if not reader:
                print("Error: The CSV file is empty.")
                return

            total, categories = calculate_stats(reader)
            
            print(f"\n--- Marketing Spend Report ---")
            print(f"Total Expenditure: ${total:.2f}")
            print("-" * 30)
            for cat, amt in categories.items():
                print(f"{cat:15}: ${amt:>8.2f}")
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()