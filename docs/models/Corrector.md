# neurosynth_compose_sdk.model.corrector.Corrector

The function/class applying statistical adjustments to the output of the meta-analysis (optional).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The function/class applying statistical adjustments to the output of the meta-analysis (optional). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | the name of the function/class performing the correction. For example FWECorrector from NiMARE would be valid. | [optional] 
**[args](#args)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | key word arguments passed to the corrector to modidy default functionality, such as number of iterations, or the particular method of correction being applied. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# args

key word arguments passed to the corrector to modidy default functionality, such as number of iterations, or the particular method of correction being applied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | key word arguments passed to the corrector to modidy default functionality, such as number of iterations, or the particular method of correction being applied. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

