import os
from soco import discover, SoCo
from time import sleep

# variables
ROOM = os.environ.get("ROOM", "Esszimmer")
VOLUME = int(os.environ.get("VOLUME", "50"))

def main():

    print(f"Getting IP for Sonos {ROOM}")

    ip_address = None
    for zone in discover():
        print(f"{zone.player_name} - {zone.ip_address}")
        if zone.player_name == ROOM:
            ip_address = zone.ip_address

    if ip_address:
        print(f"Connecting to {ROOM} - {ip_address}")

        sonos = SoCo(ip_address)

        while(True):

            # if TV source is active
            if sonos.music_source == "TV":
                print(f"Setting volume to {VOLUME} to {ROOM}")
                sonos.volume = 50
            else:
                print("TV source is not active. Waiting...")

            sleep(10)

    else:
        print("No Sonos device found. Exit.")

if __name__ == "__main__":
    main()
