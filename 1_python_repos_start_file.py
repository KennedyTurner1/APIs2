import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #Status code: 200, means that it ran correctly

#Store API response in a variable
response_dict = r.json() 

#print out total number of repositories
print(f"Total Repositories Returned: {response_dict['total_count']}") #Total Repositories Returned: 5947585 current repository

#Explore each repository
#items is a list of dictionaries that has information about each repository
repo_dicts = response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}" #length of the list of dictionaries)

for repo_dict in repo_dicts[:10]: #for dictionary in list
    print(f"Name: {repo_dicts['name']}")
    print(f"Owner: {repo_dicts['owner']['login']]}")
    print(f"Stars: {repo_dicts['stargazers_count']}")
    print(f"Repository url: {repo_dicts['repos_url']}")


'''
list out the:
1) name
2) owner (owner login)
3) stars (stargazers count) how many hits the pository gets
4) url 
5) when it was created
6) when it was updated
7) description
'''

