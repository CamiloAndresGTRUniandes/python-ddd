from functools import singledispatch
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Query(ABC):
    ...

@dataclass
class QueryResult:
    result: None

class QueryHandler(ABC):
    @abstractmethod
    def handle(self, query: Query) -> QueryResult:
        raise NotImplementedError()

@singledispatch
def execute_query(query):
    raise NotImplementedError(f'Not implemented query type {type(query).__name__}')