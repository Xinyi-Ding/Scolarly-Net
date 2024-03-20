## Test Analysis: Article Parsing Functionality

This detailed analysis scrutinizes the efficacy of the article parsing function, emphasizing its capability to accurately extract and compare metadata, content, author details, and references from PDF article files against a manually curated dataset. The approach adopted for this testing encompasses a tolerance for minor discrepancies in abstracts and references to ensure such variations don't detract from the overall evaluation of extraction accuracy.

### Test Environment Setup
- **Languages & Frameworks**: The test harness is built using Python and incorporates standard libraries such as `json` for data serialization and `difflib` for comparing differences between text data. Custom services and types are also employed to tailor the testing environment to the specific needs of the parsing function.
- **Data Source**: The benchmark dataset comprises manually extracted data from a diverse selection of seven articles, which includes five articles with references and two without. This data is stored in JSON format to facilitate structured comparison and analysis.
- **Target Platform**: The article parsing system under test is designed to handle articles in PDF format, extracting key pieces of information such as metadata, content, author details, and references for further processing or display.

Each test component in this analysis is devised to scrutinize a distinct aspect of the parsing function, with a singular test case applied uniformly across all seven selected articles to maintain consistency and rigor in the testing methodology.

### Test Component: Metadata Extraction
- **Based on Test Topic:** This component was introduced during the development phase as an essential aspect of ensuring the accuracy of metadata displayed on websites or databases, even though it wasn't part of the initial design specification.
- **Test Component Description:** The focus here is on the precision of extracting crucial metadata elements from academic articles in PDF format, such as article titles, DOIs, journal names, publication dates, and publishers.
- **Test Component Objective:** The goal is to affirm the parsing function's ability to extract and accurately represent metadata in comparison to a manually vetted benchmark dataset, thus ensuring the integrity and reliability of metadata displayed on digital platforms.
- **Test Cases:**
    1. **Test Case: Comprehensive Metadata Extraction**
        - **TC ID:** ME01
        - **Input:** A collection of seven sample articles in PDF format, chosen to represent a variety of publication styles and formats.
        - **Expected Output:** The parsing function is expected to extract metadata that precisely matches the manually curated dataset, ensuring the integrity of titles, DOIs, journal names, publication dates, and publishers.
        - **Actual Output:** The parsing function succeeded in accurately extracting the complete set of metadata from all seven articles, demonstrating its robustness and reliability in metadata extraction tasks.
        - **Result Analysis:** The function showcased exemplary performance in metadata extraction across the board. Instances where certain articles lacked specific metadata elements highlight the importance of designing parsing functions that can gracefully handle such anomalies without compromising the overall accuracy.

