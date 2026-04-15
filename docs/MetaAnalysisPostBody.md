# MetaAnalysisPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**MetaAnalysisSpecification**](MetaAnalysisSpecification.md) |  | [optional] 
**studyset** | [**MetaAnalysisStudyset**](MetaAnalysisStudyset.md) |  | [optional] 
**annotation** | [**MetaAnalysisAnnotation**](MetaAnalysisAnnotation.md) |  | [optional] 
**name** | **str** | Human-readable name of the meta-analysis. | [optional] 
**description** | **str** | Long form description of the meta-analysis. | [optional] 
**public** | **bool** | whether the meta-analysis is public or private | [optional] 
**tags** | [**MetaAnalysisTags**](MetaAnalysisTags.md) |  | [optional] 
**results** | [**MetaAnalysisResults**](MetaAnalysisResults.md) |  | [optional] 
**provenance** | **object** |  | [optional] 
**project** | **str** |  | [optional] 
**run_key** | **str** | a special key used to upload the results of this meta analysis. Can be used as an alternative to using your auth token from login.  | [optional] [readonly] 
**snapshots** | **List[object]** | Ordered history of (studyset, annotation) snapshot pairs recorded each time a MetaAnalysisResult is created. Each entry contains studyset_id, studyset_md5, annotation_id, annotation_md5, result_id, and created_at.  | [optional] [readonly] 
**neurostore_analysis** | [**NeurostoreAnalysis**](NeurostoreAnalysis.md) |  | [optional] 
**cognitive_contrast_cogatlas** | **str** |  | [optional] 
**cognitive_contrast_cogatlas_id** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas_id** | **str** |  | [optional] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_post_body import MetaAnalysisPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisPostBody from a JSON string
meta_analysis_post_body_instance = MetaAnalysisPostBody.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysisPostBody.to_json())

# convert the object into a dict
meta_analysis_post_body_dict = meta_analysis_post_body_instance.to_dict()
# create an instance of MetaAnalysisPostBody from a dict
meta_analysis_post_body_from_dict = MetaAnalysisPostBody.from_dict(meta_analysis_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


