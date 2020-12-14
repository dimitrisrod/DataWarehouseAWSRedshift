import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """Loading data into Staging tables."""
    for query in copy_table_queries:
        """ Run the copy query."""
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Inserting data into Fact and Dimension tables."""
    for query in insert_table_queries:
        """Run the insert query."""
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    """Reading the parameters."""
    config.read('dwh.cfg')
    
    """Getting database connection."""
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()