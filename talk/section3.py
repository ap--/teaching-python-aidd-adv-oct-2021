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


