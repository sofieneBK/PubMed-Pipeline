# Drug Mention Graph Builder

This project provides a data pipeline to identify mentions of drugs in scientific literature and clinical trials. It processes data from various sources, cleans and standardizes the information, and generates a JSON-based graph that links drugs to the publications where they are mentioned.

## ✨ Features

- **Multi-Source Ingestion**: Processes data from CSV and JSON files, including PubMed articles and clinical trial records.
- **Data Cleaning**: Normalizes drug names, publication titles, and dates to a consistent format.
- **Mention Linking**: Identifies drug mentions within publication titles based on a predefined list of drugs.
- **Graph Generation**: Outputs a structured JSON file representing the network of drug mentions, including the source, journal, and date of each mention.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.8+

### Installation & Setup

1.  **Navigate to the Pipeline directory:**
    ```bash
    cd Pipeline
    ```

2.  **Create and activate a virtual environment:**

    *   On **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On **Windows**:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    > You’ll know the environment is activated when you see `(venv)` in your terminal prompt.

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run

To execute the entire data pipeline, run the main script from the `Pipeline` directory:

```bash
python -m src.main
```

The script will process the input files and generate the output graph in the `output/` directory.

To disable the virtual environment : 

```bash
deactivate
```

## 📂 Project Structure

The project is organized as follows:

```
Pipeline/
├── data/
│   ├── clinical_trials.csv
│   ├── drugs.csv
│   ├── pubmed.csv
│   └── pubmed.json
├── output/
│   └── drug_mentions_graph.json
├── src/
│   ├── config/
│   │   └── config.py
│   ├── sources/
│   │   └── loaders.py
│   ├── transformers/
│   │   ├── cleaner.py
│   │   └── mentions.py
│   ├── utils/
│   │   └── utils.py
│   ├── writer/
│   │    └── writer.py
│   └── main.py
├── test/
│   └── test.py
├── requirements.txt
└── README.md
```

## ⚙️ Data Pipeline Explained

### 1. Input Data

The pipeline ingests data from the following files located in the `data/` directory:
- `drugs.csv`: A list of drugs to be identified.
- `pubmed.csv` & `pubmed.json`: Scientific publication records.
- `clinical_trials.csv`: Clinical trial information.

### 2. Processing and Cleaning

The raw data undergoes several cleaning steps:
- **Date Normalization**: Dates are standardized to a consistent `YYYY-MM-DD` format.
- **Text Standardization**: Titles and journal names are converted to lowercase, and special characters or accents are removed.
- **Deduplication**: Duplicate entries are handled to ensure data integrity.

### 3. Mention Identification

- A **drug** is considered "mentioned" if its name appears as a whole word in the title of a publication or clinical trial.
- A **journal** is linked to a drug if it has published an article that mentions the drug.

### 4. Output Format

The final output is a single JSON file (`output/drug_mentions_graph.json`) that represents the graph of drug mentions.

**Example Snippet:**
```json
{
  "aspirin": [
    {
      "source": "pubmed",
      "journal": "the lancet",
      "date": "2020-05-03",
      "title": "aspirin reduces heart attack"
    },
    {
      "source": "clinical_trials",
      "journal": "nejm",
      "date": "2019-11-10",
      "title": "clinical effect of aspirin in stroke"
    }
  ]
}
```