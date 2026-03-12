# Knowledge Roadmap Builder

Knowledge Roadmap Builder is a Python + Streamlit + agentic AI app that generates **course/learning roadmaps** as interactive graphs based on a simple natural-language prompt from the user.

## 🚀 What This App Does

- Takes a user prompt like:  
  *"I want a roadmap to learn full‑stack web development"*  
- Uses an AI **agent** to:
  - Break the goal into topics, subtopics, and learning stages
  - Order them into a sensible sequence (prerequisites → core → advanced)
  - Add short descriptions and suggested resources (optional)
- Renders the result as a **graph/roadmap** directly in the Streamlit UI.

## 🧱 Tech Stack

- **Python 3.11+**
- **Streamlit** for the web UI
- **Agentic AI stack** (e.g. Langgraph) to orchestrate roadmap generation
- A hosted or local **LLM API** (Euron API key(OpenAI))
- **Graph/visualization** library (`graphviz`)

## ✨ Core Features

- Natural-language input: “Data Science roadmap”, “DSA roadmap for interviews”, “NLP roadmap”, etc.
- AI-generated nodes:
  - Milestones (Beginner, Intermediate, Advanced)
  - Topics and subtopics
  - Dependencies between concepts
- Interactive graph view:
  - Zoom / pan
  - Click nodes to see details (description, notes, resources)
- One-click **regenerate** / **refine**:
  - “Add more math topics”
  - “Make it 6-month plan”
  - “Focus on Python only”

## 🧩 How It Works (High Level)

1. **User input**  
   User describes the roadmap they want (domain, level, constraints).

2. **Agent planning**  
   An AI agent:
   - Analyzes the goal
   - Plans stages (Foundations → Core → Projects → Advanced)
   - Expands each stage into nodes and edges

3. **Graph construction**  
   Nodes and edges are converted into a graph data structure.

4. **Visualization**  
   Streamlit renders the graph and any metadata (tables, sidebars, descriptions).

## 📦 Installation

```bash
git clone https://github.com/<your-username>/knowledge-roadmap-builder.git
cd knowledge-roadmap-builder

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
