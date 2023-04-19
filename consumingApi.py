import requests

# Make a GET request to the API endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if the request was successful (200 status code)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the first item in the response
    print(data[0])
else:
    print("Error: Could not retrieve data from API.")