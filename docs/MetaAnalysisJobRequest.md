# MetaAnalysisJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_analysis_id** | **str** | Identifier of the meta-analysis to submit. | 
**no_upload** | **bool** | Skip upload of results to Neurostore/Neurovault. | [optional] [default to False]

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_job_request import MetaAnalysisJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisJobRequest from a JSON string
meta_analysis_job_request_instance = MetaAnalysisJobRequest.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisJobRequest.to_json())

# convert the object into a dict
meta_analysis_job_request_dict = meta_analysis_job_request_instance.to_dict()
# create an instance of MetaAnalysisJobRequest from a dict
meta_analysis_job_request_from_dict = MetaAnalysisJobRequest.from_dict(meta_analysis_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


