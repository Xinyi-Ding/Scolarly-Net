# Academic Papers Analysis System

## Functional Requirement Analysis

### Extracting Information from PDFs
To effectively screen and analyze paper information, a substantial dataset of papers is required. Given that a significant portion of papers is available in PDF format on major websites, the primary focus is on extracting valuable information from these PDF documents. The extraction process involves capturing text, images, tables, and links to enhance the depth of analysis.

#### Text Extraction
The extraction of text information is crucial for comprehensive paper analysis. The process entails breaking down the content into individual words, with the ideal outcome being the identification of meaningful phrase combinations. This detailed extraction is fundamental to understanding and categorizing the textual content within each paper.

#### Image and Table Extraction
In addition to textual content, the project requires the extraction of images and tables present in the papers. This encompasses the identification and retrieval of charts, graphs, and other visual elements that contribute to the overall information presented in the documents. The extraction of tabular data enhances the ability to analyze structured information within the papers.

#### Link Extraction
As part of the data extraction process, identifying and capturing links within the PDF documents is essential. Links play a vital role in establishing connections between different papers, authors, or external references. Extracting and cataloging these links enables a more comprehensive understanding of the interconnectivity of information within the dataset.

#### Priority on PDF Format
Given that most papers are published in PDF format on major websites, a top priority is assigned to the extraction of information from PDF documents. This ensures that the system can effectively handle the predominant format in which academic papers are presented online.

#### Build Database
By satisfying these requirements, the project can use the extracted data to establish a comprehensive database. This database will serve as a foundation for subsequent data retrieval and detailed analysis of the website's content.

### Data Storage

The data storage system is responsible for storing the physical data of an article in a database when extracting data from academic papers. In order to fulfil this requirement, the following main implementation goals were considered: selecting a robust database solution capable of efficiently handling large amounts of data, supporting multiple data formats to accommodate different types of entity data from academic papers. Implement a comprehensive indexing system to include key attributes in the articles, such as author names, dates, disciplines, titles, and so on. Also ensure efficient data retrieval, using a relational database model to organise and manage data effectively.

### Query Data

The analytical query component is the primary user interface for interacting with the database. It receives queries from the interface and searches for relevant data from the database. In order to achieve this, it must fulfil several key requirements. Firstly, it should be fully capable of holding various types of analytical queries, such as subject clustering, author association and reference networks, to ensure diversity of query functionality. Second, the system should be adept at handling complex queries to meet the diverse and complex information needs of users. In addition, the system should process queries quickly to minimise waiting time and enhance user experience. Finally, the system should package the retrieved data so that it can be transferred to the interface for easy viewing and use by users.

### Accepting User Query Input

This system is designed to analyze and organize relationships among academic papers based on user queries, an essential functionality for its operation. The types of user input that can be processed are diverse, catering to various analytical needs in the academic field:

1. **Topic**: This allows users to query all papers under a specific topic, delve into relationships between different topics, and explore connections between topics and authors. It's a feature that opens avenues for researchers to understand the landscape of ongoing research and its historical development under specific themes.
2. **Author**: Users can explore papers written by a particular author, uncover relationships among different authors, and examine links between authors and topics. This functionality is crucial for tracking the contributions of individual researchers and understanding collaborative networks and intellectual lineages.
3. **Reference**: This feature lets users search for papers citing a particular reference, helping them understand the impact of seminal works and the evolution of ideas in the academic community.
4. **Time**: Users can find all papers within a specific time frame, analyzing trends, shifts in research focus, and the emergence of new topics over time.
5. // TODO: Further functionalities and query types to be determined.

// TODO: Corresponding database ER diagram and interface table needed.

In addition to leveraging its database to establish connections between academic papers, the system is also equipped to receive and analyze new papers submitted by users. This integration not only enhances the database's content but also ensures that the system remains current with the latest research developments. Advanced text analysis and data mining techniques will be employed to extract relevant information and relationships from these new submissions.

// TODO: Corresponding database ER diagram and interface table required for this feature.

### Query from Database for Academic Paper Analysis

To conduct in-depth analysis and establish meaningful connections within our dataset, which primarily consists of academic paper data, authors, and related information, the project will focus on implementing a robust querying system. This system will allow users to extract valuable insights through queries that revolve around authors and their associated papers.

#### Database Integration
- **Database Selection:** The project will integrate with databases such as MySQL, Neo4j, or MongoDB to store and manage the academic paper dataset, author information, and their relationships.

#### Query Capabilities
- **Author-Centric Queries:**
  - Retrieve a list of papers authored by a specific author.
  - Extract key details about an author, including their affiliation, publication history, and collaboration network.

- **Paper-Centric Queries:**
  - Retrieve information about a specific paper, including its title, abstract, and authors.
  - Identify other papers related to a particular research topic or field.

#### Relationship Analysis
- **Collaboration Network:**
  - Query and visualize the collaboration network of a specific author, showcasing co-authors and their shared publications.
  - Identify prolific authors based on the number of collaborations within the dataset.

- **Author-Keyword Associations:**
  - Explore associations between authors and keywords, helping to identify expertise areas.
  - Extract trends in research topics based on keyword co-occurrence among authors.

#### Query Optimization
- **Indexing:** Implement indexing strategies to optimize query performance, especially for large datasets.
- **Caching Mechanism:** Introduce a caching mechanism to store frequently queried results and enhance response times.

#### Security and Access Control
- **Authentication:** Implement a secure authentication system to control access to sensitive data.
- **Authorization:** Define user roles and permissions to restrict or grant access to specific query functionalities.

