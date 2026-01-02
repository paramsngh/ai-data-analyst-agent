AI Data Analyst Agent
Overview

AI Data Analyst Agent is an automated data exploration tool that analyzes CSV datasets and generates meaningful visual insights without requiring manual chart selection.

The goal of this project is to replicate how a real data analyst approaches an unfamiliar dataset by profiling its structure, detecting patterns, and presenting a concise set of relevant visualizations.

This repository contains Prototype v1, which focuses on clean architecture, interpretability, and extensibility. Machine learning based intelligence will be introduced in future versions.

Key Features

• Upload any CSV file through a modern web interface
• Automatically profile dataset structure and data types
• Detect numeric, categorical, and time-based columns
• Generate rule-driven analytical insights
• Select appropriate visualizations automatically
• Render charts inline inside a clean, modern UI
• Maintain analysis context for repeated runs

How to Run the Project
Prerequisites

Make sure the following are installed on your system:

Python 3.9 or newer

pip (Python package manager)

Setup Instructions

Clone the repository:

git clone https://github.com/paramsngh/ai-data-analyst-agent.git
cd ai-data-analyst-agent


Install dependencies:

pip install -r requirements.txt


If requirements.txt does not exist yet, create it with the following content:

pandas
matplotlib
streamlit


Then run:

pip install -r requirements.txt

Run the Application

Start the Streamlit app using:

python -m streamlit run app.py


Once the app starts, open your browser and go to:

http://localhost:8501

How to Use the Agent

Upload a CSV file using the file uploader

Preview the dataset inside the UI

Click Analyze Data

The agent will automatically:

Profile the dataset

Detect insights

Generate and render visualizations inline

No manual chart selection is required.

Notes

This project is currently Prototype Version 1 and focuses on automated exploratory data analysis using rule-based logic. Future versions will introduce PyTorch based machine learning, insight prioritization, and conversational analysis features.


How It Works

The agent follows a structured analysis pipeline similar to real analytics workflows:

Load the dataset safely

Profile rows, columns, data types, and missing values

Generate insights using rule-based reasoning

Select the most relevant visualizations

Render results inside the web interface

The system prioritizes clarity over quantity and avoids overwhelming users with unnecessary charts.

Project Architecture

The project is built with modular components to reflect real-world engineering practices:

• DataLoader – Handles CSV ingestion
• DataProfiler – Analyzes dataset structure and column statistics
• InsightRules – Applies reasoning rules to generate insights
• VisualizationEngine – Creates charts based on insight types
• ChartSelector – Maps insights to appropriate visualizations
• Agent – Coordinates the full analysis pipeline
• Memory – Stores analysis context for future conversational features
• UI – Streamlit-based interface for user interaction

This separation makes the system easy to extend and evolve.

Why This Project Exists

Most analytics tools require users to manually decide what to analyze and how to visualize it. This project explores a different approach by asking:

What if the system decides what matters first?

The agent surfaces the most relevant insights automatically while keeping the experience simple and intuitive.

Current Limitations

This is an early prototype and intentionally avoids aggressive automation.

The agent currently does not:
• Automatically clean or modify data
• Apply statistical or machine learning models
• Accept free-form natural language questions

These limitations are intentional and will be addressed incrementally.

Roadmap and Planned Improvements

Future versions of this project will focus on intelligence and adaptability, including:

• Data quality reporting and anomaly detection
• Insight prioritization instead of equal weighting
• Natural language explanations for charts
• Interactive follow-up actions and comparisons
• Machine learning based insight ranking using PyTorch
• Learning user preferences for analysis style
• Conversational analysis with memory-aware reasoning

PyTorch will be introduced to move from purely rule-based logic to learning-based decision making.

Tech Stack

• Python
• Pandas
• Matplotlib
• Streamlit

Planned additions include PyTorch for machine learning components.

Project Status

This repository represents Prototype Version 1.

The system is functional, extensible, and designed to grow into a more intelligent data analysis agent in future iterations.

If you want next, I can help you write resume bullets, create a demo script, design Version 2 with PyTorch, or polish this further for rec
