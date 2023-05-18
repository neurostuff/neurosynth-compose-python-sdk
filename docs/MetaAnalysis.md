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
**internal_studyset_id** | **str** | The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**internal_annotation_id** | **str** | The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**results** | [**List[MetaAnalysisResultsInner]**](MetaAnalysisResultsInner.md) | array of neurostore ids representing the results of this meta-analysis (nominally all results should be the same, but machine architecture differences/algorithm stochastic-ness may lead to slightly different outcomes for each result. | [optional] 
**provenance** | **object** |  | [optional] 
**project** | **str** |  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.meta_analysis import MetaAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of MetaAnalysis from a JSON string
meta_analysis_instance = MetaAnalysis.from_json(json)
# print the JSON string representation of the object
print MetaAnalysis.to_json()

# convert the object into a dict
meta_analysis_dict = meta_analysis_instance.to_dict()
# create an instance of MetaAnalysis from a dict
meta_analysis_form_dict = meta_analysis.from_dict(meta_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


