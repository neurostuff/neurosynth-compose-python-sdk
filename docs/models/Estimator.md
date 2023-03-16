# neurosynth_compose_sdk.model.estimator.Estimator

the specification for the function/class running the meta-analysis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | the specification for the function/class running the meta-analysis | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | the meta-analytic algorithm applied to the data. Currently this should be directly tied to the function/class running the meta-analysis. For example, ALE, or MKDADensity are valid NiMARE classes to put here. | [optional] 
**[args](#args)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | arbitrary keyword arguments to be passed into the function/class to modify default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the function/class (like MKDADensity). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# args

arbitrary keyword arguments to be passed into the function/class to modify default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the function/class (like MKDADensity).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | arbitrary keyword arguments to be passed into the function/class to modify default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the function/class (like MKDADensity). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

