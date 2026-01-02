import streamlit as st
import pandas as pd

from data_loader import DataLoader
from data_profiler import DataProfiler
from insight_rules import InsightRules
from visualization_engine import VisualizationEngine
from chart_selector import ChartSelector


def render_ui():
    # Page configuration
    st.set_page_config(
        page_title="AI Data Analyst Agent",
        page_icon="📊",
        layout="wide"
    )

    # Custom dark tech styling
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: #e6e6e6;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            height: 3em;
            font-size: 16px;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("## 🤖 AI Data Analyst Agent")
    st.markdown(
        "Upload a CSV file and let the agent automatically analyze and visualize your data."
    )

    st.divider()

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.markdown("### 📄 Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

        st.divider()

        if st.button("🚀 Analyze Data"):
            with st.spinner("Analyzing data..."):
                # Save temp CSV
                temp_path = "uploaded_data.csv"
                df.to_csv(temp_path, index=False)

                # Run analysis pipeline
                loader = DataLoader(temp_path)
                df_loaded = loader.load_csv()

                profiler = DataProfiler(df_loaded)
                profile = profiler.profile()

                rules = InsightRules(df_loaded, profile)
                insights = rules.generate_insights()

                viz = VisualizationEngine(df_loaded)
                selector = ChartSelector(viz)

                numeric_col = next(
                    col for col, info in profile["columns"].items()
                    if info["type"] == "numeric"
                )

            st.success("Analysis completed successfully!")

            st.markdown("### 📊 Generated Visualizations")

            for insight in insights:
                fig = selector.render_chart(insight, numeric_col=numeric_col)
                if fig:
                    st.pyplot(fig)
