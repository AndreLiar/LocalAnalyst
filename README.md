

# 🧠 Local LLM Analyst

A local, privacy-focused tool for multimodal data analysis using LLMs via Ollama.

---

## 📦 Requirements

- Python 3.8+
- [Ollama](https://ollama.ai)
- Models: `llama3`, `llava` (for image analysis)
- streamlit

---

## ✨ Features

- Analyze text files (CSV, JSON, TXT)
- Basic image analysis (requires multimodal model)
- Works completely offline
- No API keys required
- Simple, intuitive interface

---

## 🚀 Installation

### 1. Install Ollama

Download Ollama from [ollama.ai/download](https://ollama.ai/download) and follow the instructions for your OS:

- **macOS**:
  ```bash
  brew install ollama

 - Linux (Ubuntu/Debian):
  ```bash
curl -fsSL https://ollama.com/install.sh | sh


-Windows: Use the Windows installer from the official site:

### 2. Download Required Models  
Open a terminal and run:

```bash
ollama pull llama3   # For text analysis  
ollama pull llava    # For image analysis (multimodal)
```
```bash
ollama run llama3
```
### 3. Clone the Repository

```bash
git clone https://github.com/AndreLiar/LocalAnalyst
cd LocalLlamaAnalyst
```

### 4. Install Python Dependencies  
Make sure you're in a virtual environment, then run:

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💡 Example Prompts

---

## 🧠 Example Prompts

### 📊 For Data Files (CSV, JSON, TXT)

#### 🔍 **Exploration / Overview**
- `"Summarize this data."`
- `"What are the key columns and how many records are there?"`
- `"What is the age range in this dataset?"`
- `"List the unique cities present in the data."`

#### 📊 **Statistical Analysis**
- `"What is the average age of individuals?"`
- `"Count the number of people per city."`
- `"Find the oldest and youngest individuals."`
- `"Calculate the standard deviation of the age column."`

#### 💡 **Insights / Trends**
- `"Identify any trends or patterns in this dataset."`
- `"What insights can we draw from this data?"`
- `"Are there any outliers in the age column?"`
- `"Suggest 3 key takeaways based on this data."`

#### 🧹 **Data Cleaning Checks**
- `"Are there any missing or inconsistent values?"`
- `"Which columns have the most repeated values?"`
- `"Is this data normalized or clean?"`

---

### 🖼️ For Images (using `llava`)

#### 👁️ **Basic Understanding**
- `"Describe the contents of this image."`
- `"What is happening in this picture?"`
- `"List all visible objects."`

#### 🧠 **Contextual Analysis**
- `"What could be the context or purpose of this image?"`
- `"What does this image represent?"`
- `"What emotions or themes are suggested?"`

#### 📈 **Specific Use Cases**
- `"Is this chart going up or down?"`
- `"What kind of business chart is this?"`
- `"Can you extract insights from this visual?"`

---

