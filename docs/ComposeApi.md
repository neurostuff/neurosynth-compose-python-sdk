# neurosynth_compose_sdk.ComposeApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](ComposeApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
[**annotations_id_get**](ComposeApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
[**annotations_id_put**](ComposeApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
[**annotations_post**](ComposeApi.md#annotations_post) | **POST** /annotations | Create a new Annotation
[**meta_analyses_get**](ComposeApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](ComposeApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
[**meta_analyses_id_put**](ComposeApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
[**meta_analyses_post**](ComposeApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
[**meta_analysis_results_get**](ComposeApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
[**meta_analysis_results_id_get**](ComposeApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
[**meta_analysis_results_id_put**](ComposeApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
[**meta_analysis_results_post**](ComposeApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | 
[**neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get**](ComposeApi.md#neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get) | **GET** /meta-analysis-jobs/{job_id} | Get status and logs for a meta-analysis job
[**neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get**](ComposeApi.md#neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get) | **GET** /meta-analysis-jobs | List meta-analysis jobs for the current user
[**neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post**](ComposeApi.md#neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post) | **POST** /meta-analysis-jobs | Submit a meta-analysis job
[**projects_get**](ComposeApi.md#projects_get) | **GET** /projects | Your GET endpoint
[**projects_id_delete**](ComposeApi.md#projects_id_delete) | **DELETE** /projects/{id} | 
[**projects_id_get**](ComposeApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
[**projects_id_put**](ComposeApi.md#projects_id_put) | **PUT** /projects/{id} | 
[**projects_post**](ComposeApi.md#projects_post) | **POST** /projects | 
[**specifications_get**](ComposeApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](ComposeApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**specifications_id_put**](ComposeApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**specifications_post**](ComposeApi.md#specifications_post) | **POST** /specifications | Create a Specification
[**studysets_get**](ComposeApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
[**studysets_id_get**](ComposeApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset
[**studysets_id_put**](ComposeApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset
[**studysets_post**](ComposeApi.md#studysets_post) | **POST** /studysets | Create a new Studyset
[**tags_get**](ComposeApi.md#tags_get) | **GET** /tags | Get a list of Tags
[**tags_id_get**](ComposeApi.md#tags_id_get) | **GET** /tags/{id} | Get information about a Tag
[**tags_post**](ComposeApi.md#tags_post) | **POST** /tags | Create a new Tag


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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
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
        print("The response of ComposeApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->annotations_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET information about an annotation
        api_response = api_instance.annotations_id_get(id)
        print("The response of ComposeApi->annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->annotations_id_get: %s\n" % e)
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
> AnnotationReturn annotations_id_put(id, annotation_update=annotation_update)

Update an Annotation

update an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn
from neurosynth_compose_sdk.models.annotation_update import AnnotationUpdate
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    annotation_update = neurosynth_compose_sdk.AnnotationUpdate() # AnnotationUpdate |  (optional)

    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id, annotation_update=annotation_update)
        print("The response of ComposeApi->annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->annotations_id_put: %s\n" % e)
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
> AnnotationReturn annotations_post(annotation_post_body=annotation_post_body)

Create a new Annotation

create a new serialized/referenced annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_post_body import AnnotationPostBody
from neurosynth_compose_sdk.models.annotation_return import AnnotationReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    annotation_post_body = neurosynth_compose_sdk.AnnotationPostBody() # AnnotationPostBody |  (optional)

    try:
        # Create a new Annotation
        api_response = api_instance.annotations_post(annotation_post_body=annotation_post_body)
        print("The response of ComposeApi->annotations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->annotations_post: %s\n" % e)
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

# **meta_analyses_get**
> MetaAnalysisList meta_analyses_get(nested=nested, ids=ids, page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc)

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example

* Bearer Authentication (JSON-Web-Token):

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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
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
        print("The response of ComposeApi->meta_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analyses_get: %s\n" % e)
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

[JSON-Web-Token](../README.md#JSON-Web-Token)

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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | show nested component instead of id (optional)

    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id, nested=nested)
        print("The response of ComposeApi->meta_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analyses_id_get: %s\n" % e)
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
> MetaAnalysisReturn meta_analyses_id_put(id, meta_analysis=meta_analysis)

Update a meta-analysis

update an existing meta-analysis (that has not yet been run)

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis import MetaAnalysis
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    meta_analysis = neurosynth_compose_sdk.MetaAnalysis() # MetaAnalysis |  (optional)

    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id, meta_analysis=meta_analysis)
        print("The response of ComposeApi->meta_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analyses_id_put: %s\n" % e)
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
> MetaAnalysisReturn meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)

Create a new meta-analysis

create a new specification, studyset, annotation bundle

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_post_body import MetaAnalysisPostBody
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    meta_analysis_post_body = neurosynth_compose_sdk.MetaAnalysisPostBody() # MetaAnalysisPostBody |  (optional)

    try:
        # Create a new meta-analysis
        api_response = api_instance.meta_analyses_post(meta_analysis_post_body=meta_analysis_post_body)
        print("The response of ComposeApi->meta_analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analyses_post: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    meta_analysis_id = 'meta_analysis_id_example' # str | search for results with this meta-analysis id (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_get(meta_analysis_id=meta_analysis_id)
        print("The response of ComposeApi->meta_analysis_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_results_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_id_get(id)
        print("The response of ComposeApi->meta_analysis_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_results_id_get: %s\n" % e)
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
> ResultReturn meta_analysis_results_id_put(id, result=result)



### Example

* Bearer Authentication (JSON-Web-Token):
* Api Key Authentication (upload_key):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result import Result
from neurosynth_compose_sdk.models.result_return import ResultReturn
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

# Configure API key authorization: upload_key
configuration.api_key['upload_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['upload_key'] = 'Bearer'

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    result = neurosynth_compose_sdk.Result() # Result |  (optional)

    try:
        # 
        api_response = api_instance.meta_analysis_results_id_put(id, result=result)
        print("The response of ComposeApi->meta_analysis_results_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_results_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **result** | [**Result**](Result.md)|  | [optional] 

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token), [upload_key](../README.md#upload_key)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analysis_results_post**
> ResultReturn meta_analysis_results_post(result_init=result_init)



### Example

* Bearer Authentication (JSON-Web-Token):
* Api Key Authentication (upload_key):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result_init import ResultInit
from neurosynth_compose_sdk.models.result_return import ResultReturn
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

# Configure API key authorization: upload_key
configuration.api_key['upload_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['upload_key'] = 'Bearer'

# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    result_init = neurosynth_compose_sdk.ResultInit() # ResultInit |  (optional)

    try:
        # 
        api_response = api_instance.meta_analysis_results_post(result_init=result_init)
        print("The response of ComposeApi->meta_analysis_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_init** | [**ResultInit**](ResultInit.md)|  | [optional] 

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token), [upload_key](../README.md#upload_key)

### HTTP request headers

 - **Content-Type**: application/json
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get status and logs for a meta-analysis job
        api_response = api_instance.neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get(job_id)
        print("The response of ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_job_resource_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)

    try:
        # List meta-analysis jobs for the current user
        api_response = api_instance.neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get()
        print("The response of ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_get: %s\n" % e)
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

# **neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post**
> MetaAnalysisJobResponse neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post(meta_analysis_job_request)

Submit a meta-analysis job

Submit a meta-analysis to the compose runner service.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.meta_analysis_job_request import MetaAnalysisJobRequest
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    meta_analysis_job_request = neurosynth_compose_sdk.MetaAnalysisJobRequest() # MetaAnalysisJobRequest | 

    try:
        # Submit a meta-analysis job
        api_response = api_instance.neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post(meta_analysis_job_request)
        print("The response of ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurosynth_compose_resources_meta_analysis_jobs_meta_analysis_jobs_resource_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_analysis_job_request** | [**MetaAnalysisJobRequest**](MetaAnalysisJobRequest.md)|  | 

### Return type

[**MetaAnalysisJobResponse**](MetaAnalysisJobResponse.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job accepted |  -  |
**401** | form when a request goes wrong |  -  |
**403** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
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
        print("The response of ComposeApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->projects_get: %s\n" % e)
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

# **projects_id_delete**
> projects_id_delete(id)



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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # 
        api_instance.projects_id_delete(id)
    except Exception as e:
        print("Exception when calling ComposeApi->projects_id_delete: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    info = True # bool | display additional information about a nested relationship without displaying fully nested object (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_id_get(id, info=info)
        print("The response of ComposeApi->projects_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->projects_id_get: %s\n" % e)
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

# **projects_id_put**
> ProjectReturn projects_id_put(id, sync_meta_analyses_public=sync_meta_analyses_public, project=project)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project import Project
from neurosynth_compose_sdk.models.project_return import ProjectReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    sync_meta_analyses_public = True # bool | when updating a project's public flag, also set each child meta-analysis to the same public value (optional)
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_id_put(id, sync_meta_analyses_public=sync_meta_analyses_public, project=project)
        print("The response of ComposeApi->projects_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->projects_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sync_meta_analyses_public** | **bool**| when updating a project&#39;s public flag, also set each child meta-analysis to the same public value | [optional] 
 **project** | [**Project**](Project.md)|  | [optional] 

### Return type

[**ProjectReturn**](ProjectReturn.md)

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

# **projects_post**
> ProjectReturn projects_post(source_id=source_id, copy_annotations=copy_annotations, project=project)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.project import Project
from neurosynth_compose_sdk.models.project_return import ProjectReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    source_id = 'source_id_example' # str | clone an existing project when creating a new project (optional)
    copy_annotations = True # bool | when cloning via `source_id`, also duplicate associated annotations (optional)
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_post(source_id=source_id, copy_annotations=copy_annotations, project=project)
        print("The response of ComposeApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| clone an existing project when creating a new project | [optional] 
 **copy_annotations** | **bool**| when cloning via &#x60;source_id&#x60;, also duplicate associated annotations | [optional] 
 **project** | [**Project**](Project.md)|  | [optional] 

### Return type

[**ProjectReturn**](ProjectReturn.md)

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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
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
        print("The response of ComposeApi->specifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->specifications_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Specification
        api_response = api_instance.specifications_id_get(id)
        print("The response of ComposeApi->specifications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->specifications_id_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    specification = neurosynth_compose_sdk.Specification() # Specification |  (optional)

    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id, specification=specification)
        print("The response of ComposeApi->specifications_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->specifications_id_put: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    specification_post_body = neurosynth_compose_sdk.SpecificationPostBody() # SpecificationPostBody |  (optional)

    try:
        # Create a Specification
        api_response = api_instance.specifications_post(specification_post_body=specification_post_body)
        print("The response of ComposeApi->specifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->specifications_post: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
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
        print("The response of ComposeApi->studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->studysets_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Studyset
        api_response = api_instance.studysets_id_get(id)
        print("The response of ComposeApi->studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->studysets_id_get: %s\n" % e)
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

# **studysets_id_put**
> StudysetReturn studysets_id_put(id, studyset=studyset)

Update a Studyset

update an existing serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset import Studyset
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 
    studyset = neurosynth_compose_sdk.Studyset() # Studyset |  (optional)

    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id, studyset=studyset)
        print("The response of ComposeApi->studysets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->studysets_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **studyset** | [**Studyset**](Studyset.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | form when a request goes wrong |  -  |
**404** | form when a request goes wrong |  -  |
**422** | form when a request goes wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post(studyset_post_body=studyset_post_body)

Create a new Studyset

create a new serialized/referenced studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_post_body import StudysetPostBody
from neurosynth_compose_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    studyset_post_body = neurosynth_compose_sdk.StudysetPostBody() # StudysetPostBody |  (optional)

    try:
        # Create a new Studyset
        api_response = api_instance.studysets_post(studyset_post_body=studyset_post_body)
        print("The response of ComposeApi->studysets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->studysets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studyset_post_body** | [**StudysetPostBody**](StudysetPostBody.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

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

# **tags_get**
> TagList tags_get(ids=ids, page=page, page_size=page_size, name=name, search=search, filter=filter, description=description, group=group, official=official, sort=sort, desc=desc, user_id=user_id)

Get a list of Tags

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag_list import TagList
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    ids = ['ids_example'] # List[str] | choose the specific ids you wish to get (optional)
    page = 56 # int | page of results (optional)
    page_size = 56 # int | number of elements to return on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    filter = 'filter_example' # str | alias for search when filtering tags (optional)
    description = 'description_example' # str | search description field for a term (optional)
    group = 'group_example' # str | filter tags by group (optional)
    official = True # bool | filter tags by official flag (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    user_id = 'user_id_example' # str | user id you want to filter on (optional)

    try:
        # Get a list of Tags
        api_response = api_instance.tags_get(ids=ids, page=page, page_size=page_size, name=name, search=search, filter=filter, description=description, group=group, official=official, sort=sort, desc=desc, user_id=user_id)
        print("The response of ComposeApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| choose the specific ids you wish to get | [optional] 
 **page** | **int**| page of results | [optional] 
 **page_size** | **int**| number of elements to return on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **filter** | **str**| alias for search when filtering tags | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **group** | **str**| filter tags by group | [optional] 
 **official** | **bool**| filter tags by official flag | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **user_id** | **str**| user id you want to filter on | [optional] 

### Return type

[**TagList**](TagList.md)

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

# **tags_id_get**
> TagReturn tags_id_get(id)

Get information about a Tag

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag_return import TagReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get information about a Tag
        api_response = api_instance.tags_id_get(id)
        print("The response of ComposeApi->tags_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->tags_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TagReturn**](TagReturn.md)

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

# **tags_post**
> TagReturn tags_post(tag=tag)

Create a new Tag

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.tag import Tag
from neurosynth_compose_sdk.models.tag_return import TagReturn
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    tag = neurosynth_compose_sdk.Tag() # Tag |  (optional)

    try:
        # Create a new Tag
        api_response = api_instance.tags_post(tag=tag)
        print("The response of ComposeApi->tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**TagReturn**](TagReturn.md)

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

