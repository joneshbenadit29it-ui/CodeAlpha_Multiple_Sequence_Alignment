import time
import requests
from Bio import Entrez

# --- Configuration ---
# NCBI and EMBL-EBI APIs require a valid email address to monitor usage and prevent spam.
USER_EMAIL = "joneshbenadit@gmail.com" 

Entrez.email = USER_EMAIL

# 5 Protein Accession IDs for Insulin from different organisms
protein_ids = ["P01308", "P01325", "P01322", "P01317", "O73727"]
fasta_file = "insulin_sequences.fasta"
alignment_file = "insulin_alignment.clustal"

# =====================================================================
# Step 1: Fetching Sequences from NCBI
# =====================================================================
print("Step 1: Fetching 5 protein sequences from NCBI...")
try:
    handle = Entrez.efetch(db="protein", id=",".join(protein_ids), rettype="fasta", retmode="text")
    fasta_data = handle.read()
    handle.close()
    
    with open(fasta_file, "w") as f:
        f.write(fasta_data)
    print(f"-> Successfully saved sequences to {fasta_file}\n")
except Exception as e:
    print(f"Error fetching data from NCBI: {e}")
    exit()

# =====================================================================
# Step 2: Submitting Job to Clustal Omega API
# =====================================================================
print("Step 2: Submitting sequences to Clustal Omega API...")
submit_url = "https://www.ebi.ac.uk/Tools/services/rest/clustalo/run"
payload = {
    'email': USER_EMAIL,
    'title': 'Insulin_MSA_Task',
    'sequence': fasta_data
}

try:
    response = requests.post(submit_url, data=payload)
    if response.status_code != 200:
        print(f"❌ Failed to submit job to Clustal Omega. Status Code: {response.status_code}")
        print(f"Server Response Details: {response.text}")
        exit()

    job_id = response.text.strip()
    print(f"-> Job submitted successfully! Job ID: {job_id}\n")
except Exception as e:
    print(f"An error occurred during API submission: {e}")
    exit()

# =====================================================================
# Step 3: Polling Server for Status
# =====================================================================
print("Step 3: Waiting for alignment to complete...")
status_url = f"https://www.ebi.ac.uk/Tools/services/rest/clustalo/status/{job_id}"

while True:
    try:
        status_resp = requests.get(status_url)
        status = status_resp.text.strip()
        print(f"-> Current Job Status: {status}")
        
        if status == "FINISHED":
            print("-> Alignment task complete!")
            break
        elif status in ["RUNNING", "PENDING"]:
            time.sleep(5)
        else:
            print(f"❌ Job stopped with status: {status}")
            exit()
    except Exception as e:
        print(f"Error checking status: {e}")
        time.sleep(5)

# =====================================================================
# Step 4: Downloading & Saving Results (FIXED ENDPOINT)
# =====================================================================
print("\nStep 4: Downloading alignment results...")
# Changed from 'aln-clustal' to 'clustalw' to prevent the 400 Bad