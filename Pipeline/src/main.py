from .sources.loaders import *
from .transformers.cleaner import *
from .transformers.mentions import map_drugs_to_publication_mentions
from .writer.writer import mentions_to_json


def main():
    """
    Execute the complete PubMed Pipeline workflow.

    Processes drug, clinical trials, and PubMed data to create a comprehensive
    mapping of drug mentions across all publications. The pipeline:
    
    1. Loads and processes drugs, clinical trials, and PubMed data
    2. Combines clinical trials and PubMed into a unified publications dataset
    3. Maps each drug to publications that mention it
    4. Exports the results to a JSON file
    
    Output is saved to the path specified in config.OUTPUT_FILE.
    """

    # loading and preprocessing:
    drugs = process_drugs(load_drugs())
    clinilical_trials = process_clinical_trials_dataframe(load_clinical_trials())
    pubmed = process_pubmed_dataframe(load_pubmed(), load_pubmed_json())

    # merge sources :
    publications = pd.concat([clinilical_trials, pubmed], ignore_index=True)

    #  build drugs graph  :
    mentions_dict = map_drugs_to_publication_mentions(drugs, publications)

    # save graph into json file:
    mentions_to_json(mentions_dict, config.OUTPUT_FILE)


if __name__ == '__main__':
    main()