### Test Component: Content Parsing
- **Based on Test Topic:** Linked to [1a. Topic Extraction](Design.md/#1a-topic-extraction-1) and [1b. Keyword Extraction](Design.md/#1b-keyword-extraction-1), this component examines the function's adeptness in parsing article abstracts, a crucial part of content analysis.
- **Test Component Description:** This segment evaluates the function's efficiency in parsing and representing abstracts from academic articles, ensuring the extracted content aligns closely with manually extracted benchmarks.
- **Test Component Objective:** To ascertain the precision of abstract extraction processes and validate their consistency against manually curated data, ensuring that the extracted abstracts maintain the semantic integrity of the original content.
- **Test Cases:**
    1. **Test Case: Abstract Extraction**
        - **TC ID:** CP01
        - **Input:** A representative sample of academic articles in PDF format, chosen to test the function's ability to handle various abstract structures and content complexities.
        - **Expected Output:** The function is expected to extract abstracts with a high degree of accuracy, ensuring that the extracted content is semantically consistent with the manually curated abstracts in the benchmark dataset.
        - **Actual Output:** The abstracts were extracted with remarkable precision, reflecting the function's capability to handle textual nuances and variances adeptly, thereby maintaining the content's integrity and meaning.
        - **Result Analysis:** The content parsing component demonstrated its proficiency in accurately extracting abstracts, reinforcing the function's reliability and effectiveness in content analysis tasks. Despite facing initial challenges in the keyword extraction phase, subsequent enhancements significantly improved the function's performance, highlighting the iterative nature of developing robust parsing functions.

### Test Component: Authors Information Parsing
- **Based on Test Topic:** [1c. Author Identification](Design.md/#1c-author-identification-1), this component is crucial for attributing the correct authorship and facilitating scholarly communications.
- **Test Component Description:** Focuses on the precision of extracting detailed author information, including names, affiliations, and email addresses, from the academic articles, which is vital for attributing authorship and facilitating academic communication.
- **Test Component Objective:** The aim is to verify the function's accuracy in identifying and extracting comprehensive author details, ensuring that the extracted information is consistent with the manually curated dataset and suitable for accurate attribution and correspondence.
- **Test Cases:**
    1. **Test Case: Comprehensive Author Information Extraction**
        - **TC ID:** AI01
        - **Input:** A selection of academic articles in PDF format, encompassing a range of disciplines and authorship configurations to test the function's versatility.
        - **Expected Output:** The parsing function is expected to accurately extract author names, affiliations, and email addresses, ensuring that the extracted details align with the manually curated dataset and are accurately represented.
        - **Actual Output:** The function reliably extracted comprehensive author details from the articles, demonstrating high accuracy and reliability in author information parsing tasks.
        - **Result Analysis:** The author information parsing component proved highly effective, consistently extracting detailed and accurate author information. Variability in performance due to external library inconsistencies, especially in name extraction, underscores the importance of continuous optimization and refinement to enhance the function's adaptability and reliability across various article formats and presentations.

### Test Component: References Parsing
- **Based on Test Topic:** [1d. Reference Extraction](Design.md/#1d-reference-extraction-1), this component evaluates the function's capability to accurately extract and match reference lists, an essential aspect of academic integrity and scholarship.
- **Test Component Description:** This segment assesses the function's ability to accurately identify, extract, and match reference lists from academic articles, a critical component for supporting academic integrity and facilitating scholarly research.
- **Test Component Objective:** To evaluate the precision of the reference list extraction process and its ability to accurately match extracted references against a manually curated dataset, thereby ensuring the reliability and integrity of reference management.
- **Test Cases:**
    1. **Test Case: Comprehensive Reference List Extraction**
        - **TC ID:** RP01
        - **Input:** A curated set of academic articles in PDF format, including articles with comprehensive reference lists to test the function's accuracy in reference extraction and matching tasks.
        - **Expected Output:** The function is expected to accurately extract and match reference lists, ensuring that the extracted references are consistent with the manually curated dataset and accurately represented.
        - **Actual Output:** The function demonstrated high precision in extracting and matching reference lists, effectively navigating through minor discrepancies and variations in reference formats.
        - **Result Analysis:** The references parsing component exhibited exemplary performance in extracting and matching reference lists,

## Test Analysis: Frontend Interactivity

This section provides an in-depth analysis of the frontend interactivity testing, encompassing the functionality of the user interface and the seamless integration of the article parsing system. The testing approach emphasizes the user experience, ensuring that the interface is intuitive, responsive, and capable of effectively communicating the parsing results to the user.

### Test Environment

- **Languages & Frameworks**: Vue.js, Vitest with relevant dependencies.
- **Data Source**: From backend API calls to the mongoDB database.
- **Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge, etc.)

### Unit Test Cases

1. **Paper Dashboard Functionality**
    - **Test Description:** Verify that the paper dashboard page functions as expected, displaying the file upload section and the cards for navigation works as expected.
    - **Test Objective:** Ensure that the user can upload a file and navigate to the relevant pages using that paper.
    - **Test Cases:**
        1. **Mounts Successfully**
            - **TC ID:** 1.1
            - **Input:** None
            - **Expected Output:** The paper dashboard page should be mounted successfully, displaying the file upload section and the navigation cards.
            - **Actual Output:** The paper dashboard page should be mounted successfully, displaying the file upload section and the navigation cards.
            - **Result Analysis:** The test case passes, indicating that the paper dashboard page can be successfully mounted.
        2. **Populates 'paper' Data After File Upload**
            - **TC ID:** 1.2
            - **Input:** A valid file object
            - **Expected Output:** The 'paper' data is populated with the object after a file object is uploaded.
            - **Actual Output:** The 'paper' data should be populated with the object after a file object is uploaded.
            - **Result Analysis:** The test case passes, indicating that the 'paper' data is successfully populated after a file object is uploaded.
        3. **Renders Dashboard Cards with Correct 'ready' States**
        - **TC ID:** 1.3
        - **Input:** None
        - **Expected Output:** The dashboard cards should be rendered with ready state set to -1.
        - **Actual Output:** The dashboard cards are rendered with ready state set to -1.
        - **Result Analysis:** The test case passes, indicating that the dashboard cards are rendered with the correct 'ready' states.
    - **Analysis:** The paper dashboard page functions as expected, displaying the file upload section and the navigation cards. The 'paper' data is populated with the object after a file object is uploaded, and the dashboard cards are rendered with the correct 'ready' states.
2. **Error Page Functionality**
    - **Test Description:** Verify that the error page is displayed when an error occurs when axios request response with error.
    - **Test Objective:** Ensure that the user is redirected to the error page when an error occurs.
    - **Test Cases:**
        1. **Renders Successfully**
            - **TC ID:** 2.1
            - **Input:** None
            - **Expected Output:** The error page should be mounted successfully, displaying the error message.
            - **Actual Output:** The error page should be mounted successfully, displaying the error message.
            - **Result Analysis:** The test case passes, indicating that the error page can be successfully mounted.
        2. **Renders Error Message From Route Query**
            - **TC ID:** 2.2
            - **Input:** Error message 'Invalid Request' in the route query.
            - **Expected Output:** The error message 'Invalid Request' should be rendered on the error page.
            - **Actual Output:** The error message 'Invalid Request' is rendered on the error page.
            - **Result Analysis:** The test case passes, indicating that the error message is rendered from the route query.
        3. **Render Back Button**
            - **TC ID:** 2.3
            - **Input:** None
            - **Expected Output:** The error page should render a back button to navigate back to the paper dashboard.
            - **Actual Output:** The error page renders a back button to navigate back to the paper dashboard.
            - **Result Analysis:** The test case passes, indicating that the error page renders a back button to navigate back to the paper dashboard.
        - **Analysis:** The error page is displayed when an error occurs, and the user is redirected to the error page. The error message is rendered from the route query, and the error page renders a back button to navigate back to the paper dashboard.
3. **Dashboard Card Component Functionality**
    - **Test Description:** Verify that the dashboard card component functions as expected, displaying the sections that are clickable and navigates to the relevant pages.
    - **Test Objective:** Ensure that the user can click on the sections of the dashboard card and navigate to the relevant pages.
    - **Test Cases:**
        1. **Mounts Successfully**
            - **TC ID:** 3.1
            - **Input:** None
            - **Expected Output:** The dashboard card component should be mounted successfully, displaying the clickable sections.
            - **Actual Output:** The dashboard card component mounts successfully, displaying the clickable sections.
            - **Result Analysis:** The test case passes, indicating that the dashboard card component can be successfully mounted.
        2. *Props Work Correctly*
            - **TC ID:** 3.2
            - **Input:** Card props containing multiple key-value pairs such as title, content, link, etc.
            - **Expected Output:** The dashboard card should display the title, content, and link as per the props provided.
            - **Actual Output:** The dashboard card displays the title, content, and link as per the props provided.
            - **Result Analysis:** The test case passes, indicating that the dashboard card component works correctly with the provided props.
        3. **getReadyIcon and getReadyStripe Work Correctly**
            - **TC ID:** 3.3
            - **Input:** Card props with ready state set to 1.
            - **Expected Output:** The dashboard card should display the ready icon and the stripe should be in 'success' color.
            - **Actual Output:** The dashboard card displays the ready icon and the stripe is in 'success' color.
            - **Result Analysis:** The test case passes, indicating that the getReadyIcon and getReadyStripe functions work correctly.
        4. **handleClick Navigates Correctly When No Paper Uploaded**
            - **TC ID:** 3.4
            - **Input:** Card props with a link to a topic page without any paper uploaded.
            - **Expected Output:** Upon clicking the card, the user should be navigated to the specified topic page without any paper ID appended to the URL.
            - **Actual Output:** Upon clicking the card, the user is navigated to the specified topic page without any paper ID appended to the URL.
            - **Result Analysis:** The test case passes, indicating that the navigation occurs correctly to the specified topic page when no paper is uploaded.
        5. **handleClick navigates correctly when paper uploaded**
            - **TC ID:** 3.5
            - **Input:** Card props with a link to a topic page and a paper ID provided.
            - **Expected Output:** Upon clicking the card, the user should be navigated to the specified topic page with the paper ID appended to the URL.
            - **Actual Output:** Upon clicking the card, the user is navigated to the specified topic page with the paper ID appended to the URL.
            - **Result Analysis:** The test case passes, indicating that the navigation occurs correctly to the specified topic page with the paper ID appended to the URL when a paper is uploaded.
    - **Analysis:** The dashboard card component functions as expected, displaying the sections that are clickable and navigates to the relevant pages. The dashboard card works correctly with the provided props, and the getReadyIcon and getReadyStripe functions work correctly. The navigation occurs correctly to the specified topic page when no paper is uploaded, and with the paper ID appended to the URL when a paper is uploaded.
4. **PaperList Component Functionality**
    - **Test Description:** Verify that the paper list component functions as expected, displaying the list of papers that related to a specific paper.
    - **Test Objective:** Ensure that the user can view the list of papers related to a specific paper.
    - **Test Cases:**
        1. **renders correctly**
            - **TC ID:** 4.1
            - **Input:** Mounting the PaperList component with a list of papers and an original paper.
            - **Expected Output:** The PaperList component should render without any errors.
            - **Actual Output:** The PaperList component renders without any errors.
            - **Result Analysis:** The test case passes, indicating that the PaperList component renders correctly.
        2. **renders the original paper**
            - **TC ID:** 4.2
            - **Input:** Mounting the PaperList component with a list of papers and an original paper.
            - **Expected Output:** The original paper should be rendered in the list.
            - **Actual Output:** The original paper is rendered in the list.
            - **Result Analysis:** The test case passes, indicating that the original paper is correctly rendered in the list of papers.
        3. **renders the list of papers**
            - **TC ID:** 4.3
            - **Input:** Mounting the PaperList component with a list of papers and an original paper.
            - **Expected Output:** The PaperList component should render the correct number of papers from the provided list.
            - **Actual Output:** The PaperList component renders the correct number of papers from the provided list.
            - **Result Analysis:** The test case passes, indicating that the PaperList component correctly renders the list of papers.
5. **SearchResult Component Functionality**
    - **Test Description:** Verify that the search result component functions as expected, displaying the search results list for a specific paper title query.
    - **Test Objective:** Ensure that the user can view the search results list for a specific paper title query, and select a paper from the list.
    - **Test Cases:**
        1. **renders correctly**
            - **TC ID:** 5.1
            - **Input:** Mounting the SearchResult component with search results.
            - **Expected Output:** The SearchResult component should render without any errors.
            - **Actual Output:** The SearchResult component renders without any errors.
            - **Result Analysis:** The test case passes, indicating that the SearchResult component renders correctly.
        2. **does not render search results when there are none**
            - **TC ID:** 5.2
            - **Input:** Mounting the SearchResult component with an empty list of search results.
            - **Expected Output:** The SearchResult component should not render any search results.
            - **Actual Output:** The SearchResult component does not render any search results.
            - **Result Analysis:** The test case passes, indicating that the SearchResult component correctly does not render search results when there are none.
        3. **renders search results when there are some**
            - **TC ID:** 5.3
            - **Input:** Mounting the SearchResult component with a list of search results.
            - **Expected Output:** The SearchResult component should render the correct number of search results.
            - **Actual Output:** The SearchResult component renders the correct number of search results.
            - **Result Analysis:** The test case passes, indicating that the SearchResult component correctly renders search results when there are some.
        4. **emits "update:modelValue" when the modal is closed**
            - **TC ID:** 5.4
            - **Input:** Closing the modal in the SearchResult component.
            - **Expected Output:** The SearchResult component should emit an "update:modelValue" event with false when the modal is closed.
            - **Actual Output:** The SearchResult component emits an "update:modelValue" event with false when the modal is closed.
            - **Result Analysis:** The test case passes, indicating that the SearchResult component emits the expected event when the modal is closed.
    - **Analysis:** The search result component functions as expected, displaying the search results list for a specific paper title query. The user can view the search results list for a specific paper title query, and select a paper from the list. The SearchResult component renders correctly, does not render search results when there are none, renders search results when there are some, and emits the expected event when the modal is closed.
6. **UserChip Component Functionality**
    - **Test Description:** Verify that the user chip component functions as expected, displaying the user's name, email and affiliation if available.
    - **Test Objective:** Ensure that the user's name, email and affiliation are displayed correctly in the user chip component.
    - **Test Cases:**
        1. **renders author name**
            - **TC ID:** 6.1
            - **Input:** Mounting the UserChip component with an author object containing a name.
            - **Expected Output:** The UserChip component should render the author's name.
            - **Actual Output:** The UserChip component renders the author's name.
            - **Result Analysis:** The test case passes, indicating that the UserChip component correctly renders the author's name.
        2. **does not render email and affiliation if not provided**
            - **TC ID:** 6.2
            - **Input:** Mounting the UserChip component with an incomplete author object.
            - **Expected Output:** The UserChip component should not render email and affiliation if they are not provided in the author object.
            - **Actual Output:** The UserChip component does not render email and affiliation when they are not provided in the author object.
            - **Result Analysis:** The test case passes, indicating that the UserChip component correctly does not render email and affiliation if not provided.
        3. **shows popover when hover**
            - **TC ID:** 6.3
            - **Input:** Hovering over the UserChip component.
            - **Expected Output:** The UserChip component should show a popover when hovered over.
            - **Actual Output:** The UserChip component shows a popover when hovered over.
            - **Result Analysis:** The test case passes, indicating that the UserChip component correctly shows a popover when hovered over.

### Manual Test Cases

1. **General Functionality**
    - **Test Description:** Verify that the general functionality of the system works as expected, including the navigation, file upload, and parsing of articles.
    - **Test Objective:** Ensure that the user can navigate through the system, upload a file, and view the parsing results.
    - **Test Cases:**
        1. **Search With An Invalid Title**
            - **TC ID:** 7.1
            - **Action Performed**: Enter an invalid paper title keyword 'xyz' in the search bar and click on the search button.
            - **Expected Result:** The 'Search Result' pop-up window should show up with title 'NO RESULTS FOR XYZ', and there should be no search results displayed in the list below.
            - **Actual Result:** The 'Search Result' pop-up window shows up with title 'NO RESULTS FOR XYZ' with empty search results list.
        2. **Generate Graph by Searching for a Paper Title**
            - **TC ID:** 7.2
            - **Action Performed**: Enter a paper title keyword 'mpi' in the search bar and click on the search button, click on one of the search results, and the graph should be generated after waiting for backend to respond.
            - **Expected Result:** There be a graph generated with the articles related to the selected paper.
            - **Actual Result:** A graph is generated with the articles related to the selected paper.
            - **Result Analysis:** The test case passes, indicating that a graph is generated with the articles related to the selected paper.
        3. **Graph Behaviour**
            - **TC ID:** 7.3
            - **Action Performed**: Generate a graph like test case 7.2, drag the canvas to move the graph, then drag one of the nodes to move it. Use scroll wheel to zoom in and out.
            - **Expected Result:** The graph should be draggable, the nodes should be draggable, and the graph should be zoom-able.
            - **Actual Result:** The graph is draggable, the nodes are draggable, and the graph is zoom-able.
            - **Result Analysis:** The test case passes, indicating that the graph fully behaves as expected.
        4. **Highlighting the Selected Paper Both In the Graph and the Paper List**
            - **TC ID:** 7.4
            - **Action Performed**: Generate a graph like test case 7.2, click on a paper node in the graph, then click on another paper node in the graph.
            - **Expected Result:** The selected paper should be highlighted in the graph and the paper list for these two clicks.
            - **Actual Result:** The selected paper is highlighted in the graph and the paper list for these two clicks.
            - **Result Analysis:** The test case passes, indicating that the highlight functionality works as expected.
2. **Linking Articles with the Same Topic**
    - **Based on Test Topic:** [2. Topic Connection](Design.md#2-topic-connection-1)
    - **Test Description:** Verify that the system can link articles with the same topic and display them in the paper list, and finally generate a network graph with their connections.
    - **Test Objective:** Ensure that the system can link articles with the same topic and generate graph of them.
    - **Test Cases:**
        1. **Access Page By Sidebar Navigation Link**
            - **TC ID:** 7.5
            - **Action Performed**: Click on the 'Same Topic' link in the 'topic' section in the sidebar navigation.
            - **Expected Result:** The user should be navigated to the 'Same Topic' page, and there should be no graph generated.
            - **Actual Result:** The user is navigated to the 'Same Topic' page, with no graph generated.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Same Topic' page as expected.
        2. **Access Page By Dashboard Card When New File Uploaded and Parsed**
            - **TC ID:** 7.6
            - **Action Performed**: Upload a new file in Dashboard page and wait for the parsing to complete. Click on the 'Same Topic' card in the dashboard.
            - **Expected Result:** The user should be navigated to the 'Same Topic' page, and there should be a graph generated with the articles related to the uploaded paper.
            - **Actual Result:** The user is navigated to the 'Same Topic' page, with a graph generated with the articles related to the uploaded paper.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Same Topic' page as expected, and a graph is generated with the articles related to the uploaded paper.
        3. **Generate Graph with No Topics Found**
            - **TC ID:** 7.7
            - **Action Performed**: Search for title keyword 'gpu' and select paper 'A Survey of CPU-GPU Heterogeneous Computing Techniques' from the search results, then wait for the graph to be generated.
            - **Expected Result:** The graph should be generated with the only one paper node of the selected paper and no other nodes.
            - **Actual Result:** The graph is generated with the only one paper node of the selected paper and no other nodes.
            - **Result Analysis:** The test case passes, indicating that the graph is capable of being generated with no topics found.
3. **Associating Authors Collaborating on the Same Paper (Co-author)**
    - **Based on Test Topic:** [3. Author Relationship](Design.md#3-author-relationship-1)
    - **Test Description:** Verify that the system can associate authors collaborating on the same paper and display them in the network graph with papers related to them.
    - **Test Objective:** Ensure that the co-author page functions as expected
    - **Test Cases:**
        1. **Access Page By Sidebar Navigation Link**
            - **TC ID:** 7.8
            - **Action Performed**: Click on the 'Co-author' link in the 'author' section in the sidebar navigation.
            - **Expected Result:** The user should be navigated to the 'Co-author' page, and there should be no graph generated.
            - **Actual Result:** The user is navigated to the 'Co-author' page, with no graph generated.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Co-author' page as expected.
        2. **Access Page By Dashboard Card When New File Uploaded and Parsed**
            - **TC ID:** 7.9
            - **Action Performed**: Upload a new file in Dashboard page and wait for the parsing to complete. Click on the 'Co-author' card in the dashboard.
            - **Expected Result:** The user should be navigated to the 'Co-author' page, and there should be a graph generated with the articles related to the uploaded paper.
            - **Actual Result:** The user is navigated to the 'Co-author' page, with a graph generated with the articles related to the uploaded paper.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Co-author' page as expected, and a graph is generated with the articles related to the uploaded paper.
        3. **Generate Graph with No Authors Found**
            - **TC ID:** 7.10
            - **Action Performed**: Search for title keyword 'association' and select paper 'Association for Professionals in Infection ControlBreak the Chain of Infection' from the search results, then wait for the graph to be generated.
            - **Expected Result:** The graph should be generated with the only one paper node of the selected paper and no other nodes.
            - **Actual Result:** The graph is generated with the only one paper node of the selected paper and no other nodes.
            - **Result Analysis:** The test case passes, indicating that the graph is capable of being generated with no authors found.
4. **Citation Tree Generation**
    - **Based on Test Topic:** [4. Reference Tree](Design.md#4-reference-tree-1)
    - **Test Description:** Verify that the system can generate and display a basic citation tree for a given paper.
    - **Test Objective:** Ensure that the citation tree generation feature functions as expected.
    - **Test Cases:**
        1. **Access Page By Sidebar Navigation Link**
            - **TC ID:** 7.11
            - **Action Performed**: Click on the 'Citation Tree' link in the 'citation' section in the sidebar navigation.
            - **Expected Result:** The user should be navigated to the 'Citation Tree' page, and there should be no graph generated.
            - **Actual Result:** The user is navigated to the 'Citation Tree' page, with no graph generated.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Citation Tree' page as expected.
        2. **Access Page By Dashboard Card When New File Uploaded and Parsed**
            - **TC ID:** 7.12
            - **Action Performed**: Upload a new file in Dashboard page and wait for the parsing to complete. Click on the 'Citation Tree' card in the dashboard.
            - **Expected Result:** The user should be navigated to the 'Citation Tree' page, and there should be a graph generated with the articles related to the uploaded paper.
            - **Actual Result:** The user is navigated to the 'Citation Tree' page, with a graph generated with the articles related to the uploaded paper.
            - **Result Analysis:** The test case passes, indicating that the user is navigated to the 'Citation Tree' page as expected, and a graph is generated with the articles related to the uploaded paper.
        3. **Generate Graph with No Citations Found**
            - **TC ID:** 7.13
            - **Action Performed**: Search for title keyword 'association' and select paper 'Association for Professionals in Infection ControlBreak the Chain of Infection' from the search results, then wait for the graph to be generated.
            - **Expected Result:** The graph should be generated with the only one paper node of the selected paper and no other nodes.
            - **Actual Result:** The graph is generated with the only one paper node of the selected paper and no other nodes.
5. **Frontend-Backend Connection Test**
   - **Test Description:** Verify that the frontend and backend are connected and communicating as expected.
   - **Test Objective:** Ensure that the frontend can send requests to the backend and receive responses.
   - **Test Cases:**
     1. **Frontend Reaction When Backend Service Is Down**
        - **TC ID:** 7.14
        - **Action Performed**: Stop the backend service and perform any action that requires a backend service, such as uploading a file or generating a graph.
        - **Expected Result:** The frontend should redirect to the error page with the error message.
        - **Actual Result:** The frontend redirects to the error page with the error message.
        - **Result Analysis:** The test case passes, indicating that the frontend reacts as expected when the backend service is down.
     - **Frontend Reaction When Backend Service Internal Error Happens**
        - **TC ID:** 7.15
        - **Action Performed**: Trigger an internal error in the backend service by sending a malformed request.
        - **Expected Result:** The frontend should redirect to the error page with the error message.
        - **Actual Result:** The frontend redirects to the error page with the error message.
        - **Result Analysis:** The test case passes, indicating that the frontend reacts as expected when the backend service internal error happens.

### Result Summary

The frontend interactivity testing has been successfully completed, with all the test cases passing as expected. The general functionality of the system, including the navigation, file upload, and other components are found to be functioning as expected. The manual test cases have also been executed, with all the test cases passing as expected. The graph generation, highlighting, and navigation functionalities have been verified, and the system has been found to be capable of some special circumstances like generating graphs with no topics, authors, or citations found. Overall, the frontend interactivity testing has been successful, and the system is ready for further integration and end-to-end testing.

### Analysis Summary

All tests passed perfectly as expected. However, there are still some improvements can be made in the future testing plan. First, for all components, the unit test can cover part of the test, but there is still a lack of some more detailed tests. For example,  whether the frontend will mistake when the data format returned by the backend changes. 

Second, the graph models are not welly tested when the data is large. The graph model is tested with a small amount of data, but when the data is large, the graph model may not be able to handle it or performs badly. So it could be a potential problem that needs to be tested in the future.

Additionally, while manual testing has been conducted to ensure that the various components of the system work together as intended, there remains a need for more extensive end-to-end testing. It is essential to verify that the system functions seamlessly as a whole, with all components interacting effectively to deliver the intended user experience. It might involve testing the system with a variety of input scenarios, including different file types, large datasets, and complex graph structures, to ensure that the system can handle diverse use cases and deliver consistent performance.

In summary, the current testing phases have shown good results, but there is a need for a more comprehensive testing strategy, which should include detailed unit tests, extensive end-to-end testing, and a deeper analysis of the system's ability to handle unexpected situations and high-load conditions. By addressing these areas, we can enhance the reliability, performance of the system.

## Test Analysis: Backend Functionality








## Test Analysis: Usability Testing

This section provides a comprehensive analysis of the usability testing conducted on our paper linking system, focusing on the user interface, user experience, and overall system usability. The testing approach consists of a series of user focused tests, including user interviews, task-based testing, and feedback forms, to evaluate the system's ease of use, efficiency, and user satisfaction.

### Test Environment

- **Test Participants**: The usability testing involved users from two different backgrounds, which are academic researchers and students.
- **Test Location**: The testing was conducted in a controlled environment, with two ways provided, which are in-person and remote testing.
- **Test Tools**: The testing was conducted using user feedback forms, task-based testing scenarios, and user interviews to gather feedback and insights from the participants.
- **Test Devices**: The system was tested on EIDF VM, for participants who do not have access to our VM, were given control of one of our group members' computer to interact with the system.

### Test Feedback Collected
1. **Task 1: Uploading a Paper**
   - **Description**: Upload a paper to the application through Dashboard page, check the paper information and the link cards that are available, and generate a graph from the uploaded paper though these available links cards.
   - **Goals:** 
     1. Successfully upload a paper.
     2. See the extracted information from the paper.
     3. Generate the graph from the uploaded paper.
   - **Test Cases:**
     1. **UTC ID: 1.1**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The UI is pretty cool, the process of uploading a paper is clear and straightforward, and the information extracted from the paper is accurate. But the information extraction process is a bit slow.
        - **Suggestions**: Improve the graph generation speed.
        - **Analysis**: The user experienced is satisfied in this case. The feedback of long waiting time for graph generation might cause by: The database is not deployed in the VM but in the Mongodb official cloud database, so the network speed between the VM and the database are slow.
        - **Improvement**: Deploy the database in the VM so that the network speed between the VM and the database can be improved.
     2. **UTC ID: 1.2**
        - **Goals Achieved**: 0 passes, 3 fails
        - **Feedback**: The process of uploading a paper is clear and straightforward, but the information extracted from the paper is not accurate because the page jumped to the error page and failed to extract the information from the paper.
        - **Suggestions**: Improve the information extraction process.
        - **Analysis**: The user experienced is not satisfied in this case. The error might cause by: Participant chose to upload a pdf file downloaded from a lecture slide, which is not a paper, so the system failed to extract the necessary information like title and abstracts.
        - **Future Improvement**: Add a validation process to check if the uploaded file is a paper, or return a more user-friendly error message to the user.
     3. **UTC ID: 1.3**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of uploading a paper is clear and straightforward with brilliant UI, and the information extracted from the paper is accurate.
        - **Suggestions**: The system is good, no suggestions.
        - **Analysis**: The user experienced is satisfied in this case.
        - **Future Improvement**: No improvement needed.
     4. **UTC ID: 1.4**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of uploading a paper is clear and straightforward, and the information extracted from the paper is accurate. There are some small difficulties in identifying what the link cards are for.
        - **Suggestions**: Info icons could be added beside the link cards to show what the link cards are for when hover on them. And there could be a reset button to reset the uploaded paper, not just think that all users know that they can upload another paper to reset the uploaded paper.
        - **Analysis**: The user experienced is partly satisfied in this case.
        - **Future Improvement**: Add info icons and a reset button as suggested.
   - **Overall Analysis**: The task of uploading a paper and generating a graph from the uploaded paper is clear and straightforward, and the information extracted from the paper is accurate. However, the information extraction process is a bit slow, and there are some small difficulties in system guidance. The system is good, but there are some improvements that can be made to enhance the user experience.
2. **Task 2: Search for A Paper**
   - **Description**: Search for a paper by title keyword in one of these sections: same topic, co-author and cited tree, then select a paper from the search results
   - **Goals:** 
     1. See the pop-up window that displays the search result list.
     2. All the papers are relevant to the search keyword.
     3. Select a paper from the list.
   - **Test Cases:**
     - **UTC ID: 2.1**
       - **Goals Achieved**: 3 passes, 0 fails
       - **Feedback**: The search process is clear and straightforward, and the search results are relevant to the search keyword. The speed of the search process is still a bit slow.
       - **Suggestions**: Improve the search speed.
       - **Analysis**: The user experienced is satisfied in this case. The feedback of long waiting time for search still might cause by the database.
       - **Improvement**: Deploy the database in the VM.
     - **UTC ID: 2.2**
       - **Goals Achieved**: 3 passes, 0 fails
       - **Feedback**: The search process is clear and straightforward, and the search results are relevant to the search keyword, but it is a bit confusing that why searching for paper title in co-author page instead of searching for author name. The network speed is a bit slow.
       - **Suggestions**: Add more search options.
       - **Analysis**: The user experienced is mostly satisfied in this case. Only search for paper title in every page is how the system is designed, but it is a bit confusing for the user without a clear explanation. 
       - **Future Improvement**: Add a clear explanation to the user, and add more search options is also a good idea because we already can do have search APIs for other options like author name or topic name, but still need to be integrated into the system.
     - **UTC ID: 2.3**
       - **Goals Achieved**: 3 passes, 0 fails
       - **Feedback**: The search process is clear and straightforward, and the search results are relevant to the search keyword. But the authors in the search results list are not fully displayed, which is a bit inconvenient.
       - **Suggestions**: The system is good, but provide a way to view the full author chip list of the paper in the search results list.
       - **Analysis**: The user experienced is mostly satisfied in this case. The display of the author chip list is limited by the space of the pop-up window, so it hides the parts that overflow.
       - **Future Improvement**: Hover on the author chip list to view the full list as suggested.
     - **UTC ID: 2.4**
       - **Goals Achieved**: 3 passes, 0 fails
       - **Feedback**: The search process is clear and straightforward, and the search results are relevant to the search keyword. But there is no search bar in the Dashboard page, which is a bit inconvenient.
       - **Suggestions**: Since every page has a search bar and can search for paper title only, it might be clearer to the user if the search bar is put in the app bar on the top of the page. In the paper list, there is a label could be added on top of each paper showing it is 'similar paper' like the 'original paper' label.
       - **Analysis**: The user experienced is partly satisfied in this case. The search bar problem is caused by the redundant search bar in each page all of which can only search for paper title, so it is a bit confusing.
       - **Future Improvement**: Add search bar in the app bar on the top of the page, change search bar in each page to an expandable icon that can be optional to show.
   - **Overall Analysis**: The search process is clear and straightforward, and the search results are relevant to the search keyword. More adjustments can be made to enhance the user experience, which should be pay attention to in the future design and development.
3. **Task 3: Generate Graphs**
   - **Description**: Generate different graphs in three available sections: Same-Topic, Co-Author, and Cited Tree using the techniques shown in the previous tasks.
   - **Goals:** 
     1. Successfully generate a graph in each section.
     2. The graph is relevant to the section title.
     3. The graph is interactive and papers can be highlighted both in the graph and the list.
   - **Test Cases:**
     1. **UTC ID: 3.1**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of generating a graph is clear and straightforward, but the title of the paper node in the graph makes the graph a bit messy. It takes too long to generate the graph.
        - **Suggestions**: Improve the graph generation speed and the display of the paper node title in the graph.
        - **Analysis**: The user experienced is partly satisfied in this case. The feedback of long waiting time for graph generation might cause by the database or the graph generation algorithm in the backend.
        - **Improvement**: Deploy the database in the VM, and optimize the graph generation algorithm in the backend.
     2. **UTC ID: 3.2**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of generating a graph is clear and straightforward, and the graph is relevant to the section title.
        - **Suggestions**: No suggestions, the system is good.
        - **Analysis**: The user experienced is satisfied in this case.
        - **Future Improvement**: No improvement needed.
     3. **UTC ID: 3.3**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of generating a graph is clear and straightforward, and the graph is relevant to the section title. But when there a lot of papers in the graph, there are nodes and title overlapping each other, which makes the graph a bit messy.
        - **Suggestions**: The system is good, but the graph layout needs to be optimized.
        - **Analysis**: The user experienced is partly satisfied in this case. The graph layout problem is caused by the graph drawing tool Vis-network, which is not easy to control the layout of the graph.
        - **Future Improvement**: Figure out a way to optimize the graph layout if possible.
     4. **UTC ID: 3.4**
        - **Goals Achieved**: 3 passes, 0 fails
        - **Feedback**: The process of generating a graph is clear and straightforward, and the graph is relevant to the section title. But the graph layout can be improved, and there is another problem that the graph will disappear when the user refreshes the page.
        - **Suggestions**: The system is good, but the graph layout needs to be optimized, and it is better that the graph can be saved when the user refreshes the page.
        - **Analysis**: The user experienced is partly satisfied in this case. The graph interaction problem is caused by the graph drawing tool Vis-network, which is not easy to control the interaction of the graph.
        - **Future Improvement**: Try to use route query to save the graph generation config, that can be used to generate the graph again when the user refreshes the page. The graph layout problem is the same as the previous case.
    - **Overall Analysis**: The process of generating a graph is clear and straightforward, and the graph is relevant to the section title. The system is good, but there are some improvements that can be made to enhance the user experience.

### Overall Feedback
**Rate:** 8.25 out of 10

### Analysis Summary
The usability testing indicated that users found the interface intuitive and the process of interacting with the system straightforward, also conducted on the application has highlighted the system's strengths and the areas that require attention, as shown below:

- **Strengths:**
  - **User Interface**: The application's user interface was mostly praised for being clear and user-friendly.
  - **Functionality**: The core functionalities, such as paper upload, search, and graph generation, met the users' expectations.
  - **Information Accuracy**: The accuracy of the information extracted from uploaded papers was highlighted as a strength, indicating the system's effectiveness in processing and extracting information from paper files.

- **Areas for Improvement:**
  - **Performance**: A common point of feedback across all tasks was the system's performance, particularly the speed of operations related to database operations.
  - **Graph Usability**: While the graph generation feature was appreciated, there are issues with graph readability, especially with large amount of data, suggested improvements in the graph's layout and the display of information.
  - **Error Handling and Validation**: The feedback also mentioned that a better error handling and validation process is needed.
  - **System Guidance**: Some users expressed confusion over certain features, suggests a need for enhanced system guidance, possibly through additional informational tooltips or clearer instructions.


### Testing Objectives

The usability testing was conducted to evaluate the system's ease of use, efficiency, and user satisfaction. The testing objectives were to gather feedback and insights from the participants to identify usability issues and areas for improvement, and to evaluate the overall user satisfaction with the system.

### Participant Selection

The participants for the usability testing were selected based on the target user demographic for the web application. The initial candidate pool was introduced in the [Design Document](Design.md), which includes students, academics, government officials, developers, and companies. But due to the limited time and resources, the participants were selected from the students and academics.

### Testing Environment

The usability testing was conducted in a controlled environment, with two ways provided, which are in-person and remote testing. The participants were given a way to access the application via EIDF VM, or the permission to control one of our group members' computer to interact with the system. The testing was conducted using user feedback forms, task-based testing scenarios, and user interviews to gather feedback and insights from the participants.

### Testing Procedure
1. The participants were provided with a brief introduction to the application and its core functionalities.
2. The participants were given a [Guide](Guide.md) on how to use the application, which included the layout of the application, the core functionalities, and the steps to perform specific tasks.
3. The participants were given a way to access the application via EIDF VM, or the permission to control one of our group members' computer to interact with the system.
4. The participants were asked to perform specific tasks written in the [Usability Test Form](Usability-Form.md) .
5. The participants were asked to finish the Usability Form after each task and give a general feedback at the end of the test.
6. The interactions and feedback were recorded and analyzed to identify usability issues and areas for improvement.

### Testing Method
The usability testing was conducted using a combination of direct observation, user feedback, and task success rates. After the forms were collected, the feedback was analyzed to identify common praise and issues, showing the strengths and weaknesses of the system. Based on these issues and feedback, useful insights were gathered to guide the future development and improvement of the system. After the issues and improvements were identified, the overall application rate was taken into account to evaluate the issues priority level and the overall user satisfaction.
