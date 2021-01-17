""" Entrada class module.
"""

from typing import Dict
from sqlalchemy import Table, MetaData, Column, Integer, Boolean  # type: ignore
from sqlalchemy.orm import mapper  # type: ignore


class Entrada():
    """ Definition and storage of entry ORM records.
    """

    def __init__(self, time: int, existe_archivo: bool):
        """ Constructor method.

        Initializes an entry record.
        ---
        Parameters:
            - time: Time of the entry
            - existe_archivo: Whether the file exists or not.
        """
        self.time: int = time
        self.existe_archivo: bool = existe_archivo

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.
        ---
        Parameters:
            - metadata: The database schema metadata
                        (used to gather the entities' definitions and mapping)
        Returns:
            A Table object with the table definition.
        """
        return Table(
            'entries',
            metadata,
            Column('time', Integer(15), primary_key=True),
            Column('existe_archivo', Boolean, nullable=False)
        )


    @classmethod
    def map(cls: type, metadata: MetaData) -> None:
        """ Maps the database user records to instances of this class.
        ---
        Parameters:
            - cls: This class.
            - metadata: The database schema metadata
                        (used to gather the entities' definitions and mapping)
        """
        mapper(
            cls,
            cls._table_definition(metadata),  # type: ignore
            properties=cls._mapping_properties()  # type: ignore
        )


    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.
        ---
        Returns:
            A dictionary with the mapping properties.
        """
        return {}
