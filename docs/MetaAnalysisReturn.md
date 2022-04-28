# MetaAnalysisReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | **bool, date, datetime, dict, float, int, list, str, none_type** | Either a string representation of the id of the specification (nested&#x3D;False) or a JSON representation of the specification itself (nested&#x3D;True). | [optional] 
**studyset** | **bool, date, datetime, dict, float, int, list, str, none_type** | Either a string representation of the id of the studyset (nested&#x3D;False) or a JSON representation of the studyset itself (nested&#x3D;True). | [optional] [readonly] 
**annotation** | **bool, date, datetime, dict, float, int, list, str, none_type** | Either a string representation of the id of the annotation (nested&#x3D;False) or a JSON representation of the annotation itself (nested&#x3D;True). | [optional] [readonly] 
**name** | **str, none_type** | Human-readable name of the meta-analysis. | [optional] 
**description** | **str, none_type** | Long form description of the meta-analysis. | [optional] 
**internal_studyset_id** | **str** | The id of the studyset on neurosynth-compose (as opposed to the id of the studyset on neurostore). Multiple snapshots of the studyset can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**internal_annotation_id** | **str** | The id of the annotation on neurosynth-compose (as opposed to the id of the annotation on neurostore). Multiple snapshots of the annotation can be stored on neurosynth-compose so knowing which snapshot is being referenced is necessary. | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime, none_type** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str, none_type** | Who owns the resource. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


