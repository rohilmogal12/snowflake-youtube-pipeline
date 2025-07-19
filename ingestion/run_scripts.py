import subprocess

# Paths to the two scripts you want to run
script1 = "ingestion/script_1_fetch_and_load_youtube.py"
script2 = "ingestion/script_2_transform_enrich.py"


# Run the first script
print(f"Running {script1}...")
subprocess.run(["python", script1], check=True)

# Run the second script
print(f"Running {script2}...")
subprocess.run(["python", script2], check=True)

print("Both scripts ran successfully.")
