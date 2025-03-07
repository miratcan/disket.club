import json
import logging
import urllib.request
from types import SimpleNamespace

logging.basicConfig(level=logging.DEBUG)



def load_config(file_path):
    try:
        with open(file_path, "r") as file:
            config_dict = json.load(file)
            return SimpleNamespace(**config_dict)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"The config file for reaching airtable API ({file_path}) was not found."
        )


def fetch_airtable_data(base_url, table_id, api_key):
    BASE_URL = "https://api.airtable.com/v0/"
    all_records = []
    url = f"{BASE_URL}{base_url}/{table_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    while url:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            raw = response.read().decode("utf-8")
            data = json.loads(raw)
            all_records.extend([
                data["fields"] for data in data.get("records", [])
            ])
        offset = data.get("offset", None)
        if offset:
            url = f"{url}?offset={offset}"
            continue
        url = None
    logging.info(f"Completed fetching all data. Total records: {len(all_records)}")
    return all_records


def main():
    config = load_config(".airtable.json")
    product_records = fetch_airtable_data(
        config.BASE_ID, config.PRODUCTS_TABLE_ID, config.AIRTABLE_API_KEY
    )
    with open("data/products.json", "w") as json_file:
        json.dump(product_records, json_file, indent=4)
    logging.info("Products updated successfully!")


if __name__ == "__main__":
    main()
