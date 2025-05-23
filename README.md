<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="assets/logo-news.png" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# ECONEWS SUMMARY

<em></em>

<!-- BADGES -->
<!-- local repository, no metadata badges. -->

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
	- [Project Structure](#project-structure)
		- [Project Index](#project-index)
	- [Getting Started](#getting-started)
		- [Prerequisites](#prerequisites)
		- [Installation](#installation)
		- [Usage](#usage)
		- [Testing](#testing)
	- [Roadmap](#roadmap)
	- [License](#license)
	- [Acknowledgments](#acknowledgments)

---

## Overview
A Python-based economic news summarizer. This application integrates with a custom API to extract raw economic data and news from specified Telegram channels, subsequently processing and generating concise summaries.

---

## Project Structure

```sh
└── EconNewsSummary/
    ├── docker-compose.yml
    ├── frontend
    │   └── app.py
    └── services
        ├── api_gateway
        ├── summarizer
        └── telegram-collector
    
```

### Project Index

<details open>
	<summary><b><code>EconNewsSummary/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/saida.txt'>saida.txt</a></b></td>
					<td style='padding: 8px;'>- The <code>saida.txt</code> file acts as a data store within the larger project<br>- It appears to collect and aggregate textual data, specifically snippets of market news and links to relevant online resources (YouTube live streams, TradingView charts)<br>- This data is likely used elsewhere in the codebase for analysis, reporting, or display within a larger financial information application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/sessao.session'>sessao.session</a></b></td>
					<td style='padding: 8px;'>- Please provide the code file and the project structure details<br>- I need that information to create the summary.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/+5571987946284.session'>+5571987946284.session</a></b></td>
					<td style='padding: 8px;'>- Please provide the code file and the project structure<br>- I need that information to create the summary.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/teste.py'>teste.py</a></b></td>
					<td style='padding: 8px;'>- The script monitors a Telegram channel for new messages<br>- It authenticates with Telegram, retrieves messages since the last check, and processes each message<br>- Processed message data, including sender, content, and timestamps, is displayed<br>- The script updates a file to track the last processed message, ensuring efficient monitoring.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/docker-compose.yml'>docker-compose.yml</a></b></td>
					<td style='padding: 8px;'>- An API gateway, a Telegram message collector, and a summarizer<br>- The gateway acts as an entry point, relying on the collector and summarizer for data processing<br>- The configuration ensures these services run concurrently, sharing environment variables and restarting automatically upon failure.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/mensagens.json'>mensagens.json</a></b></td>
					<td style='padding: 8px;'>- The <code>mensagens.json</code> file serves as a repository of marketing and informational messages within the larger project<br>- These messages, which appear to be short promotional snippets and links to live streams and market analyses, are likely used for broadcasting updates and driving user engagement across various communication channels within the application<br>- The content suggests a focus on financial markets and trading.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/collector.ipynb'>collector.ipynb</a></b></td>
					<td style='padding: 8px;'>- The <code>collector.ipynb</code> Jupyter Notebook acts as the data acquisition component within the larger project<br>- It uses the Telethon library to connect to Telegram, retrieve historical message data from specified channels, and likely stores this data (though the storage mechanism isnt shown in the snippet)<br>- Essentially, its the core function responsible for fetching the raw data that the rest of the project (whose structure is unknown from the provided context) will process and analyze.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- frontend Submodule -->
	<details>
		<summary><b>frontend</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ frontend</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/frontend/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Localhost:8080/resumo`<br>- It displays this summary using Streamlit, providing a user interface with an update button to refresh the news<br>- Error handling is included to manage API request failures<br>- The application enhances the user experience by presenting the news in a formatted markdown style.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- api_gateway Submodule -->
	<details>
		<summary><b>api_gateway</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ api_gateway</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/api_gateway/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>- The Dockerfile configures a Python 3.11 runtime environment for the API gateway service<br>- It installs system dependencies, installs Python packages specified in requirements.txt, copies the application code, and sets environment variables<br>- Finally, it executes the main application script, <code>main.py</code>, within the container<br>- This ensures consistent and reproducible deployment of the API gateway within the larger project.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- services Submodule -->
	<details>
		<summary><b>services</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ services</b></code>
			<!-- api_gateway Submodule -->
			<details>
				<summary><b>api_gateway</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ services.api_gateway</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/api_gateway/+5571987946284.session'>+5571987946284.session</a></b></td>
							<td style='padding: 8px;'>- Please provide the code file and the project structure<br>- I need that information to create the summary.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/api_gateway/.env'>.env</a></b></td>
							<td style='padding: 8px;'>- The <code>.env</code> file configures the API gateway service by providing essential credentials<br>- It establishes connections to Telegram, specifying API details, channel, and session, and integrates with Google services via an API key<br>- These settings are crucial for the API gateways functionality, enabling communication and data exchange with external platforms.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/api_gateway/main.py'>main.py</a></b></td>
							<td style='padding: 8px;'>- The <code>main.py</code> file functions as an API gateway, orchestrating the telegram message summarization process<br>- It receives requests, triggers a message collection process using a separate telegram collector service, and then passes the collected data to a summarization service<br>- Finally, it returns the generated summary to the client, handling potential errors during each stage.</td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- telegram-collector Submodule -->
			<details>
				<summary><b>telegram-collector</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ services.telegram-collector</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/telegram-collector/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>- The <code>requirements.txt</code> file specifies dependencies for the Telegram collector service<br>- It ensures the service utilizes Telethon for Telegram interaction and python-dotenv for environment variable management<br>- Within the broader project architecture, this file facilitates the correct setup and execution of the Telegram data collection component<br>- Its role is crucial for consistent and reliable operation across different environments.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/telegram-collector/+5571987946284.session'>+5571987946284.session</a></b></td>
							<td style='padding: 8px;'>- Please provide the code file and the project structure details<br>- I need that information to create the summary.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/telegram-collector/Dockerfile'>Dockerfile</a></b></td>
							<td style='padding: 8px;'>- The Dockerfile configures a containerized Python 3.11 application, specifically the Telegram collector service<br>- It installs system dependencies, installs Python packages from requirements.txt, copies the application code, and sets environment variables<br>- Finally, it executes the <code>collector.py</code> script, enabling the service to run within a Docker container.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/telegram-collector/collector.py'>collector.py</a></b></td>
							<td style='padding: 8px;'>- The <code>collector.py</code> script retrieves all messages from a specified Telegram channel for the previous day, with a special case for Mondays<br>- It connects to the Telegram API using credentials from a <code>.env</code> file, collects text messages, and outputs them as a JSON array<br>- This service acts as a data source within a larger system, providing historical Telegram channel data for further processing or analysis.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/telegram-collector/cache-aside.py'>cache-aside.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- summarizer Submodule -->
			<details>
				<summary><b>summarizer</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ services.summarizer</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/summarizer/summary_cache.json'>summary_cache.json</a></b></td>
							<td style='padding: 8px;'>- The <code>summary_cache.json</code> file in the <code>services/summarizer</code> directory acts as a cache for previously generated summaries within the larger project<br>- It stores summaries, likely of financial market data (as indicated by the example content), indexed by date, allowing the application to quickly retrieve previously computed summaries instead of regenerating them, thus improving performance and efficiency.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/summarizer/Dockerfile'>Dockerfile</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Users/vitor/Projects/NewsSummary/blob/master/services/summarizer/summarize.py'>summarize.py</a></b></td>
							<td style='padding: 8px;'>- The <code>summarize.py</code> service generates daily summaries of financial news<br>- It leverages a large language model (LLM) via the Langchain framework to process input text, cleaning and summarizing it into a concise, topical format<br>- A caching mechanism improves efficiency by reusing summaries when available, reducing LLM calls<br>- The output is a structured summary suitable for reporting or other downstream applications.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>


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
