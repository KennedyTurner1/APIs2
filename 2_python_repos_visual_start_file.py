import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
# create 3 lists 
response_dict = r.json() #loading the url into a file
repo_dicts = response_dict['items'] #list of dictionary 
repo_links, stars, labels = [], [], [] #three empty lists

for repo_dict in repo_dicts: #for repository in list of repositories
    name = repo_dict['name']
    repo_url = repo_dict['html_url']

    repo_link = f" <a href='{repo_url}'>{name}</a" #link to the repository is the name of the repository and url, x axis

    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    label = f"{owner}<br> />{description}" #label for the hovertext, the owner and description of the repository

    star = repo_dict['stargazers_count'] #starcount is the y axis, the number of visits to the repository
    
    repo_links.append(repo_link) 
    labels.append(label) 
    stars.append(star)

    

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
