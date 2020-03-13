# embedded_iot_power_model
This is a temporal power state model, in Watts.  
It has an external class called State, imported from node.py  
The class has the following instance attribute:  
* Name: String  
* pValue: Worst case probability value coefficient
* qp: Quiescent Power * pValue
* dp: Dynamic Power * pValue
