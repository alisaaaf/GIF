import requests


def get_gif():
    params = {"api_key": "Y9JsIxBkRclvHtj36ZY1Y0YUq3rXUHl0", "q": "dog", "limit": "1"}
    url = "https://api.giphy.com/v1/gifs/search"

    response = requests.get(url, params=params)
    response.raise_for_status()
    gif_url = response.json()['data'][0]['images']['original']['url']


    gif_response = requests.get(gif_url)
    gif_response.raise_for_status()
    return gif_response.content


def save_gif(gif_content):

    with open("gif.gif", "wb") as file:
        file.write(gif_content)


if __name__ == '__main__':
    gif_content = get_gif()
    save_gif(gif_content)