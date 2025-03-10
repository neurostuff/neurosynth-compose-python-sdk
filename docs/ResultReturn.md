# ResultReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_analysis_id** | **str** | the meta analysis this result was derived from. | [optional] 
**cli_version** | **str** | version of the command-line-tool that is uploading the results.  | [optional] 
**neurovault_collection** | [**NeurovaultCollectionReturn**](NeurovaultCollectionReturn.md) |  | [optional] 
**methods_description** | **str** | the description of the methods applied to create this result. | [optional] 
**diagnostic_table** | **str** | a text representation of a tsv that marks the contribution of each study to each particular cluster. | [optional] 
**cli_args** | **object** | additional parameters that were passed to the commandline tool at runtime.  | [optional] 
**status** | **str** |  | [optional] 
**id** | **str** | the identifier for the resource. | [optional] 
**updated_at** | **datetime** | when the resource was last modified. | [optional] [readonly] 
**created_at** | **datetime** | When the resource was created. | [optional] [readonly] 
**user** | **str** | Who owns the resource. | [optional] 
**username** | **str** |  | [optional] [readonly] 

## Example

```python
from neurosynth_compose_sdk.models.result_return import ResultReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ResultReturn from a JSON string
result_return_instance = ResultReturn.from_json(json)
# print the JSON string representation of the object
print(ResultReturn.to_json())

# convert the object into a dict
result_return_dict = result_return_instance.to_dict()
# create an instance of ResultReturn from a dict
result_return_from_dict = ResultReturn.from_dict(result_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


