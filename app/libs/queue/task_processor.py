import queue
import threading
from flask import Flask

# GLobal queue accessible by all threads within the module
transaction_queue = queue.Queue()

def start_processing(app: Flask):
    # Start a thread to process the transactions from queue

    def process_transactions():
        with app.app_context():
            while True:
                try:
                    task_func, args, kwargs = transaction_queue.get(block=True)
                    task_func(*args, **kwargs)
                    transaction_queue.task_done()
                except Exception as e:
                    print(e)
        
    thread = threading.Thread(target=process_transactions)
    thread.daemon = True
    thread.start()

def add_transaction_to_queue(task_func, *args, **kwargs):
    """Add a transaction to the queue to be processed by the thread"""
    transaction_queue.put((task_func, args, kwargs))
        

