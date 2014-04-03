#! /bin/bash

for i in {1000,10000,100000,1000000};
do
    ./generate_input_data.py ${i}
    echo "number of records: ${i}"
    echo -n "redis: "
    { time ./redis_insert.py; } 2>&1 | head -n 2 | tail -n 1 | awk '{ print $2; }'
    echo -n "postgres: ";
    { time ./postgres_insert.py; } 2>&1 | head -n 2 | tail -n 1 | awk '{ print $2; }'
    echo
done
