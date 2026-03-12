import logging
import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")
if not SERP_API_KEY:
    logging.warning("SERP_API_KEY is not set; Google search will return empty results.")


def search_google(query: str) -> list:
    """Perform a SerpAPI Google search and return organic results.

    If the request fails or returns invalid JSON, an empty list is returned
    so that callers can continue operating.
    """
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        logging.warning("SerpAPI request failed: %s", exc)
        return []
    except ValueError as exc:
        logging.warning("SerpAPI returned invalid JSON: %s", exc)
        return []

    return data.get("organic_results", [])