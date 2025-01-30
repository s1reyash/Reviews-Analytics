import streamlit as st
import os

# Configure Page
st.set_page_config(page_title="Google Play Store Analytics", page_icon="📊", layout="wide")

# Graphs Information
graphs = {
    "Top Categories": {"file": "Category_1.html", "desc": "Analysis of the most popular app categories."},
    "Installation Metrics": {"file": "Installs_6.html", "desc": "Breakdown of app installations."},
    "Rating Analysis": {"file": "Rating_4.html", "desc": "Detailed analysis of app ratings."},
    "User Sentiment": {"file": "Sentiment_5.html", "desc": "Analysis of user feedback trends."},
    "Update Trends": {"file": "Update Graph 9.html", "desc": "Analysis of app update frequencies."},
    "Genre Analysis": {"file": "Genre.html", "desc": "Breakdown of app genres and their popularity."}
}

# Sidebar Navigation
st.sidebar.title("📊 Google Play Store Analytics")
menu_options = ["📈 Main Dashboard"] + list(graphs.keys())
selected_option = st.sidebar.radio("Navigation", menu_options)

# --- Main Dashboard (Landing Page) ---
if selected_option == "📈 Main Dashboard":
    st.markdown("# 🏠 Google Play Store Analytics Dashboard")
    st.write("Welcome to the interactive dashboard showcasing Google Play Store analytics. Explore various insights below:")

    # Display all graphs in a grid layout
    cols = st.columns(2)
    for idx, (title, data) in enumerate(graphs.items()):
        graph_path = os.path.join("graphs", data["file"])
        
        with cols[idx % 2]:  # Arrange in two columns
            st.markdown(f"### {title}")
            st.write(data["desc"])
            
            if os.path.exists(graph_path):
                with open(graph_path, "r", encoding="utf-8") as f:
                    graph_html = f.read()
                st.components.v1.html(graph_html, height=400, scrolling=True)
            else:
                st.error(f"⚠️ Graph file `{data['file']}` not found!")

# --- Individual Graph Pages ---
else:
    graph_data = graphs[selected_option]
    
    st.markdown(f"## {selected_option}")
    st.write(graph_data["desc"])

    graph_path = os.path.join("graphs", graph_data["file"])
    if os.path.exists(graph_path):
        with open(graph_path, "r", encoding="utf-8") as f:
            graph_html = f.read()
        st.components.v1.html(graph_html, height=600, scrolling=True)
    else:
        st.error(f"⚠️ Graph file `{graph_data['file']}` not found!")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.write("👤 **Shreyash Chawade**")
st.sidebar.write("[GitHub](https://github.com/s1reyash) | [LinkedIn](https://www.linkedin.com/in/shreyash8421/)")
