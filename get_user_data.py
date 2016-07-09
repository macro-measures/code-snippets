import time

import requests


KEY = 'Your API key goes here'
URL = 'https://api-new.macromeasures.com/twitter/users.json?key={key}'.format(
    key=KEY
)
def fetch_macromeasures_data(user_inputs, use_usernames=True):
    """Fetches data on the specified users (by user ID or username) from the
    Macromeasures API."""
    user_input_param = 'usernames' if use_usernames else 'ids'
    url = URL + '&' + user_input_param + '=' + ','.join(user_inputs)

    while True:
        response = requests.get(url)
        result = response.json()
        if result['complete']:
            return result

        time.sleep(1)


def fetch_by_username(*user_inputs):
    """Fetches data on the specified usernames from the Macromeasures API. You
    should run no more than 100 users at a time."""
    return fetch_macromeasures_data(user_inputs, use_usernames=True)


def fetch_by_user_id(*user_inputs):
    """Fetches data on the specified user IDs from the Macromeasures API. More
    efficient than fetching by username, but you'll need to use the Twitter API
    to get the user IDs. You should run no more than 100 users at a time."""
    return fetch_macromeasures_data(user_inputs, use_usernames=False)


# Fetch by username. This will print out a large JSON document.
print fetch_by_username('aircanada', 'neiltyson', 'dellsystem')

# Fetch by user ID. The same data as above, just specified by user ID.
print fetch_by_user_id('54904679', '19725644', '20442149')
