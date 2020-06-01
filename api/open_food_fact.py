import requests

payload = {"search_terms": "Nestle", "json": 1}

CATEGORIES = ["Plats préparés", "Fromages", "Desserts", "Viandes"]
for category in CATEGORIES:
    config = {
        "action": "process",
        "tagtype_0": "categories",
        "tag_0": category,
        "tag_contains_0": "contains",
        "page_size": 30,
        "json": 1,
    }


def search_api(url):
    liste = []
    for category in CATEGORIES:
        config = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_0": category,
            "tag_contains_0": "contains",
            "page_size": 10,
            "json": 1,
        }
        res = requests.get(url, params=config)
        results = res.json()
        product = results["products"]
    for products in product:
        liste.append(products["product_name"])
    return liste


if __name__ == "__main__":
    a = search_api("https://fr.openfoodfacts.org/cgi/search.pl?")
    print(a)
