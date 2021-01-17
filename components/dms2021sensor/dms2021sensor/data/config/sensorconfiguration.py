""" SensorConfiguration class module.
"""

from dms2021core.data.config import Configuration, ConfigurationValueType


class SensorConfiguration(Configuration):
    """ Class responsible of storing a specific authentication service configuration.
    """

    def _component_name(self) -> str:
        """ The component name, to categorize the default config path.
        ---
        Returns:
            A string identifying the component which will categorize the configuration.
        """

        return 'dms2021sensor'

    def __init__(self):
        """ Initialization/constructor method.
        """

        Configuration.__init__(self)

    def _validate_values(self, values: dict) -> None:
        """ Validates a set of configuration values.

        Subclasses are expected to override this method and provide their own
        domain-specific validation.
        ---
        Parameters:
            - values: The dictionary of configuration values.
        Throws:
            - A `ValueError` exception if validation is not passed.
        """

    def get_db_connection_string(self) -> str:
        """ Gets the db_connection_string configuration value.
        ---
        Returns:
            A string with the value of db_connection_string.
        """

        return str(self.get_value('db_connection_string'))

    def get_service_host(self) -> str:
        """ Gets the host configuration value.
        ---
        Returns:
            A string with the value of host.
        """

        return str(self.get_value('host'))

    def get_service_port(self) -> int:
        """ Gets the port configuration value.
        ---
        Returns:
            An integer with the value of port.
        """

        value = self.get_value('port')
        return int(str(value))

    def get_debug_flag(self) -> bool:
        """ Gets whether the debug flag is set or not.
        ---
        Returns:
            A boolean with the value of debug.
        """

        return bool(self.get_value('debug'))


    def __get_auth_service_value(self) -> dict:
        """ Gets the value of the auth_service configuration dictionary.
        ---
        Returns:
            A dictionary with the authentication service configured parameters.
        """
        auth_service_value: ConfigurationValueType = self.get_value(
            'auth_service'
        )
        if not isinstance(auth_service_value, dict):
            raise TypeError(
                'Configuration parameter auth_service is expected to be a dictionary. Received: '
                + str(type(auth_service_value))
            )
        return auth_service_value

        
    def get_auth_service_host(self) -> str:
        """ Gets the authentication service host configuration value.
        ---
        Returns:
            A string with the value of authservice host.
        Throws:
            - TypeError: if the authservice parameter is not a dictionary.
        """

        auth_service_value: dict = self.__get_auth_service_value()
        return str(auth_service_value['host'])
    
    
    def get_auth_service_port(self) -> int:
        """ Gets the authentication service port configuration value.
        ---
        Returns:
            An integer with the value of authservice port.
        Throws:
            - TypeError: if the authservice parameter is not a dictionary.
        """

        auth_service_value: dict = self.__get_auth_service_value()
        return int(str(auth_service_value['port']))

    def __get_rules_value(self) -> dict:
        """ Gets the value of the rules configuration dictionary.
        ---
        Returns:
            A dictionary with the rules configured parameters.
        Throws:
            - TypeError: if the authservice parameter is not a dictionary.
        """
        rules_value: ConfigurationValueType = self.get_value(
            'rules'
        )
        if not isinstance(rules_value, dict):
            raise TypeError(
                'Configuration parameter auth_service is expected to be a dictionary. Received: '
                + str(type(rules_value))
            )
        return rules_value


    def get_rules_route(self) -> str:
        """ Gets the route from the rules configuration value.
        ---
        Returns:
            A string with the route from rules.
        Throws:
            - TypeError: if the authservice parameter is not a dictionary.
        """

        rules_value: dict = self.__get_rules_value()
        return str(rules_value['route'])
    
    
    def get_rules_time(self) -> int:
        """ Gets the time rule configuration value.
        ---
        Returns:
            An integer with the value of the time rule.
        Throws:
            - TypeError: if the authservice parameter is not a dictionary.
        """

        rules_value: dict = self.__get_rules_value()
        return rules_value['time']


