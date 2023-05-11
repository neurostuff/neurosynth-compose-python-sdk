# neurosynth_compose_sdk.model.annotation.Annotation

a holder/reference to the annotation on neurostore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | a holder/reference to the annotation on neurostore | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**neurostore_id** | str,  | str,  | the id of the annotation on neurostore | [optional] 
**[snapshot](#snapshot)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | [optional] 
**studyset** | str,  | str,  | The related studyset to this annotation. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# snapshot

the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | the snapshot taken of the annotation pending a successful run of the meta-analytic algorithm | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

