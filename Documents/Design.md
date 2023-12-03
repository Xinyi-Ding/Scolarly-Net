# PSD Project Design

## Introduction

## System Overview

## High-level design of an end-to-end solution

## Requirements Analysis

### 1. Paper Details Extraction (Topic/Keyword/Author/Reference)

描述做成什么样的效果

### 2. Topic Connection

### 3. Author Relationship

### 4. Reference Tree

### 5. User defined filter and search

### 5. [User Defined Filter and Search](#user-defined-filter-and-search)
One crucial aspect of the proposed system is the implementation of a robust user-defined filter and search functionality. This feature empowers users across different domains, including students, academics, government officials, developers, and companies, to tailor their research queries based on specific criteria. The system will provide a highly customizable search interface allowing users to filter academic papers and other sources with precision.

## Architectural Design

## Design Details


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

### 5a. <a id="customizable-filters">Customizable Filters</a>

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

### 5b. <a id="advanced-keyword-search">Advanced Keyword Search</a>

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

### 5c. <a id="dynamic-query-building">Advanced Keyword Search</a>

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

### 5d. <a id="real-time-feedback">Real-time Feedback</a>

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

### 5e. <a id="saved-queries">Saved Queries (optional)</a>

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

### 5f. <a id="intuitive-user-interface">Intuitive User Interface (Optional)</a>

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

### 5g. <a id="compatibility-across-user-categories">Compatibility Across User Categories (Optional)</a>

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

## Test Plan

### Test Object

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
