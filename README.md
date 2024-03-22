# Group Carlson-Johnson
[![pipeline status](https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson/badges/main/pipeline.svg)](https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson/-/commits/main)

## Table of Content

- [Project Description](#project-description)
- [Quick Start](#quick-start)
- [Project Documents List](#project-documents-list)
  - [Formative Assessment](#formative-assessment)
  - [Group Assessment](#group-assessment)
  - [Project Meeting](#project-meeting)
- [Contributers](#contributers)

## Project Description

The aim of this project is to develop a system for analysing academic papers. The system will support analyses of authorship, sentiment, subject and topic. Users will be able to import articles into the data store in order to perform a variety of analytical queries including paper topic clustering, inter-author linking, inter-topic linking, relationships between authors and topics, sentiment analysis, paper outcomes, citation networks and timelines.

### Client
The client for this project is the course organisation team for practical software development in the EPCC MSc programme.

## Quick Start
Our project has been deployed in the EIDF VM and the implementation can be found in the CICD implementation documentation. Users who have access to the EIDF `eidf018-psd-assessment10a` VM can directly use the browser in the VM to access http://localhost:90. If you want to run this application on your local computer, you can refer the [setup](Documents/Setup.md) document.

![VM Deployment](./Documents/Image/CD.png)
*Figure 1: The flow chart of the deployment in EIDF VM.*

### Instruction
1. Login to [EIDF protal](https://portal.eidf.ac.uk) by using your SAFE account.
![Step1](./Documents/Image/QUICK1.png)
*Figure 2: Screenshot for EIDF protal.*

2. Choose `VDI Login` under Projects >> Your Projects
![Step2](./Documents/Image/QUICK2.png)
*Figure 3: Screenshot for find VDI login.*

3. Select the `eidf018-psd-assessment10a_rdp` connection.
![Step3](./Documents/Image/QUICK3.png)
*Figure 4: Screenshot for find VM connection.*

4. When login to the VM connection, click web browser and type http://localhost:90 to access our application. The full detail how to interact with our website can refer to [guide](Documents/Guide.md) documents.
![Step4](./Documents/Image/QUICK4.png)
*Figure 5: Screenshot for how to access our web application in web browser.*

## Project Documents List

### Formative Assessment

The given prototype of the project is located in branch '[proto](https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson/-/tree/proto)'.

- [Formative Assessment](https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson/-/blob/proto/README.md)

### Group Assessment

All project documents are located in [Documents](./Documents/) folder.
Certainly! Here are the checklists with checkboxes for each item:

- Design Stage
  - [System Design](./Documents/Design.md)
- Planning Stage
  - [Architecture and Components Designn](./Documents/Architecture-And-Components-Design.md)
  - [Project Planning](./Documents/Plan.md)
- Implementation Stage
  - [Setup Instruction](./Documents/Setup.md)
  - [Guild to Use the Web Application](./Documents/Guide.md)
  - [Backend API Documentation](./Documents/API/api-docs.md)
  - [CI/CD Deployment and Implementation](./Documents/CICD.md)
  - [Test Analysis](./Documents/Test-Analysis.md)
  - [Evaluation](./Documents/Evaluation.md)

### Group Presentation

- [Group Presentation Slices](./Documents/Carlson-Johnson-PSD-Presentation.pptx)

### Project Meeting

- [Project Meeting Minutes](https://git.ecdf.ed.ac.uk/psd2324/Carlson-Johnson/-/wikis/Meeting-Minutes)


## Contributers

- Kejia Zhang
- Xinyi Ding
- Yongkang Qiu
- Yucheng Liang

Supported by Daniyal Arshad

## Acknowledgement
We would like to extend our heartfelt appreciation to the EPCC PSD Course Supervisor Team and Daniyal Arshad for their invaluable support and guidance throughout this project. Their expertise and encouragement have been essential to our success.
