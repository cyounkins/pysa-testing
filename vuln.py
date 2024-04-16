from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Engine


def my_source() -> str:
    return 'foo'


def my_sink(foo) -> None:
    return


def vulnerable_func() -> None:
    engine: Engine = create_engine('sqlite:///test.db')
    reveal_type(engine.execute)
    user_input = my_source()

    # Vulnerable SQL execution
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    result = engine.execute(query)
    reveal_type(engine.execute)

    my_sink(query)
