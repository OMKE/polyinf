from abc import ABC, abstractmethod
from core.models.user import User


class AuthInterface(ABC):

    @abstractmethod
    def user(self) -> User:
        raise NotImplementedError('Must be implemented by a subclass')
