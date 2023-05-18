# neurosynth_compose_sdk.SpecificationsApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specifications_get**](SpecificationsApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](SpecificationsApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**specifications_id_put**](SpecificationsApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**specifications_post**](SpecificationsApi.md#specifications_post) | **POST** /specifications | Create a Specification


# **specifications_get**
> SpecificationList specifications_get()

Get a list of Specifications

list of meta-analysis specifications

### Example

```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.specification_list import SpecificationList
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
    api_instance = neurosynth_compose_sdk.SpecificationsApi(api_client)

    try:
        # Get a list of Specifications
        api_response = api_instance.specifications_get()
        print("The response of SpecificationsApi->specifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpecificationsApi->specifications_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SpecificationList**](SpecificationList.md)

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

# **specifications_id_get**
> SpecificationReturn specifications_id_get(id)

Get information about a Specification

get a meta-analysis specification

### Example

```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.specification_return import SpecificationReturn
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
    api_instance = neurosynth_compose_sdk.SpecificationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Specification
        api_response = api_instance.specifications_id_get(id)
        print("The response of SpecificationsApi->specifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpecificationsApi->specifications_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SpecificationReturn**](SpecificationReturn.md)

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

# **specifications_id_put**
> SpecificationReturn specifications_id_put(id, specification=specification)

Update Meta-Analysis specification

update an existing meta analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.specification import Specification
from neurosynth_compose_sdk.models.specification_return import SpecificationReturn
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
    api_instance = neurosynth_compose_sdk.SpecificationsApi(api_client)
    id = 'id_example' # str | 
    specification = neurosynth_compose_sdk.Specification() # Specification |  (optional)

    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id, specification=specification)
        print("The response of SpecificationsApi->specifications_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpecificationsApi->specifications_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **specification** | [**Specification**](Specification.md)|  | [optional] 

### Return type

[**SpecificationReturn**](SpecificationReturn.md)

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

# **specifications_post**
> SpecificationReturn specifications_post(specification_post_body=specification_post_body)

Create a Specification

create a new meta-analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.specification_post_body import SpecificationPostBody
from neurosynth_compose_sdk.models.specification_return import SpecificationReturn
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
    api_instance = neurosynth_compose_sdk.SpecificationsApi(api_client)
    specification_post_body = neurosynth_compose_sdk.SpecificationPostBody() # SpecificationPostBody |  (optional)

    try:
        # Create a Specification
        api_response = api_instance.specifications_post(specification_post_body=specification_post_body)
        print("The response of SpecificationsApi->specifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpecificationsApi->specifications_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification_post_body** | [**SpecificationPostBody**](SpecificationPostBody.md)|  | [optional] 

### Return type

[**SpecificationReturn**](SpecificationReturn.md)

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
**422** | Unprocessable Entity (WebDAV) |  -  |
**500** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

