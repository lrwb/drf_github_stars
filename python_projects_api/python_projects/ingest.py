"""
Ingest data at the defined API with the expected structure.
"""
# Python imports
from datetime import datetime
import json
import urllib.parse
import urllib.request

# Third party imports
import pytz

# Package imports


def get_github_python_stars(base_url):
    """
    Get the results at the url.

    Args:
        base_url (string) - The url base.
    """
    values = {"q": "language:python", "sort": "stars", "order": "desc"}

    query_params = urllib.parse.urlencode(values)

    full_req = f"{base_url}?{query_params}"

    with urllib.request.urlopen(full_req) as response:
        results = response.read()

    results_str = results.decode("utf-8")
    data = json.loads(results_str)
    data_items = data["items"]
    print(f"There are {len(data_items)} data items")

    top_results = []
    for data_item in data_items:
        item_results = {}
        item_results["repo_name"] = data_item.get("full_name")
        item_results["repo_id"] = data_item.get("id")
        item_results["url"] = data_item.get("url")
        item_results["creation_time"] = pytz.utc.localize(
            datetime.strptime(data_item.get("created_at"), "%Y-%m-%dT%H:%M:%SZ")
        )
        item_results["last_push_time"] = pytz.utc.localize(
            datetime.strptime(data_item.get("pushed_at"), "%Y-%m-%dT%H:%M:%SZ")
        )
        data_description = data_item.get("description", "")
        item_results["description"] = (
            data_description if data_description is not None else ""
        )
        item_results["stars"] = data_item.get("stargazers_count")
        top_results.append(item_results)

    return top_results
