import time
import os
import subprocess

TARGET_FILE = "data.csv"
SCRIPT_TO_RUN = "etl.py"

def watch_file():
    print(f"[*] Watching '{TARGET_FILE}' for real-time changes...")
    print("[*] Press Ctrl+C to stop the trigger service.\n")
    
    # Get the initial modification time of the file
    if not os.path.exists(TARGET_FILE):
        print(f"Error: {TARGET_FILE} does not exist.")
        return
        
    last_mtime = os.path.getmtime(TARGET_FILE)
    
    try:
        while True:
            # Check file modification time every 1 second
            current_mtime = os.path.getmtime(TARGET_FILE)
            
            if current_mtime != last_mtime:
                print(f"\n[!] Change detected in {TARGET_FILE}! Triggering ETL Pipeline...")
                
                # Run the etl.py script automatically
                result = subprocess.run(["python3", SCRIPT_TO_RUN], capture_output=True, text=True)
                print(result.stdout)
                
                if result.stderr:
                    print("Errors:", result.stderr)
                    
                print("-" * 40)
                print("[*] Resuming watch... waiting for next update.")
                
                last_mtime = current_mtime
                
            time.sleep(1) # Wait for 1 second before checking again
            
    except KeyboardInterrupt:
        print("\n[*] File watcher stopped by user.")

if __name__ == "__main__":
    watch_file()
