# coding: utf-8

"""
    Analysis Specification for Meta-analysis

    api to create a meta-analysis specification  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""

from neurosynth_compose_sdk.paths.users.get import UsersGet
from neurosynth_compose_sdk.paths.users_id.get import UsersIdGet
from neurosynth_compose_sdk.paths.users_id.put import UsersIdPut
from neurosynth_compose_sdk.paths.users.post import UsersPost


class UsersApi(
    UsersGet,
    UsersIdGet,
    UsersIdPut,
    UsersPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
