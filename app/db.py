from cassandra.cluster import Cluster

from cassandra.cqlengine.connection import register_connection, set_default_connection

from dotenv import load_dotenv

from . import config

settings = config.get_settings()


def get_cluster():
    cluster = Cluster(['127.0.0.1'], port=9042)
    return cluster


def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    register_connection(str(session), session=session)
    set_default_connection(str(session))
    return session


#session = get_session()
#row = session.execute("select release_version from system.local").one()
#if row:
#    print(row[0])
#else:
#    print("An error occurred.")
    