# neurosynth_compose_sdk.StudysetApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studysets_get**](StudysetApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
[**studysets_id_get**](StudysetApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset
[**studysets_id_put**](StudysetApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset
[**studysets_post**](StudysetApi.md#studysets_post) | **POST** /studysets | Create a new Studyset


# **studysets_get**
> StudysetList studysets_get()

Get a list of Studysets

get a list of serialized/referenced studysets

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import studyset_api
from neurosynth_compose_sdk.model.studyset_list import StudysetList
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = studyset_api.StudysetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of Studysets
        api_response = api_instance.studysets_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling StudysetApi->studysets_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StudysetList**](StudysetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_id_get**
> StudysetReturn studysets_id_get(id)

Get information about a Studyset

get a single serialized/referenced studyset

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import studyset_api
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = studyset_api.StudysetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a Studyset
        api_response = api_instance.studysets_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling StudysetApi->studysets_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_id_put**
> StudysetReturn studysets_id_put(id)

Update a Studyset

update an existing serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import studyset_api
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.studyset import Studyset
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
    api_instance = studyset_api.StudysetApi(api_client)
    id = "id_example" # str | 
    studyset = Studyset(
        neurostore_id="neurostore_id_example",
        snapshot={},
    ) # Studyset |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling StudysetApi->studysets_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id, studyset=studyset)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling StudysetApi->studysets_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **studyset** | [**Studyset**](Studyset.md)|  | [optional]

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post()

Create a new Studyset

create a new serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import studyset_api
from neurosynth_compose_sdk.model.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
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
    api_instance = studyset_api.StudysetApi(api_client)
    studyset_post_body = StudysetPostBody(None) # StudysetPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Studyset
        api_response = api_instance.studysets_post(studyset_post_body=studyset_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling StudysetApi->studysets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studyset_post_body** | [**StudysetPostBody**](StudysetPostBody.md)|  | [optional]

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

