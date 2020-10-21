from operator import itemgetter
import json 
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' #shows the ID's of the news articles in a list 
r = requests.get(url)
print(f"Status code: {r.status_code}") #print the entire links code

# Process information about each submission.
submission_ids = r.json() #stores the ID's in this list
submission_dicts = [] #create an empty list to hold dictionaries

for submission_id in submission_ids[:10]: #for the top ten ID's in the list
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" #get the link to the story
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}") #print the top 10 ID's in the list and their code
    response_dict = r.json() #save the dictionary into the file
    
    try:
    # Build a dictionary for each article.
        submission_dict = { #create a dictionary for each submission
            'title': response_dict['title'], 
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants']   
    }
    except:
        pass
    
    submission_dicts.append(submission_dict) #append the dictionary to the list

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) #sort the list of dictionaries by the number of comments

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"\nDiscussion Link: {submission_dict['hn_link']}")
    print(f"\nNumber of Comments: {submission_dict['comments']}")

    


