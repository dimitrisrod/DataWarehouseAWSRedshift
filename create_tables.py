import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """Drop tables before starting."""
    for query in drop_table_queries:
        """Run the drop table queries."""
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create the tables."""
    for query in create_table_queries:
        """Run the create table queries."""
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    """Read the parameters"""
    config.read('dwh.cfg')
    
    """Establish connection to database"""
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()