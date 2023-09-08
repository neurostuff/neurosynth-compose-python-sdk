# MetaAnalysisReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**MetaAnalysisSpecification**](MetaAnalysisSpecification.md) |  | [optional] 
**studyset** | [**MetaAnalysisStudyset**](MetaAnalysisStudyset.md) |  | [optional] 
**annotation** | [**MetaAnalysisAnnotation**](MetaAnalysisAnnotation.md) |  | [optional] 
**name** | **str** | Human-readable name of the meta-analysis. | [optional] 
**description** | **str** | Long form description of the meta-analysis. | [optional] 
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
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis_return import MetaAnalysisReturn

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysisReturn from a JSON string
meta_analysis_return_instance = MetaAnalysisReturn.from_json(json)
# print the JSON string representation of the object
print MetaAnalysisReturn.to_json()

# convert the object into a dict
meta_analysis_return_dict = meta_analysis_return_instance.to_dict()
# create an instance of MetaAnalysisReturn from a dict
meta_analysis_return_form_dict = meta_analysis_return.from_dict(meta_analysis_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


