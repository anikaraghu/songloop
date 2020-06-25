import os
import sys
import spotipy
import spotipy.util as util
import time

scope = 'user-modify-playback-state,user-read-playback-state'

def main():
    username = login()
    token = util.prompt_for_user_token(username, scope)
    if token: 
        play_loop(token)
    else:
        print("Can't get token for", username)

def login():
    username = input("Please enter spotify username: ")
    if username == '':
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()
    return username

# TODO: more precise timing 
def play_loop(token):
    song = input("Please enter spotify song URI: ") 
    album_link = True if song.find('album') != -1 else False
    start_pos = input("Please enter start time in seconds: ")
    start_time = int(start_pos) * 1000
    end_pos = input("Please enter end time in seconds: ")
    loop_len = int(end_pos) - int(start_pos)
    sp = spotipy.Spotify(auth=token)
    all_devices = sp.devices()
    all_devices = {'devices': []}
    print(all_devices)
    if 'devices' not in all_devices or len(all_devices['devices']) < 1 or 'id' not in all_devices['devices'][0]:
        print("No device found. Restarting spotify may fix this.")
        sys.exit()
    device = all_devices['devices'][0]['id']
    start_looping = time.time()
    if album_link:
        sp.start_playback(device_id=device, context_uri=song, position_ms=start_time)
    else:
        sp.start_playback(device_id=device, uris=[song], position_ms=start_time)
    while True:
        if (time.time() - start_looping) % loop_len == 0:
            if album_link:
                sp.start_playback(device_id=device, context_uri=song, position_ms=start_time)
            else:
                sp.start_playback(device_id=device, uris=[song], position_ms=start_time)

if __name__ == "__main__":
    main()

