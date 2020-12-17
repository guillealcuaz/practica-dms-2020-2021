""" AuthService class module.
"""

import json
from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse, HTTPException
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from dms2021core.data import UserRightName


class AuthService():
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

    def is_running(self) -> bool:
        """ Tests whether the authentication service is running or not.
        ---
        Returns:
            True if the authentication service could be contacted successfully; false otherwise.
        """
        try:
            connection: HTTPConnection = self.__get_connection()
            connection.request('GET', '/')
            response: HTTPResponse = connection.getresponse()
            if response.status == 200:
                return True
            return False
        except HTTPException:
            return False
        except ConnectionRefusedError:
            return False

    def login(self, username: str, password: str) -> str:
        """ Logs in a user in the authentication server.
        ---
        Parameters:
            - username: The user name string.
            - password: The user password string.
        Returns:
            The session id string.
        Throws:
            - InvalidCredentialsError: If the credentials provided are not correct.
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'username': username, 'password': password})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', '/sessions', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            response_data_json = response.read()
            response_data = json.loads(response_data_json)
            return response_data['session_id']
        if response.status == 401:
            raise InvalidCredentialsError()
        if response.status == 500:
            raise HTTPException('Server error')
        return ''

    def logout(self, session_id: str):
        """ Logs out a user from the authentication server.
        ---
        Parameters:
            - session_id: The session id string.
        Throws:
            - UnauthorizedError: If the provided session is incorrect or closed.
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('DELETE', '/sessions', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            return

        if response.status == 401:
            raise UnauthorizedError()
        if response.status == 500:
            raise HTTPException('Server error')

    def create_user(self, username: str, password: str, session: str) -> str:
        """ Creates a user in the authentication server.
        ---
        Parameters:
            - username: The name string of the new user.
            - password: The password string of the new user.
            - session: The session id of the user creating the new user.
        Throws:
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'username': username, 'password': password, 'session_id': session})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', '/users', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("User created")
        if response.status == 400:
            raise ValueError
        if response.status == 401:
            print("You lack the rights to create a user")
        if response.status == 409:
            print("The user already exists")
        if response.status == 500:
            raise HTTPException('Server error')
        return ''

    def grant(self, username: str, right_name: str, session: str) -> str:
        """ Grants a right to a user in the authentication server.
        ---
        Parameters:
            - username: The name string of the new user.
            - right_name: The name of the right to be granted.
            - session: The session id of the user granting the right.
        Throws:
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'session_id': session})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        address='/users/' + username + '/rights/' + right_name
        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', address, form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("Right granted")
        if response.status == 401:
            print("Session not found or inssuficient rights")
        if response.status == 404:
            print("User not found")
        if response.status == 500:
            raise HTTPException('Server error')
        return ''

    def revoke(self, username: str, right_name: str, session: str) -> str:
        """ Revokes a right from a user in the authentication server.
        ---
        Parameters:
            - username: The name string of the new user.
            - right_name: The name of the right to be revoked.
            - session: The session id of the user granting the right.
        Throws:
            - HTTPException: On an unhandled 500 error.
        """
        form: str = urlencode({'session_id': session})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        address='/users/' + username + '/rights/' + right_name
        connection: HTTPConnection = self.__get_connection()
        connection.request('DELETE', address, form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("Right revoked")
        if response.status == 401:
            print("Session not found or inssuficient rights")
        if response.status == 404:
            print("User not found")
        if response.status == 500:
            raise HTTPException('Server error')
        return ''