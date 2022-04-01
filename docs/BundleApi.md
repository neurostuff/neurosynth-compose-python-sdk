# neurosynth_compose_sdk.BundleApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_get**](BundleApi.md#meta_analyses_get) | **GET** /meta-analyses | Your GET endpoint
[**meta_analyses_id_get**](BundleApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | Your GET endpoint
[**meta_analyses_id_put**](BundleApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update Bundle
[**meta_analyses_post**](BundleApi.md#meta_analyses_post) | **POST** /meta-analyses | Create Bundle


# **meta_analyses_get**
> MetaAnalysisList meta_analyses_get()

Your GET endpoint

list all runnable meta-analysis, studyset, annotation bundles

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import bundle_api
from neurosynth_compose_sdk.model.meta_analysis_list import MetaAnalysisList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)
    nested = "nested_example" # str | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analyses_get(nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **str**| show nested component instead of id | [optional]

### Return type

[**MetaAnalysisList**](MetaAnalysisList.md)

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

# **meta_analyses_id_get**
> MetaAnalysisReturn meta_analyses_id_get(id)

Your GET endpoint

get a bundle (specification, annotation, and studyset)

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import bundle_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)
    id = "id_example" # str | 
    nested = "nested_example" # str | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analyses_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analyses_id_get(id, nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **nested** | **str**| show nested component instead of id | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

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

# **meta_analyses_id_put**
> MetaAnalysisReturn meta_analyses_id_put(id)

Update Bundle

update an existing meta-analysis (that has not yet been run)

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import bundle_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
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
    api_instance = bundle_api.BundleApi(api_client)
    id = "id_example" # str | 
    meta_analysis = MetaAnalysis(
        specification=None,
        studyset=None,
        annotation=None,
        name="name_example",
        description="description_example",
    ) # MetaAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Bundle
        api_response = api_instance.meta_analyses_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Bundle
        api_response = api_instance.meta_analyses_id_put(id, meta_analysis=meta_analysis)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **meta_analysis** | [**MetaAnalysis**](MetaAnalysis.md)|  | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

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

# **meta_analyses_post**
> MetaAnalysisReturn meta_analyses_post()

Create Bundle

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import bundle_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.meta_analysis import MetaAnalysis
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
    api_instance = bundle_api.BundleApi(api_client)
    meta_analysis = MetaAnalysis(
        specification=None,
        studyset=None,
        annotation=None,
        name="name_example",
        description="description_example",
    ) # MetaAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Bundle
        api_response = api_instance.meta_analyses_post(meta_analysis=meta_analysis)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling BundleApi->meta_analyses_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_analysis** | [**MetaAnalysis**](MetaAnalysis.md)|  | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

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

