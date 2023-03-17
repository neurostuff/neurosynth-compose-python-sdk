<a name="__pageTop"></a>
# neurosynth_compose_sdk.apis.tags.meta_analyses_api.MetaAnalysesApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_get**](#meta_analyses_get) | **get** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](#meta_analyses_id_get) | **get** /meta-analyses/{id} | GET meta-analysis information
[**meta_analyses_id_put**](#meta_analyses_id_put) | **put** /meta-analyses/{id} | Update a meta-analysis
[**meta_analyses_post**](#meta_analyses_post) | **post** /meta-analyses | Create a new meta-analysis
[**meta_analysis_results_get**](#meta_analysis_results_get) | **get** /meta-analysis-results | Your GET endpoint
[**meta_analysis_results_id_get**](#meta_analysis_results_id_get) | **get** /meta-analysis-results/{id} | Your GET endpoint
[**meta_analysis_results_id_put**](#meta_analysis_results_id_put) | **put** /meta-analysis-results/{id} | 
[**meta_analysis_results_post**](#meta_analysis_results_post) | **post** /meta-analysis-results | 

# **meta_analyses_get**
<a name="meta_analyses_get"></a>
> MetaAnalysisList meta_analyses_get()

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_list import MetaAnalysisList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only optional values
    query_params = {
        'nested': True,
    }
    try:
        # GET a list of meta-analyses
        api_response = api_instance.meta_analyses_get(
            query_params=query_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/problem+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
nested | NestedSchema | | optional


# NestedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analyses_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#meta_analyses_get.ApiResponseFor400) | form when a request goes wrong

#### meta_analyses_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysisList**](../../models/MetaAnalysisList.md) |  | 


#### meta_analyses_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analyses_id_get**
<a name="meta_analyses_id_get"></a>
> MetaAnalysisReturn meta_analyses_id_get(id)

GET meta-analysis information

get a meta-analysis (specification, annotation, and studyset)

### Example

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'nested': True,
    }
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/problem+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
nested | NestedSchema | | optional


# NestedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analyses_id_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#meta_analyses_id_get.ApiResponseFor401) | form when a request goes wrong
404 | [ApiResponseFor404](#meta_analyses_id_get.ApiResponseFor404) | form when a request goes wrong

#### meta_analyses_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysisReturn**](../../models/MetaAnalysisReturn.md) |  | 


#### meta_analyses_id_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analyses_id_put**
<a name="meta_analyses_id_put"></a>
> MetaAnalysisReturn meta_analyses_id_put(id)

Update a meta-analysis

update an existing meta-analysis (that has not yet been run)

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(
            path_params=path_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = MetaAnalysis(
        specification=None,
        studyset=None,
        annotation=None,
        name="name_example",
        description="description_example",
        internal_studyset_id="internal_studyset_id_example",
        internal_annotation_id="internal_annotation_id_example",
        results=[
            None
        ],
        provenance=dict(),
        project="project_example",
        run_key="run_key_example",
    )
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/problem+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysis**](../../models/MetaAnalysis.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analyses_id_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#meta_analyses_id_put.ApiResponseFor400) | form when a request goes wrong
401 | [ApiResponseFor401](#meta_analyses_id_put.ApiResponseFor401) | form when a request goes wrong
404 | [ApiResponseFor404](#meta_analyses_id_put.ApiResponseFor404) | form when a request goes wrong
422 | [ApiResponseFor422](#meta_analyses_id_put.ApiResponseFor422) | form when a request goes wrong

#### meta_analyses_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysisReturn**](../../models/MetaAnalysisReturn.md) |  | 


#### meta_analyses_id_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_id_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analyses_post**
<a name="meta_analyses_post"></a>
> MetaAnalysisReturn meta_analyses_post()

Create a new meta-analysis

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only optional values
    body = MetaAnalysisPostBody(None)
    try:
        # Create a new meta-analysis
        api_response = api_instance.meta_analyses_post(
            body=body,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/problem+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysisPostBody**](../../models/MetaAnalysisPostBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analyses_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#meta_analyses_post.ApiResponseFor400) | form when a request goes wrong
422 | [ApiResponseFor422](#meta_analyses_post.ApiResponseFor422) | form when a request goes wrong
500 | [ApiResponseFor500](#meta_analyses_post.ApiResponseFor500) | form when a request goes wrong

#### meta_analyses_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MetaAnalysisReturn**](../../models/MetaAnalysisReturn.md) |  | 


#### meta_analyses_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### meta_analyses_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationProblemjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**detail** | str,  | str,  |  | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analysis_results_get**
<a name="meta_analysis_results_get"></a>
> ResultList meta_analysis_results_get()

Your GET endpoint

### Example

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.result_list import ResultList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only optional values
    query_params = {
        'meta_analysis_id': "meta_analysis_id_example",
    }
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_get(
            query_params=query_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
meta_analysis_id | MetaAnalysisIdSchema | | optional


# MetaAnalysisIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analysis_results_get.ApiResponseFor200) | OK

#### meta_analysis_results_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResultList**](../../models/ResultList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analysis_results_id_get**
<a name="meta_analysis_results_id_get"></a>
> ResultReturn meta_analysis_results_id_get(id)

Your GET endpoint

### Example

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analysis_results_id_get.ApiResponseFor200) | OK

#### meta_analysis_results_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResultReturn**](../../models/ResultReturn.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analysis_results_id_put**
<a name="meta_analysis_results_id_put"></a>
> ResultReturn meta_analysis_results_id_put(id)



### Example

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.meta_analysis_results_id_put(
            path_params=path_params,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = Result(
        images=dict(),
        meta_analysis_id="meta_analysis_id_example",
        cli_version="cli_version_example",
        estimator=Estimator(
            type="MKDADensity",
            args=dict(),
        ),
        neurostore_id="neurostore_id_example",
        neurovault_collection=NeurovaultCollection(
            collection_id="collection_id_example",
            files=[
                None
            ],
            result="result_example",
        ),
    )
    try:
        api_response = api_instance.meta_analysis_results_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Result**](../../models/Result.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analysis_results_id_put.ApiResponseFor200) | OK

#### meta_analysis_results_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResultReturn**](../../models/ResultReturn.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **meta_analysis_results_post**
<a name="meta_analysis_results_post"></a>
> ResultReturn meta_analysis_results_post()



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.apis.tags import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)

    # example passing only optional values
    body = Result(
        images=dict(),
        meta_analysis_id="meta_analysis_id_example",
        cli_version="cli_version_example",
        estimator=Estimator(
            type="MKDADensity",
            args=dict(),
        ),
        neurostore_id="neurostore_id_example",
        neurovault_collection=NeurovaultCollection(
            collection_id="collection_id_example",
            files=[
                None
            ],
            result="result_example",
        ),
    )
    try:
        api_response = api_instance.meta_analysis_results_post(
            body=body,
        )
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Result**](../../models/Result.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#meta_analysis_results_post.ApiResponseFor200) | OK

#### meta_analysis_results_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResultReturn**](../../models/ResultReturn.md) |  | 


### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

