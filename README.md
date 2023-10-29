# analyst_read_data
## Ingest 5 Essential Data Sources Like a Pro using Python [The Programmatic Analyst's Handbook]

Analysts are tasked with finding meaningful insight from data in their domain.

Wrangling data from a mirade of sources and transforming it's content into meaningful information is a foundational task in providing value as an analyst.

This package provides examples on how to incorporate common types of data into Python objects which are ready for your analysis.

Data types and sources covered include:

* Structured files
* Unstructured files
* API sources
* Scraped website sources
* Cloud managed

Key Objective:

* Provide a template for analysts to extract various data sources into structured Python objects.

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

## Understanding the Package Structure

This package's goal is to provide a template for analysts to extract various data sources into structured Python objects. 

So how does the package allow analysts to work with the data we listed(structured files, unstructured files, API sources, scraped website sources, cloud data)?

The code that allows analysts to extract these data exists within the `/src` (the directory that is used to name source code by many programmers) directory's sub-directory called `read_data`.

```
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
```

Beautiful - here each type of listed data source looks to have it's own folder. Within each folder exists one or more python files and a file called `__init__.py`. If you are an analyst new to Python packaging - just know that this blank `__init__.py` file acts as a declaration that our folders should be viewed as a Python package and we want to be able to import different code/functions from the file-structure.

The later part of this overview will cover the subfolders and their functions, but let's quickly understand the other parts of this repository.

With the `/src` folder exists a `/data` folder. This is simply a folder to store structured and unstructured data files exemplified in this example.

```
│   ├───data
│   │       CPIAUCSL.csv
│   │       CPIAUCSL.xls
│   │       en_historic_events.json
│   │       text_product_data.txt
```

In your use-case, you can use the `/data` folder to store files you would like to extract and explore.

When working with modern data sources like API endpoints and Cloud service providers like Amazon/Microsoft/Google, analyst's will need credentials to authenticate their access. The `/config` folder exists as a sibling to the `/src` folder and has been hidden to avoid sharing secret information(a mandatory practice for analysts interested in learning programming). I hide this folder's information by including a `.gitignore` file where I define what files I want to be ignored when I publish code to Github. My folder's structure is shown below and contains json files that will be used to access Google Cloud Platform services and a NewsAPI in this demo.

```
├───config
│       gcp_service_account.json
│       news_api_key.json
```

The next folder which is a sibling to `/src` is the `/utils` folder.

```
└───utils
        api_utils.py
        gcp_utils.py
        __init__.py
```

This folder assists with importing our secret information and storing Python objects needed to extract data from APIs and GCP.

Finally, refer to the `demo.ipynb` Python notebook for quick and simple explanations on how to extract each data source using Python and this package's source code(which you can modify for your own needs).

```
analyst_read_data
│   .gitignore
│   demo.ipynb
```

## Extracting Common Examples of Structured Data

Common filetypes analysts must utilize include .csv, .excel, and .json files.These filetypes are consiered structured because the have a well-defined and consistent format for storing and organizing the data within them.

```
│       ├───structured
│       │       read.py
│       │       __init__.py
```

Within the `read.py` file exists functions to "get" these data as Pandas DataFrame objects.

```
import pandas as pd
import json

def get_csv_data(path, **kwargs):
    return pd.read_csv(path, **kwargs)

def get_excel_data(path, **kwargs):
    # pip install xlrd for xls files 
    return pd.read_excel(path, **kwargs)

def get_json_data(method, path, **kwargs):
...
```

Now how do analysts's leverage these functions from within the package?

### CSV Data

>example data: US Federal Reserve Consumer Price Index Data Over Time

In the `demo.ipynb` file, you can see how the functions are imported (in relation to where `demo.ipynb` exists within the package structure) and used to extract the csv data as a Pandas DataFrame object.

```
from src.read_data.structured.read import get_csv_data
cpi = get_csv_data(".\src\data\CPIAUCSL.csv")
```

### Excel Data

>example data: US Federal Reserve Consumer Price Index Data Over Time

The same process works for reading an excel file.

```
from src.read_data.structured.read import get_excel_data
cpi = get_excel_data(".\src\data\CPIAUCSL.xls")
```

With this technique, analysts are empowered to programatically load data in a programatic environment instead of a restrictive environment like Microsoft Excel.

### JSON Data

>example data: Historic Events by Date

To import JSON data. run:

```
from src.read_data.structured.read import get_json_data
history = get_json_data(method="pandas",path=".\src\data\en_historic_events.json", orient="index")
```

