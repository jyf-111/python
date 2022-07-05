import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept':'application/vnd.github.v3+json'}

r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")

response_dict = r.json()
print(response_dict.keys())

print(f"Total respositories:{response_dict['total_count']}")


repo_dicts = response_dict['items']
print(f"Repostories returned: {len(repo_dicts)}")

# repo_dict = repo_dicts[0]
# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


for repo_dict in repo_dicts:
    print(f"\n Selected information about first repository")
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f":{repo_dict['stargazers_count']}")
    print(f":{repo_dict['html_url']}")
    print(f":{repo_dict['created_at']}")
    print(f":{repo_dict['updated_at']}")
    print(f":{repo_dict['description']}")