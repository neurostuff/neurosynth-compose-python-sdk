# Result

describes the output of a meta-analysis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_analysis_id** | **str** | the meta analysis this result was derived from. | [optional] 
**cli_version** | **str** | version of the command-line-tool that is uploading the results.  | [optional] 
**neurovault_collection_id** | **str** | the specific neurovault collection associated with this result. | [optional] 
**methods_description** | **str** | the description of the methods applied to create this result. | [optional] 
**neurovault_images** | [**List[NeurovaultFile]**](NeurovaultFile.md) | the representation of the neurovault images associated with the result. | [optional] 
**diagnostic_table** | **str** | a text representation of a tsv that marks the contribution of each study to each particular cluster. | [optional] 
**cli_args** | **object** | additional parameters that were passed to the commandline tool at runtime.  | [optional] 

## Example

```python
from neurosynth_compose_sdk.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print Result.to_json()

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_form_dict = result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


