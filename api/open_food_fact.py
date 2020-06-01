import requests

payload = {"search_terms": "Nestle", "json": 1}


def search_api(url, payload):
    liste = []
    res = requests.get(url, params=payload)
    results = res.json()
    product = results["products"]
    for products in product:
        liste.append(products["product_name"])
    return liste


if __name__ == "__main__":
    payload = {"search_terms": "Nestle", "json": 1}
    a = search_api("https://fr.openfoodfacts.org/cgi/search.pl?", payload)
    print(a)
