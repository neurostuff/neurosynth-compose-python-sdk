# neurosynth_compose_sdk.AnnotationApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](AnnotationApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
[**annotations_id_get**](AnnotationApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
[**annotations_id_put**](AnnotationApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
[**annotations_post**](AnnotationApi.md#annotations_post) | **POST** /annotations | Create a new Annotation


# **annotations_get**
> AnnotationList annotations_get()

GET a list of annotations

get a list of serialized/referenced annotations

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_list import AnnotationList
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
    api_instance = annotation_api.AnnotationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET a list of annotations
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
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotations_id_get**
> AnnotationReturn annotations_id_get(id)

GET information about an annotation

get a single annotation

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
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
    api_instance = annotation_api.AnnotationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GET information about an annotation
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
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotations_id_put**
> AnnotationReturn annotations_id_put(id)

Update an Annotation

update an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_update import AnnotationUpdate
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
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
    api_instance = annotation_api.AnnotationApi(api_client)
    id = "id_example" # str | 
    annotation_update = AnnotationUpdate(None) # AnnotationUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id, annotation_update=annotation_update)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **annotation_update** | [**AnnotationUpdate**](AnnotationUpdate.md)|  | [optional]

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotations_post**
> AnnotationReturn annotations_post()

Create a new Annotation

create a new serialized/referenced annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import annotation_api
from neurosynth_compose_sdk.model.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.annotation_post_body import AnnotationPostBody
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
    annotation_post_body = AnnotationPostBody(None) # AnnotationPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Annotation
        api_response = api_instance.annotations_post(annotation_post_body=annotation_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling AnnotationApi->annotations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_post_body** | [**AnnotationPostBody**](AnnotationPostBody.md)|  | [optional]

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

