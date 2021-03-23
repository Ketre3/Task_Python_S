import random
import json
import string

import requests

BASE_API_URL = 'http://127.0.0.1:8000/api'


session = requests.Session()


with open('config.json', 'r') as f:
    settings = json.load(f)


def _api_post(uri, json_data={}, jwt_token=None):
    if jwt_token:
        headers = {"Authorization": f"Bearer {jwt_token}"}
    else:
        headers = None
    
    response = session.post(
        f"{BASE_API_URL}/{uri}",
        json=json_data,
        headers=headers,
    )
    response.raise_for_status()

    return response.json()


def register(username, password):
    return _api_post(
        'account/register/',
        json_data = {
            "username": username,
            "password": password,
        },
    )
    

def create_post(jwt_token, title, text):
    return _api_post(
        'post/create/',
        json_data={
            "title": title,
            "text": text,
        },
        jwt_token=jwt_token,
    )


def like_post(jwt_token, post_id):
    return _api_post(
        f'post/{post_id}/like/',
        jwt_token=jwt_token,
    )


def random_word(*, length=8):
    symbols = random.choices(string.ascii_letters, k=length)
    return "".join(symbols)


def generate_random_username_and_password():
    username = random_word(length=8)
    password = random_word(length=8)
    return username, password


def main():
    jwt_tokens = []
    for _ in range(settings['number_of_users']):
        username, password = generate_random_username_and_password()
        tokens = register(username, password)
        jwt_tokens.append(tokens['access'])
    
    posts_id = []
    for token in jwt_tokens:
        max_number_of_posts = settings['max_posts_per_user']
        number_of_posts = random.randint(1, max_number_of_posts)
        for _ in range(number_of_posts):
            post = create_post(
                jwt_token=token,
                title=random_word(),
                text=random_word(length=30),
            )
            posts_id.append(post['id'])
    
    for token in jwt_tokens:
        max_number_of_likes = settings['max_likes_per_user']
        number_of_likes = random.randint(1, max_number_of_likes)

        for _ in range(number_of_likes):
            post_id = random.choice(posts_id)
            like_post(
                jwt_token=token,
                post_id=post_id,
            )


if __name__ == "__main__":
    main()
