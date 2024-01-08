# PSD Project Design

## Introduction

## System Overview

## High-level design of an end-to-end solution

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

### 5. [User Defined Filter and Search](#user-defined-filter-and-search)
One crucial aspect of the proposed system is the implementation of a robust user-defined filter and search functionality. This feature empowers users across different domains, including students, academics, government officials, developers, and companies, to tailor their research queries based on specific criteria. The system will provide a highly customizable search interface allowing users to filter academic papers and other sources with precision.

## Architectural Design

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

### 5. <a id="user-defined-filter-and-search">User Defined Filter and Search</a>

#### Key Components:
- 5a. [**Customizable Filters**](#customizable-filters)

- 5b. [**Advanced Keyword Search**](#advanced-keyword-search)

- 5c. [**Dynamic Query Building**](#dynamic-query-building)

- 5d. [**Real-time Feedback(optional)**](#real-time-feedback)

- 5e. [**Saved Queries(optional)**](#saved-queries)

- 5f. [**Intuitive User Interface(optional)**](#intuitive-user-interface)

- 5g. [**Compatibility Across User Categories(optional)**](#compatibility-across-user-categories)

Incorporating these user-defined filter and search capabilities adds a layer of flexibility and precision to the system, ensuring that researchers can efficiently navigate vast datasets and extract valuable insights pertinent to their specific areas of interest.

#### 5a. <a id="customizable-filters">Customizable Filters</a>

#### Description:
Users can define filters based on various parameters such as author names, publication dates, keywords, and thematic categories. This flexibility ensures that users can narrow down their searches to retrieve the most relevant and targeted information.

#### Design Details:
- **Requirement Design:**
  - Users should be able to define filters for parameters such as author names, publication dates, keywords, and thematic categories.
  - The goal is to offer flexibility in search queries, accommodating diverse research requirements.

- **Implementation Details:**
  - Implement a user-friendly interface where users can input and adjust filter settings.
  - Develop backend logic to process and apply these filters to the dataset.
  - Ensure that the system can handle a variety of filter combinations for comprehensive search capabilities.

- **Requirement Test:**
  - Refer to [Test Object - 5a. Customizable Filters](#5a-test)

#### 5b. <a id="advanced-keyword-search">Advanced Keyword Search</a>

#### Description:
The advanced keyword search feature enables users to input specific terms or phrases, enhancing the efficiency and accuracy of information retrieval. This component aims to facilitate a more targeted search experience for users seeking particular details within academic papers and other sources.

#### Design Details:
- **Requirement Design:**
  - Users should have the ability to perform searches using specific terms or phrases related to their research interests.
  - The system should support advanced keyword search algorithms for improved relevance.

- **Implementation Details:**
  - Implement a search algorithm that considers synonyms, related terms, and contextual relevance.
  - Ensure the system ranks search results based on keyword relevance to provide meaningful outcomes.
  - Design a user interface that allows users to easily input and modify their keyword search queries.

- **Requirement Test:**
  - Refer to [Test Object - 5b. Customizable Filters](#5b-test)

#### 5c. <a id="dynamic-query-building">Advanced Keyword Search</a>

#### Description:
Dynamic query building empowers users to create complex queries on-the-fly. This feature supports the combination of multiple filters and search criteria, providing users with a powerful tool for obtaining highly specific and refined results.

#### Design Details:
- **Requirement Design:**
  - Users should be able to dynamically create complex queries by combining multiple filters and search criteria.
  - The goal is to offer flexibility in query construction for nuanced research needs.

- **Implementation Details:**
  - Develop an intuitive user interface with drag-and-drop or toggle functionalities for adding and removing query components.
  - Implement backend logic to dynamically adjust the query based on user interactions.
  - Ensure real-time updates in response to user modifications for a seamless query-building experience.
- **Requirement Test:**
  - Refer to [Test Object - 5c. Dynamic Query Building](#5c-test)

#### 5d. <a id="real-time-feedback">Real-time Feedback</a>

#### Description:
Real-time feedback is essential for an interactive and responsive user experience. This component ensures that users receive immediate feedback as they apply filters or modify search parameters, facilitating efficient exploration of academic papers and sources.

#### Design Details:
- **Requirement Design:**
  - Users should receive instant feedback on the impact of applied filters or modified search parameters.
  - Real-time feedback enhances the user's ability to iteratively refine their queries.

- **Implementation Details:**
  - Implement mechanisms to update search results dynamically as filters are applied or modified.
  - Utilize asynchronous processing to ensure minimal latency in providing feedback.
  - Design a visually intuitive interface to convey changes and updates to users in real-time.

- **Requirement Test:**
  - Refer to [Test Object - 5d. Real-time Feedback](#5d-test)

#### 5e. <a id="saved-queries">Saved Queries (optional)</a>

#### Description:
The optional "Saved Queries" feature allows users to store frequently used or complex queries for future reference. This enhances productivity by enabling users to revisit and reuse previously defined search criteria without the need to recreate them.

#### Design Details:
- **Requirement Design:**
  - Users should have the option to save and manage their frequently used or complex queries.
  - This feature provides a convenient way to reuse predefined search criteria.

- **Implementation Details:**
  - Implement a user interface for saving, organizing, and retrieving saved queries.
  - Develop backend storage to persistently store user-defined queries.
  - Ensure security measures to protect and manage saved queries according to user permissions.

- **Requirement Test:**
  - Refer to [Test Object - 5e. Saved Queries (optional)](#5e-test)

#### 5f. <a id="intuitive-user-interface">Intuitive User Interface (Optional)</a>

#### Description:
An intuitive user interface is designed to ensure that users, regardless of their technical expertise, can navigate and utilize the filter and search functionalities seamlessly.

#### Design Details:
- **Requirement Design:**
  - The user interface should be user-friendly, requiring minimal training for effective use.
  - The goal is to create a visually appealing and intuitive design that enhances the overall user experience.

- **Implementation Details:**
  - Employ user interface design principles such as simplicity, consistency, and feedback.
  - Conduct usability testing to refine the interface based on user feedback.
  - Ensure responsive design for seamless user experiences across different devices.

- **Requirement Test:**
  - Refer to [Test Object - 5f. Intuitive User Interface (Optional)](#5f-test)

#### 5g. <a id="compatibility-across-user-categories">Compatibility Across User Categories (Optional)</a>

#### Description:
The optional "Compatibility Across User Categories" feature ensures that the filter and search functionalities cater to the specific needs of diverse user categories, including students, academics, government officials, developers, and companies.

#### Design Details:
- **Requirement Design:**
  - The system should adapt its presentation and functionality based on the unique requirements of different user categories.
  - Ensure that the interface and features are relevant and useful for each user category.

- **Implementation Details:**
  - Implement user category-specific profiles or settings to customize the user experience.
  - Conduct user interviews and feedback sessions to understand the distinct needs of each user category.
  - Design flexible components that can be enabled or disabled based on user category preferences.

- **Requirement Test:**
  - Refer to [Test Object - 5g. Compatibility Across User Categories (Optional)](#5g-test)
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

#### 5a. <a id="5a-test">Customizable Filters</a>

**Test Cases:**
1. **Filter Creation:** Verify that users can successfully create filters for author names, publication dates, keywords, and thematic categories.
   - *Test Steps:* Create filters for each parameter and validate their existence in the filter list.

2. **Filter Application:** Test the application of filters to ensure that the system accurately narrows down search results.
   - *Test Steps:* Apply filters individually and in combination, then check if the displayed results align with the specified criteria.

3. **Filter Flexibility:** Ensure the system can handle a variety of filter combinations.
   - *Test Steps:* Create complex filter combinations and verify that the system responds without errors.

#### 5b. <a id="5b-test">Advanced Keyword Search</a>

**Test Cases:**
1. **Keyword Input:** Confirm that users can input specific terms or phrases for advanced keyword searches.
   - *Test Steps:* Enter various terms and phrases into the search bar and validate the system's recognition.

2. **Synonym Recognition:** Test the system's ability to recognize synonyms and related terms during keyword searches.
   - *Test Steps:* Input synonymous terms and ensure the system provides relevant results.

3. **Contextual Relevance:** Validate that the system considers contextual relevance in keyword searches.
   - *Test Steps:* Input terms in different contexts and verify that the search results align with the intended context.

#### 5c. <a id="5c-test">Dynamic Query Building</a>

**Test Cases:**
1. **Query Modification:** Verify that users can dynamically add, remove, and modify query components.
   - *Test Steps:* Dynamically adjust queries and confirm the system updates accordingly.

2. **Query Complexity:** Ensure the system supports the creation of complex queries by combining multiple filters and search criteria.
   - *Test Steps:* Build intricate queries and verify that the system accurately interprets and executes them.

3. **Real-time Query Updates:** Test for real-time updates as users modify queries.
   - *Test Steps:* Make changes to queries and ensure the system provides instant feedback and updates.

#### 5d. <a id="5d-test">Real-time Feedback (Optional)</a>

**Test Cases:**
1. **Instant Filter Impact:** Confirm that applying filters or modifying search parameters results in real-time updates.
   - *Test Steps:* Apply filters and check if the displayed results update instantly.

2. **User Interaction:** Validate that users receive feedback when interacting with the system in real-time.
   - *Test Steps:* Modify search parameters and confirm that the system provides visual or textual feedback promptly.

3. **Asynchronous Processing:** Ensure the system utilizes asynchronous processing to maintain minimal latency in providing real-time feedback.
   - *Test Steps:* Introduce deliberate delays and confirm that real-time feedback is not affected.

#### 5e. <a id="5e-test">Saved Queries (Optional)</a>

**Test Cases:**
1. **Query Saving:** Confirm that users can successfully save queries for future reference.
   - *Test Steps:* Save multiple queries and verify their existence in the saved queries section.

2. **Query Retrieval:** Test the retrieval of saved queries to ensure users can reuse them without recreating.
   - *Test Steps:* Retrieve saved queries and check if the system accurately reinstates the specified search criteria.

3. **Security Measures:** Validate the security of saved queries, ensuring they are protected and managed according to user permissions.
   - *Test Steps:* Test different user permissions to ensure saved queries are accessed and managed appropriately.

#### 5f. <a id="5f-test">Intuitive User Interface (Optional)</a>

**Test Cases:**
1. **Usability Testing:** Conduct usability testing to ensure the user interface is intuitive and requires minimal training.
   - *Test Steps:* Engage users with varying technical expertise to perform common tasks and gather feedback.

2. **Design Principles:** Validate that the user interface adheres to design principles such as simplicity, consistency, and feedback.
   - *Test Steps:* Evaluate the interface against established design principles and make adjustments accordingly.

3. **Responsive Design:** Ensure the user interface is responsive across different devices for a seamless user experience.
   - *Test Steps:* Access the system from various devices with different screen sizes and confirm consistent usability.

#### 5g. <a id="5g-test">Compatibility Across User Categories (Optional)</a>

**Test Cases:**
1. **User Category-Specific Profiles:** Confirm that the system adapts its presentation and functionality based on user category-specific profiles.
   - *Test Steps:* Log in with different user profiles and verify that the interface adjusts according to user categories.

2. **User Interviews:** Conduct user interviews and feedback sessions to understand the distinct needs of each user category.
   - *Test Steps:* Gather feedback from representatives of each user category and implement necessary adjustments.

3. **Flexible Components:** Ensure that components can be enabled or disabled based on user category preferences.
   - *Test Steps:* Test the system's ability to flexibly adjust features based on user category settings.

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
