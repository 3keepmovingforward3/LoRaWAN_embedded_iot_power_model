# embedded_iot_power_model
This is a temporal power state model, in Watts.  
It has an external class called State, imported from node.py  
The class has the following instance attribute:  
* Name: String  
* pValue: Worst case probability value coefficient
* qp: Quiescent Power * pValue
* dp: Dynamic Power * pValue

# LoRa Specification
I'll be using the 2017 LoRa Alliance  
[2017 LoRa Specifications](https://lora-alliance.org/sites/default/files/2018-05/lorawan_regional_parameters_v1.0.2_final_1944_1.pdf "2017 LoRa Specifications")

# LoRaWAN Implementation 
Using the following as a specification guideline  
[Understanding the Limits of LoRaWAN](https://arxiv.org/pdf/1607.08011.pdf "Understanding the Limits of LoRaWAN")

# Version Changelog
alpha: The simple power model will not include actual payload data. It will only be a proof of concept.   
beta: Using Numpy for vectors and Matplotlib of plotting  
## Future Plans
To use the results for selecting a solar panel.