JSON data's key value pairs can vary based on source. In order to deal with this variability, the `get_json_data()` function (and any functions analysts need to edit) has been modified to correctly load the JSON data in an expected table format.

```
def get_json_data(method, path, **kwargs):
    if method not in ("pandas","custom"):
        raise ValueError("method must be set to either 'pandas' or 'custom'")

    if method=='pandas':
        return pd.read_json(path, **kwargs)
    
    if method == 'custom':
        # Load the JSON file
        with open(path, 'r') as file:
            data = json.load(file)

        # Extract the list of "event" objects from the JSON
        events = data['result']['events']

        # Create a Pandas DataFrame
        df = pd.DataFrame(events)

        # Select specific columns
        df = df[['date', 'description', 'lang', 'category1', 'category2', 'granularity']]

        # Display the DataFrame
        return df
```

By using the `method="custom"` argument the JSON data is loaded per requirements.

```
from src.read_data.structured.read import get_json_data
history = get_json_data(method="custom",path=".\src\data\en_historic_events.json", orient="index")
```

## Extracting Unstructured Data from Text Files

>example data: A Text Document with Product Specifications

Text files hold useful information, but do not exist in a structured format. 

Python allows practitioners to read text and apply structure to the information.

The `text.py` file exemplifies how to read text files and add structure to the example file with product information.

```
│       └───unstructured
│               text.py
│               __init__.py
```

```
ITEM 1
Binding=Electronics
Brand=Mediasonic
...

ITEM 2
Binding=Electronics
Brand=SANOXY
...
```

A common way to read text files looks like:

```
def read_text_file_lines(txt_file):
    with open(txt_file, 'r') as file:
        return file.readlines()
```

... but this does not returned a structured data output analysts can use for analysis beyond NLP.

To read the text file and and apply structure to the data, the `text.py` file includes functions specific to the product data in this example:

1. Identify all keys under lines titled "ITEM" (`get_dict_from_txt()`). 
2. Create a dictionary from the keys identified (`get_structured_dict()`).
3. Transform the dictionary to a Pandas DataFrame (`get_structured_dataframe()`).

```
from src.read_data.unstructured.text import get_dict_from_txt, get_structured_dict, get_structured_dataframe

d_unstructured, unique_keys = get_dict_from_txt(".\\src\\data\\text_product_data.txt")

d_structured = get_structured_dict(d_unstructured,unique_keys)

d_dataframe = get_structured_dataframe(d_structured)
```

## Leverage APIs to Access Data from Web Applications

>example data: News Headlines

Modern application programming interfaces (APIs) allow analysts to programmatically access structured data in a scaleable and efficient manner.

Often times, you will have to communicate with the API to ensure a secure data transfer. APIs will often require authentication which allows you to access the APIs data after providing a secret key in your request.

This package includes commonly used code allowing you to specify an API URL to access and provide specific parameters/authentication as an argument (params).

```
def get_request_data(base_url : str, params : dict):
    
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        return response.json()

    else:
        print("Failed to retrieve news data. Status code:", response.status_code)
```

The `demo.ipynb` notebook contains an example of how to access the NewsAPI to load trending news topics into a Python environment.

```
from utils.api_utils import get_api_key
from src.read_data.api.request import get_request_data

url = "https://newsapi.org/v2/top-headlines"
api_key = get_api_key(".\\config\\news_api_key.json","key")
params = {
    "country":"us",
    "apiKey":api_key
}

news_headlines = get_request_data(url, params)
news_headlines
```

Notice we are using similiar logic from our JSON section to load in a private API key from a secrets file by importing `get_api_key()` which looks like:

```
def get_api_key(path, key_name):
    # Open and read the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Extract the "key" value
    return data[key_name]
```

With this secret stored as a variable (which we extracted from the "key" key in the JSON file), it can be inserted as a parameter in the `get_request_data()` function, and a DataFrame is populated.

## Scraping Web Data when All Else Fails

>example data: A National Oceanic and Atmospheric Administration Article

Analysts are bound to encounter useful information on websites with no file format exports or APIs to provide structured and accesible data.

There is no need to move a good idea into a blocked ticket due to limited data exports. Analysts can leverage web scraping to request website DOMs (elements, metadata, text, and more on a webpage) and store the pages' information.

A building block to accessing and extracting information from web pages is to familiarize yourself with the BeautifulSoup package in tandem with the Requests package which assist in scraping web pages.

```
def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for successful request

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None
```

```
from src.read_data.scraped.beautifulsoup import scrape_website

noaa = scrape_website("https://www.climate.gov/news-features/understanding-climate/2023-24-us-winter-outlook-wetter-south-warmer-north")
noaa
```

