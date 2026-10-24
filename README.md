# CVMatch AI

An open-source, Gemma-powered resume analyzer that compares a candidate's CV with a job description and provides evidence-based feedback.

## Features

- Resume and job description analysis
- Matched skills and potential skill gaps
- Estimated job-match score
- CV improvement suggestions
- Transparent analysis with supporting evidence

## Technology Stack

- Python
- Streamlit
- Google Gen AI SDK
- Gemma through the Gemini API

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file with `GEMINI_API_KEY` and `GEMMA_MODEL`.
5. Run `streamlit run app.py`.

## Model and Licensing

The application source code is licensed under MIT.

The Gemma model has separate terms and licensing requirements. Review and link the applicable model terms for the exact model used.

## Limitations

The match score is an approximate decision-support indicator, not a probability of being hired. Results may contain errors and should be reviewed by the applicant.
