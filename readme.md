# HowTo use this example

Open Terminal 1 and run:
> cd servers/confluent
> docker-compose up

Open any WEB-browser and start to AKHQ UI topic page
(wait until Kafka server starts and then F5)
> http://localhost:8080/ui/docker-kafka-server/topic

Open Terminal 2 and run:
> cd clients
> python3 -m venv .venv
> . .venv/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
> python confluent_kafka-consumer.py

Open Terminal 3 and run:
> cd clients
> . .venv/bin/activate
> python confluent_kafka-producer.py
