from fastapi import Query, Depends
from typing import Annotated


def query_params(
    q: Annotated[str | None, Query()] = None,
    limit: Annotated[int, Query()] = 100,
    skip: Annotated[int, Query()] = 0,
):
    print("common parameters dependency called")

    return {"q": q, "limit": limit, "skip": skip}



QueryParamsDep = Annotated[dict, Depends(query_params)]