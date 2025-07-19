import psycopg2

from config import config

class PGVectorHandler:
    def __init__(self):
        self.__conn = psycopg2.connect(config.PGVECTOR_CONN)

    def has_file(self, category, file):
        cursor = self.__conn.cursor()

        query = """
        SELECT 1
        FROM langchain_pg_embedding
        WHERE cmetadata->>'category' = %s AND cmetadata->>'file' = %s
        LIMIT 1;
        """

        cursor.execute(query, (category, file))
        result = cursor.fetchone()

        cursor.close()

        return result is not None

    def del_file(self, category, file):
        cursor = self.__conn.cursor()

        query = """
        DELETE FROM langchain_pg_embedding
        WHERE cmetadata->>'category' = %s AND cmetadata->>'file' = %s
        """

        cursor.execute(query, (category, file))
        self.__conn.commit()

        cursor.close()

    def get_mtime(self, category, file):
        cursor = self.__conn.cursor()

        query = """
        SELECT cmetadata->>'mtime'
        FROM langchain_pg_embedding
        WHERE cmetadata->>'category' = %s AND cmetadata->>'file' = %s
        LIMIT 1;
        """

        cursor.execute(query, (category, file))
        result = cursor.fetchone()

        cursor.close()

        return result[0]

    def get_filenames(self):
        cursor = self.__conn.cursor()

        query = """
        SELECT DISTINCT cmetadata->>'category', cmetadata->>'file'
        FROM langchain_pg_embedding
        """

        cursor.execute(query)

        filenames = {category + config.SPLIT_TAG + file for category, file in cursor.fetchall()}

        cursor.close()

        return filenames

pg_vector_handler = PGVectorHandler()
