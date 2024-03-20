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
        1. **Search With a Invalid Title**
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

All tests passed perfectly as expected. However, there are still some problems in some part of testing. First, for all components, the unit test can cover part of the test, but there is still a lack of some more detailed tests. For example,  whether the frontend will mistake when the data format returned by the backend changes. 

Second, the graph models are not welly tested when the data is large. The graph model is tested with a small amount of data, but when the data is large, the graph model may not be able to handle it or performs badly.

Overall, the system works well and passes the test.
