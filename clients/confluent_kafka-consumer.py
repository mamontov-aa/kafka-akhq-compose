from confluent_kafka import Consumer, KafkaException

cfg = {'bootstrap.servers': 'localhost:29092', 'group.id': 'hello_group'}
# cfg['auto.offset.reset'] = 'earliest'
# cfg['enable.auto.commit'] = False

topics = ['my_topic']

def assignment_callback(consumer, partitions):
    for p in partitions:
        print(f'Assigned to {p.topic}, partition {p.partition}')

if __name__ == '__main__':
    consumer = Consumer(cfg)
    consumer.subscribe(topics=topics, on_assign=assignment_callback)
    try:
        while True:
            event = consumer.poll(1.0)
            if event is None:
                continue
            if event.error():
                raise KafkaException(event.error())
            else:
                val = event.value().decode('utf8')
                partition = event.partition()
                print(f'Received: {val} from partition {partition}    ')
                # consumer.commit(event)    except KeyboardInterrupt:
        print('Canceled by user.')
    finally:
        consumer.close()