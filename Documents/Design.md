# PSD Project Design

## Introduction

## System Overview
The proposed PSD (Paper Source Discovery) system is designed to provide a comprehensive platform for the analysis and exploration of academic papers and related sources. The system integrates various features to facilitate efficient information extraction, connection mapping, and user-driven exploration.
### Key Components:
  1. **Paper Details Extraction:**
  2. **Topic Connection:**
  3. **Author Relationship:**
  4. **Reference Tree:**
  5. **User Defined Filter and Search:**
### System Interaction:
Researchers and analysts can upload articles, triggering the extraction of key details. The system then creates a dynamic network of connections between articles, authors, and topics. Users can explore these connections through an intuitive interface, supported by visualizations such as topic clusters, author collaboration networks, and citation trees.

The system aims to not only streamline information retrieval but also foster a deeper understanding of the relationships and influences within the academic landscape. It supports real-time query processing, interactive analysis, and collaborative features to enhance the overall research experience.

## High-level design of an end-to-end solution

## Architectural Design

### Technology Stack Architecture
<img src="/Documents/Image/TechStack.jpg" alt="Technology Stack Architecture" width="700" height="600">

#### Description
The overall architecture involves Vue and Axios for frontend development, FastApi for backend API services, Python for backend data processing, and MongoDB/Neo4j for data storage. The dependencies establish a seamless flow of data and operations between the frontend and backend components.

#### Front End
- **Components**:
  - **Vue:** A progressive JavaScript framework for building modern, responsive user interfaces. Vue emphasizes declarative rendering, component-based architecture, and seamless integration with other libraries.
  - **Vuex:** A state management library designed specifically for Vue.js applications. Vuex facilitates centralized state management, enabling efficient handling of shared data between components and maintaining a predictable state flow within the application.
  - **ElementUI:** A comprehensive Vue.js component library that provides a diverse set of pre-designed UI elements, such as forms, tables, and modals. ElementUI promotes rapid development by offering a consistent and visually appealing design system.
  - **Webpack:** A powerful module bundler and build tool for JavaScript applications. Webpack simplifies the management of project assets, facilitates code splitting, and optimizes the performance of web applications through efficient bundling and minification processes.
  - **Axios:** A promise-based HTTP client for the browser and Node.js, Axios seamlessly integrates with Vue.js to simplify asynchronous data fetching and manipulation. It provides a clean and concise API for handling HTTP requests and responses.
  - **ECharts:** A versatile JavaScript charting library that supports various chart types and interactive features. ECharts is particularly suitable for creating dynamic and visually engaging data visualizations, making it an ideal choice for representing complex datasets in a user-friendly manner.

- **Dependencies**
  - **Vue → Vuex**  
  Vue depends on Vuex for managing application-level state. Vuex provides a centralized statemanagement pattern for Vue applications, allowing efficient state sharing among components.
  - **Vue → ElementUI**  
  Vue relies on ElementUI as a component library to enhance the user interface. ElementUIprovides a set of pre-designed and customizable UI components, simplifying the process ofbuilding modern and visually appealing Vue applications.
  - **Vue → Axios** 
  Vue utilizes Axios for handling HTTP requests. Axios is a JavaScript library thatfacilitates asynchronous data fetching, making it an essential dependency for Vueapplications to communicate with backend servers and APIs.
  - **Vue → ECharts**  
  Vue integrates with ECharts to enable data visualization within the application. ECharts isa JavaScript charting library that provides a variety of interactive and dynamic chartoptions, allowing Vue applications to present data in a visually compelling manner.
  - **Webpack → Vue**  
  Webpack is responsible for bundling and managing front-end resources. Vue is one of thefront-end frameworks that Webpack supports, allowing developers to organize Vue components,templates, and styles efficiently.
  - **Webpack → ElementUI**  
  Webpack includes ElementUI as part of the front-end build process. Webpack manages theintegration of ElementUI components into the application, ensuring that the necessary stylesand scripts are bundled correctly.
  - **Webpack → Axios:**  
  Webpack incorporates Axios to handle HTTP requests during the build process. This allows Vue applications, managed by Webpack, to make asynchronous requests for data, ensuring a seamless integration of data fetching and bundling.

#### Back End
- **Components**:
  - **FastApi:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
  - **Python:** A versatile programming language used for data processing and analysis in the backend. Python provides powerful libraries for various tasks, making it a suitable choice for backend development.
  - **MongoDB/Neo4j:** NoSQL databases used for storing and retrieving data in the backend. MongoDB is a document-oriented database, while Neo4j is a graph database, allowing flexibility in data modeling based on the application's requirements.

- **Dependencies**
  - **Vue + Axios → FastApi**  
  Vue, along with Axios, depends on FastApi for handling API requests. FastApi serves as the backend API framework, efficiently managing the communication between the frontend and backend components.
  - **FastApi → Python**  
  FastApi relies on Python for implementing the business logic and data processing tasks. Python's rich ecosystem of libraries makes it well-suited for handling complex backend operations.
  - **FastApi → MongoDB/Neo4j**  
  FastApi interacts with MongoDB and/or Neo4j databases to store and retrieve data. This dependency enables FastApi to persistently store information and perform data-related operations based on the chosen database model.
  - **Python → MongoDB/Neo4j**  
  Python communicates with MongoDB and/or Neo4j databases for data processing and analysis. This interaction allows Python to leverage the data stored in these databases, supporting functionalities such as data manipulation, aggregation, and analysis.

### Component Architecture
<img src="/Documents/Image/ComponentGraph.png" alt=" Component Architecture" width="700" height="600">

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


## Requirements Analysis

### 1. [Paper Details Extraction (Topic/Keyword/Author/Reference)](#1-paper-details-extraction-topickeywordauthorreference)

Extracting information from articles is one of the most basic functions in the whole system. This feature extracts key information such as topics, keywords, authors and references from user uploaded articles or existing article databases. The extracted information can be stored in the database which can be queried and retrieved by other functions in the system. This will help researchers to quickly understand and organise the literature and make it easier for researchers to analyse and organise connections between academic sources.

### 2. <a id="topic-connection">Topic Connection</a>
The system must enable users to explore and navigate through different topics or interconnected topics within the same domain. This includes facilitating the discovery of related subtopics and presenting articles covering diverse but relevant subjects within broader domains.
    
### 3. <a id="author-relationship">Author Relationship</a>
The system should establish and display various types of relationships between authors based on their professional connections. This includes associating authors who have collaborated on the same paper, linking authors working in the same company or department, and showcasing relationships between authors with shared accolades.

### 4. Reference Tree
Most academic papers cite other research works, usually listed in the References section at the end of the document. This feature aims to enable users to construct a citation tree based on the References section of a current paper. It visually represents the citations of the current paper and its subsequent references, offering a clearer understanding of the paper's citation network.
Optionally, we could also develop a 'Cited-by Tree' to identify all papers that have cited the current paper, along with their previous level of references. This helps users comprehend the impact of the paper on subsequent research.

