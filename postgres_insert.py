#! /usr/bin/python

import psycopg2

def main():
    conn = psycopg2.connect(open('postgres_string.txt', 'r').read().strip())
    cur = conn.cursor()
    cur.execute("CREATE TEMP TABLE test (id varchar PRIMARY KEY, data varchar);")
    with open('input_data.txt', 'r') as f:
        for index, record in enumerate(f):
            cur.execute("INSERT INTO test (id, data) VALUES (%s, %s)", (str(index), record))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
