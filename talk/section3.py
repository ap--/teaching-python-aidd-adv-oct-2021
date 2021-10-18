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
# === NETWORKING TAKE HOME MESSAGE ===

import requests  # <-- just use this instead of urllib
requests.get(...).json()
requests.post(...)


# Start writing your scripts that might run in the cloud with fsspec
# >>> https://filesystem-spec.readthedocs.io/

import pandas as pd
with fs.open('./data/.csv') as f:
    df = pd.read_csv(f, sep='|', header=None)

with fs.open(''):
    pass
