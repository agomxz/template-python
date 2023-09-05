import logging
import os
import pathlib

from dotenv import load_dotenv

"""
Example config project class, use to load env and others configuration.
"""


class Config:
    logger = logging.getLogger()

    def __init__(self):
        self.load_env_file()
        self.load_env_variables()

    def load_env_file(self) -> None:
        try:
            load_dotenv()
            env_path = pathlib.Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)
        except Exception as e:
            logging.warning(f"Failed to load .env file: {e}")

    def load_env_variables(self) -> None:
        self.db_user = os.getenv("DB_USER")
        self.db_pass = os.getenv("DB_PASS")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")

        if not all([
            self.db_user,
            self.db_pass,
            self.db_host,
            self.db_port,
            self.db_name
        ]):
            self.logger.warning("Incomplete example configuration."
                                "Please check environment variables.")


config = Config()