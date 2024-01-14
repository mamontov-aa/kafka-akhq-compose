from confluent_kafka import Producer

cfg = {'bootstrap.servers': 'localhost:29092'}
producer = Producer(cfg)
producer.produce('my_topic', key='hello_key', value='world_value')
producer.flush()
