# TinyScrape – Smart Proxy Gathering CLI

---

## 🚀 Features

- **Country-Based Proxy Collection**
  - Select from a curated list of countries
  - Fetch fresh HTTP proxies from ProxyScrape
  - Save results to local proxy files

- **Interactive Terminal UI**
  - Guided menu for easy country selection
  - Clear screen flow for focused use
  - Input validation and user-friendly prompts

- **Command-Line Mode**
  - Use `-c/--country` to fetch proxies directly
  - Save output to a custom file with `-o/--output`
  - Optional non-pause display for automated workflows

- **Modular Python Architecture**
  - `app/` package with clean separation of concerns
  - `GatherProxyScraper` handles data retrieval and storage
  - `InteractiveMenu` manages terminal navigation
  - `Proxy` model for structured proxy metadata

- **Resilient Network Handling**
  - Handles request failures gracefully
  - Ensures output directory creation
  - Reports clear error messages on failure

---

## 🛠 Tech Stack

- **Core Language**
  - Python 3 — lightweight scripting and CLI logic

- **Libraries**
  - `requests` — HTTP proxy fetching
  - `argparse` — command-line parsing
  - `dataclasses` — structured proxy models

- **Architecture**
  - CLI-driven workflow
  - Interactive terminal menu
  - File persistence in `proxy/` folder

---

## 💡 Usage

- Run the interactive menu:
  ```bash
  python app.py
  ```

- Fetch proxies for a specific country directly:
  ```bash
  python app.py -c "United States"
  ```

- Save proxies to a custom output file:
  ```bash
  python app.py -c Brazil -o brazil_proxies.txt
  ```

---

## 🔮 Future Enhancements

- HTTPS and SOCKS proxy support
- Proxy validation and latency scoring
- Batch country collection and parallel fetching
- Export to CSV/JSON
- Proxy rotation and auto-refresh workflows
- Integration with proxy testing utilities

---

## ⚠️ Status

- **Active development**
- Core proxy gathering flow is implemented
- CLI and interactive experience are available
- Improvements for validation, formatting, and export are planned

## 👨‍💻 Developer

m223rx – 2026

© 2026 m223rx. All rights reserved.
