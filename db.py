from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy.sql import table, column, select
import os


class UserAccounts:
    """Create user accounts from submissions."""

    def __init__(self, username, email, gravatar):
        self.username = username
        self.email = email
        self.gravatar = gravatar

    def insert_user_record(self):
        """Select records for all confirmed new hires which have yet to be onboarded."""
        engine = create_engine(os.environ['URI'], client_encoding="UTF-8")
        meta = MetaData(bind=engine, reflect=True)
        readers_table = meta.tables['readers']
        ins = readers_table.insert().values(username=self.username, email=self.email, gravatar=self.gravatar)
        result = engine.connect(ins)
        return result
