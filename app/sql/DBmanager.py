import psycopg2
from config import Config


class ConnectionErrors(Exception):
    pass


class SQLError(Exception):
    pass


class UseDataBase:

    def __init__(self) -> None:
        self.configuration = Config.dbconfig

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.InterfaceError as err:
            raise ConnectionErrors(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is psycopg2.ProgrammingError:
            raise SQLError(exc_val)
        elif exc_type:
            raise exc_type(exc_val)

get_posts_by_search = '''WITH user_ids AS (
                    SELECT DISTINCT
                        followed_id user_id
                    FROM
                        followers
                    WHERE
                        follower_id = {0}
                    )
                    SELECT
                        "user".username
                      , "user".id
                      , post.body
                    FROM
                        post
                    JOIN
                      "user"
                        ON "user".id = post.user_id
                    WHERE
                        (
                            user_id = {0} OR
                            user_id = ANY(TABLE user_ids)
                        ) AND
                        to_tsvector('simple'::regconfig, body) @@ to_tsquery('simple'::regconfig, '{1}'::text)'''

