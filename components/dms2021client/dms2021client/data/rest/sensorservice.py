""" SensorService class module.
"""

import json
from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse, HTTPException

class SensorService():
    """ REST client to connect to the authentication service.
    """

    def __init__(self, host: str, port: int):
        """ Constructor method.

        Initializes the client.
        ---
        Parameters:
            - host: The authentication service host string.
            - port: The authentication service port number.
        """
        self.__host: str = host
        self.__port: int = port

    def __get_connection(self) -> HTTPConnection:
        """ Creates a new connection to the authentication server.
        ---
        Returns:
            The connection object.
        """
        return HTTPConnection(self.__host, self.__port)

    def modify_rules(self, time: int, route: str) -> str:
        """ Changes the sensor rules
        ---
        Parameters:
            - time: periodicity of checks
            - route: checked route
        Throws:
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'time': time, 'route': route})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('PATCH', '/rules', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("Rules changed")
        if response.status == 500:
            raise HTTPException('Server error')
        return ''

    def latest_entries(self) -> str:
        """ Shows the latest 5 sensor entries.
        ---
        Throws:
            - HTTPException: On an unhandled 500 error.
        """
        form: str = ''
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/entries', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print(response.read())
        if response.status == 500:
            raise HTTPException('Server error')
        return ''