### 5. User Defined Filter and Search
One crucial aspect of the proposed system is the implementation of a robust user-defined filter and search functionality. This feature empowers users across different domains, including students, academics, government officials, developers, and companies, to tailor their research queries based on specific criteria. The system will provide a highly customizable search interface allowing users to filter academic papers and other sources with precision.

## Design Details

### 1. <a id="1-paper-details-extraction-topickeywordauthorreference">User Defined Filter and Search</a>

#### Key Components

- 1a. [**Topic Extraction**](#topic-extraction)

- 1b. [**Keyword Extraction**](#keyword-extraction)

- 1c. [**Author Identification**](#author-identification)

- 1d. [**Reference Extraction**](#reference-extraction)

#### 1a. <a id="topic-extraction">Topic Extraction</a>

##### Description

This function should be able to extract the main research areas or core themes of discussion from the input papers. Eventually the information shourl be deposited into a database and the papers can be grouped by using the selected topic as key.

##### Design Details

- Requirement Design:
  - This should be able to identify and extract the main areas of research or core themes discussed from papers.

  - This should be able to handle papers from a variety of academic fields and accurately identify sprcialisms or disciplines.

  - Can accurately determine the sub-disciplines under each discipline.

  - It is possible to query the database for existing topic categories and add multiple articles to the same category.

  - It can handle different representations of the same subject and still recognise that it is the same subject.

- Implementation Details:

  - Text pre-processing: Text is extracted using PDF parsing tool (PyPDF2) and cleaned by using NLP library and regular expression.

  - Topic Extraction and Categorisation: Use topic modelling tools from NLP libraries (e.g. Gensim's LDA model) to identify and extract the main research areas and core topics in the paper. Apply machine learning classification algorithms (e.g., Scikit-learn's Support Vector Machines or Random Forest) to categorise documents into predefined disciplines and sub-disciplines.

  - Database Interaction: Use a graph database (Neo4j) for storing extracted topic and classification information and supporting efficient queries. Implement an API interface for querying existing subject categories in the database and support the ability to add multiple papers to the same category.

#### 1b. <a id="keyword-extraction">Keyword Extraction</a>

##### Description

This function extracts obvious keywords from the article, such as the subject of the experiment, the object of the experiment, and so on. In addition, it should also be possible to summarise implicit keywords.

##### Design Details

- Requirement Design:
  - Keywords or phrases should be extracted from the paper that summarise the main content or research focus of the paper.

  - It can be located exactly to the keyword section of the article.

  - It is possible to match different keywords that express the same meaning.

- Implementation Details:
  - Keyword Extraction Algorithm: uses the NLP functionality of spaCy to tag text and identify noun phrases and adjectives.

  - Keyword Normalization and Disambiguation: Normalisation of extracted keywords, e.g., unification of morphological variations and normalisation of synonyms. The NLP package (WordNet with NLTK) is used to distinguish and match different keywords that express the same meaning.

  - Database Integration: Uses a graph database to store keywords and their associated article information for subsequent querying and analysis. Implement a database query function that allows quick retrieval of keywords and associations to related articles.

#### 1c. <a id="author-identification">Author Identification</a>

##### Description

This feature extracts the author's information from the article and can store the relationship between the author and the article together in a database. In addition, it needs to be able to recognise author information already in the database and add multiple articles for the same author.

##### Design Details

- Requirement Design:

  - The name, affiliation and contact details of the authors should be able to be extracted accurately from the paper.

  - Should handle multi-author situations and be able to return multiple authors for a single article in the database.

  - Should have the ability to differentiate between authors with the same name, which may need to be combined with additional data such as the author's institutional information, contact details, etc.

  - It is possible to query the database for existing author information and add multiple articles for the same author.

- Implementation Details:
  - Author Information Extraction: Develop a parsing algorithm to extract the author's name, organisation, and contact information from a document using an NLP tool (e.g., spaCy or NLTK) in combination with regular expressions. Use machine learning methods such as Named Entity Recognition (NER) to identify and extract author information fields.

  - Handling Multi-Author Scenarios: Implement a logic that recognises multiple authors in a document and correctly assigns their respective information. Designing a Neo4j database storage interface to store multi-author information allows a single article to be associated with multiple author entities.

  - Disambiguation of Authors with Same Name: An algorithm (e.g., based on author institution information) is used to distinguish authors with the same name. Implement a unique identifier in the database, such as ORCID iD, to help distinguish between different authors with the same name.

  - Database Querying and Update: Develop an API interface to allow querying of existing author information and updating the list of related articles for matching authors as they are found. Design database operations to support adding and updating multiple articles by the same author.

#### 1d. <a id="reference-extraction">Reference Extraction</a>

##### Description

The aim of this feature is to extract automatically a list of references from an academic paper and to parse out precise details of each reference, such as author, article title, journal name and year of publication. The achieved effect is to associate articles with their references in a database, supporting multiple citation formats and being able to recognise articles already in the database for data association.

##### Design Details

- Requirement Design:

  - Should be able to extract a list of references from a paper and accurately parse out the individual components of each reference (e.g. author, article title, journal name, year of publication, etc.).

  - It should be possible to store the relationship between the article and the articles in the references in a database.

  - Should support handling different citation formats (e.g. APA, MLA, Chicago, etc.).

  - It should be possible to identify articles that are already in the database and to correlate them.

- Implementation Details:
  - Reference Location: development of a parser using NLP tools (e.g. spaCy) for identifying the reference part of an article.

  - Reference Parsing: development of a module, based on regular expressions and NLP packages, designed specifically to identify and extract the various components of a citation format, such as author, title, journal name and year of publication. Implement specific parsing rules for different citation formats (APA, MLA, Chicago, etc.).

  - Identification of Existing Articles: Implement an algorithm or query logic for identifying identical citations in a database and associating them with newly extracted citations. Consider using a document's DOI (Digital Object Identifier) or other unique identifier to help identify and match documents.
### 2. [Topic Connection](#topic-connection)
#### 2a. Linking Articles with the Same Topic:
- **Description:**
    - The system should link articles that share the same topic. 
    - Example: When a user chooses the "high performance computing (HPC)" topic, the system should present articles  discussing HPC.
- **Priorisation:** High
- **Design Details:**

    - **Requirement Design:**
        - The system is required to establish connections between articles that share a common topic. This functionality aims to facilitate users in exploring content related to specific topics of interest. Users should be able to select a topic, and the system should retrieve and present articles relevant to that chosen topic, allowing users to delve deeper into subject matters they are interested in.
    - **Implementation Details:**
        - Introduce a "Topic" entity in the database to represent different topics.
        - Each article should be associated with one or more topics using a many-to-many relationship.
        - Create an "Article_Topic" associative table to manage the connections.
    
#### 2b. Establishing Connections Between Various Topics:
- **Description:** 
    - The system should establish connections between various topics within the same domain. 
    - Example: When a user explores the topic "Computer Science," the system should showcase articles covering diverse but related subjects like machine learning and high-performance computing.
- **Priorisation:** Medium
- **Design Details:**
    - **Requirement Design:**
        - The system needs to create connections between different topics within the same domain to enhance users' exploration experience. This involves identifying relationships between topics that are conceptually related or interlinked. When users explore a broad topic, the system should present articles covering various related subjects within that broader domain, enabling users to navigate through interconnected topics easily.
    - **Implementation Details:**
        - Extend the database schema to include relationships between different topics.
        - Implement algorithms to analyze co-occurrences and relevancy between topics.

### 3. [Author Relationship](#author-relationship)
#### 3a. Associating Authors Collaborating on the Same Paper: (Co-author)
- **Description:**
    - The system should establish connections between authors who are credited for the same paper. The relationship should be presented as "Co-author."
    - Example: If authors A and B are credited for the paper titled "Advancements in Artificial Intelligence," the system should display a "Co-author" relationship between A and B.
- **Priorisation:** High
- **Design Details:**
    - **Requirement Design:**
        - The system is tasked with establishing connections between authors who have collaborated on the same paper, presenting this relationship as "Co-author." This functionality ensures that users can discover other authors who have contributed to the same research or publication, fostering collaboration and acknowledgment within the academic community.
    - **Implementation Details:**
        - Create a "Co-Authorship" entity in the database to capture relationships between authors collaborating on the same paper.
        - Implement algorithms to identify co-authorship based on shared article credits.
#### 3b. Linking Authors Working in the Same Company or Department (Colleague):
- **Description:**
    - The system should connect authors who work in the same company or department. The relationship should be presented as "Colleague."
    - Example: If authors X and Y both work at XYZ Corporation, the system should show a "Colleague" relationship between X and Y.
- **Priorisation:** Medium
- **Design Details:**
    - **Requirement Design:**
        - The system should connect authors who work in the same company or department, representing this relationship as "Colleague." This functionality enables users to explore professional connections among authors within a specific organizational context, facilitating networking and collaboration opportunities within the same workplace.
    - **Implementation Details:**
        - Introduce a "Colleague" relationship in the database schema.
        - Implement algorithms to identify authors working in the same company or department based on their affiliation data.
#### 3c. Co-Recipients of Awards Relationship (Co-Recipients of Awards):
- **Description:**
    - If two authors have jointly received a specific award, the system should showcase their relationship as "Co-Recipients of Awards."
    - Example: If authors M and N were both recipients of the "Outstanding Research Contribution Award," the system should display a "Co-Recipients of Awards" relationship between M and N.
- **Priorisation:** Low
- **Design Details:**
    - **Requirement Design:**
        - The system should showcase relationships between authors who have jointly received specific awards, presenting this relationship as "Co-Recipients of Awards." This functionality highlights the achievements and collaborations between authors who have been recognized for their contributions, enhancing the visibility of their shared accolades within the academic or professional community.
    - **Implementation Details:**
        - Introduce an "Awards" entity to capture information about awards received by authors.
        - Establish relationships between authors who have jointly received the same award.

### 4. Reference Tree
#### 4a. Citation Tree Generation
- **Description**: 
	- This component involves developing an algorithm to visually represent the citation network of a paper. It will display the immediate citations of the current paper and allow users to explore second and higer levels citations, which are the references cited by the papers in the previous-level citations.
- **Design Details:**
	- **Requirement Design**: 
		- The citation tree should be interactive, allowing users to navigate through different levels of citations. It must accurately represent the hierarchical structure of citations and be capable of dynamically updating as new references are added.
	- **Implementation Details**: 
		- The algorithm will parse the citation data and construct a hierarchical tree structure. The tree will be displayed graphically, with nodes representing individual papers and edges indicating citation relationships. Features will include collapsibility of branches for easy navigation and tooltips or additional information windows to provide details about each citation.
#### 4b. Cited-by Tree Feature
- **Description**: 
	- This functionality involves creating a reverse citation tree that identifies papers which have cited the current paper. It also includes the references of these citing papers to understand their citation context.
- **Design Details:**
	- **Requirement Design**: 
		- The 'Cited-by Tree' should offer insights into the impact of the paper on subsequent research. It should be able to dynamically update as new citing papers are published and identified.
	- **Implementation Details**: 
		- The system will use a reverse lookup algorithm to find papers that cite the current paper. A separate tree structure, similar to the citation tree, will be generated. This tree will also be interactive, allowing users to explore the citation networks of the papers that have cited the current paper.
#### 4c. User Interface
- **Description**: 
	- The user interface is crucial for providing a user-friendly way to interact with the citation and 'Cited-by' trees. It needs to be intuitive, responsive, and visually appealing.
- **Design Details:**
	- **Requirement Design**: 
		- The UI should allow users to easily navigate the complex network of citations. It should include graphical representations, clickable elements, and features like search, filter, and different views for better usability.
	- **Implementation Details**: 
		- The UI will be developed using web technologies (like HTML, CSS, JavaScript) or appropriate software frameworks. It will feature a main viewing area for the trees, a toolbar or menu for navigation controls, and possibly a sidebar or pop-up windows for detailed information about each citation. The design will ensure that the interface remains uncluttered and easy to use, even with large datasets.

### 5. User Defined Filter and Search
#### 5a. Customizable Filters
- **Description**:
  - Users can define filters based on various parameters such as author names, publication dates, keywords, and thematic categories. This flexibility ensures that users can narrow down their searches to retrieve the most relevant and targeted information.
- **Priorisation**: High
- **Design Details:**
  - **Requirement Design:**
    - Users should be able to define filters for parameters such as author names, publication dates, keywords, and thematic categories.
    - The goal is to offer flexibility in search queries, accommodating diverse research requirements.
  - **Implementation Details:**
    - Implement a user-friendly interface where users can input and adjust filter settings.
    - Develop backend logic to process and apply these filters to the dataset.
    - Ensure that the system can handle a variety of filter combinations for comprehensive search capabilities.

#### 5b. Advanced Keyword Search
- **Description:**
  - The advanced keyword search feature enables users to input specific terms or phrases, enhancing the efficiency and accuracy of information retrieval. This component aims to facilitate a more targeted search experience for users seeking particular details within academic papers and other sources.
- **Priorisation**: High
- **Design Details:**
  - **Requirement Design:**
    - Users should have the ability to perform searches using specific terms or phrases related to their research interests.
    - The system should support advanced keyword search algorithms for improved relevance.
  - **Implementation Details:**
    - Implement a search algorithm that considers synonyms, related terms, and contextual relevance.
    - Ensure the system ranks search results based on keyword relevance to provide meaningful outcomes.
    - Design a user interface that allows users to easily input and modify their keyword search queries.

#### 5c. Dynamic Query Building
- **Description:**
  - Dynamic query building empowers users to create complex queries on-the-fly. This feature supports the combination of multiple filters and search criteria, providing users with a powerful tool for obtaining highly specific and refined results.
- **Priorisation**: Low
- **Design Details:**
  - **Requirement Design:**
    - Users should be able to dynamically create complex queries by combining multiple filters and search criteria.
    - The goal is to offer flexibility in query construction for nuanced research needs.
  - **Implementation Details:**
    - Develop an intuitive user interface with drag-and-drop or toggle functionalities for adding and removing query components.
    - Implement backend logic to dynamically adjust the query based on user interactions.
    - Ensure real-time updates in response to user modifications for a seamless query-building experience.

#### 5d. Real-time Feedback (Optional)
- **Description:**
  - Real-time feedback is essential for an interactive and responsive user experience. This component ensures that users receive immediate feedback as they apply filters or modify search parameters, facilitating efficient exploration of academic papers and sources.
- **Priorisation**: Low
- **Design Details:**
  - **Requirement Design:**
    - Users should receive instant feedback on the impact of applied filters or modified search parameters.
    - Real-time feedback enhances the user's ability to iteratively refine their queries.
  - **Implementation Details:**
    - Implement mechanisms to update search results dynamically as filters are applied or modified.
    - Utilize asynchronous processing to ensure minimal latency in providing feedback.
    - Design a visually intuitive interface to convey changes and updates to users in real-time.


#### 5e. Saved Queries (Optional)
- **Description:**
  - The optional "Saved Queries" feature allows users to store frequently used or complex queries for future reference. This enhances productivity by enabling users to revisit and reuse previously defined search criteria without the need to recreate them.
- **Priorisation**: Low
- **Design Details:**
  - **Requirement Design:**
    - Users should have the option to save and manage their frequently used or complex queries.
    - This feature provides a convenient way to reuse predefined search criteria.
  - **Implementation Details:**
    - Implement a user interface for saving, organizing, and retrieving saved queries.
    - Develop backend storage to persistently store user-defined queries.
    - Ensure security measures to protect and manage saved queries according to user permissions.

#### 5f. Intuitive User Interface (Optional)
- **Description:**
  - An intuitive user interface is designed to ensure that users, regardless of their technical expertise, can navigate and utilize the filter and search functionalities seamlessly.
- **Priorisation**: Low
- **Design Details:**
  - **Requirement Design:**
    - The user interface should be user-friendly, requiring minimal training for effective use.
    - The goal is to create a visually appealing and intuitive design that enhances the overall user experience.
  - **Implementation Details:**
    - Employ user interface design principles such as simplicity, consistency, and feedback.
    - Conduct usability testing to refine the interface based on user feedback.
    - Ensure responsive design for seamless user experiences across different devices.

#### 5g. Compatibility Across User Categories (Optional)
- **Description:**
  - The optional "Compatibility Across User Categories" feature ensures that the filter and search functionalities cater to the specific needs of diverse user categories, including students, academics, government officials, developers, and companies.
- **Priorisation**: Low
- **Design Details:**
  - **Requirement Design:**
    - The system should adapt its presentation and functionality based on the unique requirements of different user categories.
    - Ensure that the interface and features are relevant and useful for each user category.
  - **Implementation Details:**
    - Implement user category-specific profiles or settings to customize the user experience.
    - Conduct user interviews and feedback sessions to understand the distinct needs of each user category.
    - Design flexible components that can be enabled or disabled based on user category preferences.


## Data Model 

### Entities:
- **Article:**

    - **Attributes:** article_id (Primary Key), title, content, publication_date, ...
    - **Relationships:** Many-to-Many with Topic and Author entities.
- **Topic:**
    - **Attributes:** topic_id (Primary Key), name.
    - **Relationships:** Many-to-Many with Article entities.
- **Author:**
    - **Attributes:** author_id (Primary Key), name, affiliation, contact_details, ...
    - **Relationships:** Many-to-Many with Article_Author entities.
- **Reference:**
    - **Attributes:** reference_id, article_id, author, article name, link, ...
    - **Relationships:** Many-to-Many with Article entity.

### Associative Tables:
- **Article_Topic:**

    - **Columns:** article_id (Foreign Key referencing Article), topic_id (Foreign Key referencing Topic).
- **Article_Author:**
    - **Columns:** article_id (Foreign Key referencing Article), author_id (Foreign Key referencing Author).

### Data Model Diagram:

```
                            +------------------+
                            |      Article     |
                            +------------------+
                            | article_id (PK)  |
                            | title            |
                            | content          |
                            | publication_date |
                            | ...              |
                            +------------------+
                                    |
                                    |
           +------------------------+------------------------+
           |                        |                        |
           |                        |                        |
   +----------------+       +----------------+     +------------------+
   |  Topic         |       |  Author        |     |    Reference     |
   +----------------+       +----------------+     +------------------+
   | topic_id (PK)  |       | author_id (PK) |     | reference_id (PK)|
   | name           |       | name           |     | reference_text   |
   +----------------+       | affiliation    |     | article_id (FK)  |
                            | contact_details|     +------------------+
                            +----------------+

   +----------------+     +----------------+
   | Article_Topic  |     | Article_Author |
   +----------------+     +----------------+
   | article_id (FK)|     | article_id (FK)|
   | topic_id (FK)  |     | author_id (FK) |
   +----------------+     +----------------+
```

## Test Plan

### Test Object
#### 1a. <a id="topic-extraction-test">Topic Extraction</a>

**Test Aim:**
Ensure that the topic extraction function accurately identifies and extracts the main research areas, core topics and sub-disciplines from multi-disciplinary academic papers, and efficiently stores this information in the database.

**Test Cases:**

1. **Text pre-processing tests:** Whether text pre-processing can extract and clean accurately.

- *Test Steps:*
  - Tests whether the text of papers in different formats (PDF) can be extracted accurately.

  - Verify that the cleaning process removes extraneous content and maintains important information.

2. **Topic extraction tests:** Test accuracy and consistency of topic modelling tools.

- *Test Steps:*
  - Verify that the topic model accurately extracts topic from the test set. The test set will have the PDF formate paper and matched pre-defined topic list.

  - Test whether different representations of the same topic are correctly recognised as the same topic.

3. **Database and API interaction tests:** Test correctness of implementation of database storage structure and API interface functionality.

- *Test Steps:*
  - Testing the database is properly storing associated topic and article data.
  - Verify that the API interface allows for efficient querying, adding and updating of database content.

#### 1b. <a id="keyword-extraction-test">Keyword Extraction</a>

**Test Aim:**
Ensure that the keyword extraction function accurately identifies explicit and implicit keywords in academic articles, normalises variants and synonyms, and stores this information in a database for search and analysis.

**Test Cases:**

1. **Keyword extraction accuracy test:** Testing using a set of papers ensures that the most relevant keywords and phrases are extracted.

- *Test Steps:*
  - Verify that the keyword section of the paper is correctly identified and that keywords can be extracted from it when the section exists.

2. **Keyword normalisation and disambiguation tests:** The effectiveness of normalisation and disambiguation.

- *Test Steps:*
  - Check that morphologically variant keywords are correctly normalised (e.g. paper and papers are all normalised to paper).

  - Ensure that different keywords expressing the same meaning are matched and recognised as synonyms.

3. **Database and API interaction tests:** The system interacts with a database to store and query keyword data.

- *Test Steps:*
  - Verify that keywords are correctly entered into the graphics database along with their associated article information.

  - Verify that the database query function efficiently and accurately retrieves the correct keywords and their related articles.

#### 1c. <a id="author-identification-test">Author Identification</a>

**Test Aim:**:
Ensure that the author recognition function can accurately extract author information from articles and can store the relationship between authors and articles in the database. In addition, the function needs to recognise author information already in the database and add multiple articles for the same author.

**Test Cases:**

1. **Keyword extraction accuracy test:** Testing using a set of papers ensures that the most relevant keywords and phrases are extracted.

- *Test Steps:*

  - Use a set of articles to test whether the names, affiliations, and contact information of authors can be extracted accurately.

  - Verify that the extraction algorithm can handle multi-author information in articles.

2. **Differentiation test for authors with the same name:** Distinguish between authors with the same name and incorporate additional information such as the author's institutional information, contact details, etc.

- *Test Steps:*

  - Check that the system can distinguish between authors with the same name by additional information (e.g. institutional information).

  - Test if authors with the same name can be correctly associated in the database by a unique identifier (e.g. ORCID).

3. **Database storage and query test:** Confirm that author information and article relationships are correctly entered into the database.

- *Test Steps:*

  - After data storing, verify that the database query function correctly retrieves author information and their related articles.

4. **Multi-article correlation test:** Evaluate whether the system can add new articles to an author's record when an author already in the database is found.

- *Test Steps:*

  - Given a set of lists of articles by the same author, query the database to see whether the articles are correctly linked to the author.

#### 1d. <a id="reference-extraction-test">Reference Extraction</a>

**Test Aim:**
Ensure that the reference extraction function automatically extracts a list of references from academic papers and accurately analyses the details of each reference (e.g. author, article title, journal name and year of publication). The target effect is to associate articles with their references in a database that supports multiple citation formats and is able to recognise articles already in the database for data association.

**Test Cases:**

1. **Reference location test:** Testing using a set of papers ensures that the most relevant keywords and phrases are extracted.

- *Test Steps:*
 
  - Test whether the developed parser accurately recognises the reference section of the article.
  
  - Test whether the text of reference list can be returned correctly.

2. **Reference parsing test:** Testing using a set of papers ensures that the most relevant keywords and phrases are extracted.

- *Test Steps:*
 
  - Test whether the developed parser accurately recognises the reference section of the article.
  
  - Test whether the text of reference list can be returned correctly.

3. **Existing article recognition test:** Implement algorithms or query logic to confirm whether the same citation can be identified in the database and associated with the newly extracted citation.

- *Test Steps:*

  - Test whether the system can find the paper in the reference list is already in the database.

  - Test whether the system can add new relationships to papers already in the graphics database.

#### 2a. Linking Articles with the Same Topic
**Test Cases:**
1. **Retrieving Articles for a Selected Topic:**
    - **Test Summary:** Verify the system's ability to retrieve and present articles associated with a selected topic.
    - **Pre-requisites:** A populated database with articles covering various topics.
    - **Test Steps:** 
        1. Select a predefined topic, e.g., "High Performance Computing," from the dropdown menu.
        2. Trigger the system to query the database for articles associated with the selected topic.
        3. Observe the presented articles.
    - **Expected Result (Happy Case):** The system successfully retrieves and displays articles specifically linked to the "High Performance Computing" topic.
    - **Expected Results (Failure Case):** The system fails to retrieve articles for the selected topic, or the presented articles are unrelated.

#### 2b. Establishing Connections Between Various Topics:
**Test Cases:**
1. **Related Subtopics:**
    - **Test Summary:** Ensure the system accurately identifies and presents related subtopics when exploring a broad topic.
    - **Pre-requisites:** A populated database with articles covering diverse subtopics within broad topics.
    - **Test Steps:** 
        1. Choose the broad topic "Computer Science" from the dropdown menu.
        2. Observe the system's response in identifying and presenting related subtopics.
        3. Verify that the presented articles cover diverse but related subjects within the chosen broad topic.
    - **Expected Result (Happy Case):** The system successfully identifies and presents related subtopics within the "Computer Science" topic, and the displayed articles are relevant.
    - **Expected Results (Failure Case):** The system fails to identify related subtopics, or the presented articles are unrelated to the chosen broad topic.

#### 3a. Associating Authors Collaborating on the Same Paper: (Co-author)
**Test Case:**
1. **Co-Authorship Relationship:**
    - **Test Summary:** Validate the system's ability to associate authors collaborating on the same paper and present the relationship as "Co-author."
    - **Pre-requisites:** A populated database with articles having multiple credited authors.
    - **Test Steps:** 
        1. Access the details of an article known to have multiple authors.
        2. Examine the system's representation of co-authors for the selected article.
        3. Verify that the identified co-authors match the actual authors credited for the paper.
    - **Expected Result (Happy Case):** The system correctly displays the co-authors for the selected article, confirming accurate identification of authors collaborating on the same paper.
    - **Expected Results (Failure Case):** The system fails to display co-authors for the selected article, or the identified co-authors are incorrect.

#### 3b. Linking Authors Working in the Same Company or Department (Colleague)
**Test Case:**
1. **Colleague Relationship:**
    - **Test Summary:** Ensure the system correctly links authors working in the same company or department and presents the relationship as "Colleague."
    - **Pre-requisites:** A populated database with authors affiliated with the same company or department.
    - **Test Steps:** 
        1. Explore the profiles of authors known to work in the same company or department.
        2. Confirm that the system displays a "Colleague" relationship between the selected authors.
        3. Verify that the identified colleagues match the actual authors working in the same organization.
    - **Expected Result (Happy Case):**
    The system accurately represents professional connections by displaying "Colleague" relationships between authors from the same company or department.
    - **Expected Results (Failure Case):**
    The system fails to display colleague relationships for the selected authors, or the identified colleagues are incorrect.

#### 3c. Co-Recipients of Awards Relationship (Co-Recipients of Awards):
**Test Case:**
1. **Co-Recipients of Awards Relationship:**
    - **Test Summary:** Verify that the system establishes relationships between authors who have jointly received the same award, presenting it as "Co-Recipients of Awards."
    - **Pre-requisites:** A populated database with authors who have received the same award.
    - **Test Steps:** 
        1. Identify authors who have received the same award.
        2. Examine the system's representation of relationships for the selected authors.
        3. Confirm that the system displays a "Co-Recipients of Awards" relationship between the authors who received the same award.
    - **Expected Result (Happy Case):** The system correctly establishes relationships between authors who have jointly received a specific award, displaying it as "Co-Recipients of Awards."
    - **Expected Results (Failure Case):** The system fails to display award relationships for the selected authors, or the identified co-recipients are incorrect.
#### 4a. Citation Tree Generation
- **Description**: 
	- This component involves developing an algorithm to visually represent the citation network of a paper. It will display the immediate citations of the current paper and allow users to explore second and higer levels citations, which are the references cited by the papers in the previous-level citations.
- **Design Details:**
	- **Requirement Design**: 
		- The citation tree should be interactive, allowing users to navigate through different levels of citations. It must accurately represent the hierarchical structure of citations and be capable of dynamically updating as new references are added.
	- **Implementation Details**: 
		- The algorithm will parse the citation data and construct a hierarchical tree structure. The tree will be displayed graphically, with nodes representing individual papers and edges indicating citation relationships. Features will include collapsibility of branches for easy navigation and tooltips or additional information windows to provide details about each citation.
#### 4b. Cited-by Tree Feature
- **Description**: 
	- This functionality involves creating a reverse citation tree that identifies papers which have cited the current paper. It also includes the references of these citing papers to understand their citation context.
- **Design Details:**
	- **Requirement Design**: 
		- The 'Cited-by Tree' should offer insights into the impact of the paper on subsequent research. It should be able to dynamically update as new citing papers are published and identified.
	- **Implementation Details**: 
		- The system will use a reverse lookup algorithm to find papers that cite the current paper. A separate tree structure, similar to the citation tree, will be generated. This tree will also be interactive, allowing users to explore the citation networks of the papers that have cited the current paper.
#### 4c. User Interface
- **Description**: 
	- The user interface is crucial for providing a user-friendly way to interact with the citation and 'Cited-by' trees. It needs to be intuitive, responsive, and visually appealing.
- **Design Details:**
	- **Requirement Design**: 
		- The UI should allow users to easily navigate the complex network of citations. It should include graphical representations, clickable elements, and features like search, filter, and different views for better usability.
	- **Implementation Details**: 
		- The UI will be developed using web technologies (like HTML, CSS, JavaScript) or appropriate software frameworks. It will feature a main viewing area for the trees, a toolbar or menu for navigation controls, and possibly a sidebar or pop-up windows for detailed information about each citation. The design will ensure that the interface remains uncluttered and easy to use, even with large datasets.

#### 5a. Customizable Filters

**Test Cases:**
1. **Filter Creation:**
   - **Test Summary:** Verify the system's capability to enable users to create filters for author names, publication dates, keywords, and thematic categories.
   - **Pre-requisites:** A populated database with diverse articles and metadata.
   - **Test Steps:** 
     1. Navigate to the filter creation section of the user interface.
     2. Create a filter for author names by inputting a valid author name.
     3. Create a filter for publication dates by specifying a date range.
     4. Create a filter for keywords by entering relevant terms.
     5. Create a filter for thematic categories by selecting a predefined category.
     6. Verify the existence of each created filter in the filter list.
   - **Expected Result (Happy Case):** All created filters are successfully generated and appear in the filter list.
   - **Expected Results (Failure Case):** One or more filters fail to be created or do not appear in the filter list.

2. **Filter Application:**
   - **Test Summary:** Assess the system's ability to accurately apply filters and narrow down search results.
   - **Pre-requisites:** A set of articles covering diverse topics and themes.
   - **Test Steps:** 
     1. Apply an author name filter to retrieve articles associated with a specific author.
     2. Apply a publication date filter to obtain articles published within a specified timeframe.
     3. Apply a keyword filter to narrow down results based on specific terms.
     4. Apply a thematic category filter to focus on articles within a predefined category.
     5. Combine multiple filters and observe the impact on the displayed results.
   - **Expected Result (Happy Case):** The system accurately filters and displays articles based on the applied criteria.
   - **Expected Results (Failure Case):** Filtered results are inaccurate, incomplete, or the system fails to apply one or more filters.

3. **Filter Flexibility:**
   - **Test Summary:** Evaluate the system's ability to handle a variety of filter combinations.
   - **Pre-requisites:** A diverse set of articles with varying metadata.
   - **Test Steps:** 
     1. Create and apply a complex filter combination involving author names, publication dates, keywords, and thematic categories.
     2. Verify that the system processes and interprets the complex filter combination without errors.
     3. Test with different permutations of filter combinations to assess overall flexibility.
   - **Expected Result (Happy Case):** The system successfully handles complex filter combinations, providing accurate and relevant results.
   - **Expected Results (Failure Case):** The system encounters errors or inaccuracies when processing complex filter combinations.

#### 5b. Advanced Keyword Search

**Test Cases:**
1. **Keyword Input:**
   - **Test Summary:** Confirm that users can input specific terms or phrases for advanced keyword searches.
   - **Pre-requisites:** A populated database with articles covering diverse topics and keywords.
   - **Test Steps:**
     1. Enter a single specific term, e.g., "Machine Learning," into the search bar.
     2. Input a phrase, e.g., "Natural Language Processing," and verify the system recognizes and processes it.
     3. Test the search with complex terms and ensure the system accurately interprets them.
   - **Expected Result (Happy Case):** The system recognizes and processes entered terms and phrases effectively.
   - **Expected Results (Failure Case):** The system fails to recognize entered terms or provides irrelevant results.

2. **Synonym Recognition:**
   - **Test Summary:** Test the system's ability to recognize synonyms and related terms during keyword searches.
   - **Pre-requisites:** A list of synonyms associated with common terms in the database.
   - **Test Steps:**
     1. Enter terms with known synonyms, e.g., "Artificial Intelligence" and "AI," and check for consistent recognition.
     2. Input terms with associated but less common synonyms to assess system robustness.
     3. Test with misspelled terms to evaluate the system's tolerance.
   - **Expected Result (Happy Case):** The system recognizes and includes synonyms in the search, providing relevant results.
   - **Expected Results (Failure Case):** Synonyms are not consistently recognized, leading to incomplete or inaccurate results.

3. **Contextual Relevance:**
   - **Test Summary:** Validate that the system considers contextual relevance in keyword searches.
   - **Pre-requisites:** Articles with terms that have multiple meanings in different contexts.
   - **Test Steps:**
     1. Input terms with multiple meanings and observe whether the system prioritizes context.
     2. Test terms in different thematic categories to assess contextual relevance.
     3. Verify that the system adapts to context changes within a single search query.
   - **Expected Result (Happy Case):** The system accurately interprets terms based on contextual relevance.
   - **Expected Results (Failure Case):** Contextual relevance is not considered, leading to irrelevant search results.

#### 5c. Dynamic Query Building

**Test Cases:**
1. **Query Modification:**
   - **Test Summary:** Verify that users can dynamically add, remove, and modify query components.
   - **Pre-requisites:** A set of predefined queries and a database with diverse articles.
   - **Test Steps:**
     1. Dynamically add a filter for author names to an existing query and ensure the system updates accordingly.
     2. Remove a thematic category filter from a query and verify the system's response.
     3. Modify date range criteria in a query and confirm real-time adjustments.
   - **Expected Result (Happy Case):** The system allows users to dynamically modify queries, updating results in real-time.
   - **Expected Results (Failure Case):** Modifications do not reflect in real-time, or the system encounters errors when adjusting queries.

2. **Query Complexity:**
   - **Test Summary:** Ensure the system supports the creation of complex queries by combining multiple filters and search criteria.
   - **Pre-requisites:** A variety of articles with diverse metadata.
   - **Test Steps:**
     1. Build a complex query involving author names, publication dates, keywords, and thematic categories.
     2. Verify that the system processes and interprets the complex query without errors.
     3. Test with different permutations of filter combinations to assess overall flexibility.
   - **Expected Result (Happy Case):** The system successfully handles complex query combinations, providing accurate and relevant results.
   - **Expected Results (Failure Case):** The system encounters errors or inaccuracies when processing complex query combinations.

3. **Real-time Query Updates:**
   - **Test Summary:** Test for real-time updates as users modify queries.
   - **Pre-requisites:** A set of predefined queries and a database with diverse articles.
   - **Test Steps:**
     1. Make changes to a query's filters and observe if the system provides instant feedback.
     2. Dynamically adjust date range criteria and confirm real-time updates in the displayed results.
     3. Test simultaneous modifications by multiple users to assess system responsiveness.
   - **Expected Result (Happy Case):** The system provides instant feedback and updates as users modify queries.
   - **Expected Results (Failure Case):** Real-time updates are delayed or do not reflect modifications accurately.

#### 5d. Real-time Feedback (Optional)

**Test Cases:**
1. **Instant Filter Impact:**
   - **Test Summary:** Confirm that applying filters or modifying search parameters results in real-time updates.
   - **Pre-requisites:** A set of predefined queries and a database with diverse articles.
   - **Test Steps:**
     1. Apply an author name filter and observe if the displayed results update instantly.
     2. Modify thematic category filters and check for real-time adjustments.
     3. Test simultaneous filter applications by multiple users to assess system responsiveness.
   - **Expected Result (Happy Case):** The system provides instant feedback, and the displayed results update promptly.
   - **Expected Results (Failure Case):** Real-time updates are delayed or do not accurately reflect the applied filters.

2. **User Interaction:**
   - **Test Summary:** Validate that users receive feedback when interacting with the system in real-time.
   - **Pre-requisites:** A responsive user interface and diverse user profiles.
   - **Test Steps:**
     1. Modify search parameters and confirm that the system provides visual or textual feedback promptly.
     2. Test interactions with dynamic query building, ensuring real-time feedback on user actions.
     3. Assess feedback consistency across different user roles and permissions.
   - **Expected Result (Happy Case):** The system provides clear and immediate feedback for user interactions.
   - **Expected Results (Failure Case):** Feedback is inconsistent, delayed, or not provided during user interactions.

3. **Asynchronous Processing:**
   - **Test Summary:** Ensure the system utilizes asynchronous processing to maintain minimal latency in providing real-time feedback.
   - **Pre-requisites:** A set of predefined queries and deliberate delay scenarios.
   - **Test Steps:**
     1. Introduce deliberate delays during query modifications and check if real-time feedback remains unaffected.
     2. Simulate high user load and assess system performance in maintaining real-time updates.
     3. Test real-time feedback across different network speeds to ensure consistent responsiveness.

   - **Expected Result (Happy Case):** Asynchronous processing maintains minimal latency, and real-time feedback is consistent.
   - **Expected Results (Failure Case):** Delays significantly impact real-time feedback, leading to a less responsive user experience.

#### 5e. Saved Queries (Optional)

**Test Cases:**
1. **Query Saving:**
   - **Test Summary:** Confirm that users can successfully save queries for future reference.
   - **Pre-requisites:** A set of diverse queries and a populated database.
   - **Test Steps:**
     1. Save multiple queries with varying filter combinations.
     2. Verify the existence of saved queries in the designated section.
     3. Test saving queries with special characters and long descriptions.
   - **Expected Result (Happy Case):** The system allows users to save queries successfully, and saved queries are accessible.
   - **Expected Results (Failure Case):** Saving queries fails, or saved queries are not displayed as expected.

2. **Query Retrieval:**
   - **Test Summary:** Test the retrieval of saved queries to ensure users can reuse them without recreating.
   - **Pre-requisites:** A set of saved queries and a populated database.
   - **Test Steps:**
     1. Retrieve saved queries and check if the system accurately reinstates the specified search criteria.
     2. Test retrieval with different user accounts and permissions.
     3. Attempt to retrieve queries with incorrect credentials to assess security measures.
   - **Expected Result (Happy Case):** The system accurately retrieves saved queries, maintaining the specified search criteria.
   - **Expected Results (Failure Case):** Retrieval fails, or the system inaccurately reinstates the search criteria.

3. **Security Measures:**
   - **Test Summary:** Validate the security of saved queries, ensuring they are protected and managed according to user permissions.
   - **Pre-requisites:** Saved queries with different access permissions and user roles.
   - **Test Steps:**
     1. Test different user permissions to ensure saved queries are accessed and managed appropriately.
     2. Attempt to modify or delete saved queries with restricted permissions.
     3. Assess the consistency of security measures across various user roles.
   - **Expected Result (Happy Case):** Saved queries are accessed and managed according to user permissions without security vulnerabilities.
   - **Expected Results (Failure Case):** Security measures fail, leading to unauthorized access or modification of saved queries.

#### 5f. Intuitive User Interface (Optional)

**Test Cases:**
1. **Usability Testing:**
   - **Test Summary:** Conduct usability testing to ensure the user interface is intuitive and requires minimal training.
   - **Pre-requisites:** A fully developed user interface.
   - **Test Steps:**
     1. Engage users with varying technical expertise to perform common tasks such as applying filters, conducting searches, and saving queries.
     2. Observe user interactions and gather feedback on the intuitiveness of the interface.
     3. Iterate and make adjustments based on user feedback to enhance usability.
   - **Expected Result (Happy Case):** Users, regardless of technical expertise, find the interface easy to navigate and perform tasks with minimal guidance.
   - **Expected Results (Failure Case):** Users struggle to navigate the interface, indicating usability issues that require improvement.

2. **Design Principles:**
   - **Test Summary:** Validate that the user interface adheres to design principles such as simplicity, consistency, and feedback.
   - **Pre-requisites:** A set of design principles defined for the user interface.
   - **Test Steps:**
     1. Evaluate the interface against established design principles, including simplicity, consistency in layout and color schemes, and provision of feedback.
     2. Identify areas where the interface may deviate from design principles.
     3. Implement adjustments to align the interface with design principles.
   - **Expected Result (Happy Case):** The user interface aligns with design principles, enhancing user experience and visual appeal.
   - **Expected Results (Failure Case):** Design principles are not consistently followed, impacting the overall aesthetic and usability.

3. **Responsive Design:**
   - **Test Summary:** Ensure the user interface is responsive across different devices for a seamless user experience.
   - **Pre-requisites:** Access to devices with varying screen sizes and resolutions.
   - **Test Steps:**
     1. Access the system from devices with different screen sizes, including desktops, tablets, and smartphones.
     2. Verify consistent usability and visual appeal across devices.
     3. Identify and address any responsiveness issues through iterative improvements.
   - **Expected Result (Happy Case):** The user interface adapts seamlessly to different devices, providing a consistent and user-friendly experience.
   - **Expected Results (Failure Case):** Responsiveness issues lead to a disjointed or compromised user experience on certain devices.

#### 5g. Compatibility Across User Categories (Optional)

**Test Cases:**
1. **User Category-Specific Profiles:**
   - **Test Summary:** Confirm that the system adapts its presentation and functionality based on user category-specific profiles.
   - **Pre-requisites:** User profiles categorized by roles such as students, academics, government officials, developers, and companies.
   - **Test Steps:**
     1. Log in with user profiles representing each category (student, academic, government official, developer, and company).
     2. Verify that the interface adjusts its presentation and available features based on the logged-in user's category.
     3. Test the consistency of user-specific adaptations across various sections of the system.
   - **Expected Result (Happy Case):** The system customizes its presentation and features according to the specific needs of each user category.
   - **Expected Results (Failure Case):** Inconsistencies or errors occur in adapting the interface based on user category, indicating a need for refinement.

2. **User Interviews:**
   - **Test Summary:** Conduct user interviews and feedback sessions to understand the distinct needs of each user category.
   - **Pre-requisites:** A diverse set of representatives from each user category willing to provide feedback.
   - **Test Steps:**
     1. Conduct one-on-one interviews with representatives from each user category, exploring their specific needs and preferences.
     2. Gather feedback on the existing user interface and note any pain points or areas for improvement.
     3. Use the feedback to inform adjustments and enhancements to cater to the distinct needs of each user category.
   - **Expected Result (Happy Case):** Insights from user interviews contribute to a user interface that effectively meets the varied needs of each user category.
   - **Expected Results (Failure Case):** User interviews reveal substantial mismatches between user expectations and the current interface, necessitating substantial revisions.

3. **Flexible Components:**
   - **Test Summary:** Ensure that components can be enabled or disabled based on user category preferences.
   - **Pre-requisites:** A modular system architecture allowing for component flexibility.
   - **Test Steps:**
     1. Test the system's ability to enable or disable specific features or components based on user category settings.
     2. Verify that changes in user category preferences dynamically impact the available components.
     3. Evaluate the consistency of component flexibility across different sections of the system.
   - **Expected Result (Happy Case):** The system allows for flexible enabling or disabling of components, aligning with user category preferences.
   - **Expected Results (Failure Case):** Component flexibility is inconsistent or does not align with user category preferences, requiring adjustments for improved customization.

## Test Environment

The testing environment for the system is designed to be comprehensive, covering various aspects such as hardware, software, and network configurations.

### Hardware Environment

- **Servers:** Utilize servers with sufficient processing power, memory, and storage capacity to handle concurrent user interactions and data processing.
- **Client Devices:** Ensure compatibility with a range of devices including laptops, tablets, and smartphones for testing responsive design.

### Software Environment

- **Operating System:** Test on multiple operating systems including Linux, Windows, and macOS to ensure cross-platform compatibility.
- **Web Browsers:** Validate compatibility with popular web browsers like Chrome, Firefox, Safari, and Edge.
- **Python Version:** Ensure compatibility with the required Python version (e.g., Python 3.7+).
- **Database:** Utilize a test database system (e.g., PostgreSQL) for data storage and retrieval testing.

### Network Environment

- **Network Speeds:** Simulate various network speeds to assess system performance under different network conditions.
- **Security Protocols:** Test the system's security features by simulating different network attack scenarios.

## Test Strategy

The test strategy involves a combination of Continuous Integration (CI) tests, unit tests, and manual testing to ensure thorough coverage and reliability.

### CI Test

Integration tests will be integrated into the CI/CD pipeline to perform automated testing on each code commit.

- **Framework:** Utilize testing frameworks compatible with FastAPI, such as Pytest.
- **Mocking:** Employ mocking techniques to simulate external dependencies and enhance test isolation.
- **API Testing:** Conduct automated tests for API endpoints, ensuring proper request handling and response generation.
- **Database Testing:** Integrate tests to validate data storage and retrieval from the database.

### Unit Test

Unit tests will focus on individual components, functions, and methods of the system.

- **Test Framework:** Use Pytest for unit testing due to its compatibility with FastAPI.
- **Isolation:** Ensure test cases are isolated, testing individual components without dependencies.
- **Code Coverage:** Monitor and improve code coverage metrics to guarantee thorough testing.
- **Edge Cases:** Include tests for edge cases to validate the robustness of the code.

## Test Process

The testing process will follow a systematic approach, encompassing the following stages:

1. **Test Planning:**
   - Define testing objectives, scope, and deliverables.
   - Identify test resources, including hardware, software, and human resources.

2. **Test Design:**
   - Develop detailed test cases for each requirement and component.
   - Prioritize test cases based on criticality and impact.

3. **Test Execution:**
   - Execute automated CI tests after each code commit.
   - Run unit tests to validate individual components.
   - Conduct manual tests for user interface interactions and user experience.

4. **Defect Reporting:**
   - Document and report any identified defects or issues.
   - Prioritize defects based on severity and impact.

5. **Regression Testing:**
   - Perform regression testing after code changes to ensure existing functionalities remain intact.

6. **Performance Testing:**
   - Conduct performance testing to assess the system's response time, scalability, and resource usage.
   - Evaluate system behavior under different loads and stress conditions.

7. **Security Testing:**
   - Implement security testing to identify and mitigate potential vulnerabilities.
   - Conduct penetration testing to simulate real-world attack scenarios.

8. **User Acceptance Testing (UAT):**
   - Collaborate with end-users to perform UAT, ensuring the system meets their expectations.
   - Gather feedback and make necessary adjustments based on user input.

9. **Documentation:**
   - Maintain comprehensive test documentation, including test plans, test cases, and test results.
   - Update documentation with any changes to the testing process or environment.
