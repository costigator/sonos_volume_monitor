# Sonos Volume Monitor

This is a small script to ensure that the Sonos volume hast always the same level when the TV is active.
The volume is then adjusted with the set-top box.

## Requirement

To start the application you need to know the IP of your Sonos speakers. Please install [Python](https://www.python.org/downloads/) and run:

```bash
pip install -r requirements.txt
python discover.py
```

## Installation

[Install Docker](https://www.docker.com/products/docker-desktop/) and run this command:

```bash
docker run -d --restart always --name sonos -e IP='192.168.1.79' -e VOLUME='50' costigator/sonos_volume_monitor
```

## Update

To update the image run:

```bash
docker pull costigator/sonos_volume_monitor
```

## Develop

To develop/test this container locally run:

```bash
docker build -t sonos .
docker run -it --rm sonos sh
```