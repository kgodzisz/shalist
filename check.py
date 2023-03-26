#!/usr/bin/env python3

import os
import hashlib

# Enter the path to the directory where the files to be analyzed are located. Here is the path to the directory in the Docker container set as the default.

dir_path = "/app/results"

# List of files analysis results.
results = []

# Go through each file in the specified directory.
for filename in os.listdir(dir_path):
    filepath = os.path.join(dir_path, filename)
    
    # Ignore system directories and files.
    if os.path.isdir(filepath) or filename.startswith('.'):
        continue
        
    # Open the file in binary mode and calculate the SHA256 checksum.
    with open(filepath, "rb") as f:
        file_data = f.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
        
    # Add the results to the list.
    results.append({"filename": filename, "sha256_hash": sha256_hash})
    
# Display the results.
print("Results of files analysis:")
for result in results:
    print(f"{result['filename']}: {result['sha256_hash']}")
