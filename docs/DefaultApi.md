# neurosynth_compose_sdk.DefaultApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_id_delete**](DefaultApi.md#meta_analyses_id_delete) | **DELETE** /meta-analyses/{id} | 
[**studyset_references_get**](DefaultApi.md#studyset_references_get) | **GET** /studyset-references | Your GET endpoint
[**studyset_references_id_get**](DefaultApi.md#studyset_references_id_get) | **GET** /studyset-references/{id} | Your GET endpoint


# **meta_analyses_id_delete**
> meta_analyses_id_delete(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurosynth_compose_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # 
        api_instance.meta_analyses_id_delete(id)
    except Exception as e:
        print("Exception when calling DefaultApi->meta_analyses_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studyset_references_get**
> StudysetReferenceList studyset_references_get(nested=nested)

Your GET endpoint



### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_reference_list import StudysetReferenceList
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.DefaultApi(api_client)
    nested = True # bool | show nested component instead of id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.studyset_references_get(nested=nested)
        print("The response of DefaultApi->studyset_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->studyset_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 

### Return type

[**StudysetReferenceList**](StudysetReferenceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studyset_references_id_get**
> StudysetReferenceReturn studyset_references_id_get(id, nested=nested)

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_reference_return import StudysetReferenceReturn
from neurosynth_compose_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://compose.neurosynth.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "https://compose.neurosynth.org/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | show nested component instead of id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.studyset_references_id_get(id, nested=nested)
        print("The response of DefaultApi->studyset_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->studyset_references_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| show nested component instead of id | [optional] 

### Return type

[**StudysetReferenceReturn**](StudysetReferenceReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

