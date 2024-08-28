from fastapi import Query, Depends
from typing import Annotated


def query_params(
    q: Annotated[str | None, Query()] = None,
    limit: Annotated[int, Query()] = 100,
    skip: Annotated[int, Query()] = 0,
):
    return {"q": q, "limit": limit, "skip": skip}


class QueryParams:
    def __init__(
        self,
        q: Annotated[str | None, Query()] = None,
        limit: Annotated[int, Query()] = 100,
        skip: Annotated[int, Query()] = 0,
    ) -> None:

        self.q = q
        self.limit = limit
        self.skip = skip


QueryParamsDep = Annotated[dict, Depends(query_params)]

ClassBasedQueryParamsDep = Annotated[dict, Depends(QueryParams)]
