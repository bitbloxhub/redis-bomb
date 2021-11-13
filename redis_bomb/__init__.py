import threading
import functools
from redis import Redis

__version__ = "0.1.0"


def bomb_thread(host, port, id, bombs):
    redis = Redis(host=host, port=port)
    for bomb in range(bombs):
        redis.set(str(id) + str(bomb), str(id) + str(bomb + 1))
        redis.get(str(id) + str(bomb))


def bomb(host, port, bombs, threads):
    threadsl = []
    for id in range(threads):
        threadsl.append(
            threading.Thread(target=bomb_thread, args=(host, port, id, bombs))
        )

    for thread in threadsl:
        thread.start()

    for thread in threadsl:
        thread.join()

    redis = Redis(host=host, port=port)
    redis.flushall()
