
<center>fECB Platform Document
--API Development SDK </center>  
![](https://i.imgur.com/Lc7MSEw.png)
===

**<center>Author: FiduciaEdge Ltd.</center>**
**<center>Last modification date and time: 02AM, 14th, Feb. 2022</center>**

---
<div STYLE="page-break-after: always;"></div>

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Document revision records](#document-revision-records)
- [User SDK instruction](#user-sdk-instruction)
  - [A-1. fECB SDK developer support image](#a-1-fecb-sdk-developer-support-image)
    - [A-1-1. Support image for Python developer](#a-1-1-support-image-for-python-developer)
    - [A-1-2. Support image for Java developer](#a-1-2-support-image-for-java-developer)
  - [A-2. Getting start with fECB SDK](#a-2-getting-start-with-fecb-sdk)
    - [A-2-1. SDK overview](#a-2-1-sdk-overview)
      - [A-2-1-1. Python SDK](#a-2-1-1-python-sdk)

        - [A-2-1-1-1. File](#a-2-1-1-1-file)
        - [A-2-1-1-2. HCservice](#a-2-1-1-2-hcservice)
        - [A-2-1-1-3. Device](#a-2-1-1-3-device)

      - [A-2-1-2. Java](#a-2-1-2-java)
        - [A-2-1-2-1. File](#a-2-1-2-1-file)
        - [A-2-1-2-2. HCservice](#a-2-1-2-2-hcservice)
        - [A-2-1-2-3. Device](#a-2-1-2-3-device)
      - [A-2-1-3. Returned code](#a-2-1-3-returned-code)

<!-- /code_chunk_output -->

---
<div STYLE="page-break-after: always;"></div>

# Document revision records
Editor                   | Time      | Date            | Modified contents         | Comments
---                      | ---       | ---             | ---                       | ---
FiduciaEdge-Edward Chang |  4:00 AM  | 20th, Jan. 2022 | First draft of this doc | -
FiduciaEdge-Jerry Yang |  2:00 AM | 14th, Feb. 2022 | Contents of [User SDK instruction](#a-2-1-1-5-data-transmission)  | -
---
<div STYLE="page-break-after: always;"></div>

# User SDK instruction

---

## A-1. fECB SDK developer support image
### A-1-1. Support image for Python developer
* There are images already installed all necessary libraries for being used in Device Resource Sandbox, HC Resource Sandbox, and Applcation Sandbox respectively: 
* ```fiduciaedge/fecb-python-sdk-dvs-support-image:v1.3```
* ```fiduciaedge/fecb-python-sdk-hc-support-image:v1.3```
* ```fiduciaedge/fecb-python-sdk-app-support-image:v1.3```
### A-1-2. Support image for Java developer
* There are images already installed all necessary libraries for being used in Device Resource Sandbox, HC Resource Sandbox, and Applcation Sandbox respectively: 
* ```fiduciaedge/fecb-java-sdk-dvs-support-image:v1.3```
* ```fiduciaedge/fecb-java-sdk-hc-support-image:v1.3```
* ```fiduciaedge/fecb-java-sdk-app-support-image:v1.3```

## A-2. Getting start with fECB SDK
### A-2-1. SDK overview
fECB SDK implements 5 main functions, Capability, File, Device, HCservice, and ServiceProxy, in Python and Java programing languages respectivly for now.

* Python SDK
    * [File](#a-2-1-1-1-file)
    * [HCservice](#a-2-1-1-2-hcservice)
    * [Device](#a-2-1-1-3-device)

* JAVA SDK
    * [File](#a-2-1-2-1-file)
    * [HCservice](#a-2-1-2-2-hcservice)
    * [Device](#a-2-1-2-3-device)


#### A-2-1-1. Python SDK



##### A-2-1-1-1. File  

According to your token, get all the files under your capability.

* Exsample Usage:  
```python =
## import fECB python SDK
from fecb_python_SDK import fecb_function_client_lib

## initialize Files function in SDK
file = fecb_function_client_lib.File()
(
## set up the saved path for your file(s)
save_path = '.'

## call file.get_file() function with save_path to get your file(s)
get_file_resp = file.get_file(save_path)

## check the result in JSON
print(get_file_resp)

## check the file(s) you get
print(get_file_resp["data"])
```

##### A-2-1-1-2. HCservice

According to your token and the heterogeneous computing services' name, shows all heterogeneous computing services' address and the access ticket.

* Exsample Usage:  
```python =
## import fECB python SDK
from fecb_python_sdk import fecb_function_client_lib

## initialize HeterogeneousComputingService function in SDK
hcservice = fecb_function_client_lib.HeterogeneousComputingService()

## set up your parameters
serviceName = "your_servicename"

## call hcservice.issue_hcservice() function with serviceName to issue your hcservice
issueHCServiceResponse = HCService.issue_hcservice(serviceName)

## check the result in JSON
print(issueHCServiceResponse)

## print the address
print(issueHCServiceResponse["service_address"])
    
        
```

##### A-2-1-1-3. Device

According to your token and the device profile, get all devices under your capability and the access ticket.

* Exsample Usage:  

```python =
## import fECB python SDK
from fecb_python_sdk import fecb_function_client_lib

## initialize Device function in SDK
device = fecb_function_client_lib.Device()

## set up your parameters
profile_name = "your_profile_name"
    
## call device.issue_device_resource() function with profile_name to issue your device
issueDeviceServiceResponse = DeviceService.issue_device_resource(profile_name)

## check the result in JSON
print("issue_device_resource_resp = ", issueDeviceServiceResponse)

## make sure there is an accessile hcservice
print(issueDeviceServiceResponse["service_address"])
```


#### A-2-1-2. Java  

##### A-2-1-2-1. File  

Provides a token that indicates the capabilities of your application(s).

* Exsample Usage:  
```java =

// import fECB java SDK
import org.json.JSONObject;
import com.fiduciaedge.fecb.FileAPIService;

public static void main(String[] args) throws Exception {
    try {
        // initialize Capability function in SDK
        FileAPIService FileService = new FileAPIService();
        
        
        // set up your parameters
        String savePath = ".";

        // call file.getFiles() function with savePath to get your file(s)
        JSONObject getFileResponse = FileService.getFiles(savePath);

        // check the result in list
        System.out.println(getFileResponse); 

}
```

##### A-2-1-2-2. HCservice  

According to your token and the heterogeneous computing services' name, shows all heterogeneous computing services' address and the access ticket.

* Exsample Usage:  
```java =
// import fECB java SDK
import org.json.JSONObject;
import com.fiduciaedge.fecb.HeterogeneousComputingAPIService;

public static void main(String[] args) throws Exception {
    try {

        // initialize HeterogeneousComputingService function in SDK
        HeterogeneousComputingAPIService  HCService = new HeterogeneousComputingAPIService();
            
        
        // set up your parameters
        String serviceName = "hc-service-java";

        // call HCService.issueHCService() function with serviceName to issue your HCService
        JSONObject issueHCServiceResponse = HCService.issueHCResource(serviceName);

        // check the result in JSON
        System.out.println(issueHCServiceResponse.get("service_address"));

       
```

##### A-2-1-2-3. Device  

According to your token and the device profile, get all devices under your capability and the access ticket.

* Exsample Usage:  

```java =
// import fECB java SDK
import org.json.JSONObject;
import com.fiduciaedge.fecb.DeviceAPIService;

public static void main(String[] args) throws Exception {
    try {

        
                    DeviceAPIService DVCService = new DeviceAPIService();    
        
        // initialize Device function in SDK
        DeviceAPIService DVCService = new DeviceAPIService();

        // set up your profileName
        String profileName = "webcam-java";

        // call device.issueDevice() function with profileName to issue your HCService
        JSONObject issueDeviceResourceResponse = DVCService.issueDeviceResource(profileName);

        // check the result in JSON
        System.out.println(issueDeviceResourceResponse.get("service_address"));

       
```

#### A-2-1-3. Returned code
* Refer to standard gRPC status code
    * https://grpc.github.io/grpc/core/md_doc_statuscodes.html

---
<div STYLE="page-break-after: always;"></div>

