import logging
import time
from concurrent.futures import ThreadPoolExecutor


def multiple_threads_function(thread_name):
    logging.info(f'start {thread_name}')
    time.sleep(5)
    logging.info(f'return {thread_name}')


if __name__ == '__main__':
    op_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=op_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(multiple_threads_function, range(3))
