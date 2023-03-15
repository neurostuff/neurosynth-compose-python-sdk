# neurosynth_compose_sdk.NeurovaultApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**neurovault_collections_get**](NeurovaultApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Your GET endpoint
[**neurovault_collections_id_get**](NeurovaultApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
[**neurovault_collections_id_put**](NeurovaultApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
[**neurovault_collections_post**](NeurovaultApi.md#neurovault_collections_post) | **POST** /neurovault-collections | 
[**neurovault_files_get**](NeurovaultApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
[**neurovault_files_id_get**](NeurovaultApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
[**neurovault_files_id_put**](NeurovaultApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
[**neurovault_files_post**](NeurovaultApi.md#neurovault_files_post) | **POST** /neurovault-files | 


# **neurovault_collections_get**
> neurovault_collections_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = neurovault_api.NeurovaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_instance.neurovault_collections_get()
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_collections_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_collections_id_get**
> NeurovaultCollectionReturn neurovault_collections_id_get(id)

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_collection_return import NeurovaultCollectionReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = neurovault_api.NeurovaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_collections_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_collections_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**NeurovaultCollectionReturn**](NeurovaultCollectionReturn.md)

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

# **neurovault_collections_id_put**
> NeurovaultCollectionReturn neurovault_collections_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_collection_return import NeurovaultCollectionReturn
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
    api_instance = neurovault_api.NeurovaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.neurovault_collections_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_collections_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**NeurovaultCollectionReturn**](NeurovaultCollectionReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurovault_collections_post**
> neurovault_collections_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
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
    api_instance = neurovault_api.NeurovaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.neurovault_collections_post()
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_collections_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **neurovault_files_get**
> NeurovaultFileList neurovault_files_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_file_list import NeurovaultFileList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = neurovault_api.NeurovaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_files_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NeurovaultFileList**](NeurovaultFileList.md)

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

# **neurovault_files_id_get**
> NeurovaultFileReturn neurovault_files_id_get(id)

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = neurovault_api.NeurovaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_files_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**NeurovaultFileReturn**](NeurovaultFileReturn.md)

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

# **neurovault_files_id_put**
> NeurovaultFileReturn neurovault_files_id_put(id)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
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
    api_instance = neurovault_api.NeurovaultApi(api_client)
    id = "id_example" # str | 
    collection_id = "collection_id_example" # str |  (optional)
    exception = "exception_example" # str, none_type |  (optional)
    traceback = "traceback_example" # str, none_type |  (optional)
    status = "status_example" # str |  (optional)
    file = 'YQ==' # str |  (optional)
    image_id = "image_id_example" # str, none_type |  (optional)
    name = "name_example" # str, none_type |  (optional)
    map_type = "map_type_example" # str, none_type |  (optional)
    cognitive_contrast_cogatlas = "cognitive_contrast_cogatlas_example" # str, none_type |  (optional)
    cognitive_contrast_cogatlas_id = "cognitive_contrast_cogatlas_id_example" # str, none_type |  (optional)
    cognitive_paradigm_cogatlas = "cognitive_paradigm_cogatlas_example" # str, none_type |  (optional)
    cognitive_paradigm_cogatlas_id = "cognitive_paradigm_cogatlas_id_example" # str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.neurovault_files_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_files_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.neurovault_files_id_put(id, collection_id=collection_id, exception=exception, traceback=traceback, status=status, file=file, image_id=image_id, name=name, map_type=map_type, cognitive_contrast_cogatlas=cognitive_contrast_cogatlas, cognitive_contrast_cogatlas_id=cognitive_contrast_cogatlas_id, cognitive_paradigm_cogatlas=cognitive_paradigm_cogatlas, cognitive_paradigm_cogatlas_id=cognitive_paradigm_cogatlas_id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_files_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **collection_id** | **str**|  | [optional]
 **exception** | **str, none_type**|  | [optional]
 **traceback** | **str, none_type**|  | [optional]
 **status** | **str**|  | [optional]
 **file** | **str**|  | [optional]
 **image_id** | **str, none_type**|  | [optional]
 **name** | **str, none_type**|  | [optional]
 **map_type** | **str, none_type**|  | [optional]
 **cognitive_contrast_cogatlas** | **str, none_type**|  | [optional]
 **cognitive_contrast_cogatlas_id** | **str, none_type**|  | [optional]
 **cognitive_paradigm_cogatlas** | **str, none_type**|  | [optional]
 **cognitive_paradigm_cogatlas_id** | **str, none_type**|  | [optional]

### Return type

[**NeurovaultFileReturn**](NeurovaultFileReturn.md)

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

# **neurovault_files_post**
> NeurovaultFileReturn neurovault_files_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import neurovault_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from neurosynth_compose_sdk.model.neurovault_file import NeurovaultFile
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
    api_instance = neurovault_api.NeurovaultApi(api_client)
    neurovault_file = NeurovaultFile(
        collection_id="collection_id_example",
        exception="exception_example",
        traceback="traceback_example",
        status="status_example",
        file='YQ==',
        image_id="image_id_example",
        name="name_example",
        map_type="map_type_example",
        cognitive_contrast_cogatlas="cognitive_contrast_cogatlas_example",
        cognitive_contrast_cogatlas_id="cognitive_contrast_cogatlas_id_example",
        cognitive_paradigm_cogatlas="cognitive_paradigm_cogatlas_example",
        cognitive_paradigm_cogatlas_id="cognitive_paradigm_cogatlas_id_example",
    ) # NeurovaultFile |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.neurovault_files_post(neurovault_file=neurovault_file)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling NeurovaultApi->neurovault_files_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neurovault_file** | [**NeurovaultFile**](NeurovaultFile.md)|  | [optional]

### Return type

[**NeurovaultFileReturn**](NeurovaultFileReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
