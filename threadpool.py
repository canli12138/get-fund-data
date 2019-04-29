# -*- coding: utf-8 -*-
import threading


def threadpool(function, url_queue, regex, result_data, max_threads=10):
    threads = []
    while threads or url_queue:
        # the crawl is still active
        for thread in threads:
            if not thread.is_alive():
                # remove the stopped threads
                threads.remove(thread)
        while len(threads) < max_threads and url_queue:
            # can start some more threads
            thread = threading.Thread(target=function, args=(url_queue.pop(), regex, result_data,))
            # set daemon so main thread can exit when receives ctrl-c
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
    # all threads have been processed
    # sleep temporary so CPU can focus execution elsewhere
    # time.sleep(SLEEP_TIME)
