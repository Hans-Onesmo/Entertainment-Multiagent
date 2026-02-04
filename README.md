# 🎬 Entertainment Multi-Agent System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

An intelligent multi-agent system that helps users discover movies and TV series using natural language. The system uses specialized AI agents that collaborate to understand user preferences, search for content, and provide curated recommendations — including trailers and critic reviews.  

---

## ✨ Key Features

- **Multi-Agent Specialization**:  
  - **Preference Agent**: Extracts user tastes and genre preferences  
  - **Movie Agent**: Recommends movies aligned with preferences  
  - **Series Agent**: Suggests TV series tailored to the user  
  - **Trailer Agent**: Provides official trailer links  
  - **Critic Agent**: Reviews and ensures diversity in recommendations  
  - **Supervisor (Crew)**: Coordinates all agents and orchestrates workflow  

- **Natural Language Understanding**: Handles queries like:  
  `"I want dark sci-fi series set in dystopian London"`  

- **Human-in-the-loop Approval**: Users can approve or reject recommendations before final output  

- **Extensible & Modular**: Add more agents, tools, or APIs easily  

- **Integration Ready**: Supports OpenAI LLMs, TMDB/IMDb, YouTube API (for trailers)
  

---

## 🛠 Key Challenges & Solutions

| Challenge | Description | Solution |
|-----------|-------------|---------|
| **Coordination** | Multiple agents can generate overlapping or contradictory results | Use a **Supervisor agent** (Crew) to sequence tasks and manage outputs |
| **Hallucinations** | LLMs may generate incorrect movie info | Use structured APIs (TMDB, IMDb) for validation |
| **Infinite Loops / Repetition** | Agents may query each other endlessly | Implement task timeouts and supervisor oversight |
| **Cost Management** | LLM queries can be expensive | Cache user preferences, batch queries, and limit model size if needed |

---

## 📋 Prerequisites

- Python 3.10+  
- OpenAI API key (GPT-4 recommended)  
- TMDB API key (free account available)  
- Git (optional, for version control)  

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Entertainment-Multiagent.git
cd Entertainment-Multiagent
