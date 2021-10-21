"""
    ███    ██ ███████ ████████ ██     ██  ██████  ██████  ██   ██ ██ ███    ██  ██████
    ████   ██ ██         ██    ██     ██ ██    ██ ██   ██ ██  ██  ██ ████   ██ ██
    ██ ██  ██ █████      ██    ██  █  ██ ██    ██ ██████  █████   ██ ██ ██  ██ ██   ███
    ██  ██ ██ ██         ██    ██ ███ ██ ██    ██ ██   ██ ██  ██  ██ ██  ██ ██ ██    ██
    ██   ████ ███████    ██     ███ ███   ██████  ██   ██ ██   ██ ██ ██   ████  ██████
"""

many_possible_topics = {
    "interacting with an api": {'urllib', 'requests'},       # <--
    "communication between processes": {'socket', 'ZeroMQ'},
    "serving an api": {'flask', 'fastapi'},
    "running a dashboard": {'plotly dash', 'streamlit'},
    "interacting with remote data": {'filesystem_spec'},     # <--
}



##
# === interacting with an api ===

# >>> start the server in the background for this to work
# super quick standard library urllib
import urllib.request

url = "http://127.0.0.1:5000/"
with urllib.request.urlopen(url) as response:
    response_text = response.read()
    print(response_text)



##
import urllib.parse

url1 = "http://127.0.0.1:5000/greeting"
params = {"name": "Andreas"}
query_string = urllib.parse.urlencode(params)
url1 = url1 + "?" + query_string

with urllib.request.urlopen(url1) as response:
    response_text = response.read()
    print(response_text)



##
# >>> pip install requests
# "Requests is an elegant and simple HTTP library for Python, built for human beings"
import requests

print(requests.get(url).text)
print(requests.get(url1, params={"name": "Peter"}).text)



##
# support for json data built in
json_endpoint = "http://127.0.0.1:5000/data.json"
dct = requests.get(json_endpoint).json()

print(dct)



##
# === introduction to filesystem_spec ===

# a common usecase data processing
import os
from pathlib import Path
import pandas as pd

def summarize_customer_data_from_csv(path: str) -> int:
    df = pd.read_csv(path)
    print(df)
    return df['C'].sum()

ROOT = Path(__file__).parent.parent
DATA = os.fspath(ROOT / "data" / "data.csv")

result = summarize_customer_data_from_csv(DATA)
print("GOT:", result)



##
# now you get an url for the newest customer data on a server
import tempfile

DATA_URL = "http://127.0.0.1:5000/data.csv"

with tempfile.NamedTemporaryFile(mode="wb") as f:
    response = requests.get(DATA_URL)
    f.write(response.content)
    f.seek(0)
    result = summarize_customer_data_from_csv(f.name)
    print(result)



##
# we moved all data to the cloud. Here's a s3 bucket

...  # need to look into boto3 and implement...



##
# now better with fsspec
# > [filesystem_spec] defines a standard interface that [logical] file-systems should adhere to,
# > such that code using them should not have to know the details of the implementation in order
# > to operate on any of a number of backends.
import fsspec

def summarize_customer_data_from_csv_fsspec(urlpath: str) -> int:
    with fsspec.open(urlpath, mode="rb") as f:
        df = pd.read_csv(f)
    print(df)
    return df['C'].sum()


print(summarize_customer_data_from_csv_fsspec(DATA))


##
# also works with a ton of remote paths

print(summarize_customer_data_from_csv_fsspec(DATA_URL))

DATA_LOCAL = "./data/data.csv"
DATA_S3 = "s3://mybucket/data.csv"
DATA_FTP = "ftp://server/data.csv"
DATA_HTTP = "http://somewhere.com/data.csv"
DATA_GCP = "gcs://mybucket/data.csv"

# full list:
# https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations



##
# a good indicator why you should start using this:

# the big datascience projects use it:
__projects_with_fsspec_support__ = {
    "dask", "pandas", "xarray", ...
}



##
# support for chaining filesystems

DATA_URL_ZIPPED = "http://127.0.0.1:5000/data.csv.zip"
NEW_URLPATH = "zip://data.csv::http://127.0.0.1:5000/data.csv.zip"

print(summarize_customer_data_from_csv_fsspec(NEW_URLPATH))

# fsppec.open_files('zip://subfolder/*.csv::s3://somebucket/data.zip')



##
# native support caching filesystems

NEW_URLPATH_CACHED_0 = "zip://data.csv::simplecache::http://127.0.0.1:5000/data.csv.zip"
print(summarize_customer_data_from_csv_fsspec(NEW_URLPATH_CACHED_0))

NEW_URLPATH_CACHED_1 = "simplecache::zip://data.csv::http://127.0.0.1:5000/data.csv.zip"
print(summarize_customer_data_from_csv_fsspec(NEW_URLPATH_CACHED_1))

#
of = fsspec.open(
    "zip://data.csv::filecache::http://127.0.0.1:5000/data.csv.zip",
    http={},
    filecache={'cache_storage': '/tmp/files'},
)
print(of)
print(list(Path('/tmp/files').glob("**/*")))



##
# === NETWORKING TAKE HOME MESSAGE ===

import requests  # <-- just use this instead of urllib
requests.get(...).json()
requests.post(...)

# Start writing your scripts that might run in the cloud with fsspec
# >>> https://filesystem-spec.readthedocs.io/

import pandas as pd

DATA_LOCAL = "./data/data.csv"
DATA_S3 = "s3://mybucket/data.csv"

with fsspec.open(DATA_LOCAL) as f:
    df = pd.read_csv(f, sep='|', header=None)
