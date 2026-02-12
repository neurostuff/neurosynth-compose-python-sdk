# MetaAnalysis

The combination of the specification determining what meta-analysis to run (required), the studyset to act as input to the meta-analytic algorithm (required), and the annotation to provide human readable annotations as well as acts as an optional filter on which analyses to select within the studyset (optional, but suggested).

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
**cached_studyset_id** | **str** | The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**cached_annotation_id** | **str** | The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**results** | [**MetaAnalysisResults**](MetaAnalysisResults.md) |  | [optional] 
**provenance** | **object** |  | [optional] 
**project** | **str** |  | [optional] 
**run_key** | **str** | a special key used to upload the results of this meta analysis. Can be used as an alternative to using your auth token from login.  | [optional] [readonly] 
**neurostore_analysis** | [**NeurostoreAnalysis**](NeurostoreAnalysis.md) |  | [optional] 
**cognitive_contrast_cogatlas** | **str** |  | [optional] 
**cognitive_contrast_cogatlas_id** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas** | **str** |  | [optional] 
**cognitive_paradigm_cogatlas_id** | **str** |  | [optional] 
**cached_studyset** | **str** |  | [optional] [readonly] 
**cached_annotation** | **str** |  | [optional] [readonly] 
**neurostore_url** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis import MetaAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysis from a JSON string
meta_analysis_instance = MetaAnalysis.from_json(json)
# print the JSON string representation of the object
print(MetaAnalysis.to_json())

# convert the object into a dict
meta_analysis_dict = meta_analysis_instance.to_dict()
# create an instance of MetaAnalysis from a dict
meta_analysis_from_dict = MetaAnalysis.from_dict(meta_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


