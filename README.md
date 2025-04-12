# Local LLM Analyst

A local, privacy-focused tool for multimodal data analysis using LLMs via Ollama.

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
