# Corrector

The function/class applying statistical adjustments to the output of the meta-analysis (optional).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the name of the function/class performing the correction. For example FWECorrector from NiMARE would be valid. | [optional] 
**args** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | key word arguments passed to the corrector to modidy default functionality, such as number of iterations, or the particular method of correction being applied. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


