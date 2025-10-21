# neurosynth_compose_sdk.GetApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](GetApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
[**annotations_id_get**](GetApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
[**meta_analyses_get**](GetApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](GetApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
[**meta_analysis_results_get**](GetApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
[**meta_analysis_results_id_get**](GetApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
[**neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get**](GetApi.md#neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get) | **GET** /meta-analysis-jobs/{job_id} | Get status and logs for a meta-analysis job
[**neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get**](GetApi.md#neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get) | **GET** /meta-analysis-jobs | List meta-analysis jobs for the current user
[**projects_get**](GetApi.md#projects_get) | **GET** /projects | Your GET endpoint
[**projects_id_get**](GetApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
[**specifications_get**](GetApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](GetApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**studysets_get**](GetApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
[**studysets_id_get**](GetApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset


# **annotations_get**
> AnnotationList annotations_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)

GET a list of annotations

get a list of serialized/referenced annotations

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_list import AnnotationList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    nested = True # bool | show nested component instead of id (optional)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # GET a list of annotations
        api_response = api_instance.annotations_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)
        print("The response of GetApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->annotations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 
 **info** | **bool**| display additional information about a nested relationship without displaying fully nested object | [optional] 

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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET information about an annotation
        api_response = api_instance.annotations_id_get(id)
        print("The response of GetApi->annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->annotations_id_get: %s\n" % e)
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

# **meta_analyses_get**
> MetaAnalysisList meta_analyses_get(nested=nested, ids=ids, page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc)

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_list import MetaAnalysisList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    nested = True # bool | show nested component instead of id (optional)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    description = 'description_example' # str | search description field for a term (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)

    try:
        # GET a list of meta-analyses
        api_response = api_instance.meta_analyses_get(nested=nested, ids=ids, page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc)
        print("The response of GetApi->meta_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->meta_analyses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 

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
> MetaAnalysisReturn meta_analyses_id_get(id, nested=nested)

GET meta-analysis information

get a meta-analysis (specification, annotation, and studyset)

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | show nested component instead of id (optional)

    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id, nested=nested)
        print("The response of GetApi->meta_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->meta_analyses_id_get: %s\n" % e)
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

# **meta_analysis_results_get**
> ResultList meta_analysis_results_get(meta_analysis_id=meta_analysis_id)

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result_list import ResultList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    meta_analysis_id = 'meta_analysis_id_example' # str | search for results with this meta-analysis id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_get(meta_analysis_id=meta_analysis_id)
        print("The response of GetApi->meta_analysis_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->meta_analysis_results_get: %s\n" % e)
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result_return import ResultReturn
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_id_get(id)
        print("The response of GetApi->meta_analysis_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->meta_analysis_results_id_get: %s\n" % e)
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

# **neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get**
> MetaAnalysisJobResponse neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get(job_id)

Get status and logs for a meta-analysis job

Retrieve the most recent status information and logs for a submitted job.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_job_response import MetaAnalysisJobResponse
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get status and logs for a meta-analysis job
        api_response = api_instance.neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get(job_id)
        print("The response of GetApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**MetaAnalysisJobResponse**](MetaAnalysisJobResponse.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**502** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get**
> MetaAnalysisJobList neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get()

List meta-analysis jobs for the current user

Return cached job submissions associated with the authenticated user.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_job_list import MetaAnalysisJobList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)

    try:
        # List meta-analysis jobs for the current user
        api_response = api_instance.neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get()
        print("The response of GetApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetaAnalysisJobList**](MetaAnalysisJobList.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | form when a request goes wrong |  -  |
**502** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> ProjectList projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id)

Your GET endpoint

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project_list import ProjectList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    description = 'description_example' # str | search description field for a term (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id)
        print("The response of GetApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

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

# **projects_id_get**
> ProjectReturn projects_id_get(id, info=info)

Your GET endpoint

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project_return import ProjectReturn
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_id_get(id, info=info)
        print("The response of GetApi->projects_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->projects_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **info** | **bool**| display additional information about a nested relationship without displaying fully nested object | [optional] 

### Return type

[**ProjectReturn**](ProjectReturn.md)

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

# **specifications_get**
> SpecificationList specifications_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)

Get a list of Specifications

list of meta-analysis specifications

### Example


```python
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    nested = True # bool | show nested component instead of id (optional)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # Get a list of Specifications
        api_response = api_instance.specifications_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)
        print("The response of GetApi->specifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->specifications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 
 **info** | **bool**| display additional information about a nested relationship without displaying fully nested object | [optional] 

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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Specification
        api_response = api_instance.specifications_id_get(id)
        print("The response of GetApi->specifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->specifications_id_get: %s\n" % e)
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

# **studysets_get**
> StudysetList studysets_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)

Get a list of Studysets

get a list of serialized/referenced studysets

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_list import StudysetList
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    nested = True # bool | show nested component instead of id (optional)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # Get a list of Studysets
        api_response = api_instance.studysets_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)
        print("The response of GetApi->studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->studysets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 
 **info** | **bool**| display additional information about a nested relationship without displaying fully nested object | [optional] 

### Return type

[**StudysetList**](StudysetList.md)

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

# **studysets_id_get**
> StudysetReturn studysets_id_get(id)

Get information about a Studyset

get a single serialized/referenced studyset

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Studyset
        api_response = api_instance.studysets_id_get(id)
        print("The response of GetApi->studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->studysets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StudysetReturn**](StudysetReturn.md)

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

