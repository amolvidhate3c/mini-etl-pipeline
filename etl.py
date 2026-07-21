import csv
import os

INPUT_FILE = "data.csv"
OUTPUT_FILE = "processed_summary.csv"

def extract_data(filepath):
    """Extracts raw data from a CSV file."""
    print("-> Extracting data from CSV...")
    rows = []
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found!")
        return rows
        
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    print(f"Extracted {len(rows)} raw rows successfully.")
    return rows

def transform_data(rows):
    """Cleans data: removes duplicates and handles missing values."""
    print("-> Transforming and cleaning data...")
    cleaned_rows = []
    seen = set()
    
    for row in rows:
        # 1. Skip rows with missing critical values (like salary or name)
        if not row["salary"] or not row["name"]:
            continue
            
        # 2. Convert salary to integer for calculations
        try:
            row["salary"] = int(row["salary"])
        except ValueError:
            continue
            
        # 3. Remove exact duplicates (excluding unique ID if needed, or row tuple check)
        row_tuple = (row["name"], row["department"], row["salary"], row["status"])
        if row_tuple in seen:
            continue
        seen.add(row_tuple)
        
        cleaned_rows.append(row)
        
    print(f"Transformation complete. Cleaned rows count: {len(cleaned_rows)}")
    return cleaned_rows

def load_data(rows, filepath):
    """Loads/saves the processed summary data into a new file."""
    print(f"-> Loading processed data into {filepath}...")
    if not rows:
        print("No data to load.")
        return
        
    fieldnames = rows[0].keys()
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("Load phase complete successfully!")

if __name__ == "__main__":
    print("=== STARTING MINI ETL PIPELINE ===")
    
    # 1. Extract
    raw_data = extract_data(INPUT_FILE)
    
    if raw_data:
        # 2. Transform
        processed_data = transform_data(raw_data)
        
        # 3. Load
        load_data(processed_data, OUTPUT_FILE)
        
        # Quick Summary Print
        print("\n--- Pipeline Summary ---")
        total_salary = sum(row["salary"] for row in processed_data)
        avg_salary = total_salary / len(processed_data) if processed_data else 0
        print(f"Total Valid Records: {len(processed_data)}")
        print(f"Average Salary: {avg_salary:.2f}")
    
    print("=== ETL PIPELINE FINISHED ===")
