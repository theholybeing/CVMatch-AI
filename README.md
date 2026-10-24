# CVMatch AI

An open-source, Gemma-powered resume analyzer that compares a candidate's CV with a job description and gives evidence-based feedback.

## MVP features

- Paste CV text and a job description
- Estimated alignment score (not a hiring probability)
- Matched skills with CV evidence
- Potential gaps based on requirements not evidenced in the CV
- CV improvement suggestions and questions to consider
- Download the result as JSON

## Requirements

- Python 3.11 or newer recommended
- Git
- A Google AI Studio API key with access to the selected Gemma model
- Internet connection for API requests

## Setup on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set your API key. Confirm that the selected `GEMMA_MODEL` is available to your account in Google AI Studio. If not, replace it with an available Gemma model ID.

Test the API:

```powershell
python test_gemma.py
```

Run the app:

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit, usually http://localhost:8501.

## Security

- Never commit `.env` or publish your API key.
- Do not use real CVs for demos unless you have permission and understand the API provider's data terms.
- Review generated recommendations; the model can be wrong.

## Licensing

The application source code is licensed under MIT (see `LICENSE`). The Gemma model is governed by separate model terms. Review the terms for the exact model you use and link them here before submission.

## Limitations

The score is a rough text-based alignment indicator, not a probability of being hired. A skill not mentioned in a CV is not necessarily a skill the applicant lacks. This tool should not be used as an automated hiring decision-maker.
