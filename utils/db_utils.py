import mysql.connector
from mysql.connector import Error
from utils.logger import get_logger


class DatabaseUtils:

    @staticmethod
    def get_connection():
        """
        Create and return MySQL database connection
        """
        logger = get_logger()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="automation_user",
                password="automation123",
                database="testdb"
            )

            logger.info("Database connection established successfully")
            return connection

        except Error as e:
            logger.error(f"Database connection failed: {e}")
            raise

    @staticmethod
    def execute_query(query):
        """
        Execute SELECT query and return results
        """
        logger = get_logger()
        logger.info(f"Executing Query: {query}")

        try:
            connection = DatabaseUtils.get_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            cursor.close()
            connection.close()

            logger.info("Query executed successfully")
            return result

        except Error as e:
            logger.error(f"Query execution failed: {e}")
            raise
     