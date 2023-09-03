import os

import dotenv

dotenv.load_dotenv()

ARXIV_LIMIT = 10  # the number of papers to be collected per query
NOTION_POST_URL = "https://api.notion.com/v1/pages"
NOTION_DB_ID = os.environ["NOTION_DB_ID"]
NOTION_API_KEY = os.environ["NOTION_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
VECTORSTORE_PATH = "faiss_index"
TOP_K = 3
SUMMARY_TEMPLATE = """\
Summarize the following article in the following format in Japanese: 

Format:
```
**これまでの流れ** 
-  bullet point
**この研究の貢献** 
- bullet point
```

Article:
\"\"\"
{article}
\"\"\"

Summary:
"""
