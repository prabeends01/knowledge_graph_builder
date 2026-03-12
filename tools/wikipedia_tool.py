import logging
import requests

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"


def search_wikipedia(query: str) -> str:
    """Return the introductory extract for the given Wikipedia page.

    If the request fails or the response cannot be decoded as JSON, an
    empty string is returned. This prevents callers from crashing when the
    upstream API returns HTML (e.g. rate‑limits, 5xx errors) or an empty
    body.
    """
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query,
    }

    try:
        resp = requests.get(WIKI_API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        logging.warning("Wikipedia request failed: %s", exc)
        return ""
    except ValueError as exc:  # JSON decoding error
        logging.warning("Wikipedia returned invalid JSON: %s", exc)
        return ""

    # navigate safely through the expected structure
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return ""

    page = next(iter(pages.values()))
    return page.get("extract", "")