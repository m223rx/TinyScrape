from .print_screen import Proxy

import os
import sys
from typing import List

import requests


class GatherProxyScraper:

    BASE_URL = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country={country_code}"
    COUNTRY_CODES = {
        "Albania": "AL",
        "Brazil": "BR",
        "China": "CN",
        "France": "FR",
        "Germany": "DE",
        "India": "IN",
        "Japan": "JP",
        "Russia": "RU",
        "United States": "US",
        "United Kingdom": "UK",
    }

    def __init__(self, country: str = "United States") -> None:
        self.country = country
        self.country_code = self.COUNTRY_CODES.get(country, "US")
        self._proxies: List[Proxy] = []

    def fetch_proxies(self) -> str:
        url = self.BASE_URL.format(country_code=self.country_code)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as err:
            sys.exit(f"[!] Network error: {err}")
        
        os.makedirs("proxy", exist_ok=True)
        
        filename = f"proxy/{self.country.lower().replace(' ', '_')}.txt"
        try:
            with open(filename, "w") as f:
                f.write(response.text.strip())
        except Exception as err:
            sys.exit(f"[!] Failed to save proxy data: {err}")

        return filename

    @staticmethod
    def clear_screen() -> None:
        os.system("cls" if os.name == "nt" else "clear")
