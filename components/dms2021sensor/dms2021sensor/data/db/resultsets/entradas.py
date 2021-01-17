""" Entradas class module.
"""

import hashlib
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2021sensor.data.db.results.entrada import Entrada


class Entradas():
    """ Class responsible of table-level users operations.
    """
    @staticmethod
    def create(session: Session, time: int, existe_archivo: bool) -> Entrada:
        """ Creates a new entry record.
        ---
        Note:
            Any existing transaction will be committed.
        Parameters:
            - session: The session object.
            - time: Time of the entry.
            - existe_archivo: Boolean that tells whether the file exists (true if exists).
        Returns:
            The created entry result.
        Throws:
            - ValueError: If the time is empty.
        """
        if not time:
            raise ValueError('Time is required.')
        try:
            new_entry = Entrada(time, existe_archivo)
            session.add(new_entry)
            session.commit()
            return new_entry
        except IntegrityError as ex:
            print("An entry with that time already exists")        

    @staticmethod
    def latest_entries(session: Session):
        """ Determines whether a user exists or not.
        ---
        Parameters:
            - session: The session object.
        Returns:
            True if a user with the given credentials exists; false otherwise.
        """
        
        query = session.query(Entrada).order_by(Entrada.time.desc()).limit(5)
        resultado = query.all()
        return resultado
    
    
