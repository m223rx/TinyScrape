from .proxy_scraper import GatherProxyScraper
from .menu_screen import InteractiveMenu

import argparse


def cli_main() -> None:
    parser = argparse.ArgumentParser(
        description="GatherProxy Scraper – fetch fresh proxies by country"
    )
    parser.add_argument(
        "-c", "--country", default="us", help="Country name (default: United States)"
    )
    parser.add_argument(
        "-o", "--output", help="Save proxies to a file (format: ip:port)"
    )
    parser.add_argument(
        "--no-pause",
        action="store_true",
        default=False,
        help="Do not pause between displayed proxies",
    )
    args = parser.parse_args()

    scraper = GatherProxyScraper(args.country)

    if args.port:
        proxies = scraper.fetch_proxies(args.port)
        if not proxies:
            print("No proxies found.")
            return
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                for p in proxies:
                    f.write(f"{p.ip}:{p.port}\n")
            print(f"Saved {len(proxies)} proxies to {args.output}")
        else:
            GatherProxyScraper.clear_screen()
            scraper.print_proxies(proxies, pause=0.0 if args.no_pause else 0.1)
    else:
        menu = InteractiveMenu(args.country)
        menu.run()
