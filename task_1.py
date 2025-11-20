import queue
import uuid

request_queue = queue.Queue()

def generate_request():
    new_request = {
        'id': uuid.uuid4(),
        'name': 'New Request',

    }
    request_queue.put(new_request)
   


def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Processing request: {current_request['id']}, Name: {current_request['name']}")
    else:
        print("The request queue is empty.")



try:
    while True:
        generate_request()
        process_request()

except KeyboardInterrupt:
    print("Exiting the program.")