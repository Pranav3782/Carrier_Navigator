import streamlit as st
import pandas as pd
import plotly.express as px
from career_data import CAREER_PATHS, SKILLS_LIST, INTERESTS_LIST

# Page configuration
st.set_page_config(
    page_title="Career Path Guidance",
    page_icon="🎯",
    layout="wide"
)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Session state initialization
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

def reset_form():
    st.session_state.step = 1
    st.session_state.user_data = {}

# Header section
st.title("🎯 Career Path Guidance")
st.write("Discover your ideal career path based on your skills, interests, and experience.")

# Progress bar (normalized to 0-1 range)
progress = (st.session_state.step - 1) / 3
st.progress(progress)

# Multi-step form
if st.session_state.step == 1:
    st.subheader("Step 1: Personal Information")
    with st.form("personal_info"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", 18, 100, 25)
        education = st.selectbox(
            "Highest Education Level",
            ["High School", "Bachelor's", "Master's", "PhD"]
        )

        if st.form_submit_button("Next"):
            if name:
                st.session_state.user_data.update({
                    "name": name,
                    "age": age,
                    "education": education
                })
                st.session_state.step += 1
                st.rerun()
            else:
                st.error("Please enter your name")

elif st.session_state.step == 2:
    st.subheader("Step 2: Skills & Interests")
    with st.form("skills_interests"):
        skills = st.multiselect(
            "Select your skills",
            SKILLS_LIST,
            default=st.session_state.user_data.get("skills", [])
        )
        interests = st.multiselect(
            "Select your interests",
            INTERESTS_LIST,
            default=st.session_state.user_data.get("interests", [])
        )
        experience = st.slider(
            "Years of work experience",
            0, 40, 
            value=st.session_state.user_data.get("experience", 0)
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Previous"):
                st.session_state.step -= 1
                st.rerun()
        with col2:
            if st.form_submit_button("Next"):
                if skills and interests:
                    st.session_state.user_data.update({
                        "skills": skills,
                        "interests": interests,
                        "experience": experience
                    })
                    st.session_state.step += 1
                    st.rerun()
                else:
                    st.error("Please select at least one skill and interest")

elif st.session_state.step == 3:
    st.subheader("Career Recommendations")

    # Calculate career matches with detailed breakdown
    matches = {}
    for career, details in CAREER_PATHS.items():
        skill_matches = set(st.session_state.user_data["skills"]) & set(details["skills"])
        interest_matches = set(st.session_state.user_data["interests"]) & set(details["interests"])

        skill_score = len(skill_matches) / len(details["skills"]) if len(details["skills"]) > 0 else 0
        interest_score = len(interest_matches) / len(details["interests"]) if len(details["interests"]) > 0 else 0

        total_score = (skill_score + interest_score) / 2
        matches[career] = {
            'total_score': total_score,
            'skill_score': skill_score,
            'interest_score': interest_score,
            'matched_skills': skill_matches,
            'matched_interests': interest_matches
        }

    # Sort careers by match percentage
    sorted_matches = dict(sorted(matches.items(), key=lambda x: x[1]['total_score'], reverse=True))

    # Display results
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("### Top Career Matches")
        for career, match_data in sorted_matches.items():
            with st.expander(f"{career} - {match_data['total_score']*100:.0f}% Overall Match"):
                st.write(f"**Description:** {CAREER_PATHS[career]['description']}")
                st.write(f"**Growth Potential:** {CAREER_PATHS[career]['growth_potential']}")

                # Detailed match breakdown
                st.write("#### Match Breakdown")
                st.write(f"- Skills Match: {match_data['skill_score']*100:.0f}%")
                if match_data['matched_skills']:
                    st.write("  Matching skills: " + ", ".join(match_data['matched_skills']))

                st.write(f"- Interests Match: {match_data['interest_score']*100:.0f}%")
                if match_data['matched_interests']:
                    st.write("  Matching interests: " + ", ".join(match_data['matched_interests']))

                st.write("\n**Required Education:**")
                for edu in CAREER_PATHS[career]['education']:
                    st.write(f"- {edu}")

    with col2:
        # Create match percentage visualization
        match_df = pd.DataFrame({
            'Career': list(sorted_matches.keys()),
            'Overall Match %': [data['total_score'] * 100 for data in sorted_matches.values()],
            'Skills Match %': [data['skill_score'] * 100 for data in sorted_matches.values()],
            'Interests Match %': [data['interest_score'] * 100 for data in sorted_matches.values()]
        })

        # Overall match chart
        fig = px.bar(
            match_df,
            x='Overall Match %',
            y='Career',
            orientation='h',
            title='Career Match Percentages'
        )
        fig.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

        # Add explanation of matching algorithm
        with st.expander("How are matches calculated?"):
            st.write("""
            The matching algorithm considers two main factors:
            1. **Skills Match**: The percentage of required skills you possess
            2. **Interest Match**: The percentage of career-related interests you have

            The overall match is the average of these two scores. A higher match percentage indicates better alignment with your profile.
            """)

    # Download report
    report = f"""Career Guidance Report for {st.session_state.user_data['name']}

Education: {st.session_state.user_data['education']}
Experience: {st.session_state.user_data['experience']} years

Top Career Matches:
{'-' * 50}"""

    for career, match_data in sorted_matches.items():
        report += f"\n{career}: {match_data['total_score']*100:.0f}% Overall Match"


    st.download_button(
        label="Download Report",
        data=report,
        file_name="career_guidance_report.txt",
        mime="text/plain"
    )

    if st.button("Start Over"):
        reset_form()
        st.rerun()

# Footer
# st.markdown("---")
# st.markdown("Made with ❤️ for career guidance")