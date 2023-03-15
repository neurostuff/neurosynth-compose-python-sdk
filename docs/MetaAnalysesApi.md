# neurosynth_compose_sdk.MetaAnalysesApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_get**](MetaAnalysesApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](MetaAnalysesApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
[**meta_analyses_id_put**](MetaAnalysesApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
[**meta_analyses_post**](MetaAnalysesApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
[**meta_analysis_results_get**](MetaAnalysesApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
[**meta_analysis_results_id_get**](MetaAnalysesApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
[**meta_analysis_results_id_put**](MetaAnalysesApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
[**meta_analysis_results_post**](MetaAnalysesApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 


# **meta_analyses_get**
> MetaAnalysisList meta_analyses_get()

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_list import MetaAnalysisList
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
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    nested = True # bool | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET a list of meta-analyses
        api_response = api_instance.meta_analyses_get(nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional]

### Return type

[**MetaAnalysisList**](MetaAnalysisList.md)

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

# **meta_analyses_id_get**
> MetaAnalysisReturn meta_analyses_id_get(id)

GET meta-analysis information

get a meta-analysis (specification, annotation, and studyset)

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    id = "id_example" # str | 
    nested = True # bool | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id, nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **nested** | **bool**| show nested component instead of id | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

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

# **meta_analyses_id_put**
> MetaAnalysisReturn meta_analyses_id_put(id)

Update a meta-analysis

update an existing meta-analysis (that has not yet been run)

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
from neurosynth_compose_sdk.model.inline_response400 import InlineResponse400
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
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    id = "id_example" # str | 
    meta_analysis = MetaAnalysis(
        specification=None,
        studyset=None,
        annotation=None,
        name="name_example",
        description="description_example",
        internal_studyset_id="internal_studyset_id_example",
        internal_annotation_id="internal_annotation_id_example",
        results=[
            None,
        ],
        provenance={},
        project="project_example",
    ) # MetaAnalysis |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id, meta_analysis=meta_analysis)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_id_put: %s\n" % e)
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

# **meta_analyses_post**
> MetaAnalysisReturn meta_analyses_post()

Create a new meta-analysis

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.model.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    meta_analysis_post_body = MetaAnalysisPostBody(None) # MetaAnalysisPostBody |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new meta-analysis
        api_response = api_instance.meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analyses_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_analysis_post_body** | [**MetaAnalysisPostBody**](MetaAnalysisPostBody.md)|  | [optional]

### Return type

[**MetaAnalysisReturn**](MetaAnalysisReturn.md)

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

# **meta_analysis_results_get**
> ResultList meta_analysis_results_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.result_list import ResultList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    meta_analysis_id = "meta_analysis_id_example" # str | search for results with this meta-analysis id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_get(meta_analysis_id=meta_analysis_id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_analysis_id** | **str**| search for results with this meta-analysis id | [optional]

### Return type

[**ResultList**](ResultList.md)

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

# **meta_analysis_results_id_get**
> ResultReturn meta_analysis_results_id_get(id)

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ResultReturn**](ResultReturn.md)

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

# **meta_analysis_results_id_put**
> ResultReturn meta_analysis_results_id_put(id)



### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    id = "id_example" # str | 
    result = Result(
        images={},
        meta_analysis_id="meta_analysis_id_example",
        cli_version="cli_version_example",
        estimator=Estimator(
            type="MKDADensity",
            args={},
        ),
        neurostore_id="neurostore_id_example",
        neurovault_collection=NeurovaultCollection(
            files=[
                None,
            ],
        ),
    ) # Result |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.meta_analysis_results_id_put(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.meta_analysis_results_id_put(id, result=result)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **result** | [**Result**](Result.md)|  | [optional]

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analysis_results_post**
> ResultReturn meta_analysis_results_post()



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import meta_analyses_api
from neurosynth_compose_sdk.model.result_return import ResultReturn
from neurosynth_compose_sdk.model.result import Result
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
    api_instance = meta_analyses_api.MetaAnalysesApi(api_client)
    result = Result(
        images={},
        meta_analysis_id="meta_analysis_id_example",
        cli_version="cli_version_example",
        estimator=Estimator(
            type="MKDADensity",
            args={},
        ),
        neurostore_id="neurostore_id_example",
        neurovault_collection=NeurovaultCollection(
            files=[
                None,
            ],
        ),
    ) # Result |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.meta_analysis_results_post(result=result)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling MetaAnalysesApi->meta_analysis_results_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | [**Result**](Result.md)|  | [optional]

### Return type

[**ResultReturn**](ResultReturn.md)

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

