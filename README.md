# Carrier_Navigator

This project is a **Career Path Guidance** tool, an interactive web application designed to help users discover careers that align with their personal skills and interests. By answering a short, two-part questionnaire, users receive personalized career recommendations complete with a detailed analysis and a visual comparison chart.

### Why is this project useful?

This project is particularly useful because it demystifies the often overwhelming process of career planning.

* **Personalized Guidance** 🧭: Instead of offering generic advice, it provides recommendations tailored specifically to the user's self-reported abilities and passions.
* **Career Discovery** 🔭: It can introduce users to potential career paths they may not have considered, broadening their horizons.
* **Clarity and Simplicity** ✨: The app uses casual, easy-to-understand language for both skills (e.g., "Explaining things clearly") and interests (e.g., "Helping and caring for people"), making it accessible to students, graduates, or anyone looking to change careers.
* **Data-Driven Approach** 📊: It provides a logical and structured way to match personal attributes to professional roles, bringing a sense of order to a complex decision.

---

### Tech Stack Used

The application is built entirely within the Python ecosystem, leveraging a few key libraries to create a powerful yet simple user experience.

* **Application Framework**: **Streamlit** is the core framework used to build the web application. It allows for the rapid creation of interactive UI elements like forms, buttons, sliders, and text inputs directly from a Python script.
* **Data Manipulation**: **Pandas** is used to structure the final recommendation scores into a DataFrame. This makes the data easy to sort and pass to the visualization library.
* **Data Visualization**: **Plotly Express** creates the interactive, professional-looking bar chart that visually compares the match percentages of the recommended careers.
* **Styling**: **CSS** is used in a separate `style.css` file to apply custom styling, giving the application a unique and polished look beyond the default Streamlit appearance.

---

### How It Works Internally: Step-by-Step

The application's logic flows through a series of steps, managed by Streamlit's session state, to guide the user from data entry to the final results.

#### Step 1: Initialization and Page Setup
When you first run the app, the `index.py` script executes.
1.  **Imports**: It loads all necessary libraries (Streamlit, Pandas, Plotly) and imports the career data from `career_data.py`.
2.  **Session State**: It initializes a "session state" to keep track of the user's progress. It creates a variable `st.session_state.step` (set to 1) to track the current page and an empty dictionary `st.session_state.user_data` to store the user's answers. This state persists as the user interacts with the app.
3.  **Custom CSS**: The app reads the `style.css` file and injects its content into the app's HTML, applying your custom styles.

#### Step 2: Gathering User Information
The application uses the `step` variable in the session state to display the correct form.
1.  **Personal Info (Step 1)**: The app shows a form asking for the user's name, age, and education level. When the "Next" button is clicked, this data is saved into the `st.session_state.user_data` dictionary. The `step` counter is then increased to 2, and Streamlit is instructed to `st.rerun()`, effectively reloading the script to show the next page.
2.  **Skills and Interests (Step 2)**: Now on the second page, the user is presented with two multi-select boxes populated with the `SKILLS_LIST` and `INTERESTS_LIST` from `career_data.py`. After making selections and clicking "Next," the chosen skills and interests are added to the user's data, the step counter is increased to 3, and the script reruns again.

#### Step 3: The Matching Algorithm
With all user data collected, the app moves to the results page and performs its core calculation.
1.  **Iteration**: The code loops through every single career defined in the `CAREER_PATHS` dictionary.
2.  **Matching**: For each career, it compares the career's required skills against the user's selected skills. It does the same for interests. It uses Python's efficient `set` intersection to find how many items match.
3.  **Scoring**: It calculates two percentages:
    * **Skill Score**: (Number of matching skills / Total skills required for the career) * 100
    * **Interest Score**: (Number of matching interests / Total interests for the career) * 100
4.  **Final Score**: The overall match score for the career is the average of the skill score and the interest score. This final score, along with the detailed breakdown, is stored for display.

#### Step 4: Displaying the Results
Once all careers are scored, the results are presented to the user.
1.  **Sorting**: The careers are sorted from the highest overall match score to the lowest.
2.  **Two-Column Layout**: The screen is split into two columns.
    * The **left column** displays the sorted list of careers. Each one is in an expandable box (`st.expander`) that shows the career description, growth potential, and a detailed breakdown of which skills and interests matched.
    * The **right column** features the Plotly bar chart, providing an immediate visual summary of the top recommendations. Below the chart, an expander explains exactly how the match was calculated, ensuring transparency for the user.
3.  **Final Actions**: The user is presented with a button to download a text file report and a "Start Over" button that resets the session state to its initial values, allowing for a fresh start.
