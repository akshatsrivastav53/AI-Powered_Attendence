# AI-Powred Attendence Managemenet App

Streamlit app for AI-powered student attendance using face and voice recognition.

## Run locally

```bash
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Push this `ai-attendance-project-app` folder to GitHub.
2. Go to https://share.streamlit.io and create a new app.
3. Select the GitHub repository and use `app.py` as the main file.
4. In **Advanced settings**, paste the contents of your local `.streamlit/secrets.toml`.
5. Deploy the app and use the generated `*.streamlit.app` link on your resume.

Do not commit `.streamlit/secrets.toml`; it contains private Supabase credentials.
