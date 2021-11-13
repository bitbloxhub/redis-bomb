import sys
import redis_bomb

redis_bomb.bomb("127.0.0.1", 6379, int(sys.argv[1]), int(sys.argv[2]))
