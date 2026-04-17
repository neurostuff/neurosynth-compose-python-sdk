# neurosynth_compose_sdk.DefaultApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_id_delete**](DefaultApi.md#meta_analyses_id_delete) | **DELETE** /meta-analyses/{id} | 
[**neurostore_annotations_id_get**](DefaultApi.md#neurostore_annotations_id_get) | **GET** /neurostore-annotations/{id} | Get a Neurostore annotation reference by Neurostore ID
[**neurostore_studies_get**](DefaultApi.md#neurostore_studies_get) | **GET** /neurostore-studies | Your GET endpoint
[**neurostore_studies_id_get**](DefaultApi.md#neurostore_studies_id_get) | **GET** /neurostore-studies/{id} | Your GET endpoint
[**neurostore_studies_id_put**](DefaultApi.md#neurostore_studies_id_put) | **PUT** /neurostore-studies/{id} | 
[**neurostore_studies_post**](DefaultApi.md#neurostore_studies_post) | **POST** /neurostore-studies | 
[**neurostore_studysets_get**](DefaultApi.md#neurostore_studysets_get) | **GET** /neurostore-studysets | List Neurostore studyset references
[**neurostore_studysets_id_get**](DefaultApi.md#neurostore_studysets_id_get) | **GET** /neurostore-studysets/{id} | Get a Neurostore studyset reference by Neurostore ID


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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_annotations_id_get**
> AnnotationReferenceReturn neurostore_annotations_id_get(id)

Get a Neurostore annotation reference by Neurostore ID

Resolve a Neurostore annotation reference using the same ID exposed by the Neurostore API.

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_reference_return import AnnotationReferenceReturn
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

    try:
        # Get a Neurostore annotation reference by Neurostore ID
        api_response = api_instance.neurostore_annotations_id_get(id)
        print("The response of DefaultApi->neurostore_annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_annotations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AnnotationReferenceReturn**](AnnotationReferenceReturn.md)

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

# **neurostore_studies_get**
> NeurostoreStudyList neurostore_studies_get()

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurostore_study_list import NeurostoreStudyList
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

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_get()
        print("The response of DefaultApi->neurostore_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studies_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NeurostoreStudyList**](NeurostoreStudyList.md)

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

# **neurostore_studies_id_get**
> NeurostoreStudyReturn neurostore_studies_id_get(id)

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn
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

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_id_get(id)
        print("The response of DefaultApi->neurostore_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NeurostoreStudyReturn**](NeurostoreStudyReturn.md)

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

# **neurostore_studies_id_put**
> NeurostoreStudyReturn neurostore_studies_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn
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
        api_response = api_instance.neurostore_studies_id_put(id)
        print("The response of DefaultApi->neurostore_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studies_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NeurostoreStudyReturn**](NeurostoreStudyReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_studies_post**
> NeurostoreStudyReturn neurostore_studies_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurostore_study_return import NeurostoreStudyReturn
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

    try:
        # 
        api_response = api_instance.neurostore_studies_post()
        print("The response of DefaultApi->neurostore_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studies_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NeurostoreStudyReturn**](NeurostoreStudyReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_studysets_get**
> StudysetReferenceList neurostore_studysets_get(nested=nested)

List Neurostore studyset references

List reference rows keyed by the actual Neurostore studyset ID.

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
        # List Neurostore studyset references
        api_response = api_instance.neurostore_studysets_get(nested=nested)
        print("The response of DefaultApi->neurostore_studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studysets_get: %s\n" % e)
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

# **neurostore_studysets_id_get**
> StudysetReferenceReturn neurostore_studysets_id_get(id, nested=nested)

Get a Neurostore studyset reference by Neurostore ID

Resolve a Neurostore studyset reference using the same ID exposed by the Neurostore API. By default, this returns each linked snapshot with its compose snapshot ID and md5.

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
        # Get a Neurostore studyset reference by Neurostore ID
        api_response = api_instance.neurostore_studysets_id_get(id, nested=nested)
        print("The response of DefaultApi->neurostore_studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->neurostore_studysets_id_get: %s\n" % e)
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

