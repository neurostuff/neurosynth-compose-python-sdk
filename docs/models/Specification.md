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
**[conditions](#conditions)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | selection of categories in the filter column to differentiate groups, or \&quot;neurosynth\&quot;, \&quot;neuroquery\&quot;, or \&quot;neurostore\&quot; to compare to a database reference group | [optional] 
**[weights](#weights)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**transformer** | None, str,  | NoneClass, str,  | A transformation applied to column(s) (e.g., binarize based on a threshold). This is likely to become deprecated. | [optional] 
**corrector** | [**Corrector**](Corrector.md) | [**Corrector**](Corrector.md) |  | [optional] 
**filter** | None, str,  | NoneClass, str,  | a column from annotations selecting which analyses to include in the meta-analysis | [optional] 
**database_studyset** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

selection of categories in the filter column to differentiate groups, or \"neurosynth\", \"neuroquery\", or \"neurostore\" to compare to a database reference group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | selection of categories in the filter column to differentiate groups, or \&quot;neurosynth\&quot;, \&quot;neuroquery\&quot;, or \&quot;neurostore\&quot; to compare to a database reference group | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | list, tuple, None,  | tuple, NoneClass,  |  | 
[one_of_1](#one_of_1) | list, tuple,  | tuple,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bool,  | BoolClass,  |  | 

# weights

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

