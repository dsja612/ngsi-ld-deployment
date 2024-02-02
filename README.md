# ngsi-ld-deployment
This repository contains docker-compose files for various deployment setups of NGSI-LD context brokers.

## Orion-LD
- `orion.aio.yml`: Contains services for the Orion-LD context broker, Mintaka, JSON IOT agent and the Mosquitto MQTT broker

## Scorpio
- `scorpio.aio.yml`: Contains services for the Scorpio context broker, JSON IOT agent and the Mosquitto MQTT broker
- `scorpio.aio.nokafka.yml`: Similar to `scorpio.aio.yml`, but without Kafka integration

## IOT Agent only
- `agent.yml`: Contains the JSON IOT agent and the Mosquitto MQTT broker

# Requirements
1. Docker

# How to install
1. Clone this repository
2. `cd ngsi-ld-deployment`
3. Run `docker-compose -f <filename> up --build`