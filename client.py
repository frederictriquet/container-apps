
from azure.storage.queue import QueueClient
import os, json, uuid, time

QUEUE_NAME="messages"
LOGS_QUEUE_NAME="logs"
CONNECTION_STRING=os.getenv("AZURE_STORAGE_CONNECTION_STRING")
queue = QueueClient.from_connection_string(conn_str=CONNECTION_STRING, queue_name=QUEUE_NAME)
logs = QueueClient.from_connection_string(conn_str=CONNECTION_STRING, queue_name=LOGS_QUEUE_NAME)

myId = str(uuid.uuid4())
outputMessage = 'Waiting for a message'
print(outputMessage)
logs.send_message(outputMessage)

def no_loop():
  inputMessage = queue.receive_message()
  if inputMessage:
    payload = json.loads(inputMessage.content)
    outputMessage = f'{myId}: {payload["value"]}'
    print(outputMessage)
    time.sleep(payload['value'])
    print('sleep done')
    logs.send_message(outputMessage)
    queue.delete_message(inputMessage)
  else:
    outputMessage = f'{myId}: NOTHING'
    print(outputMessage)
    logs.send_message(outputMessage)

def loop():
  while True:
    inputMessage = queue.receive_message()
    if inputMessage:
      payload = json.loads(inputMessage.content)
      outputMessage = f'{myId}: {payload["value"]}'
      print(outputMessage)
      time.sleep(payload['value'])
      print('sleep done')
      logs.send_message(outputMessage)
      queue.delete_message(inputMessage)
    else:
      time.sleep(10)


# no_loop()
loop()