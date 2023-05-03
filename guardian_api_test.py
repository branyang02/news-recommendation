import requests
import json

api_key = '9b098f62-24d1-40c3-991b-2604cc98d4c1'
base_url = 'https://content.guardianapis.com/search'

# Define query parameters
params = {
    'api-key': api_key,
    'q': 'technology',  # search keyword
    'page-size': 10,  # number of results per page
    'show-fields': 'headline,body'  # fields to be returned
}

# Make the API request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    results = data['response']['results']

    # Print the articles
    for index, article in enumerate(results, start=1):
        print(f"{index}. {article['webTitle']}")
        print(f"URL: {article['webUrl']}")
        print(f"Headline: {article['fields']['headline']}")
        print(f"Content: {article['fields']['body'][:200]}...")  # Display only the first 200 characters
        print('\n')

else:
    print(f"Error: {response.status_code} - {response.reason}")
