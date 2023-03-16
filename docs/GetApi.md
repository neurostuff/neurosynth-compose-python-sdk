# neurosynth_compose_sdk.GetApi

All URIs are relative to *http://localhost:81/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](GetApi.md#annotations_get) | **GET** /annotations | GET a list of annotations
[**annotations_id_get**](GetApi.md#annotations_id_get) | **GET** /annotations/{id} | GET information about an annotation
[**meta_analyses_get**](GetApi.md#meta_analyses_get) | **GET** /meta-analyses | GET a list of meta-analyses
[**meta_analyses_id_get**](GetApi.md#meta_analyses_id_get) | **GET** /meta-analyses/{id} | GET meta-analysis information
[**meta_analysis_results_get**](GetApi.md#meta_analysis_results_get) | **GET** /meta-analysis-results | Your GET endpoint
[**meta_analysis_results_id_get**](GetApi.md#meta_analysis_results_id_get) | **GET** /meta-analysis-results/{id} | Your GET endpoint
[**neurovault_collections_get**](GetApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Your GET endpoint
[**neurovault_collections_id_get**](GetApi.md#neurovault_collections_id_get) | **GET** /neurovault-collections/{id} | Your GET endpoint
[**neurovault_files_get**](GetApi.md#neurovault_files_get) | **GET** /neurovault-files | Your GET endpoint
[**neurovault_files_id_get**](GetApi.md#neurovault_files_id_get) | **GET** /neurovault-files/{id} | Your GET endpoint
[**projects_get**](GetApi.md#projects_get) | **GET** /projects | Your GET endpoint
[**projects_id_get**](GetApi.md#projects_id_get) | **GET** /projects/{id} | Your GET endpoint
[**specifications_get**](GetApi.md#specifications_get) | **GET** /specifications | Get a list of Specifications
[**specifications_id_get**](GetApi.md#specifications_id_get) | **GET** /specifications/{id} | Get information about a Specification
[**studysets_get**](GetApi.md#studysets_get) | **GET** /studysets | Get a list of Studysets
[**studysets_id_get**](GetApi.md#studysets_id_get) | **GET** /studysets/{id} | Get information about a Studyset


# **annotations_get**
> AnnotationList annotations_get()

GET a list of annotations

get a list of serialized/referenced annotations

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # GET a list of annotations
        api_response = api_instance.annotations_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->annotations_get: %s\n" % e)
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
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GET information about an annotation
        api_response = api_instance.annotations_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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
> MetaAnalysisList meta_analyses_get()

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    nested = True # bool | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET a list of meta-analyses
        api_response = api_instance.meta_analyses_get(nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->meta_analyses_get: %s\n" % e)
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
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 
    nested = True # bool | show nested component instead of id (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->meta_analyses_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET meta-analysis information
        api_response = api_instance.meta_analyses_id_get(id, nested=nested)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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
> ResultList meta_analysis_results_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    meta_analysis_id = "meta_analysis_id_example" # str | search for results with this meta-analysis id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_get(meta_analysis_id=meta_analysis_id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.meta_analysis_results_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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

# **neurovault_collections_get**
> neurovault_collections_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_instance.neurovault_collections_get()
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->neurovault_collections_get: %s\n" % e)
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
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.neurovault_collection_return import NeurovaultCollectionReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_collections_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->neurovault_collections_id_get: %s\n" % e)
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

# **neurovault_files_get**
> NeurovaultFileList neurovault_files_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.neurovault_file_list import NeurovaultFileList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->neurovault_files_get: %s\n" % e)
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
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.neurovault_file_return import NeurovaultFileReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->neurovault_files_id_get: %s\n" % e)
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

# **projects_get**
> ProjectList projects_get()

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.project_list import ProjectList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your GET endpoint
        api_response = api_instance.projects_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->projects_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectList**](ProjectList.md)

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

# **projects_id_get**
> ProjectReturn projects_id_get(id)

Your GET endpoint

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.project_return import ProjectReturn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:81/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurosynth_compose_sdk.Configuration(
    host = "http://localhost:81/api"
)


# Enter a context with an instance of the API client
with neurosynth_compose_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your GET endpoint
        api_response = api_instance.projects_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->projects_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
> SpecificationList specifications_get()

Get a list of Specifications

list of meta-analysis specifications

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of Specifications
        api_response = api_instance.specifications_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->specifications_get: %s\n" % e)
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
from neurosynth_compose_sdk.api import get_api
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
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a Specification
        api_response = api_instance.specifications_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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
> StudysetList studysets_get()

Get a list of Studysets

get a list of serialized/referenced studysets

### Example


```python
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.studyset_list import StudysetList
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
    api_instance = get_api.GetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of Studysets
        api_response = api_instance.studysets_get()
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
        print("Exception when calling GetApi->studysets_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
import time
import neurosynth_compose_sdk
from neurosynth_compose_sdk.api import get_api
from neurosynth_compose_sdk.model.studyset_return import StudysetReturn
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
    api_instance = get_api.GetApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get information about a Studyset
        api_response = api_instance.studysets_id_get(id)
        pprint(api_response)
    except neurosynth_compose_sdk.ApiException as e:
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

