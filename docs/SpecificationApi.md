# neurosynth_compose_sdk.SpecificationApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specifications_get**](SpecificationApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](SpecificationApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**specifications_id_put**](SpecificationApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**specifications_post**](SpecificationApi.md#specifications_post) | **POST** /specifications | Create a Specification


# **specifications_get**
> SpecificationList specifications_get()

Get a list of Specifications

list of meta-analysis specifications

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import specification_api
from neurosynth_compose_sdk.model.specification_list import SpecificationList
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
    api_instance = specification_api.SpecificationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of Specifications
        api_response = api_instance.specifications_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling SpecificationApi->specifications_get: %s\n" % e)
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import specification_api
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = specification_api.SpecificationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a Specification
        api_response = api_instance.specifications_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling SpecificationApi->specifications_id_get: %s\n" % e)
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
> SpecificationReturn specifications_id_put(id)

Update Meta-Analysis specification

update an existing meta analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import specification_api
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.specification import Specification
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
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
    api_instance = specification_api.SpecificationApi(api_client)
    id = "id_example" # str | 
    specification = Specification(
        type="type_example",
        estimator=Estimator(
            type="MKDADensity",
            args={},
        ),
        mask="mask_example",
        contrast="contrast_example",
        transformer="transformer_example",
        corrector=Corrector(
            type="FWECorrector",
            args={},
        ),
        filter="filter_example",
    ) # Specification |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling SpecificationApi->specifications_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id, specification=specification)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling SpecificationApi->specifications_id_put: %s\n" % e)
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
> SpecificationReturn specifications_post()

Create a Specification

create a new meta-analysis specification

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import specification_api
from neurosynth_compose_sdk.model.specification_post_body import SpecificationPostBody
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
from neurosynth_compose_sdk.model.specification_return import SpecificationReturn
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
    api_instance = specification_api.SpecificationApi(api_client)
    specification_post_body = SpecificationPostBody(None) # SpecificationPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Specification
        api_response = api_instance.specifications_post(specification_post_body=specification_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling SpecificationApi->specifications_post: %s\n" % e)
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

