# Script to run a segment of a song in a loop on Spotify [WIP]

## Setup
Install spotipy with pip:
```
pip install spotipy
```

Create a Spotify developer app. Once created, edit the redirect URL (in "Edit Settings") to be `http://localhost`.

To run the script, you will need to set the following environmental variables:
```
export SPOTIPY_CLIENT_ID="your-spotify-client-id"
export SPOTIPY_CLIENT_SECRET="your-spotify-client-secret"
export SPOTIPY_REDIRECT_URI="http://localhost"
```

You may do this manually or use something like an Anaconda environment so that this does not need to be set each time. You can follow [these](https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0) instructions for the latter approach.

## Running
Now you can run the script by simply running `python songloop.py`! It will prompt you for the spotify URI and the times over which to loop, and you should be good to go :) 
