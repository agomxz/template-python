import os
import pathlib
from dotenv import load_dotenv

class Config:
    """
    Config project class, use to load env and others configuration.

    Crate class method to handle individual configuration and been able to
    scalade
    and debug easily
    """
    def __init__(self):
        self.load_env()
        self.load_database_config()

    def load_env(self) -> None:
        try:
            load_dotenv()
            env_path = pathlib.Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)
        except Exception as e:
            print(f"Failed to load .env file: {e}")

    def load_database_config(self) -> None:
        db_host = os.getenv('DB_HOST')
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_pass = os.getenv('DB_PASS')
        db_port = os.getenv('DB_PORT')

        if all([db_host, db_name, db_user, db_pass, db_port]):
            self.database_url = (
                f'postgresql+psycopg2://{db_user}:{db_pass}@'
                f'{db_host}:{db_port}/{db_name}'
            )
        else:
            print("Incomplete database configuration."
                              "Please check environment variables.")


config = Config()