# ngsi-ld-deployment
This repository contains docker-compose files for various deployment setups of NGSI-LD context brokers.

## Orion-LD
- `orion.aio.yml`: Contains services for the Orion-LD context broker, Mintaka, JSON IOT agent and the Mosquitto MQTT broker
- `orion.yml`: Contains services for the Orion-LD context broker and Mintaka.

## Scorpio
- `scorpio.aio.yml`: Contains services for the Scorpio context broker, JSON IOT agent and the Mosquitto MQTT broker
- `scorpio.aio.nokafka.yml`: Similar to `scorpio.aio.yml`, but without Kafka integration
- `scorpio.yml`: Contains services for the Scorpio context broker.
- `scorpio.nokafka.yml`: Similar to `scorpio.yml`, but without Kafka integration

## IOT Agent only
- `agent.yml`: Contains the JSON IOT agent and the Mosquitto MQTT broker

## API Gateway
As different context brokers have different endpoints or ports for services (i.e., temporal API), there will be multiple dockerfiles and `nginx.conf` files for each broker. Edit the `.conf` files in [`/nginx`](/nginx) to modify the URLs.
- `orion.gateway.yml`: Contain setup for an NGINX reverse proxy serving as an API gateway for the Orion-LD context broker with Mintaka and IOTAgent-JSON support. 
- `scorpio.gateway.yml`: Contain setup for an NGINX reverse proxy serving as an API gateway for the Scorpio context broker with IOTAgent-JSON support. 

# Requirements
1. Docker

# How to install
1. Clone this repository
2. Run `cd ngsi-ld-deployment`
3. Create a copy of the `.env.sample` file and rename it to `.env`. Edit the variables as needed.
4. Run `docker-compose -f <filename> up --build`
5. To stop the services, run `docker-compose -f <filename> down`