# neurosynth_compose_sdk.model.specification.Specification

a machine readable specification of how to run a meta-analysis (currently specifically tailored to NiMARE).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | a machine readable specification of how to run a meta-analysis (currently specifically tailored to NiMARE). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | the type of meta-analysis being run, typically either cbma or ibma, but others may become available in the future. | [optional] 
**estimator** | [**Estimator**](Estimator.md) | [**Estimator**](Estimator.md) |  | [optional] 
**mask** | None, str,  | NoneClass, str,  | a string representing a binary nifti file to select which voxels a user wants to include in the analysis. | [optional] 
**contrast** | None, str,  | NoneClass, str,  | underspecified selection of columns to contrast (TODO, make better). | [optional] 
**transformer** | None, str,  | NoneClass, str,  | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | None, str,  | NoneClass, str,  | a boolean column from annotations selecting which analyses to include in the meta-analysis | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

