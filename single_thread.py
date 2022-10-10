import threading
import logging
import time


def thread_function(thread_name):
    logging.info(f'thread {thread_name} started')
    time.sleep(5)
    logging.info(f'thread {thread_name} stops')


if __name__ == "__main__":
    op_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=op_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,)) # optparam - deamon=true: this thread gets terminated as soon as main function is done
    logging.info("Main: before running thread")
    x.start()
    a = 20 + 10
    logging.info(a)
    logging.info("Main: wait for the thread to finish")
    x.join()
    logging.info("Main: all done")