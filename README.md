# Local LLM Analyst

A local, privacy-focused tool for multimodal data analysis using LLMs via Ollama.

## 📦 Requirements
Python 3.8+

Ollama

Models: llama3, llava
## Features

- Analyze text files (CSV, JSON, TXT)
- Basic image analysis (requires multimodal model)
- Works completely offline
- No API keys required
- Simple, intuitive interface

## Installation

1. **Install Ollama**:
   - Download and install Ollama from [ollama.ai](https://ollama.ai/)

2. **Download Models** (run in terminal):
   ```bash
   ollama pull llama3  # For text analysis
   ollama pull llava   # For image analysis (multimodal)

3. Clone this repository
```bash
git clone https://github.com/<your-username>/LocalLlamaAnalyst.git
cd LocalLlamaAnalyst
4. Install Python dependencies
Make sure you're in a virtual environment:

```bash
pip install -r requirements.txt
5. Run the application
```bash
streamlit run app.py
Then visit http://localhost:8501 in your browser.

💡 Example Prompts
📄 For CSV / JSON / Text:
"Summarize this dataset"

"Find the average age by city"

"What are the main insights from this data?"

🖼️ For Images (with llava):
"Describe what is shown in this image"

"List the objects and context"

"What does this image represent?"

