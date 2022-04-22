import requests # type: ignore

response = requests.get("https://www.engineerspock.com/")
print(response.status_code)

if response:
    print('Works!')

for url in ["https://www.engineerspock.com/", "https://www.engineerspock.com/inexistent"]:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'Error:{http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print("Connected Successfully!")

#response = requests.get("https://api.github.com/").json()
#print(response)
blog_response = requests.get("https://www.engineerspock.com/")
github_response = requests.get("https://api.github.com/")

#print(blog_response.headers,end='\n')
#print(github_response.headers,end='\n')

print(blog_response.headers["content-type"])

#print(placeholder_response = requests.get("https://jsonplaceholder.typicode.com/comments", params=b'postId=1'))