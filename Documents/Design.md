# Academic Papers Analysis System

## Functional Requirement Analysis

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