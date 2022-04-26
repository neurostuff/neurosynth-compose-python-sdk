# neurosynth_compose_sdk.AnnotationApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](AnnotationApi.md#annotations_get) | **GET** /annotations | Your GET endpoint
[**annotations_id_get**](AnnotationApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
[**annotations_id_put**](AnnotationApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update Annotation
[**annotations_post**](AnnotationApi.md#annotations_post) | **POST** /annotations | Create Annotation


# **annotations_get**
> AnnotationList annotations_get()

Your GET endpoint

get a list of serialized annotations

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_response = api_instance.annotations_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AnnotationList**](AnnotationList.md)

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

# **annotations_id_get**
> AnnotationReturn annotations_id_get(id)

Your GET endpoint

get a single annotation

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_api.AnnotationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

# **annotations_id_put**
> AnnotationReturn annotations_id_put(id)

Update Annotation

update an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
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
    api_instance = annotation_api.AnnotationApi(api_client)
    id = "id_example" # str | 
    annotation = Annotation(
        neurostore_id="neurostore_id_example",
        snapshot={},
        studyset="studyset_example",
    ) # Annotation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Annotation
        api_response = api_instance.annotations_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Annotation
        api_response = api_instance.annotations_id_put(id, annotation=annotation)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **annotation** | [**Annotation**](Annotation.md)|  | [optional]

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

# **annotations_post**
> AnnotationReturn annotations_post()

Create Annotation

create a new serialized annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation import Annotation
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
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
    api_instance = annotation_api.AnnotationApi(api_client)
    annotation = Annotation(
        neurostore_id="neurostore_id_example",
        snapshot={},
        studyset="studyset_example",
    ) # Annotation |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Annotation
        api_response = api_instance.annotations_post(annotation=annotation)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | [**Annotation**](Annotation.md)|  | [optional]

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

