from streamlit import button, code, text_input, title
title("Cold Email Generator")
url_input = text_input("Enter a URL:", value="https://jobs.nike.com/job/R-45354?from=job%20search%20funnel")
submit_button = button("submit")

if submit_button:
    code("Hello Hiring Manager, I am from AtliQ", language='markdown')