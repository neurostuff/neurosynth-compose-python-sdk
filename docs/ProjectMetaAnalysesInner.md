# ProjectMetaAnalysesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**MetaAnalysisSpecification**](MetaAnalysisSpecification.md) |  | [optional] 
**studyset** | [**MetaAnalysisStudyset**](MetaAnalysisStudyset.md) |  | [optional] 
**annotation** | [**MetaAnalysisAnnotation**](MetaAnalysisAnnotation.md) |  | [optional] 
**name** | **str** | Human-readable name of the meta-analysis. | [optional] 
**description** | **str** | Long form description of the meta-analysis. | [optional] 
**internal_studyset_id** | **str** | The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**internal_annotation_id** | **str** | The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**results** | [**List[MetaAnalysisResultsInner]**](MetaAnalysisResultsInner.md) | array of neurostore ids representing the results of this meta-analysis (nominally all results should be the same, but machine architecture differences/algorithm stochastic-ness may lead to slightly different outcomes for each result. | [optional] 
**provenance** | **object** |  | [optional] 
**project** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.project_meta_analyses_inner import ProjectMetaAnalysesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMetaAnalysesInner from a JSON string
project_meta_analyses_inner_instance = ProjectMetaAnalysesInner.from_json(json)
# print the JSON string representation of the object
print ProjectMetaAnalysesInner.to_json()

# convert the object into a dict
project_meta_analyses_inner_dict = project_meta_analyses_inner_instance.to_dict()
# create an instance of ProjectMetaAnalysesInner from a dict
project_meta_analyses_inner_form_dict = project_meta_analyses_inner.from_dict(project_meta_analyses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


