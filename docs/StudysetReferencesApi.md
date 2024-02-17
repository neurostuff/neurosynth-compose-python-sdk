# neurosynth_compose_sdk.StudysetReferencesApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studyset_references_get**](StudysetReferencesApi.md#studyset_references_get) | **GET** /studyset-references | Your GET endpoint
[**studyset_references_id_get**](StudysetReferencesApi.md#studyset_references_id_get) | **GET** /studyset-references/{id} | Your GET endpoint


# **studyset_references_get**
> StudysetReferenceList studyset_references_get(nested=nested)

Your GET endpoint



### Example

```python
import time
import os
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
    api_instance = neurosynth_compose_sdk.StudysetReferencesApi(api_client)
    nested = True # bool | show nested component instead of id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.studyset_references_get(nested=nested)
        print("The response of StudysetReferencesApi->studyset_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudysetReferencesApi->studyset_references_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurosynth_compose_sdk.StudysetReferencesApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | show nested component instead of id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.studyset_references_id_get(id, nested=nested)
        print("The response of StudysetReferencesApi->studyset_references_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudysetReferencesApi->studyset_references_id_get: %s\n" % e)
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

