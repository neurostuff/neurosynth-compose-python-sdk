# MetaAnalysis

The combination of the specification determining what meta-analysis to run (required), the studyset to act as input to the meta-analytic algorithm (required), and the annotation to provide human readable annotations as well as acts as an optional filter on which analyses to select within the studyset (optional, but suggested).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**studyset** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**annotation** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**name** | **str, none_type** | Human-readable name of the meta-analysis. | [optional] 
**description** | **str, none_type** | Long form description of the meta-analysis. | [optional] 
**internal_studyset_id** | **str** | The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**internal_annotation_id** | **str** | The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**results** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | array of neurostore ids representing the results of this meta-analysis (nominally all results should be the same, but machine architecture differences/algorithm stochastic-ness may lead to slightly different outcomes for each result. | [optional] 
**provenance** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**project** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


