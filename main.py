import os, sys
from soco import SoCo
from time import sleep


def load_environment_variables():
    """Load environment variables"""

    global IP
    global VOLUME
    global CHECK_INTERVAL

    IP = os.environ.get("IP", "192.168.1.79")
    VOLUME = int(os.environ.get("VOLUME", "50"))
    CHECK_INTERVAL = int(os.environ.get("CHECK_INTERVAL", "10"))

    print("=" * 50)
    print("Enviroment variables:")
    print(f"IP: {IP}")
    print(f"VOLUME: {VOLUME}")
    print(f"CHECK_INTERVAL: {CHECK_INTERVAL}")
    print("=" * 50)

def main():

    load_environment_variables()

    print(f"Connecting to {IP}")

    try:
        sonos = SoCo(IP)
        print(f"Sonos UID: {sonos.uid}")
    except:
        print("Could not connect to Sonos")
        sys.exit(1)


    while(True):

        try:

            # if TV source is active
            if sonos.music_source == "TV":
                print(f"Setting volume to {VOLUME} to {IP}")
                sonos.volume = 50
            else:
                print("TV source is not active. Waiting...")

        except:
            print("Could not set volume because of an error.")

        sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