But the `scrape_website()` function does not structure the data in a useful format.

In order to extract common elements like URL, Title, Description, Images, and Links - use the `get_website_data()` function to scrape (`scrape_website()` from above) the URL and output structured information on the page.

```
def get_website_data(url):
        
        soup = scrape_website(url)
        # Extract title, description, images, and links
        title = soup.title.string if soup.title else "N/A"
        description = soup.find('meta', attrs={'name': 'description'})
        description = description['content'] if description else "N/A"
        images = [img['src'] for img in soup.find_all('img') if img.get('src')]
        links = [a['href'] for a in soup.find_all('a') if a.get('href')]

        # Create a Pandas DataFrame
        data = {
            'URL': [url],
            'Title': [title],
            'Description': [description],
            'Images': [images],
            'Links': [links]
        }
        df = pd.DataFrame(data)

        return df
```

```
from src.read_data.scraped.beautifulsoup import get_website_data

noaa_data = get_website_data("https://www.climate.gov/news-features/understanding-climate/2023-24-us-winter-outlook-wetter-south-warmer-north")
noaa_data
```

## Interacting with Cloud Services to Access Data

Analysts interested in developing their programming skills are right to familiarize themselves with Cloud Service offerings like Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), etc.

These important and commonly buzzed about services can be thought of as giant computers which leverage APIs (which we previously covered) that allow you to perform computation (any function you do on your computer).

The services most relevant to analysts will be production-level databases provided by their business entity.

Before showing how to access cloud databases, let's take a step back and explore how to access another cloud service relevant to analysts working to ingest data for insight... Google Sheets.

### Google Sheets

>example data: Business Product Information


An earlier function explained how to load csvs and excel files into a Python DataFrame.

But how do we load a similar structured data source (Google Sheet) when it is stored on a cloud server? 

We combine the previous foundations behind the Structured and API code-base.

We will need to specify a location of our Google Sheet (similar to loading a csv from a path) and authenticate ourselves as an identity who has been granted access to that Sheet (API Authentication).

Preporatory Steps:

1. Allow editor access to your Google Service Account file's email within your Google Sheet
2. Enable Drive API from Google Cloud Platform to avoid 403 error
3. Enable Google Sheet API from Google Cloud Platform to avoid 403 error
4. Create and store a GCP Service Account JSON file in the `/config` directory

Once these steps are complete, we need to need a way to get our GCP Service Account JSON file's path from the `/config` folder.

To create this utility function that will grab the JSON path, we store a re-useable function for this process within the `/utils` folder. 

```
import os

def get_gcp_credentials_path():

    config_dir = os.path.join(os.path.dirname(__file__), "../config")
    json_path = os.path.join(config_dir, "gcp_service_account.json")

    return json_path

key_path = get_gcp_credentials_path()
```
Next we import the path to the credential file (`key_path`), and leverage the `pygsheets` Python package to access our Google Sheet.

```
from utils.gcp_utils import key_path
from src.read_data.cloud.google_sheet import get_google_sheet_data

products = get_google_sheet_data(
    method="pygsheets", 
    google_sheet_name="results-20230709-163100", 
    worksheet_name="Sheet1", 
    credential_path=key_path
    ) 
products.head()
```

### Google Cloud Platform's BigQuery Database

>example data: A Company's Web Analytics Summary Table

The final most frequented method analysts will leverage to access data is connecting to a database and ingesting its information into a DataFrame using SQL.

You will need to read your database provider's documentation, but this example shows how the package works with Google BigQuery.

The documentation notes service account credentials should be used to create a `client` object to connect to the database.

Since this seems like a re-usable utility, we write the following function under the package's `/utils` directory within the `gcp_utils.py` file (and we use the `key_path` variable from earlier).

```
from google.cloud import bigquery
from google.oauth2 import service_account

def return_client(key_path : str):
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    return bigquery.Client(credentials=credentials, project=credentials.project_id,)

client = return_client(key_path)
```

With the authenticated `client`, we import `client` and `get_bigquery_data()` to query for information.

```
from utils.gcp_utils import client
from src.read_data.cloud.gcp import get_bigquery_data

clickstream = get_bigquery_data("SELECT * FROM `{project}.{dataset}.{table}`", client)
clickstream.head()
```

Note that this can be wildly helpful for scheduling a miriade of reports and data requests in the future. Since we can reuse this `get_bigquery_data()` function with any variation of SQL we need, the power of programmatic analysis becomes apparent.