from kafka import KafkaConsumer
import json
def function_execute(data):
    jsonstr = data.decode()
    db = json.loads(jsonstr)
    print(db)
consumer = KafkaConsumer(
    'sampleTopic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
)
for message in consumer:
    function_execute(message.value)
