from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.meta_analysis import MetaAnalysis
from ...models.meta_analysis_return import MetaAnalysisReturn
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetaAnalysis,
) -> Dict[str, Any]:
    url = "{}/meta-analyses/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, MetaAnalysisReturn]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MetaAnalysisReturn.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
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
    client: AuthenticatedClient,
    json_body: MetaAnalysis,
) -> Response[Union[Any, MetaAnalysisReturn]]:
    """Update a meta-analysis

     update an existing meta-analysis (that has not yet been run)

    Args:
        id (str):
        json_body (MetaAnalysis): The combination of the specification determining what meta-
            analysis to run (required), the studyset to act as input to the meta-analytic algorithm
            (required), and the annotation to provide human readable annotations as well as acts as an
            optional filter on which analyses to select within the studyset (optional, but suggested).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetaAnalysis,
) -> Optional[Union[Any, MetaAnalysisReturn]]:
    """Update a meta-analysis

     update an existing meta-analysis (that has not yet been run)

    Args:
        id (str):
        json_body (MetaAnalysis): The combination of the specification determining what meta-
            analysis to run (required), the studyset to act as input to the meta-analytic algorithm
            (required), and the annotation to provide human readable annotations as well as acts as an
            optional filter on which analyses to select within the studyset (optional, but suggested).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetaAnalysis,
) -> Response[Union[Any, MetaAnalysisReturn]]:
    """Update a meta-analysis

     update an existing meta-analysis (that has not yet been run)

    Args:
        id (str):
        json_body (MetaAnalysis): The combination of the specification determining what meta-
            analysis to run (required), the studyset to act as input to the meta-analytic algorithm
            (required), and the annotation to provide human readable annotations as well as acts as an
            optional filter on which analyses to select within the studyset (optional, but suggested).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetaAnalysisReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetaAnalysis,
) -> Optional[Union[Any, MetaAnalysisReturn]]:
    """Update a meta-analysis

     update an existing meta-analysis (that has not yet been run)

    Args:
        id (str):
        json_body (MetaAnalysis): The combination of the specification determining what meta-
            analysis to run (required), the studyset to act as input to the meta-analytic algorithm
            (required), and the annotation to provide human readable annotations as well as acts as an
            optional filter on which analyses to select within the studyset (optional, but suggested).

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
            json_body=json_body,
        )
    ).parsed
