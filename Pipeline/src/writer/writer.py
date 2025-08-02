import json
import os


def mentions_to_json(drug_mentions: dict, output_path: str):
    # create the folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # file with writing rights
    with open(output_path, "w", encoding="utf-8") as f:
        # set the content of the json with the dictionnary
        json.dump(drug_mentions, f, indent=2, ensure_ascii=False)
