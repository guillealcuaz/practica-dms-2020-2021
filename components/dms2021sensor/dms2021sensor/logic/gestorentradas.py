""" ManagerBase class module.
"""

from dms2021sensor.data.config.sensorconfiguration import SensorConfiguration
from dms2021sensor.data.db.schema import Schema
from dms2021sensor.data.db.resultsets.entradas import Entradas

class GestorEntradas():
    """ Base class for all logic manager classes.
    """

    def __init__(self, config: SensorConfiguration, schema: Schema):
        """ Constructor method.

        Initializes the manager.
        ---
        Parameters:
            - config: An SensorConfiguration instance with the manager configurable parameters.
            - schema: The database schema instance to use.
        """
        self.__set_configuration(config)
        self.__set_schema(schema)

    def get_schema(self) -> Schema:
        """ Gets the schema being used by this instance.
        ---
        Returns:
            The DB schema object used by the manager.
        """
        return self.__schema

    def __set_schema(self, schema: Schema):
        """ Sets the schema to be used by this instance.
        ---
        Parameters:
            - schema: The database schema instance to use.
        """
        self.__schema = schema

    def get_configuration(self) -> SensorConfiguration:
        """ Gets the configuration being used by this instance.
        ---
        Returns:
            The configuration object used by the manager.
        """
        return self.__configuration

    def __set_configuration(self, config: SensorConfiguration):
        """ Sets the configuration to be used by this instance.
        ---
        Parameters:
            - config: The configuration instance to use.
        """
        self.__configuration = config


    def create_entry(self,time: int, existe_archivo: bool):
        """ Creates a user.
        ---
        Parameters:
            - username: A non-empty user name string.
            - password: A non-empty user password string.
            - session_token: The token of the session, used to verify that
                             the requestor has sufficient rights.
            - right_validator: The user right validator to use.
            - superuser: If set, will not validate the requestor rights.
                         Use ONLY for administrative purposes.
        Throws:
            - InsufficientRightsError: If the requestor does not have the required rights.
            - ValueError: if either the username or the password is empty.
        """
        if not time:
            raise ValueError('Time is required.')
        session = self.get_schema().new_session()
        Entradas.create(session, time, existe_archivo)

    def latest_entries(self):
        """ Verifies whether a user with the given credentials exists or not.
        ---
        Parameters:
            - username: The user name string.
            - password: The user password string.
        Returns:
            True if the user exists and the credentials are correct; false otherwise.
        """
        session = self.get_schema().new_session()
        return Entradas.latest_entries(session)

    
