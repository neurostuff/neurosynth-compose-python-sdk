# MetaAnalysisJobList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MetaAnalysisJobResponse]**](MetaAnalysisJobResponse.md) |  | [optional] 
**metadata** | [**MetaAnalysisJobListMetadata**](MetaAnalysisJobListMetadata.md) |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_job_list import MetaAnalysisJobList

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisJobList from a JSON string
meta_analysis_job_list_instance = MetaAnalysisJobList.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisJobList.to_json())

# convert the object into a dict
meta_analysis_job_list_dict = meta_analysis_job_list_instance.to_dict()
# create an instance of MetaAnalysisJobList from a dict
meta_analysis_job_list_from_dict = MetaAnalysisJobList.from_dict(meta_analysis_job_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


