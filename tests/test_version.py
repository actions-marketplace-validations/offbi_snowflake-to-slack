from snowflake_to_slack import __version__
import configparser


def test_version():
    config = configparser.ConfigParser()
    config.read('setup.cfg')
    assert __version__ == config["metadata"]["version"]
