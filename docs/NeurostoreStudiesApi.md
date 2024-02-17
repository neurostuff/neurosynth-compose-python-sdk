# neurosynth_compose_sdk.NeurostoreStudiesApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**neurostore_studies_get**](NeurostoreStudiesApi.md#neurostore_studies_get) | **GET** /neurostore-studies | Your GET endpoint
[**neurostore_studies_id_get**](NeurostoreStudiesApi.md#neurostore_studies_id_get) | **GET** /neurostore-studies/{id} | Your GET endpoint
[**neurostore_studies_id_put**](NeurostoreStudiesApi.md#neurostore_studies_id_put) | **PUT** /neurostore-studies/{id} | 
[**neurostore_studies_post**](NeurostoreStudiesApi.md#neurostore_studies_post) | **POST** /neurostore-studies | 


# **neurostore_studies_get**
> NeurostoreStudyList neurostore_studies_get()

Your GET endpoint

### Example

```python
import time
import os
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
    api_instance = neurosynth_compose_sdk.NeurostoreStudiesApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_get()
        print("The response of NeurostoreStudiesApi->neurostore_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudiesApi->neurostore_studies_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurosynth_compose_sdk.NeurostoreStudiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_id_get(id)
        print("The response of NeurostoreStudiesApi->neurostore_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudiesApi->neurostore_studies_id_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurosynth_compose_sdk.NeurostoreStudiesApi(api_client)
    id = 'id_example' # str | 

    try:
        # 
        api_response = api_instance.neurostore_studies_id_put(id)
        print("The response of NeurostoreStudiesApi->neurostore_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudiesApi->neurostore_studies_id_put: %s\n" % e)
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
import time
import os
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
    api_instance = neurosynth_compose_sdk.NeurostoreStudiesApi(api_client)

    try:
        # 
        api_response = api_instance.neurostore_studies_post()
        print("The response of NeurostoreStudiesApi->neurostore_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudiesApi->neurostore_studies_post: %s\n" % e)
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

