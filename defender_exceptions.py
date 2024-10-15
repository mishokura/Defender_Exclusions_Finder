import os
import subprocess
import concurrent.futures

# list directories up to a specific depth
def list_directories_to_depth(path, depth):
    directories = []
    for root, dirs, files in os.walk(path):
        current_depth = root[len(path):].count(os.sep)
        
        if current_depth < depth:
            for directory in dirs:
                full_path = os.path.join(root, directory)
                directories.append(full_path)
        else:
            dirs[:] = []

    return directories

# Defender scan for a specific directory
def run_defender_scan(directory):
    command = f'"C:\\Program Files\\Windows Defender\\MpCmdRun.exe" -Scan -ScanType 3 -File "{directory}\\|*"'
    result = subprocess.run(command, capture_output=True, text=True)
    
    if "skipped" in result.stdout:
        print(f'{directory} is a Defender Exclusion Directory.')
        return directory  # if "skipped" is detected from output it means the folder is exluded.
    return None

def main():
    path = "C:\\"
    depth = 3
    stop_on_first = True
    directories = list_directories_to_depth(path, depth)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(run_defender_scan, d): d for d in directories}
        for future in concurrent.futures.as_completed(futures):
            exclusion_dir = future.result()
            if exclusion_dir:
                print(f"Defender Exclusion Directory found: {exclusion_dir}")
                if stop_on_first:
                    break  # Stop scanning on first directory that is found

if __name__ == "__main__":
    main()
