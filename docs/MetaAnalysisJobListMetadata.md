# MetaAnalysisJobListMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of jobs in the response. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_job_list_metadata import MetaAnalysisJobListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisJobListMetadata from a JSON string
meta_analysis_job_list_metadata_instance = MetaAnalysisJobListMetadata.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisJobListMetadata.to_json())

# convert the object into a dict
meta_analysis_job_list_metadata_dict = meta_analysis_job_list_metadata_instance.to_dict()
# create an instance of MetaAnalysisJobListMetadata from a dict
meta_analysis_job_list_metadata_from_dict = MetaAnalysisJobListMetadata.from_dict(meta_analysis_job_list_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


