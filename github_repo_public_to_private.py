#!/usr/bin/env python
# coding: utf-8

# # Change Public Repositories into Private

# In[ ]:


# !pip install requests
# !pip install pygithub


# In[ ]:


import requests

# Replace these with your GitHub username and personal access token
username = "YOUR_USERNAME"
access_token = "YOUR_ACCESSTOKEN"

# Define the API endpoint for listing user repositories, including public ones
url = f"https://api.github.com/user/repos?type=public"

# Set up headers with the access token for authentication
headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"  # Specify API version
}

# Send a GET request to the GitHub API to list public repositories
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repositories = response.json()

    # Print the names of your public repositories
    print("Your public GitHub repositories:")
    for index, repo in enumerate(repositories):
        print(f"{index + 1}. {repo['name']}")

    # Change the visibility of all public repositories to private
    for index, repo in enumerate(repositories):
        repo_name = repo["name"]
        visibility_url = f"https://api.github.com/repos/{username}/{repo_name}"
        visibility_payload = {
            "private": True
        }
        visibility_response = requests.patch(visibility_url, headers=headers, json=visibility_payload)
        if visibility_response.status_code == 200:
            print(f"Changed visibility of '{repo_name}' to private.")
        else:
            print(f"Failed to change visibility of '{repo_name}' to private. Status code: {visibility_response.status_code}")
else:
    print(f"Failed to retrieve public repositories. Status code: {response.status_code}")c

