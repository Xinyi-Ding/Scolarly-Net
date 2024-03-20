# Architectural Design
## Technology Stack Architecture
![Technology Stack Architecture](/Documents/Image/TechStack.jpg)
*Figure 1: Technology stack architecture.*

### **Description**
The proposed architecture employs Vue coupled with Axios for front-end development, FastAPI for backend API services, Python for backend data processing, and MongoDB as the data storage solution. The defined dependencies ensure a fluid exchange of data and operations between the front-end and back-end components, promoting a cohesive and efficient workflow.

#### *Why Front-End*?
The architectural choice of a separated front-end in our system architecture is essential for several strategic reasons:
1. **Specialized Focus:** Front-end separation allows for a focused approach to user experience design, tailored specifically to the varied needs of our users. By decoupling the user interface from the server-side logic, we can tailor the front-end to support scenarios such as data-driven academic research, policy analysis, and comprehensive literature reviews without being constrained by back-end processes.
2. **Agility and Scalability:** A separated front-end facilitates agile development and deployment. As the needs of students, academics, and professionals evolve, the front-end can be updated and scaled independently of the back-end services, ensuring the system remains responsive to the changing demands of evidence-based decision-making.
3. **Performance and Optimization:** This separation allows for the optimization of front-end resources for speed and efficiency, critical for tasks such as rendering complex data visualizations or managing extensive literature databases, ensuring that the system is both powerful and responsive.
4. **Enhanced User Interaction:** By focusing on the front-end, we can ensure that features such as citation tracking, note-taking, and customizable searches are implemented in a way that is intuitive and efficient, enhancing the overall user experience and facilitating the academic writing process.
5. **Flexibility in Technology Stack:** The separation allows us to choose the most appropriate technologies for the front-end, ensuring that the system's interface is built using tools best suited for creating a dynamic and user-friendly environment. It also means that as new front-end technologies emerge, the system can adapt without the need for extensive back-end overhauls.
6. **Streamlined Development Workflow:** A separate front-end enables a streamlined workflow for developers, where front-end and back-end teams can work in parallel on different aspects of the system. This approach reduces bottlenecks and accelerates the development process, which is essential for a complex system designed to handle a vast array of academic research functions.
7. **Ease of Testing and Maintenance:** Testing the user interface becomes more manageable when it is decoupled from the back-end logic. The front-end can be tested for usability and performance independently, ensuring that the system remains reliable and effective for user-driven exploration and analysis.

In essence, the decision to architect a distinct front-end directly supports the system's ambition to be a comprehensive research and analysis platform that remains user-centric, agile, and technologically robust. This separation is vital for ensuring that the system not only meets but exceeds the expectations of its diverse user base.

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

### **Test Components**
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

### **Deployment Components**
#### *Component List:*
- `Docker`: A containerization platform that encapsulates applications and their environments for consistent deployment across different systems. Docker ensures that applications run the same, regardless of where they are deployed. It provides a way to package the application with its environment and dependencies into a container, which can be transported and run anywhere Docker is supported.

#### *Component Dependencies:*
- `Frontend Container -> All Frontend Components`: The frontend container bundles all frontend components including Vue, Vuex, ElementUI, Webpack, Axios, and ECharts. This container is responsible for the presentation layer of the application, providing the user interface and handling interactions with the user.
  
- `Backend Container -> All Backend Components (Except Grobid Component)`: The backend container encompasses the components required for the application's server-side operations, such as FastAPI, Python, and MongoDB. This container handles API requests, business logic, data processing, and analysis. It interacts with the frontend container to serve processed data and accept user inputs.
  
- `Grobid Container -> Grobid`: This container is dedicated to running Grobid, a tool for extracting information from PDF documents. It acts as a standalone service that can be utilized by the backend for processing academic documents and transforming them into structured data.

