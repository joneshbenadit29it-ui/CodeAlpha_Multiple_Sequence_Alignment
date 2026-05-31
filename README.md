🧬 CodeAlpha: Multiple Sequence Alignment (MSA) 

Welcome to my submission for **Task 13: Multiple Sequence Alignment** as part of my Bioinformatics Internship at **@CodeAlpha**! This project automates the retrieval of protein sequences from biological databases and analyzes evolutionary conservation patterns across species.

---

## 📌 Project Overview
This repository contains a fully automated Python pipeline that connects directly to the **NCBI Entrez** database to extract genetic datasets, submits them dynamically to the **EMBL-EBI Clustal Omega API**, and performs multiple sequence alignments to isolate and track conserved biological motifs.

### 🧪 Target Protein: Insulin
Insulin was selected as the reference protein family due to its critical functional role across vertebrate species. We analyze its molecular structure across five distinct organisms:
*   👤 **Human** (*Homo sapiens*)
*   🐭 **Mouse** (*Mus musculus*)
*   🐀 **Rat** (*Rattus norvegicus*)
*   🐂 **Bovine** (*Bos taurus*)
*   🐟 **Zebrafish** (*Danio rerio*)

---

## ⚙️ Features
*   🖥️ **Automated Data Retrieval:** Uses Biopython to pull real-time structural sequence inputs directly from NCBI using accession numbers.
*   ☁️ **Cloud-Based Alignment Computation:** Dynamically hands off high-throughput compute sequences to the EMBL-EBI REST API cluster.
*   📊 **Clean Output Generation:** Downloads and saves standard formatting profiles (`.fasta` and `.clustal`) locally for research tracking.
*   🔍 **Motif Highlight Analysis:** Identifies highly preserved functional domains (such as essential disulfide bonds).

---

## 📁 Repository Structure
```text
📂 CodeAlpha_Multiple_Sequence_Alignment/
│
├── 📄 msa_task.py             # 🐍 Main Python execution pipeline script
├── 📄 insulin_sequences.fasta # 🧬 Downloaded raw multi-FASTA file from NCBI
├── 📄 insulin_alignment.clustal# 📊 Final ClustalW multiple alignment results
└── 📄 README.md               # 📖 Beautiful project documentation
🚀 Getting Started & Execution
1️⃣ Installation
Ensure you have Python installed, then run the terminal setup block to download the required biological communication libraries:

Bash
pip install biopython requests
2️⃣ Run the Pipeline
Execute the alignment engine inside your terminal using:

Bash
python msa_task.py
📊 Alignment Results & Interpretation Breakdown
Organism	Common Name	Protein Accession ID	Evolutionary Identity
Homo sapiens	Human	P01308	Reference Base (100%)
Mus musculus	Mouse	P01325	Highly Conserved (>90%)
Rattus norvegicus	Rat	P01322	Highly Conserved (>90%)
Bos taurus	Bovine	P01317	Highly Conserved (>85%)
Danio rerio	Zebrafish	O73727	Distant Match (Conserved Core)
🔍 Motif & Symbol Breakdown Guide
When inspecting your generated insulin_alignment.clustal file output, use the following key to map sequence conservation:

🌟 Asterisk (*) -> Fully Conserved Residue. Critical functional zones that haven't mutated across hundreds of millions of years of divergence.

💎 Colon (:) -> Strongly similar functional structural property substitutions.

🔹 Period (.) -> Weakly similar physical property mutations.

⚠️ Dash (-) -> Evolutionary gaps/insertions across phylogenetic branches.

📢 Internship Requirements Checklist
[x] Share internship status update on LinkedIn tagging @CodeAlpha.

[x] Complete Assigned MSA Coding project task goals.

[x] Build and upload repository contents directly to GitHub workspace.

[ ] Record and attach required project video walkthrough evaluation link.

✨ Developed as part of the CodeAlpha Bioinformatics Virtual Internship track.
