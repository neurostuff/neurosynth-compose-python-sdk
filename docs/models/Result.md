# neurosynth_compose_sdk.model.result.Result

describes the output of a meta-analysis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | describes the output of a meta-analysis | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta_analysis_id** | str,  | str,  |  | [optional] 
**cli_version** | None, str,  | NoneClass, str,  |  | [optional] 
**neurovault_collection_id** | None, str,  | NoneClass, str,  |  | [optional] 
**methods_description** | None, str,  | NoneClass, str,  |  | [optional] 
**[neurovault_images](#neurovault_images)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**diagnostic_table** | None, str,  | NoneClass, str,  |  | [optional] 
**[cli_args](#cli_args)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# neurovault_images

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NeurovaultFile**](NeurovaultFile.md) | [**NeurovaultFile**](NeurovaultFile.md) | [**NeurovaultFile**](NeurovaultFile.md) |  | 

# cli_args

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