### **Decision-Making for Technology Selection**
The architecture and choice of technologies for the this system were methodically planned to align with the project's objectives, the proficiency of the development team, and the specific needs of our target users.
#### 1. *Development Team Background*
- Our team comprises skilled developers with a strong background in modern JavaScript frameworks, experience in Python for data processing, and proficiency with NoSQL databases. This existing expertise strongly influenced the selection of Vue.js, FastAPI, and MongoDB to capitalize on our team's strengths and ensure a smooth development process.
#### 2. *Project and User Requirements Fit*
- Through in-depth discussions and iterative feedback sessions with stakeholders, we mapped out the crucial features and performance expectations for the system. The client emphasized the need for a responsive UI, robust data processing capabilities, and a flexible data storage approach that can accommodate complex queries, leading to our technology choices.
- The technology stack was designed to strike a balance between development efficiency and product scalability. Vue.js, along with its associated libraries, was chosen for its reactive nature and ease of integration, which aligns with our aim to deliver a responsive user experience. FastAPI, paired with Python's rapid development and rich library ecosystem, addresses our backend data processing requirements. MongoDB's schema-less design is particularly suited to our needs, offering the flexibility necessary for the varied and evolving datasets encountered in academic research. Additionally, most PDF article extractors, including plugins and libraries, output data in formats like Python dictionaries, XML, or JSON. For instance, the format used by Grobid, the tool we employ for article extraction, is XML. These formats are inherently compatible with MongoDB's storage mechanism, which uses BSON objects. This compatibility is a considerable advantage for storing and managing the data efficiently within our system.
#### 3. *Security and Data Integrity*
In an academic research platform like ours, where the integrity of scholarly work and the privacy of personal and institutional data are of utmost importance, the selection of backend technologies that prioritize security and data integrity is crucial. **FastAPI** and **MongoDB** have been chosen with these priorities in mind, offering advanced security features tailored to the needs of our diverse user base, from students to government agencies.

- **FastAPI:** This framework is designed with security as a core feature, offering easy integration with secure authentication and authorization systems like OAuth2 and JWT tokens. This is particularly important for our system, which caters to a wide range of users, each requiring controlled access to different levels of data and functionality. For example, students may need access to public academic resources, while academics and government officials may require access to sensitive or proprietary data.
  
- **MongoDB:** Known for its robust security mechanisms, MongoDB offers encryption at rest and in transit, ensuring that all data, from student notes to confidential research findings, is securely stored and transferred. Access control, auditing features, and regular security patches further enhance data integrity, providing peace of mind for users reliant on the system for their research and decision-making processes.

The integration of these technologies ensures that all user interactions with the system, from data entry to complex queries, are conducted in a secure environment, safeguarding against unauthorized access and data breaches. This adherence to high security and data integrity standards is essential for maintaining the trust and reliability expected by our users in their scholarly and professional endeavors.

#### 4. *Data Volume Considerations*
Given the system's aim to serve as a comprehensive platform for academic research, it will initially handle approximately 10,000 records, encompassing a wide range of data types from simple bibliographic information to complex analysis results. **MongoDB** has been selected as our database solution for its exceptional ability to manage such diverse data volumes efficiently.

- **Scalability:** MongoDB's document-oriented structure and schema-less design provide significant flexibility, allowing us to easily accommodate the evolving nature of academic data. This is particularly important as the system grows to include more records and more complex types of data analysis, ensuring that we can scale our database infrastructure without extensive re-engineering.

- **Performance:** MongoDB's indexing capabilities, sharding, and replication features are designed to maintain high performance even as data volume grows. This is crucial for our system, which must deliver quick and accurate search results across vast datasets to users conducting time-sensitive research.

- **Data Management:** The system's features, such as advanced research functionality, data management tools, and analysis and visualisation capabilities, require a database that can handle complex queries and aggregate functions efficiently. MongoDB's rich query language and aggregation framework enable us to provide these sophisticated features without compromising on performance.

The choice of MongoDB, with its emphasis on performance, scalability, and flexibility, aligns with our project's goals and the varied requirements of our users. Whether it's a student compiling a literature review or a government agency conducting policy analysis, our database infrastructure is equipped to support their diverse needs effectively.
#### 5. *Concurrency and Scalability*
In the context of the diverse and dynamic needs outlined in the system's purpose and intended user base, the system's architecture must be inherently scalable and capable of handling concurrent access across varied use cases. From in-depth literature reviews by students to complex data analysis for government policy formulation, the system's workload can be highly variable and unpredictable. This necessitates a backend infrastructure that can effortlessly adapt to changing demands without degradation in performance.

The choice to build the backend with **FastAPI** and deploy it within **Docker containers** is strategic, ensuring lightweight, isolated environments that are both efficient and portable. This containerization serves multiple purposes:
- **Isolation:** Each Docker container provides an isolated environment for a segment of the system's functionality, ensuring that any changes or issues within one container do not affect others, which is crucial for maintaining the system's stability across its varied user base.
- **Portability:** Docker containers can be easily moved, copied, and deployed across different environments, enhancing the development lifecycle and ensuring consistency between development, testing, and production environments. This is particularly beneficial given the system's broad scope, which might require deployment across different institutions with varying infrastructure setups.
- **Resource Efficiency:** Containers require less overhead than traditional virtual machines, allowing more efficient use of system resources. This is key for a system expected to handle complex data processing tasks such as extracting paper details, analyzing topic connections, and visualizing author relationships.

