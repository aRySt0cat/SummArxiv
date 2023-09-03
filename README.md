# SummArxiv
This is an app that searches for papers on ArXiv using a query, summarizes their abstracts using ChatGPT, and saves them to Notion.

<img width="1802" alt="example" src="https://github.com/aRySt0cat/SummArxiv/assets/55921454/ac774d4e-0af6-4c52-b0b8-80f3755ddc6c">

## Usage
### poetry
Please execute the following commands in the project's root directory.
```sh
poetry install
poetry run python main.py
```

## Settings
You'll need the following files:

- `query.yaml`: Describes the search queries for ArXiv. A sample is included in this repository. Please modify the content for your use.
- `.env`: Add your NOTION_API_KEY, NOTION_DATABASE_ID, and OPENAI_API_KEY.  

For other settings, please refer to `settings.py`.
