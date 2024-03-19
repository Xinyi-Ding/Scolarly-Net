# Architectural Design
## Technology Stack Architecture
![Technology Stack Architecture](/Documents/Image/TechStack.jpg)
*Figure 1: Technology stack architecture.*

### **Description**
The proposed architecture employs Vue coupled with Axios for front-end development, FastAPI for backend API services, Python for backend data processing, and MongoDB as the data storage solution. The defined dependencies ensure a fluid exchange of data and operations between the front-end and back-end components, promoting a cohesive and efficient workflow.

### **Frontend Components**
#### *Components List:*
- `Vue`
    - A progressive JavaScript framework used for crafting modern, interactive user interfaces. Vue is known for its declarative rendering, component-based structure, and its ability to smoothly blend with other libraries and tools. 
    - [**Vue Official Documentation**](https://vuejs.org/v2/guide/)
- `Vuex`
    - This state management pattern library is tailored for Vue.js. It serves as a centralized store for all the components in an application, with rules ensuring the state can only be mutated in a predictable fashion. 
    - [**Vuex Official Documentation**](https://vuex.vuejs.org/)
- `ElementUI`
    - A Vue.js UI toolkit for web development, ElementUI offers a collection of high-quality components and tools for building rich, responsive interfaces. 
    - [**ElementUI Official Documentation**](https://element.eleme.io/#/en-US)
- `Webpack` 
    - As a static module bundler for modern JavaScript applications, Webpack processes your application's modules and efficiently bundles them into static assets. 
    - [**Webpack Official Documentation**](https://webpack.js.org/concepts/)
- `Axios`
    - A promise-based HTTP client for making HTTP requests from the browser or Node.js applications, Axios integrates easily with Vue.js and provides a straightforward API for interaction. 
    - [**Axios Official Documentation**](https://axios-http.com/docs/intro)
- `ECharts` 
    - A powerful, interactive charting and data visualization library for the browser. It offers a variety of chart types and can be easily integrated into Vue applications. 
    - [**ECharts Official Documentation**](https://echarts.apache.org/en/index.html)

#### *Component Dependencies:*
- `Vue → Vuex` 
    - Vuex serves as the state management pattern for applications using Vue. It is essential for maintaining a centralized and coherent state across the application.
- `Vue → ElementUI` 
    - Vue utilizes ElementUI for rich UI components, which are integral to crafting an engaging user interface.
- `Vue → Axios` 
    - Axios is crucial for Vue applications to handle HTTP requests, allowing seamless communication with back-end services.
- `Vue → ECharts`
    - integration of ECharts with Vue enables the creation of interactive data visualizations within the user interface.
- `Webpack → Vue` 
    - Webpack is leveraged to bundle Vue components efficiently, enhancing application performance and asset management.
- `Webpack → ElementUI` 
    - ElementUI components are managed and bundled within the Webpack ecosystem, ensuring correct integration and styling.
- `Webpack → Axios`
    - Axios is configured within Webpack to handle asynchronous HTTP requests as part of the build process.

### **Backend Components**
#### *Component List*:
- `FastAPI`
    - A contemporary, high-performance web framework for building APIs with Python, based on standard Python type hints. 
    - [**FastAPI Official Documentation**](https://fastapi.tiangolo.com/)
- `Python`
    - As a programming language, Python is used extensively for data processing and analysis in the backend due to its powerful libraries and versatility. 
    - [**Python Official Documentation**](https://docs.python.org/3/)
- `MongoDB`
    - A document-based NoSQL database known for its scalability and flexibility, MongoDB serves as the storage engine for handling large volumes of data. 
    - [**MongoDB Official Documentation**](https://docs.mongodb.com/)
- `Grobid`
    - An open-source software library for document conversion and the extraction of bibliographical data in PDF files. It is typically used for processing academic documents and transforming them into structured TEI encoded documents. 
    - [**Grobid Official Documentation**](https://grobid.readthedocs.io/)
#### *Component Dependencies:*
- `Vue + Axios → FastAPI`
    - The front-end framework Vue, in combination with Axios, depends on FastAPI for processing API requests, enabling robust communication between the client and server.
- `FastAPI → Python`
    - FastAPI harnesses Python's capabilities to execute complex backend logic and data processing routines.
- `Python → MongoDB`
    - Python uses libraries such as PyMongo to interact with MongoDB, allowing data manipulation and retrieval for back-end processing.
- `Python → Grobid` 
    - Python may call upon Grobid services for the extraction of information from PDF documents, further processed within the business logic.

### Test Components
#### *Component List:*
- `Vitest:` 
    - A unit testing framework for Vue.js applications, designed to provide fast and reliable test execution. 
    - [**Vitest Official Documentation**](https://vitest.dev/)
- `Pytest` 
    - A mature full-featured Python testing tool that helps you write better programs. It is used for writing and executing tests on the back-end side, ensuring the reliability of Python code. 
    - [**Pytest Official Documentation**](https://docs.pytest.org/en/stable/)
#### *Component Dependencies:*
- `Vitest → Vue`
    - Vitest is utilized for testing Vue components, ensuring the front-end logic behaves as expected.
- `Pytest → Python`
    - Pytest is employed to test Python code, including data processing and business logic in the back-end, guaranteeing code quality and performance.
- `Pytest → FastAPI`
    - Pytest is also used to test FastAPI endpoints, verifying the correct behavior of API calls and responses.

### **Overal Decision-Making for Technology Selection**
The architecture and choice of technologies for the this system were methodically planned to align with the project's objectives, the proficiency of the development team, and the specific needs of our target users.

#### 1. Development Team Background
Our team comprises skilled developers with a strong background in modern JavaScript frameworks, experience in Python for data processing, and proficiency with NoSQL databases. This existing expertise strongly influenced the selection of Vue.js, FastAPI, and MongoDB to capitalize on our team's strengths and ensure a smooth development process.

#### 2. Client Communication and Requirements
Through in-depth discussions and iterative feedback sessions with stakeholders, we mapped out the crucial features and performance expectations for the system. The client emphasized the need for a responsive UI, robust data processing capabilities, and a flexible data storage approach that can accommodate complex queries, leading to our technology choices.

#### 3. Project and User Requirements Fit
The technology stack was designed to strike a balance between development efficiency and product scalability. Vue.js, along with its associated libraries, was chosen for its reactive nature and ease of integration, which aligns with our aim to deliver a responsive user experience. FastAPI, paired with Python's rapid development and rich library ecosystem, addresses our backend data processing requirements. MongoDB's schema-less design is particularly suited to our needs, offering the flexibility necessary for the varied and evolving datasets encountered in academic research. Additionally, most PDF article extractors, including plugins and libraries, output data in formats like Python dictionaries, XML, or JSON. For instance, the format used by Grobid, the tool we employ for article extraction, is XML. These formats are inherently compatible with MongoDB's storage mechanism, which uses BSON objects. This compatibility is a considerable advantage for storing and managing the data efficiently within our system.

#### 4. Security and Data Integrity
Security and data integrity are paramount in academic research platforms. Our backend technologies provide robust security features and the ability to handle sensitive data with the necessary precautions, ensuring users' data remain protected and intact.

#### 5. Data Volume Considerations
Initially, the project deals with approximately 10,000 records. MongoDB is well-suited for this data volume due to its performance efficiency. Moreover, it offers excellent horizontal scalability, reassuring us that as the project's data grows over time, we can expand our database infrastructure seamlessly.

#### 6. Concurrency and Scalability
The current concurrency requirements for the system are modest, with access provided primarily to internal staff and select clients. The backend, built on FastAPI, is deployed in Docker containers, which are lightweight and portable. Looking ahead, we can utilize Kubernetes (k8s) to orchestrate these containers, enabling horizontal scaling to accommodate any surge in user traffic without compromising performance.

#### Conclusion
The chosen technology stack is a reflection of a strategic alignment with the project goals, our team's capabilities, and the user's best interests. This harmony between technology and project requirements is expected to result in a platform that is not only effective in meeting the diverse needs of its users but also robust, secure, and scalable for future expansion.

### **Horizontal comparison of each component**
The selection of each technology component within our stack was the result of a deliberate evaluation of its strategic advantages, suitability for meeting both the project goals and the client's specific needs, and its comparison to other potential alternatives. Below we detail the rationale for our choices:

#### `Vue.js`
- **Chosen Over:** Angular, React  
- **Advantages:** Provides a simplified and adaptable structure for rapid UI development. Its component-driven architecture is ideal for dynamic user interfaces.  
- **Justification:** The selection was based on Vue.js's gentle learning curve, thorough documentation, and vibrant community. For a platform intended to serve a diverse user base, from students to government officials, a smooth and interactive user experience is paramount, which Vue.js offers with its reactive system.

#### `Vuex`
- **Chosen Over:** Redux, MobX  
- **Advantages:** Offers a streamlined state management system, essential for maintaining cohesive state throughout the application.  
- **Justification:** Vuex's native integration with Vue.js significantly simplifies state management. For a system that includes complex features like user-defined filters and search, this simplicity is invaluable.

#### `ElementUI`
- **Chosen Over:** Ant Design, BootstrapVue  
- **Advantages:** Delivers a rich suite of pre-designed components, well-integrated with Vue.js, which expedites the UI development process.  
- **Justification:** ElementUI’s consistent design language fits perfectly with our vision of an intuitive user interface that caters to the platform's wide-ranging functionality from data visualization to literature management.

#### `Webpack`
- **Chosen Over:** Rollup, Parcel  
- **Advantages:** Optimizes loading time and ensures high performance, essential for a seamless user experience.  
- **Justification:** Its wide range of plugins and community support offers a more customizable setup, which is vital for handling the complex asset management our system requires.

#### `Axios`
- **Chosen Over:** Fetch API, SuperAgent  
- **Advantages:** Presents a robust solution for HTTP requests with a promise-based API, simplifying server communication.  
- **Justification:** Axios's widespread adoption and ease of use make it the best choice for our project, especially considering the need for efficient communication between the system's front end and the back end.

#### `ECharts`
- **Chosen Over:** D3.js, Chart.js  
- **Advantages:** Offers comprehensive charting and interactive visualization capabilities, crucial for academic data representation.  
- **Justification**:_ ECharts strikes a balance between customization and ease of use, making it suitable for the advanced data analysis and visualization required by our users, from students conducting literature reviews to companies engaging in market analysis.

#### `FastAPI`
- **Chosen Over:** Flask, Django REST framework  
- **Advantages:** Known for its fast performance and asynchronous nature, ideal for high-performance APIs.  
- **Justification:** The modern approach to API development and automatic Swagger documentation generation aligns with our goal to provide a powerful yet user-friendly platform for academic research.

#### `MongoDB`
- **Chosen Over:** MySQL, PostgreSQL  
- **Advantages:** The schema-less design offers unparalleled flexibility in managing diverse datasets.  
- **Justification:** MongoDB's ability to handle unstructured data efficiently is crucial for the academic articles and related metadata, ensuring the system remains adaptive and scalable.

#### `Grobid`
- **Chosen Over:** Tika, PDFBox  
- **Advantages:** Specializes in extracting information from PDF documents, essential for processing academic papers.  
- **Justification:** Given the system's focus on academic literature analysis, Grobid is ideally suited for converting articles into a structured format for further processing and analysis.

#### `Vitest`
- **Chosen Over:** Jest, Mocha  
- **Advantages:** Provides an efficient and reliable framework for Vue.js front-end testing.  
- **Justification:** The system requires robust front-end testing to maintain a high-quality user experience, and Vitest offers superior integration with Vue.js compared to other frameworks.

#### `Pytest`
- **Chosen Over:** unittest, Nose2  
- **Advantages:** Enables comprehensive backend testing, indispensable for data processing integrity.  
- **Justification:** Pytest's extensive plugin system and simplicity ensure a streamlined testing process, which is vital for the complex data handling our system performs.

#### `Docker and Kubernetes`
- **Chosen Over:** Traditional VMs, Heroku  
- **Advantages:** Provide the flexibility to manage and scale applications seamlessly, necessary for modern application deployment.
- **Justification:** The agility afforded by Docker and Kubernetes in deployment and infrastructure management will enable the system to adapt to user growth and changing requirements effectively.

#### Conclusion
In conclusion, the selected technology stack not only fulfills the individual requirements of performance, scalability, and usability but also integrates into a cohesive architecture that aligns with the overall purpose of the PSD system. Each technology component has been chosen with a strategic perspective, ensuring that the system is well-equipped to support the intricate tasks of academic literature research and analysis, catering to the diverse needs of students, researchers.

### **Example of Alternative Technology Stack**

#### `React + Redux`
- **Chosen Over:** Vue.js + Vuex  
- **Advantages:** Offers a robust ecosystem and is highly performant in large-scale applications.
- **Limitations:** React and Redux introduce a steeper learning curve and added complexity, which might not align with the ease of use required for our academic-focused platform.

#### `Tailwind CSS`
- **Chosen Over:** ElementUI  
- **Advantages:** Provides a utility-first approach for more granular control over design and responsive features.
- **Limitations:** Lacks a comprehensive suite of pre-designed components, potentially slowing down the development process.

#### `Vite`
- **Chosen Over:** Webpack  
- **Advantages:** Promises faster rebuilds and simpler configuration.
- **Limitations:** The relative newness means a smaller plugin ecosystem and less community support compared to Webpack.

#### `Fetch API`
- **Chosen Over:** Axios  
- **Advantages:** Built-in within browsers, removing the need for external libraries.
- **Limitations:** Does not provide features like automatic JSON data transformation that Axios offers.

#### `Chart.js`
- **Chosen Over:** ECharts  
- **Advantages:** Lightweight with a straightforward API, suitable for basic charting requirements.
- **Limitations:** Does not support complex and interactive visualizations that our system requires for academic data analysis.

#### `Django + Django REST Framework`
- **Chosen Over:** FastAPI  
- **Advantages:** A full-stack framework with a mature ecosystem, complemented by a RESTful API-building toolkit.
- **Limitations:** Lacks the performance and modern API development features of FastAPI, such as automatic Swagger documentation.

#### `PostgreSQL`
- **Chosen Over:** MongoDB  
- **Advantages:** Powerful SQL database with strong compliance to standards.
- **Limitations:** Not as adept as MongoDB at handling unstructured data, which is critical for our evolving academic datasets.

#### `Cypress`
- **Chosen Over:** Vitest  
- **Advantages:** Offers an excellent setup for end-to-end testing with a rich feature set.
- **Limitations:** More focused on end-to-end testing and could be less efficient for unit testing specific to Vue.js.

#### `Flask + Flask RESTPlus`
- **Chosen Over:** FastAPI  
- **Advantages:** Simple and easy to learn, with Flask RESTPlus for building RESTful APIs.
- **Limitations:** Does not provide the same level of performance and built-in data validation features as FastAPI.

#### `Heroku`
- **Chosen Over:** Docker + Kubernetes  
- **Advantages:** Simplifies application deployment directly in the cloud.
- **Limitations:** Does not offer the containerization and orchestration capabilities necessary for scalable and complex deployments.

#### Comparative Analysis
The alternative stack provides certain benefits; however, it poses significant limitations in terms of the complexity of learning and managing the technologies, the development speed, performance, and flexibility in handling unstructured data, as well as in scalability and deployment management. These limitations underscore the reasons for our selected technology stack, which provides a more user-friendly, efficient, and scalable solution tailored to the needs of a diverse academic audience.

### Component Architecture
![Component Architecture](/Documents/Image/ComponentGraph.png)
*Figure 2: The overview of the component architecture for the application.*

#### Overview
the system utilizes a 5-tier architecture to separate concerns, enhance scalability, and improve maintainability. This architecture allows for a clear distinction between the client interface, presentation logic, business processes, integration services, and resource management. By dividing the system into these layers, the system benefits from increased modularity, which simplifies updates and maintenance. Each tier can be developed and scaled independently, facilitating easier upgrades and integration with other systems or services. The separation also aids in security, as each layer acts as a gatekeeper to the next, ensuring that only authorized operations are performed.

#### Client Tier
- **ClientUI**: 
  - Description: The user interface through which users interact with the system. It is designed to be intuitive and facilitate easy access to the system's features.
  - Relation: This is the primary interface for users to input queries and view results related to academic paper analysis.

#### Presentation Tier
- **Controller**: 
  - Description: Manages user input, processes user requests, and sends commands to the model to update the view accordingly.
  - Relation: Acts as an intermediary between the ClientUI and the business logic, ensuring that user actions are translated into operations on the model.
- **View**: 
  - Description: Displays data to the user and sends user commands to the controller.
  - Relation: Represents the visualization of the data that the system handles, such as showing the extracted paper details and connection maps.

#### Business Tier
- **SessionFacade**: 
  - Description: Provides a simplified interface to complex subsystems in the business tier, often used to reduce network calls.
  - Relation: In the system, it could manage user sessions and streamline interactions with complex data processing tasks for paper analysis.
- **ValueObject**: 
  - Description: Holds data that is passed between components, reducing the number of method calls required.
  - Relation: Transfers relevant data like paper details and metadata across different components of the system.

#### Integration Tier
- **DataAccessObject (DAO)**: 
  - Description: Abstracts and encapsulates all access to the data source, managing the connection to the database and the execution of queries.
  - Relation: Responsible for retrieving and storing data related to academic papers from the database in the system.
- **ServiceActivator**: 
  - Description: Invokes services in an asynchronous fashion, can be used for message-driven beans or to initiate services without a direct client request.
  - Relation: In the system, it may handle asynchronous tasks such as initiating analysis of new academic papers or updating the reference tree.

#### Resource Tier
- **DataBase**: 
  - Description: Stores all the persistent data needed for the system to function, such as user accounts, paper details, and connection data.
  - Relation: Acts as the central repository for the system, where all the academic papers and related metadata are stored.
- **WebService**: 
  - Description: Provides a way for the system to communicate with external services over the internet, such as external databases of academic papers.
  - Relation: Could be used in the system to fetch paper details from external sources or to integrate with other academic research tools.