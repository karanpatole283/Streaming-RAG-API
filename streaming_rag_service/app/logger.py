import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def log_request(data):
    
    logging.info(f"Received request: {data}")
