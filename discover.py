from soco import discover

zones = discover()
if zones:
    for zone in zones:
        print(f"{zone.player_name} - {zone.ip_address}")
else:
    print("No Sonos device found.")
