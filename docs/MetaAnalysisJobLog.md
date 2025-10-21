# MetaAnalysisJobLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Epoch timestamp returned by the compose runner. | [optional] 
**message** | **str** | Log message emitted by the compose runner. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_job_log import MetaAnalysisJobLog

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisJobLog from a JSON string
meta_analysis_job_log_instance = MetaAnalysisJobLog.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisJobLog.to_json())

# convert the object into a dict
meta_analysis_job_log_dict = meta_analysis_job_log_instance.to_dict()
# create an instance of MetaAnalysisJobLog from a dict
meta_analysis_job_log_from_dict = MetaAnalysisJobLog.from_dict(meta_analysis_job_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


