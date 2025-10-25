import requests
def number_of_subscribers(subreddit):
    url="https://www.reddit.com/r/{}/about.json"

        headers={'User-Agent':'My User Agent 5.0'}
        response=requests.get(url,headers=headers)
        if response.status_code== 200:
            return response.json()
        return 0