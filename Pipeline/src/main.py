from .sources.loaders import *
from .transformers.cleaner import *
from .transformers.mentions import map_drugs_to_publication_mentions
from .writer.writer import mentions_to_json


def main():

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