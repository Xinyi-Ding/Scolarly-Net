# Academic Papers Analysis System

## Functional Requirement Analysis

### Data Storage

The data storage system is responsible for storing the physical data of an article in a database when extracting data from academic papers. In order to fulfil this requirement, the following main implementation goals were considered: selecting a robust database solution capable of efficiently handling large amounts of data, supporting multiple data formats to accommodate different types of entity data from academic papers. Implement a comprehensive indexing system to include key attributes in the articles, such as author names, dates, disciplines, titles, and so on. Also ensure efficient data retrieval, using a relational database model to organise and manage data effectively.

### Query Data

The analytical query component is the primary user interface for interacting with the database. It receives queries from the interface and searches for relevant data from the database. In order to achieve this, it must fulfil several key requirements. Firstly, it should be fully capable of holding various types of analytical queries, such as subject clustering, author association and reference networks, to ensure diversity of query functionality. Second, the system should be adept at handling complex queries to meet the diverse and complex information needs of users. In addition, the system should process queries quickly to minimise waiting time and enhance user experience. Finally, the system should package the retrieved data so that it can be transferred to the interface for easy viewing and use by users.
