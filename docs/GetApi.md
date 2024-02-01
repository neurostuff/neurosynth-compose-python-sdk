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
[**neurovault_collections_get**](GetApi.md#neurovault_collections_get) | **GET** /neurovault-collections | Get neurovault collections
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
import os
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

    try:
        # GET a list of annotations
        api_response = api_instance.annotations_get()
        print("The response of GetApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
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
import os
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
> MetaAnalysisList meta_analyses_get(nested=nested, ids=ids)

GET a list of meta-analyses

list all runnable specification, studyset, annotation bundles

### Example

```python
import time
import os
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

    try:
        # GET a list of meta-analyses
        api_response = api_instance.meta_analyses_get(nested=nested, ids=ids)
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
import time
import os
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
import time
import os
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
import time
import os
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

# **neurovault_collections_get**
> neurovault_collections_get()

Get neurovault collections

### Example

```python
import time
import os
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)

    try:
        # Get neurovault collections
        api_instance.neurovault_collections_get()
    except Exception as e:
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
import os
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_collections_id_get(id)
        print("The response of GetApi->neurovault_collections_id_get:\n")
        pprint(api_response)
    except Exception as e:
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
import os
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_get()
        print("The response of GetApi->neurovault_files_get:\n")
        pprint(api_response)
    except Exception as e:
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
import os
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.neurovault_files_id_get(id)
        print("The response of GetApi->neurovault_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
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

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
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

    try:
        # Your GET endpoint
        api_response = api_instance.projects_get()
        print("The response of GetApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetApi->projects_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
import time
import os
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
    api_instance = neurosynth_compose_sdk.GetApi(api_client)

    try:
        # Get a list of Specifications
        api_response = api_instance.specifications_get()
        print("The response of GetApi->specifications_get:\n")
        pprint(api_response)
    except Exception as e:
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
> StudysetList studysets_get()

Get a list of Studysets

get a list of serialized/referenced studysets

### Example

```python
import time
import os
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

    try:
        # Get a list of Studysets
        api_response = api_instance.studysets_get()
        print("The response of GetApi->studysets_get:\n")
        pprint(api_response)
    except Exception as e:
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
import os
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

