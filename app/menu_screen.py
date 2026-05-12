from .proxy_scraper import GatherProxyScraper

import sys
import time


class InteractiveMenu:
    COUNTRIES = [
        "Albania",
        "Brazil",
        "China",
        "France",
        "Germany",
        "India",
        "Japan",
        "Russia",
        "United States",
        "United Kingdom",
    ]

    def __init__(self, country: str = "Albania") -> None:
        self.scraper = GatherProxyScraper(country)
        self.country = country

    def _display_country_menu(self) -> None:
        GatherProxyScraper.clear_screen()
        print(r"""
             ______  ____  ____   __ __  _____   __  ____    ____  ____   ___ 
            |      ||    ||    \ |  |  |/ ___/  /  ]|    \  /    ||    \ /  _]
            |      | |  | |  _  ||  |  (   \_  /  / |  D  )|  o  ||  o  )  [_ 
            |_|  |_| |  | |  |  ||  ~  |\__  |/  /  |    / |     ||   _/    _]
              |  |   |  | |  |  ||___, |/  \ /   \_ |    \ |  _  ||  | |   [_ 
              |  |   |  | |  |  ||     |\    \     ||  .  \|  |  ||  | |     |
              |__|  |____||__|__||____/  \___|\____||__|\_||__|__||__| |_____|
                                                                                                                                        
            """)
        print("=" * 80)
        print("|" + "By : m223rx".center(78) + "|")
        print("|" + "https://github.com/m223rx".center(78) + "|")
        print("=" * 80)
        print("\n  Select Country:\n")
        for i, c in enumerate(self.COUNTRIES, 1):
            print(f"    [{i:02d}] {c}")
        print("    [99] Exit")
        print()

    def run(self) -> None:
        while True:
            self._display_country_menu()
            try:
                choice = int(input("select@country~# : "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(1)
                continue

            if choice == 99:
                print("Goodbye!")
                sys.exit(0)
            elif 1 <= choice <= len(self.COUNTRIES):
                self.country = self.COUNTRIES[choice - 1]
                self.scraper = GatherProxyScraper(self.country)
                print(f"\nFetching proxies for {self.country} ...\n")
                filename = self.scraper.fetch_proxies()
                print(f"Proxies saved to {filename}")
                input("\nPress Enter to continue...")
            else:
                print("No choice")
                time.sleep(1)