Looking forward, the integration of **Kubernetes (k8s)** for container orchestration will enable the system to dynamically scale resources across containers in response to real-time demand. Kubernetes facilitates:
- **Horizontal Scaling:** Automatically increasing or decreasing the number of container instances based on the system's current load. This ensures that the system can handle peak loads efficiently, such as during exam periods for students or end-of-quarter analysis for companies, without permanent allocation of excessive resources.
- **Load Balancing:** Distributing user requests intelligently across multiple container instances to ensure optimal resource utilization and response times. This is crucial for maintaining a seamless user experience, whether it's a student rapidly searching for literature or a company conducting extensive market analysis.
- **Self-healing:** Automatically restarting failed containers, replacing them, and rebalancing loads without downtime. This resilience is vital for a system that supports critical research and decision-making processes across different sectors.

In summary, the system's backend architecture, built on FastAPI and deployed in Docker containers with future Kubernetes integration, is designed to meet the scalability and concurrency requirements inherent in serving a diverse and demanding user base. This approach ensures that the system remains responsive, efficient, and adaptable, catering to the dynamic needs of students, academics, government agencies, and companies engaged in various forms of academic and industry-specific research.
#### Conclusion
The selection of Vue.js, FastAPI, and MongoDB was a strategic decision grounded in a comprehensive understanding of our team's strengths, project requirements, and user needs. This thoughtful alignment is poised to yield a platform that is not only effective in fulfilling the diverse requirements of its users but is also fortified with the robustness, security, and scalability needed for future growth. The integration of these technologies underscores our commitment to delivering a high-quality, user-centric academic research platform.

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
In conclusion, the selected technology stack not only fulfills the individual requirements of performance, scalability, and usability but also integrates into a cohesive architecture that aligns with the overall purpose of the system. Each technology component has been chosen with a strategic perspective, ensuring that the system is well-equipped to support the intricate tasks of academic literature research and analysis, catering to the diverse needs of students, researchers.

### **Alternative Technology Stack**
Here is an alternative technology stack that could have been chosen for the system, along with a comparative analysis of its advantages and limitations compared to the selected stack.

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

## Software Architecture
![Component Architecture](/Documents/Image/ComponentGraph.png)
*Figure 2: Component architecture for the application.*

### **Overview**
The system adopts a 5-tier architecture, strategically designed to modularize the functional aspects of academic literature research and analysis. This tiered approach enables effective separation of concerns, fostering enhanced scalability, improved maintainability, and secure operation. It ensures that the client interface, presentation logic, business processes, integration services, and resource management remain distinct yet seamlessly interact. This design not only streamlines development and maintenance but also optimizes the system’s security by layering access controls and operational permissions.

#### **Client Tier**
- **Description:** The Client Tier is the system's front-facing layer, hosting the ClientUI that users interact with. This tier is dedicated to delivering the user interface through which all user inputs and interactions occur, designed for accessibility and usability.
- **Relation:** It directly interacts with the Presentation Tier, sending user requests down the tier hierarchy and presenting processed data back to the user.
- **Components:**
    - `ClientUI`
- **Advantages:** Provides a centralized interface for all user interactions, simplifying the user experience and offering a gateway to the underlying functionalities.
- **Potential Downsides:** As the most exposed layer, it's vulnerable to attacks; hence, it requires robust security measures.

#### **Presentation Tier**
- **Description:** The Presentation Tier manages the application's logic for presenting data to the user. It interprets commands from the Client Tier and decides how to represent information to users effectively.
- **Relation:** It acts as an intermediary, transforming data from the Business Tier into a user-friendly format and vice versa.
- **Components:**
    - `AuthorAffilliation`
    - `CoAuthors`
    - `CitedTree`
    - `SameTopic`
    - `TopicConnection`
    - `PaperDashboard`
    - `CatalogAPI`
    - `AnalysisAPI`
- **Advantages:** Separates the logic of how data is displayed from the core business logic, allowing designers and developers to work independently.
- **Potential Downsides:** Increased complexity in data handling and potential performance bottlenecks if not well-optimized.

#### **Business Tier**
- **Description:** This tier contains the core business logic of the system, processing user requests, performing operations, and making logical decisions.
- **Relation:** It interfaces with the Presentation Tier to receive processed user inputs and interacts with the Integration Tier to fetch and manipulate data.
- **Components:**
    - `Models`
    - `Schema`
    - `Catalog`
    - `Analysis`
    - `Extractor`
    - `GrobidClient`
    - `Client`
    - `Parser`
    - `Types`