#### Documentation and Reporting
- **Query Documentation:** Provide comprehensive documentation for supported queries, including syntax and usage examples.
- **Reporting Tools:** Implement tools for generating reports based on query results, facilitating data interpretation and analysis.

#### User Interface
- **Query Interface:** Develop a user-friendly interface that allows users to input queries easily.
- **Visualization:** Integrate visualization tools to represent query results in a visually interpretable manner.

#### Scalability and Performance
- **Database Scaling:** Design the system to handle the growing volume of academic papers and authors over time.
- **Query Optimization:** Continuously optimize queries for improved performance as the dataset expands.

#### Continuous Improvement
- **Feedback Mechanism:** Establish a feedback mechanism for users to provide insights on query results, leading to iterative improvements.
- **Adaptability:** Ensure the system remains adaptable to evolving requirements and technological advancements.

#### Documentation
- **Code Documentation:** Maintain thorough documentation for the database schema, query implementations, and overall system architecture.
- **User Guide:** Develop a user guide for stakeholders to effectively use the query system and interpret the analytical results.

By fulfilling these requirements, the project aims to empower users to extract valuable insights from the academic paper dataset, fostering a deeper understanding of authorship relationships and research trends.

## Technology Stack

### Farse PDFs
To fulfill the requirements of extracting information from PDFs for effective paper screening and analysis, a systematic approach employing various tools and technologies is essential. Below is a brief idea on how to implement this requirement.

#### Parsing Text
- **Library Choice:** Utilize Python libraries such as PyPDF2 or pdfplumber for extracting text from PDFs.
  - **PyPDF2** is a Python library specifically designed for handling PDF files. It allows basic operations such as splitting, merging, and extracting text and metadata from PDFs. This library primarily focuses on extracting plain text from PDFs. It does not provide advanced features for extracting structured data like tables or images.
  - **pdfplumber** is a more advanced PDF parsing library for Python. It builds on top of PyPDF2 and provides additional features for extracting structured data, including text, tables, and images. pdfplumber excels in extracting text, and it also offers features for extracting tables and images from PDFs.
  
  Both libraries can extract text, but pdfplumber   provides better support for formatted text and handles more complex PDF structures. However, pdfplumber surpasses PyPDF2 by offering capabilities for extracting tables and images, making it more suitable for projects requiring comprehensive data extraction.
  
#### Parsing Image and Table
PyPDF2 can be utilized for extracting images from PDF files, providing a straightforward solution for obtaining visual content embedded within the documents.

tabula-py offers robust capabilities for table extraction from PDFs, allowing the conversion of extracted tables into a DataFrame or JSON format, and they can be saved as CSV, TSV, or JSON files, which enhancing flexibility and usability in various data processing workflows.

#### Parsing Link
To extract links from PDF documents, a combination of regular expressions (regex) and a PDF parsing library like PyPDF2 can be employed. This approach involves searching through the text content of the PDF to identify and capture URLs or hyperlinks. 

#### Comparision of Prototype
When comparing the prototype libraries, PyPDF2 emerges as a more adept tool for parsing PDFs in contrast to the pdf2docx library. While pdf2docx is primarily designed for converting PDFs to Word documents and lacks advanced features for structured data extraction, PyPDF2 proves versatile in extracting text, images, and links from PDFs. Its capabilities are further enhanced when used alongside tabula-py, addressing the challenge of extracting tables comprehensively. Unlike pdf2docx, PyPDF2 excels in accurately representing diverse data types within PDFs, making it the preferred choice for projects requiring a nuanced and comprehensive analysis of PDF content.

### Back-End
#### Python

We considered using Python for the back-end development of the project. It has extensive support for third-party libraries and good data manipulation and analysis capabilities. The third-party libraries of Python include a large number of data manipulation and analysis tools, such as pandas, NumPy, and spaCy. Besides that, it also supports interfaces and libraries for a wide range of databases, such as MySQLdb, py2neo, and pymongo.  In addition, Python can be used for machine learning tasks, which can be used to integrate machine learning models, such as NLP, into projects to capture information from articles in the future.

#### Database

Based on the database requirements in this procject, we mainly consider the following database options.

1. SQL Database:\
MySQL is a relational database where data is organized in tables, each consisting of rows and columns. Data is stored in a structured manner in MySQL, with each table having predefined columns and data types. Relationships between tables can be established through primary keys and foreign keys to achieve data consistency and integrity.

2. NoSQL Database:\
MongoDB is a document-oriented NoSQL database where data is organized as documents and stored in a JSON-style format. A document is a dynamic structure that can contain different fields, with no predefined primary and foreign keys. MongoDB's document structure makes querying and creating entity data in articles more flexible.

3. Graph Database:\
Neo4j is a graphical database where data is organized in the form of nodes and relationships, which can be used to represent relationships between authors and references between articles. Each node and relationship can have properties that can be used to store additional metadata. The main features of a graph database are the ability to quickly traverse and query relationships, as well as perform complex graph analysis, such as constructing author networks.

### Interface

#### FastAPI

FastAPI is a fast and high performance web framework. It utilizes Python's type hints to enhence the code clarity and maintainability. It also automatically generates documentation for the APIs, which can improve development efficiency and APIs testability. In addition, FastAPI supports asynchronous programming, which means that it can provide high performance on applications that have a high volume of data processing or require fast responses. Furthermore, it can easily integrate with a variety of powerful libraries for Python, enabling flexible development of complex web applications. The website for FastAPI is here: https://fastapi.tiangolo.com.
