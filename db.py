from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy.sql import table, column, select
import os


class UserAccounts:
    """Create user accounts from submissions."""

    def __init__(self, username, email, gravatar):
        self.username = str(username).encode("utf-8")
        self.email = str(email).encode("utf-8")
        self.gravatar = gravatar
        self.create_account = self.insert_user_record()

    def insert_user_record(self):
        """Select records for all confirmed new hires which have yet to be onboarded."""
        URI = str(os.environ['URI'])

        engine = create_engine(URI)
        with engine.connect() as conn:
            try:
                sql = text("INSERT INTO readers (username, email, gravatar), VALUES :usr, :email, :grav);")
                res = conn.execution_options(stream_results=True).execute(sql, {'usr': self.username, 'email': self.email, 'grav': self.gravatar})  # .construct_params()
                return [dict(row) for row in res]
            except KeyError:
                print('something broke. sorry.')
                raise
            finally:
                conn.close()
