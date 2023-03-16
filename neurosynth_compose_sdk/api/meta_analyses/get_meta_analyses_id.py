from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.meta_analysis_return import MetaAnalysisReturn
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    nested: bool,
) -> Dict[str, Any]:
    url = "{}/meta-analyses/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["nested"] = nested

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, MetaAnalysisReturn]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MetaAnalysisReturn.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, MetaAnalysisReturn]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    nested: bool,
) -> Response[Union[Any, MetaAnalysisReturn]]:
    """GET meta-analysis information

     get a meta-analysis (specification, annotation, and studyset)

    Args:
        id (str):
        nested (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        nested=nested,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Client,
    nested: bool,
) -> Optional[Union[Any, MetaAnalysisReturn]]:
    """GET meta-analysis information

     get a meta-analysis (specification, annotation, and studyset)

    Args:
        id (str):
        nested (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    return sync_detailed(
        id=id,
        client=client,
        nested=nested,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    nested: bool,
) -> Response[Union[Any, MetaAnalysisReturn]]:
    """GET meta-analysis information

     get a meta-analysis (specification, annotation, and studyset)

    Args:
        id (str):
        nested (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        nested=nested,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    nested: bool,
) -> Optional[Union[Any, MetaAnalysisReturn]]:
    """GET meta-analysis information

     get a meta-analysis (specification, annotation, and studyset)

    Args:
        id (str):
        nested (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            nested=nested,
        )
    ).parsed
