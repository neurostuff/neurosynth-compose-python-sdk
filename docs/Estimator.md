# Estimator

the specification for the function/class running the meta-analysis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the meta-analytic algorithm applied to the data. Currently this should be directly tied to the function/class running the meta-analysis. For example, ALE, or MKDADensity are valid NiMARE classes to put here. | [optional] 
**args** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | arbitrary keyword arguments to be passed into the function/class to modify default functionality, this could modify the kernel, resampling methods, or any other behavior defined in the function/class (like MKDADensity). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


