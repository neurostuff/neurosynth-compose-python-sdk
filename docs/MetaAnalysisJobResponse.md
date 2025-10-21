# MetaAnalysisJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Identifier returned by the compose runner service. | [optional] 
**meta_analysis_id** | **str** | Identifier of the meta-analysis that was submitted. | [optional] 
**artifact_prefix** | **str** | Artifact key prefix for logs and outputs. | [optional] 
**status** | **str** | Latest known status reported by the compose runner. | [optional] 
**status_url** | **str** | Convenience URL for polling job status. | [optional] 
**environment** | **str** | Deployment environment the job was submitted to. | [optional] 
**no_upload** | **bool** | Indicates whether the upload step was skipped. | [optional] 
**start_time** | **datetime** | Start time reported by the compose runner status endpoint. | [optional] 
**output** | **Dict[str, object]** | Raw output payload returned by the compose runner. | [optional] 
**logs** | [**List[MetaAnalysisJobLog]**](MetaAnalysisJobLog.md) | Aggregated log events returned by the compose runner. | [optional] 
**created_at** | **datetime** | Timestamp when the job entry was cached. | [optional] 
**updated_at** | **datetime** | Timestamp when the job entry was last refreshed. | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_job_response import MetaAnalysisJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisJobResponse from a JSON string
meta_analysis_job_response_instance = MetaAnalysisJobResponse.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisJobResponse.to_json())

# convert the object into a dict
meta_analysis_job_response_dict = meta_analysis_job_response_instance.to_dict()
# create an instance of MetaAnalysisJobResponse from a dict
meta_analysis_job_response_from_dict = MetaAnalysisJobResponse.from_dict(meta_analysis_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


