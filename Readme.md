# Resume Insights

Resume Insights is an advanced resume parsing and analysis tool that leverages the power of LlamaIndex, Gemini, and Streamlit to extract key information from PDF resumes and present it in an intuitive, interactive format.

## Features

- **PDF Resume Parsing**: Seamlessly extract information from PDF resumes using LlamaParse.
- **AI-Powered Analysis**: Utilizes Gemini LLM for intelligent information extraction and skill matching.
- **Interactive UI**: Built with Streamlit for a user-friendly experience.
- **Skill Visualization**: Displays top skills with interactive progress bars.
- **Job Matching**: Analyzes skill relevance for specific job positions.
- **Structured Output**: Extracts name, email,skills and experience in a structured format using Pydantic models.

## 🚀 Quick Start

1. Clone the repository:
   ```
   git clone [https://github.com/nsatya02/resume-insights.git]
   cd resume-insights
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export GOOGLE_API_KEY=your_google_api_key
   export LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Tech Stack

- **LlamaIndex**: For document processing, indexing, and querying.
- **Gemini**: AI model for natural language understanding and generation.
- **Streamlit**: For building the interactive web application.
- **Pydantic**: For data validation and settings management.
- **LlamaParse**: For efficient PDF parsing.

## How It Works

1. **Document Processing**: Resumes are parsed using LlamaParse and split into manageable chunks.
2. **Indexing**: Processed documents are indexed using LlamaIndex's VectorStoreIndex.
3. **Information Extraction**: The system extracts key information like name, email, age, and skills.
4. **Skill Analysis**: Top skills are displayed with visualizations.
5. **Job Matching**: Skills are analyzed for relevance to specific job positions.
6. **Interactive UI**: Users can explore extracted information and job matching results through a Streamlit interface.

##  Key Components

- `ResumeInsights`: Main class for processing resumes and extracting information.
- `Candidate`: Pydantic model for structured candidate data.
- `JobSkill`: Pydantic model for skill relevance to job positions.
- Streamlit app: Provides the user interface for uploading resumes and displaying insights.