- **Advantages:** Centralizes business logic, promoting reusability and consistency across the system.
- **Potential Downsides:** Complex logic can be difficult to manage and may become a bottleneck for performance if not carefully architected.

#### **Integration Tier**
- **Description:** This tier orchestrates the communication between the Business Tier and the Resource Tier, facilitating the integration of different data sources and external services.
- **Relation:** It serves as a conduit for data, ensuring that requests and responses flow between the front-end and back-end systems correctly and efficiently.
- **Components:**
    - `CatalogAccess`
- **Advantages:** Allows for a decoupled architecture where the core business logic is insulated from changes in data sources and external services.
- **Potential Downsides:** Adds another layer of complexity and can be a point of failure if not robustly designed.

#### **Resource Tier**
- **Description:** The Resource Tier is responsible for managing all data storage and retrieval operations, ensuring data integrity and security.
- **Relation:** It interacts directly with the Integration Tier to provide the necessary data to fulfill business operations.
- **Components:**
    - `MongoengineModels`
- **Advantages:** Provides a dedicated layer for data operations, allowing for optimized data management and scalability.
- **Potential Downsides:** Requires careful management to prevent data bottlenecks and maintain performance, especially under high load conditions.

Each tier’s design considers the project’s goals and user needs, ensuring that students, academics, and professionals can effectively conduct literature research, analysis, and visualization without facing the complexities of the underlying system. The architecture provides the framework to support the advanced research functionality, data management tools, citation tracking, and analysis and visualization capabilities that are key to meeting the diverse requirements of the system's users. However, the layered approach, while beneficial for organization and scalability, introduces additional complexity and may necessitate careful consideration of performance and security implications at each level.

### Components Design

#### `ClientUI`
#### `AuthorAffilliation`
#### `CoAuthors`
#### `CitedTree`
#### `SameTopic`
#### `TopicConnection`
#### `PaperDashboard`
#### `CatalogAPI`
#### `AnalysisAPI`


### Alternative Software Architecture
While the 5-tier architecture described provides a robust and scalable framework for the system, an alternative architecture could be considered to address specific needs or constraints. One such alternative might be a microservices-based architecture. In this approach, the system is decomposed into a set of small, autonomous services, each implementing a specific business capability.

#### Microservices-based Architecture
- **Description:** A microservices architecture structures an application as a collection of loosely coupled services, each designed to execute a unique business function. Each service is self-contained and can be developed, deployed, and scaled independently.
- **Components:**
    - `Search Service`: Manages literature search functionalities.
    - `User Management Service`: Handles authentication and user profiles.
    - `Data Processing Service`: Executes extraction, analysis, and parsing of academic papers.
    - `Data Storage Service`: Manages data persistence and retrieval.
    - `API Gateway`: Provides a single entry point for all client requests.

#### Limitations and Misalignments with Business and Project Goals
- **Tight Coupling with Components**: While microservices offer independence, they may require more coordination when changes occur that span multiple services. This could lead to a tightly coupled system if not managed correctly, which contradicts the goal of having a modular system that simplifies updates and maintenance.

- **Complex Service Interactions**: The system aims to create dynamic networks of connections between articles, authors, and topics. Microservices communicating over a network can introduce complexity and latency in these interactions, potentially reducing the system's responsiveness and user experience.

- **Data Consistency**: The Resource Tier in the 5-tier architecture ensures consistent and centralized data management. In a microservices architecture, each service may have its own database, leading to challenges in maintaining data consistency across services, which is critical for the system's intended use in academia and policy analysis.

- **Deployment Overhead**: The intended users include students and academics who may not have extensive technical expertise. A microservices architecture could introduce overhead in deployment and management, potentially complicating the operational aspect for such users.

- **Security**: Each microservice might expose its own API, which could increase the attack surface of the system. The 5-tier architecture's layering of access controls might be more straightforward to secure compared to the numerous endpoints that microservices would introduce.

- **Resource Utilization**: Microservices can be more resource-intensive, as each service may require its own runtime environment. For smaller user groups like individual researchers or small companies, this might not align with the project goal of providing a user-friendly and cost-effective system.

- **User Experience Consistency**: Given the system’s diverse user base, consistent user experience is crucial. The 5-tier architecture facilitates a unified user interface, whereas a microservices approach might lead to fragmentation, affecting usability for students and academics who are the primary users.

In conclusion, while a microservices architecture offers certain advantages such as independence and scalability, it may not align well with the system's current goals and user requirements. The complexity, potential for tight coupling, challenges in maintaining data consistency, deployment overhead, and security considerations present significant limitations for the project. The original 5-tier architecture is better suited to the system’s need for a coherent, secure, and user-friendly platform for academic literature research and analysis.