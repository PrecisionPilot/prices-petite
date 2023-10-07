import requests

SEARCH_URL = "https://price-analytics.p.rapidapi.com/search-by-term"
POLL_URL = "https://price-analytics.p.rapidapi.com/poll-job/"

payload = {
    "source": "amazon",
    "country": "CA",
    "values": "iphone 11"
}
headers = {
    "X-RapidAPI-Key": "ab1a7a6071msh3e71cf55162df28p134164jsnc9f08e68eeb3",
    "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
}

response = requests.post(SEARCH_URL, data=payload, headers=headers)
print(response.json())
jobID = response.json()["job_id"]
print(jobID)

response = requests.get(POLL_URL + jobID, headers=headers)
print(response.json())