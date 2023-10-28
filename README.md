# analyst_read_data
## Extract the 5 Most Common Data Sources Like a Pro using Python [The Programmatic Analyst's Handbook]

Analysts are tasked with finding meaningful insight from data in their domain.

Wrangling data from a mirade of sources and transforming it's content into meaningful information is a foundational task in providing value as an analyst.

This package provides examples on how to incorporate common types of data into Python objects ready for analysis.

Data types and sources covered include:

* Structured files
* Unstructured files
* API sourced
* Scraped website sourced
* Cloud managed

Key Objective:

* Provide a template for analysts to read various data sources into structured Python objects.

Key Benefits:

* Time-saving and re-producible functions to incorporate data into Python objects.
* Introduce a foundation to programatically extract data for meaningful reporting and automation.

Secondary Benfits:

* Introduce Python package management to analysts hoping to grow their programming expertise.
* Display a simple, working Python package that analyst's can understand and modify for their own needs.

The Package Structure at a Glance:
```
analyst_read_data
│   .gitignore
│   demo.ipynb
│
├───config
│       gcp_service_account.json
│       news_api_key.json
│
├───src
│   ├───data
│   │       CPIAUCSL.csv
│   │       CPIAUCSL.xls
│   │       en_historic_events.json
│   │       text_product_data.txt
│   │
│   └───read_data
│       │   __init__.py
│       │
│       ├───api
│       │       request.py
│       │       __init__.py
│       │
│       ├───cloud
│       │       aws.py
│       │       azure.py
│       │       gcp.py
│       │       google_sheet.py
│       │       __init__.py
│       │
│       ├───scraped
│       │       beautifulsoup.py
│       │       scrapy.py
│       │       __init__.py
│       │
│       ├───structured
│       │       read.py
│       │       __init__.py
│       │
│       └───unstructured
│               text.py
│               __init__.py
│
└───utils
        api_utils.py
        gcp_utils.py
        __init__.py
```