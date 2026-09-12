# neurosynth_compose_sdk.ComposeApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_analyses_get**](ComposeApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](ComposeApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
[**meta_analyses_id_put**](ComposeApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
[**meta_analyses_post**](ComposeApi.md#meta_analyses_post) | **POST** /meta-analyses | Create a new meta-analysis
[**meta_analysis_jobs_get**](ComposeApi.md#meta_analysis_jobs_get) | **GET** /meta-analysis-jobs | List meta-analysis jobs for the current user
[**meta_analysis_jobs_job_id_get**](ComposeApi.md#meta_analysis_jobs_job_id_get) | **GET** /meta-analysis-jobs/{job_id} | Get status and logs for a meta-analysis job
[**meta_analysis_jobs_post**](ComposeApi.md#meta_analysis_jobs_post) | **POST** /meta-analysis-jobs | Submit a meta-analysis job
[**meta_analysis_results_get**](ComposeApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | List meta-analysis results
[**meta_analysis_results_id_get**](ComposeApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Get a meta-analysis result by ID
[**meta_analysis_results_id_put**](ComposeApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | Update a meta-analysis result with files or snapshots
[**meta_analysis_results_post**](ComposeApi.md#meta_analysis_results_post) | **POST** /meta-analysis-results | Create a new meta-analysis result
[**neurostore_annotations_id_get**](ComposeApi.md#neurostore_annotations_id_get) | **GET** /neurostore-annotations/{id} | Get a Neurostore annotation reference by Neurostore ID
[**neurostore_studies_get**](ComposeApi.md#neurostore_studies_get) | **GET** /neurostore-studies | Your GET endpoint
[**neurostore_studies_id_get**](ComposeApi.md#neurostore_studies_id_get) | **GET** /neurostore-studies/{id} | Your GET endpoint
[**neurostore_studysets_get**](ComposeApi.md#neurostore_studysets_get) | **GET** /neurostore-studysets | List Neurostore studyset references
[**neurostore_studysets_id_get**](ComposeApi.md#neurostore_studysets_id_get) | **GET** /neurostore-studysets/{id} | Get a Neurostore studyset reference by Neurostore ID
[**neurovault_collections_get**](ComposeApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Get neurovault collections
[**neurovault_collections_id_get**](ComposeApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
[**neurovault_collections_id_put**](ComposeApi.md#neurovault_collections_id_put) | **PUT** /neurovault-collections/{id} | 
[**neurovault_collections_post**](ComposeApi.md#neurovault_collections_post) | **POST** /neurovault-collections | Create neurovault collection
[**neurovault_files_get**](ComposeApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
[**neurovault_files_id_get**](ComposeApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
[**neurovault_files_id_put**](ComposeApi.md#neurovault_files_id_put) | **PUT** /neurovault-files/{id} | 
[**neurovault_files_post**](ComposeApi.md#neurovault_files_post) | **POST** /neurovault-files | 
[**projects_get**](ComposeApi.md#projects_get) | **GET** /projects | Your GET endpoint
[**projects_id_delete**](ComposeApi.md#projects_id_delete) | **DELETE** /projects/{id} | 
[**projects_id_get**](ComposeApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
[**projects_id_put**](ComposeApi.md#projects_id_put) | **PUT** /projects/{id} | 
[**projects_post**](ComposeApi.md#projects_post) | **POST** /projects | 
[**snapshot_annotations_get**](ComposeApi.md#snapshot_annotations_get) | **GET** /snapshot-annotations | GET a list of annotations
[**snapshot_annotations_id_get**](ComposeApi.md#snapshot_annotations_id_get) | **GET** /snapshot-annotations/{id} | GET information about an annotation
[**snapshot_annotations_id_put**](ComposeApi.md#snapshot_annotations_id_put) | **PUT** /snapshot-annotations/{id} | Update an Annotation
[**snapshot_annotations_post**](ComposeApi.md#snapshot_annotations_post) | **POST** /snapshot-annotations | Create a new Annotation
[**snapshot_studysets_get**](ComposeApi.md#snapshot_studysets_get) | **GET** /snapshot-studysets | Get a list of Studysets
[**snapshot_studysets_id_get**](ComposeApi.md#snapshot_studysets_id_get) | **GET** /snapshot-studysets/{id} | Get information about a Studyset
[**snapshot_studysets_id_put**](ComposeApi.md#snapshot_studysets_id_put) | **PUT** /snapshot-studysets/{id} | Update a Studyset
[**snapshot_studysets_post**](ComposeApi.md#snapshot_studysets_post) | **POST** /snapshot-studysets | Create a new Studyset
[**specifications_get**](ComposeApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](ComposeApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**specifications_id_put**](ComposeApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**specifications_post**](ComposeApi.md#specifications_post) | **POST** /specifications | Create a Specification
[**tags_get**](ComposeApi.md#tags_get) | **GET** /tags | Get a list of Tags
[**tags_id_get**](ComposeApi.md#tags_id_get) | **GET** /tags/{id} | Get information about a Tag
[**tags_post**](ComposeApi.md#tags_post) | **POST** /tags | Create a new Tag
[**users_get**](ComposeApi.md#users_get) | **GET** /users | GET list of Users
[**users_id_get**](ComposeApi.md#users_id_get) | **GET** /users/{id} | Get User Info by User ID
[**users_id_put**](ComposeApi.md#users_id_put) | **PUT** /users/{id} | Update User Information
[**users_post**](ComposeApi.md#users_post) | **POST** /users | Create A New User


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

# **meta_analysis_jobs_get**
> MetaAnalysisJobList meta_analysis_jobs_get()

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
        api_response = api_instance.meta_analysis_jobs_get()
        print("The response of ComposeApi->meta_analysis_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_jobs_get: %s\n" % e)
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

# **meta_analysis_jobs_job_id_get**
> MetaAnalysisJobResponse meta_analysis_jobs_job_id_get(job_id)

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
        api_response = api_instance.meta_analysis_jobs_job_id_get(job_id)
        print("The response of ComposeApi->meta_analysis_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_jobs_job_id_get: %s\n" % e)
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

# **meta_analysis_jobs_post**
> MetaAnalysisJobResponse meta_analysis_jobs_post(meta_analysis_job_request)

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
        api_response = api_instance.meta_analysis_jobs_post(meta_analysis_job_request)
        print("The response of ComposeApi->meta_analysis_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_jobs_post: %s\n" % e)
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

# **meta_analysis_results_get**
> ResultList meta_analysis_results_get(meta_analysis_id=meta_analysis_id)

List meta-analysis results

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
        # List meta-analysis results
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

Get a meta-analysis result by ID

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
        # Get a meta-analysis result by ID
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
> ResultReturn meta_analysis_results_id_put(id, statistical_maps=statistical_maps, cluster_tables=cluster_tables, diagnostic_tables=diagnostic_tables, method_description=method_description, method_references=method_references, snapshot_studyset=snapshot_studyset, snapshot_annotation=snapshot_annotation)

Update a meta-analysis result with files or snapshots

### Example

* Bearer Authentication (JSON-Web-Token):
* Api Key Authentication (upload_key):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.result_return import ResultReturn
from neurosynth_compose_sdk.models.result_upload_statistical_maps import ResultUploadStatisticalMaps
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
    statistical_maps = neurosynth_compose_sdk.ResultUploadStatisticalMaps() # ResultUploadStatisticalMaps |  (optional)
    cluster_tables = neurosynth_compose_sdk.ResultUploadStatisticalMaps() # ResultUploadStatisticalMaps |  (optional)
    diagnostic_tables = neurosynth_compose_sdk.ResultUploadStatisticalMaps() # ResultUploadStatisticalMaps |  (optional)
    method_description = 'method_description_example' # str | the description of the methods applied to create this result. (optional)
    method_references = 'method_references_example' # str | BibTeX-formatted references cited by method_description.  (optional)
    snapshot_studyset = 'snapshot_studyset_example' # str | JSON-encoded studyset snapshot payload, optionally provided in multipart form. (optional)
    snapshot_annotation = 'snapshot_annotation_example' # str | JSON-encoded annotation snapshot payload, optionally provided in multipart form. (optional)

    try:
        # Update a meta-analysis result with files or snapshots
        api_response = api_instance.meta_analysis_results_id_put(id, statistical_maps=statistical_maps, cluster_tables=cluster_tables, diagnostic_tables=diagnostic_tables, method_description=method_description, method_references=method_references, snapshot_studyset=snapshot_studyset, snapshot_annotation=snapshot_annotation)
        print("The response of ComposeApi->meta_analysis_results_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->meta_analysis_results_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **statistical_maps** | [**ResultUploadStatisticalMaps**](ResultUploadStatisticalMaps.md)|  | [optional] 
 **cluster_tables** | [**ResultUploadStatisticalMaps**](ResultUploadStatisticalMaps.md)|  | [optional] 
 **diagnostic_tables** | [**ResultUploadStatisticalMaps**](ResultUploadStatisticalMaps.md)|  | [optional] 
 **method_description** | **str**| the description of the methods applied to create this result. | [optional] 
 **method_references** | **str**| BibTeX-formatted references cited by method_description.  | [optional] 
 **snapshot_studyset** | **str**| JSON-encoded studyset snapshot payload, optionally provided in multipart form. | [optional] 
 **snapshot_annotation** | **str**| JSON-encoded annotation snapshot payload, optionally provided in multipart form. | [optional] 

### Return type

[**ResultReturn**](ResultReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token), [upload_key](../README.md#upload_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_analysis_results_post**
> ResultReturn meta_analysis_results_post(result_init=result_init)

Create a new meta-analysis result

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
        # Create a new meta-analysis result
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

# **neurostore_annotations_id_get**
> AnnotationReferenceReturn neurostore_annotations_id_get(id)

Get a Neurostore annotation reference by Neurostore ID

Resolve a Neurostore annotation reference using the same ID exposed by the Neurostore API, including each linked snapshot's compose ID and md5.

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.annotation_reference_return import AnnotationReferenceReturn
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
        # Get a Neurostore annotation reference by Neurostore ID
        api_response = api_instance.neurostore_annotations_id_get(id)
        print("The response of ComposeApi->neurostore_annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurostore_annotations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AnnotationReferenceReturn**](AnnotationReferenceReturn.md)

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

# **neurostore_studies_get**
> NeurostoreStudyList neurostore_studies_get()

Your GET endpoint

### Example


```python
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_get()
        print("The response of ComposeApi->neurostore_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurostore_studies_get: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.ComposeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.neurostore_studies_id_get(id)
        print("The response of ComposeApi->neurostore_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurostore_studies_id_get: %s\n" % e)
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

# **neurostore_studysets_get**
> StudysetReferenceList neurostore_studysets_get(nested=nested)

List Neurostore studyset references

List reference rows keyed by the actual Neurostore studyset ID, including compact snapshot summaries.

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_reference_list import StudysetReferenceList
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

    try:
        # List Neurostore studyset references
        api_response = api_instance.neurostore_studysets_get(nested=nested)
        print("The response of ComposeApi->neurostore_studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurostore_studysets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| show nested component instead of id | [optional] 

### Return type

[**StudysetReferenceList**](StudysetReferenceList.md)

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

# **neurostore_studysets_id_get**
> StudysetReferenceReturn neurostore_studysets_id_get(id, nested=nested)

Get a Neurostore studyset reference by Neurostore ID

Resolve a Neurostore studyset reference using the same ID exposed by the Neurostore API, including each linked snapshot's compose ID and md5.

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.studyset_reference_return import StudysetReferenceReturn
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
        # Get a Neurostore studyset reference by Neurostore ID
        api_response = api_instance.neurostore_studysets_id_get(id, nested=nested)
        print("The response of ComposeApi->neurostore_studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurostore_studysets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| show nested component instead of id | [optional] 

### Return type

[**StudysetReferenceReturn**](StudysetReferenceReturn.md)

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

# **neurovault_collections_get**
> neurovault_collections_get()

Get neurovault collections

### Example


```python
import neurosynth_compose_sdk
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

    try:
        # Get neurovault collections
        api_instance.neurovault_collections_get()
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_collections_get: %s\n" % e)
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn
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
        api_response = api_instance.neurovault_collections_id_get(id)
        print("The response of ComposeApi->neurovault_collections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_collections_id_get: %s\n" % e)
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_collection_return import NeurovaultCollectionReturn
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
        api_response = api_instance.neurovault_collections_id_put(id)
        print("The response of ComposeApi->neurovault_collections_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_collections_id_put: %s\n" % e)
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
> neurovault_collections_post(neurovault_collection=neurovault_collection)

Create neurovault collection



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_collection import NeurovaultCollection
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
    neurovault_collection = neurosynth_compose_sdk.NeurovaultCollection() # NeurovaultCollection |  (optional)

    try:
        # Create neurovault collection
        api_instance.neurovault_collections_post(neurovault_collection=neurovault_collection)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_collections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neurovault_collection** | [**NeurovaultCollection**](NeurovaultCollection.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_file_list import NeurovaultFileList
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

    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_get()
        print("The response of ComposeApi->neurovault_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_files_get: %s\n" % e)
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
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn
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
        api_response = api_instance.neurovault_files_id_get(id)
        print("The response of ComposeApi->neurovault_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_files_id_get: %s\n" % e)
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
> NeurovaultFileReturn neurovault_files_id_put(id, collection_id=collection_id, exception=exception, traceback=traceback, status=status, image_id=image_id, name=name, url=url, file=file)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn
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
    collection_id = 'collection_id_example' # str |  (optional)
    exception = 'exception_example' # str |  (optional)
    traceback = 'traceback_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    image_id = 'image_id_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    url = 'url_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # 
        api_response = api_instance.neurovault_files_id_put(id, collection_id=collection_id, exception=exception, traceback=traceback, status=status, image_id=image_id, name=name, url=url, file=file)
        print("The response of ComposeApi->neurovault_files_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_files_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collection_id** | **str**|  | [optional] 
 **exception** | **str**|  | [optional] 
 **traceback** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **image_id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

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
> NeurovaultFileReturn neurovault_files_post(neurovault_file=neurovault_file)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.neurovault_file import NeurovaultFile
from neurosynth_compose_sdk.models.neurovault_file_return import NeurovaultFileReturn
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
    neurovault_file = neurosynth_compose_sdk.NeurovaultFile() # NeurovaultFile |  (optional)

    try:
        # 
        api_response = api_instance.neurovault_files_post(neurovault_file=neurovault_file)
        print("The response of ComposeApi->neurovault_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->neurovault_files_post: %s\n" % e)
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

# **projects_get**
> ProjectList projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id, include_provenance=include_provenance, tag=tag, exclude_tag=exclude_tag)

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
    include_provenance = True # bool | include the project provenance payload in project responses (optional) (default to True)
    tag = ['tag_example'] # List[str] | only return projects carrying every one of these tag names (case-insensitive) (optional)
    exclude_tag = ['exclude_tag_example'] # List[str] | drop projects carrying any of these tag names (case-insensitive); use this to hide projects a user has tagged away (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_get(page=page, page_size=page_size, name=name, search=search, description=description, sort=sort, desc=desc, user_id=user_id, include_provenance=include_provenance, tag=tag, exclude_tag=exclude_tag)
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
 **include_provenance** | **bool**| include the project provenance payload in project responses | [optional] [default to True]
 **tag** | [**List[str]**](str.md)| only return projects carrying every one of these tag names (case-insensitive) | [optional] 
 **exclude_tag** | [**List[str]**](str.md)| drop projects carrying any of these tag names (case-insensitive); use this to hide projects a user has tagged away | [optional] 

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
> ProjectReturn projects_id_get(id, info=info, include_provenance=include_provenance)

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
    include_provenance = True # bool | include the project provenance payload in project responses (optional) (default to True)

    try:
        # Your GET endpoint
        api_response = api_instance.projects_id_get(id, info=info, include_provenance=include_provenance)
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
 **include_provenance** | **bool**| include the project provenance payload in project responses | [optional] [default to True]

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

# **snapshot_annotations_get**
> AnnotationList snapshot_annotations_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)

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
        api_response = api_instance.snapshot_annotations_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)
        print("The response of ComposeApi->snapshot_annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_annotations_get: %s\n" % e)
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

# **snapshot_annotations_id_get**
> AnnotationReturn snapshot_annotations_id_get(id)

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
        api_response = api_instance.snapshot_annotations_id_get(id)
        print("The response of ComposeApi->snapshot_annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_annotations_id_get: %s\n" % e)
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

# **snapshot_annotations_id_put**
> AnnotationReturn snapshot_annotations_id_put(id, annotation_update=annotation_update)

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
        api_response = api_instance.snapshot_annotations_id_put(id, annotation_update=annotation_update)
        print("The response of ComposeApi->snapshot_annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_annotations_id_put: %s\n" % e)
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

# **snapshot_annotations_post**
> AnnotationReturn snapshot_annotations_post(annotation_post_body=annotation_post_body)

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
        api_response = api_instance.snapshot_annotations_post(annotation_post_body=annotation_post_body)
        print("The response of ComposeApi->snapshot_annotations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_annotations_post: %s\n" % e)
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

# **snapshot_studysets_get**
> StudysetList snapshot_studysets_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)

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
        api_response = api_instance.snapshot_studysets_get(nested=nested, ids=ids, page=page, page_size=page_size, search=search, sort=sort, desc=desc, user_id=user_id, info=info)
        print("The response of ComposeApi->snapshot_studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_studysets_get: %s\n" % e)
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

# **snapshot_studysets_id_get**
> StudysetReturn snapshot_studysets_id_get(id)

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
        api_response = api_instance.snapshot_studysets_id_get(id)
        print("The response of ComposeApi->snapshot_studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_studysets_id_get: %s\n" % e)
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

# **snapshot_studysets_id_put**
> StudysetReturn snapshot_studysets_id_put(id, studyset=studyset)

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
        api_response = api_instance.snapshot_studysets_id_put(id, studyset=studyset)
        print("The response of ComposeApi->snapshot_studysets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_studysets_id_put: %s\n" % e)
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

# **snapshot_studysets_post**
> StudysetReturn snapshot_studysets_post(studyset_post_body=studyset_post_body)

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
        api_response = api_instance.snapshot_studysets_post(studyset_post_body=studyset_post_body)
        print("The response of ComposeApi->snapshot_studysets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->snapshot_studysets_post: %s\n" % e)
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

# **users_get**
> UserList users_get()

GET list of Users

List all users

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.user_list import UserList
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

    try:
        # GET list of Users
        api_response = api_instance.users_get()
        print("The response of ComposeApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserList**](UserList.md)

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

# **users_id_get**
> UserReturn users_id_get(id)

Get User Info by User ID

Retrieve the information of the user with the matching user ID.

### Example


```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.user_return import UserReturn
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
        # Get User Info by User ID
        api_response = api_instance.users_id_get(id)
        print("The response of ComposeApi->users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->users_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserReturn**](UserReturn.md)

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

# **users_id_put**
> UserReturn users_id_put(id, user=user)

Update User Information

update information about a user

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.user import User
from neurosynth_compose_sdk.models.user_return import UserReturn
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
    user = neurosynth_compose_sdk.User() # User |  (optional)

    try:
        # Update User Information
        api_response = api_instance.users_id_put(id, user=user)
        print("The response of ComposeApi->users_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->users_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**UserReturn**](UserReturn.md)

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

# **users_post**
> UserReturn users_post(user=user)

Create A New User

create a single user

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurosynth_compose_sdk
from neurosynth_compose_sdk.models.user import User
from neurosynth_compose_sdk.models.user_return import UserReturn
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
    user = neurosynth_compose_sdk.User() # User |  (optional)

    try:
        # Create A New User
        api_response = api_instance.users_post(user=user)
        print("The response of ComposeApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposeApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**UserReturn**](UserReturn.md)

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

