import streamlit as st
import pandas as pd
import json
import tempfile
import os

from utils.file_handlers import handle_file_upload
from utils.model_utils import analyze_with_llama, get_available_models, pull_model

# App configuration
st.set_page_config(page_title="Local LLM Analyst", layout="wide")

def main():
    st.title("🧠 Local LLM Analyst")
    st.caption("Multimodal data analysis using local LLMs via Ollama")

    # Check required models
    required_models = ["llama3", "llava"]
    available_models = get_available_models()
    missing_models = [m for m in required_models if m not in available_models]

    with st.sidebar:
        st.header("🧠 Models Status")

        # Check which models are already available
        available_models = get_available_models()
        required_models = ["llama3", "llava"]
        missing_models = [m for m in required_models if m not in available_models]

        if missing_models:
            st.warning(f"⚠️ Missing model(s): {', '.join(missing_models)}")

            for model in missing_models:
                if st.button(f"📥 Download {model}"):
                    with st.spinner(f"Downloading {model}..."):
                        pull_model(model)
                        st.success(f"✅ {model} downloaded successfully.")
                        if hasattr(st, "experimental_rerun"):
                            st.experimental_rerun()
                        elif hasattr(st, "rerun"):
                            st.rerun()
                        else:
                            st.info("Model downloaded. Please refresh manually.")
        else:
            st.success("✅ All required models (llama3 & llava) are installed and ready to use!")

        # Slider for creativity
        temperature = st.slider(
            "Creativity (temperature)",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1
        )


    tab1, tab2 = st.tabs(["📄 Data Analysis", "🖼️ Image Analysis"])

    # -------- TEXT / DATA TAB -------- #
    with tab1:
        st.subheader("Upload CSV, JSON, or TXT")
        uploaded_file = st.file_uploader(
            "Upload a file",
            type=["csv", "json", "txt"]
        )

        if uploaded_file:
            file_content = None

            st.subheader("📊 File Preview")

            if uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)
                file_content = df.to_string()

            elif uploaded_file.type == "application/json":
                data = json.load(uploaded_file)
                st.json(data)
                file_content = json.dumps(data, indent=2)

            else:  # Plain text
                file_content = uploaded_file.getvalue().decode("utf-8")
                st.text(file_content[:1000] + "..." if len(file_content) > 1000 else file_content)

            st.caption("💡 Exemples : 'Summarize this data', 'Find average age by city', 'Any outliers?'")

            user_query = st.text_area(
                "What would you like to analyze?",
                placeholder="E.g., What are the key insights in this dataset?"
            )

            if st.button("Analyze") and user_query and file_content:
                with st.spinner("Analyzing with llama3..."):
                    response = analyze_with_llama(
                        model="llama3",
                        prompt=user_query,
                        context=file_content,
                        temperature=temperature
                    )
                    st.subheader("🧠 Analysis Results")
                    st.write(response)

    # -------- IMAGE TAB -------- #
    with tab2:
        st.subheader("Upload an image for analysis")
        st.info("🧠 Requires a multimodal model like `llava`")

        uploaded_image = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_image:
            if uploaded_image:
                st.image(uploaded_image, caption="🖼️ Preview", use_container_width=True)


            image_query = st.text_area(
                "What do you want to know about this image?",
                placeholder="E.g., What is shown in this image?"
            )

            if st.button("Analyze Image") and image_query:
                with st.spinner("Analyzing with llava..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                        tmp.write(uploaded_image.getbuffer())
                        tmp_path = tmp.name

                    response = analyze_with_llama(
                        model="llava",
                        prompt=image_query,
                        image_path=tmp_path,
                        temperature=temperature
                    )

                    st.subheader("📌 Image Analysis Results")
                    st.write(response)

                    try:
                        os.remove(tmp_path)
                    except Exception:
                        pass

if __name__ == "__main__":
    main()
