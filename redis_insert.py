#! /usr/bin/python

import redis

def main():
    redis_server = redis.Redis('localhost')
    with open('input_data.txt', 'r') as f:
        for index, record in enumerate(f):
            redis_server.set(str(index), record)

if __name__ == "__main__":
    main()
