# neurosynth_compose_sdk.PutApi

All URIs are relative to *https://compose.neurosynth.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_id_put**](PutApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an Annotation
[**meta_analyses_id_put**](PutApi.md#meta_analyses_id_put) | **PUT** /meta-analyses/{id} | Update a meta-analysis
[**meta_analysis_results_id_put**](PutApi.md#meta_analysis_results_id_put) | **PUT** /meta-analysis-results/{id} | 
[**projects_id_put**](PutApi.md#projects_id_put) | **PUT** /projects/{id} | 
[**specifications_id_put**](PutApi.md#specifications_id_put) | **PUT** /specifications/{id} | Update Meta-Analysis specification
[**studysets_id_put**](PutApi.md#studysets_id_put) | **PUT** /studysets/{id} | Update a Studyset


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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    annotation_update = neurosynth_compose_sdk.AnnotationUpdate() # AnnotationUpdate |  (optional)

    try:
        # Update an Annotation
        api_response = api_instance.annotations_id_put(id, annotation_update=annotation_update)
        print("The response of PutApi->annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->annotations_id_put: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    meta_analysis = neurosynth_compose_sdk.MetaAnalysis() # MetaAnalysis |  (optional)

    try:
        # Update a meta-analysis
        api_response = api_instance.meta_analyses_id_put(id, meta_analysis=meta_analysis)
        print("The response of PutApi->meta_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->meta_analyses_id_put: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    result = neurosynth_compose_sdk.Result() # Result |  (optional)

    try:
        # 
        api_response = api_instance.meta_analysis_results_id_put(id, result=result)
        print("The response of PutApi->meta_analysis_results_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->meta_analysis_results_id_put: %s\n" % e)
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

# **projects_id_put**
> ProjectReturn projects_id_put(id, project=project)



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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    project = neurosynth_compose_sdk.Project() # Project |  (optional)

    try:
        # 
        api_response = api_instance.projects_id_put(id, project=project)
        print("The response of PutApi->projects_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->projects_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    specification = neurosynth_compose_sdk.Specification() # Specification |  (optional)

    try:
        # Update Meta-Analysis specification
        api_response = api_instance.specifications_id_put(id, specification=specification)
        print("The response of PutApi->specifications_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->specifications_id_put: %s\n" % e)
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
    api_instance = neurosynth_compose_sdk.PutApi(api_client)
    id = 'id_example' # str | 
    studyset = neurosynth_compose_sdk.Studyset() # Studyset |  (optional)

    try:
        # Update a Studyset
        api_response = api_instance.studysets_id_put(id, studyset=studyset)
        print("The response of PutApi->studysets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PutApi->studysets_id_put: %s\n" % e)
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

