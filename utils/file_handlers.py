
import pandas as pd
import json

def handle_file_upload(uploaded_file):
    """Process uploaded files and return their content as text."""
    file_type = uploaded_file.type
    
    try:
        if file_type == "text/csv":
            df = pd.read_csv(uploaded_file)
            return df.to_string()
        elif file_type == "application/json":
            data = json.load(uploaded_file)
            return json.dumps(data, indent=2)
        else:  # Plain text
            return uploaded_file.getvalue().decode("utf-8")
    except Exception as e:
        return f"Error processing file: {str(e)}"
