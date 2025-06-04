<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="assets/logo-news.png" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# ECONEWS SUMMARY


<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [ECONEWS SUMMARY](#econews-summary)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [ToDo](#todo)
  - [Project Structure](#project-structure)
  - [Roadmap](#roadmap)
  - [License](#license)

---

## Overview
A Python-based economic news summarizer. This application integrates with a custom API to extract raw economic data and news from specified Telegram channels, subsequently processing and generating concise summaries.

---

## ToDo
- Acrescentar RSS de sites
- Acrescentar dados do PIB, IPCA, Emprego, Taxa de Juros

**Fontes:**
- https://www.cmegroup.com/pt/markets/interest-rates/cme-fedwatch-tool.html
- Curvas de juros
- Variação do Dólar
- Renda Fixa na Prática
- MoneyDrop

## Project Structure

```sh
└── EconNewsSummary/
    ├── LICENSE
    ├── README.md
    ├── assets
    │   └── logo-news.png
    ├── docker-compose.yml
    ├── frontend
    │   └── app.py
    ├── mensagens.json
    ├── requirements.txt
    ├── services
    │   ├── api_gateway
    │   ├── summarizer
    │   └── telegram-collector
    └── tests
        ├── collector.ipynb
        └── teste.py
    
```

---

## Roadmap

- [ ] **`Task 1`**: Add an API to send the summary to Discord channel.
- [ ] **`Task 2`**: Add new feeds of news.


---

## License

Newssummary is protected under the [APACHE LICENSE 2.0](http://www.apache.org/licenses/LICENSE-2.0) License.

<div align="right">

[![][back-to-top]](#top)

</div>

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
