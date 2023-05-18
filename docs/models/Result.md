# neurosynth_compose_sdk.model.result.Result

describes the output of a meta-analysis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | describes the output of a meta-analysis | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta_analysis_id** | str,  | str,  | the meta analysis this result was derived from. | [optional] 
**cli_version** | None, str,  | NoneClass, str,  | version of the command-line-tool that is uploading the results.  | [optional] 
**neurovault_collection_id** | None, str,  | NoneClass, str,  | the specific neurovault collection associated with this result. | [optional] 
**methods_description** | None, str,  | NoneClass, str,  | the description of the methods applied to create this result. | [optional] 
**[neurovault_images](#neurovault_images)** | list, tuple, None,  | tuple, NoneClass,  | the representation of the neurovault images associated with the result. | [optional] 
**diagnostic_table** | None, str,  | NoneClass, str,  | a text representation of a tsv that marks the contribution of each study to each particular cluster. | [optional] 
**[cli_args](#cli_args)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | additional parameters that were passed to the commandline tool at runtime.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# neurovault_images

the representation of the neurovault images associated with the result.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | the representation of the neurovault images associated with the result. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NeurovaultFile**](NeurovaultFile.md) | [**NeurovaultFile**](NeurovaultFile.md) | [**NeurovaultFile**](NeurovaultFile.md) |  | 

# cli_args

additional parameters that were passed to the commandline tool at runtime. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | additional parameters that were passed to the commandline tool at runtime.  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

