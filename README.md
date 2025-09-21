# Carrier_Navigator
# 🎯 Career Path Guidance Navigator

An interactive web application built with Streamlit to help you discover your ideal career path based on your unique skills and interests.

---

## 🌟 Overview

The Career Path Guidance Navigator is a user-friendly tool designed to simplify the complex process of career planning. Through a simple multi-step questionnaire, the application gathers information about your abilities and passions to provide personalized, data-driven career recommendations.

This project is perfect for:
* Students exploring future career options.
* Professionals considering a career change.
* Anyone seeking clarity on how their skills and interests align with the job market.

## ✨ Features

* **Interactive Multi-Step Form**: A guided questionnaire that collects your personal information, skills, and interests in a seamless flow.
* **Personalized Recommendations**: A smart matching algorithm scores and ranks various careers to find the best fit for you.
* **Diverse Career Database**: Includes a wide range of careers from tech and business to creative arts and healthcare, using accessible, everyday language.
* **Detailed Breakdown**: For each recommendation, see exactly *why* it's a match by viewing which of your skills and interests align with the career.
* **Data Visualization**: An interactive bar chart from Plotly Express provides an at-a-glance comparison of your top career matches.
* **Downloadable Report**: Get a personalized text summary of your results to save and review later.
* **Easy to Customize**: The entire career database is managed in a single Python file (`career_data.py`), making it simple to add new careers, skills, or interests.

## 🛠️ Tech Stack

The application is built with a simple yet powerful stack, all within the Python ecosystem:

* **Framework**: **Streamlit** is used for the core web application and user interface components.
* **Data Manipulation**: **Pandas** structures the final recommendation scores for sorting and visualization.
* **Data Visualization**: **Plotly Express** creates the interactive and responsive bar chart.
* **Styling**: **CSS** is used for custom styling to enhance the default look and feel of the application.

## ⚙️ How It Works Internally

The application's logic is straightforward and effective:

1.  **Data Collection**: The app uses Streamlit's `session_state` to store your inputs as you move through the multi-step form.
2.  **Matching Algorithm**: After you submit your information, the app iterates through each career in its database. For each one, it calculates a match score.
3.  **Scoring**: The score is based on two key metrics:
    * **Skill Score**: The percentage of a career's required skills that you possess.
    * **Interest Score**: The percentage of a career's associated interests that you have.
4.  **Final Score Calculation**: The overall match score is the average of the skill and interest scores:
    ```latex
    $$
    \text{Total Score} = \frac{(\text{Skill Score} + \text{Interest Score})}{2}
    $$
    ```
5.  **Results Display**: The careers are sorted by their final score and presented in a clean, two-column layout with detailed expanders and a summary chart.

## 🚀 Getting Started

To run this project locally, follow these steps:

**1. Prerequisites**
* Make sure you have Python 3.8 or higher installed.

**2. Clone the Repository**
```bash
git clone [https://github.com/your-username/career-path-guidance.git](https://github.com/your-username/career-path-guidance.git)
cd career-path-guidance
    * The **left column** displays the sorted list of careers. Each one is in an expandable box (`st.expander`) that shows the career description, growth potential, and a detailed breakdown of which skills and interests matched.
    * The **right column** features the Plotly bar chart, providing an immediate visual summary of the top recommendations. Below the chart, an expander explains exactly how the match was calculated, ensuring transparency for the user.
3.  **Final Actions**: The user is presented with a button to download a text file report and a "Start Over" button that resets the session state to its initial values, allowing for a fresh start.
