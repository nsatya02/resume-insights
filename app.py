import streamlit as st
import tempfile
import random

from resume_insights import ResumeInsights


def main():
    st.set_page_config(page_title="Resume Insights", page_icon="📄")

    st.title("Resume Insights")
    st.write("Upload a resume PDF to extract key information.")

    # Show upload file control
    uploaded_file = st.file_uploader(
        "Select Your Resume (PDF)", type="pdf", help="Choose a PDF file up to 5MB"
    )

    if uploaded_file is not None:
        if st.button("Get Insights"):
            with st.spinner("Parsing resume... This may take a moment."):
                try:
                    # Temporary file handling
                    with tempfile.NamedTemporaryFile(
                        delete=False, suffix=".pdf" or ".docx"
                    ) as temp_file:
                        temp_file.write(uploaded_file.getvalue())
                        temp_file_path = temp_file.name

                    # Extract the candidate data from the resume
                    st.session_state.resumeInsights = ResumeInsights(temp_file_path)
                    st.session_state.insights = (
                        st.session_state.resumeInsights.extract_candidate_data()
                    )
                    
                except Exception as e:
                    st.error(f"Failed to extract insights: {str(e)}")

        if "insights" in st.session_state:
            insights = st.session_state.insights

            st.subheader("Extracted Information")
            st.write(f"**Name:** {insights.name}")
            st.write(f"**Contact:** {insights.contact}")
            st.write(f"**Email:** {insights.email}")
            st.write(f"**Location:** {insights.location}")
            st.write(f"**Skills:** {insights.skills}")
            st.write(f"**Experience:** {insights.experience}")

            # The Free Tier Gemini API has a limitation of 10k bytes on the request payload,
            # and since the query engine is going to augment the prompt
            # with conxtextual information found in the document,
            # reducing the skill's number would limit the request payload.
            # skills = insights.skills[:20]
            # display_skills(skills)

    else:
        st.info("Please upload a PDF resume to get started.")

    # App information
    st.sidebar.title("VYASA")
    st.sidebar.info(
        "This app uses LlamaIndex and Gemini to parse resumes and extract key information. "
        "Upload a PDF resume to see it in action!"
    )
    st.sidebar.subheader("Long Rank Dependencies Limitation")


# def display_skills(skills: list[str]):
#     if skills:
#         st.subheader("Top Skills")

#         # Custom CSS for skill bars
#         st.markdown(
#             """
#         <style>
#         .stProgress > div > div > div > div {
#             background-image: linear-gradient(to right, #4CAF50, #8BC34A);
#         }
#         .skill-text {
#             font-weight: bold;
#             color: #1E1E1E;
#         }
#         </style>
#         """,
#             unsafe_allow_html=True,
#         )

#         # Display skills with progress bars and hover effect
#         for skill in skills:
#             col1, col2 = st.columns([3, 7])
#             with col1:
#                 st.markdown(
#                     f"<p class='skill-text'>{skill}</p>", unsafe_allow_html=True
#                 )
#             with col2:
#                 # TODO: USE Proficiency level property generated by the model.
#                 proficiency = random.randint(60, 100)
#                 st.progress(proficiency / 100)

#         # Expandable section for skill details
#         job_position = st.selectbox(
#             "Select a job position:",
#             [
#                 "Founding AI Data Engineer",
#                 "Founding AI Engineer",
#                 "Founding AI Engineer, Backend",
#                 "Founding AI Solutions Engineer",
#             ],
#             on_change=lambda: st.session_state.pop("job_matching_skills", None),
#         )
#         company = "LlamaIndex"

#         st.subheader(
#             f"How relevant are the skills for {job_position} Position at {company}?"
#         )

#         with st.spinner("Matching candidate's skills to job position..."):
#             if "job_matching_skills" not in st.session_state:
#                 st.session_state.job_matching_skills = (
#                     st.session_state.resumeInsights.match_job_to_skills(
#                         skills, job_position, company
#                     ).skills
#                 )
#             else:
#                 with st.expander("Skill Relevance"):
#                     for skill in st.session_state.job_matching_skills:
#                         st.write(
#                             f"**{skill}**: {st.session_state.job_matching_skills[skill].relevance}"
#                         )

#         # Interactive elements
#         selected_skill = st.selectbox(
#             "Select a skill to highlight:",
#             st.session_state.job_matching_skills,
#         )
#         st.info(f"{st.session_state.job_matching_skills[selected_skill].reasoning}")


if __name__ == "__main__":
    main()



