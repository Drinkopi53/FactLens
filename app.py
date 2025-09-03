# Main application file for FactLens
import streamlit as st
import google.generativeai as genai
import os

# --- Gemini Function ---
def generate_gemini_report(api_key, topic):
    """
    Generates a report using the Google Gemini API.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro-latest')

        prompt = f"""Tugas Anda adalah membuat laporan lengkap dan terverifikasi tentang topik berikut: "{topic}".
Syarat:
1. Jelaskan secara terstruktur: Latar belakang, perkembangan terkini, dampak, dan konteks.
2. Hindari ambiguitas dan berita palsu. Gunakan hanya sumber terpercaya.
3. Sertakan daftar referensi di bagian akhir.
4. Gunakan bahasa yang jelas dan mudah dipahami."""

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Provide a more user-friendly error message
        st.error(f"An error occurred while communicating with the Gemini API: {e}")
        return None

# --- Main Application ---
st.title("FactLens: Your AI-Powered Fact-Checker")

st.write("Enter a topic below, and FactLens will generate a comprehensive, fact-checked report using Google's Gemini model.")

# --- User Input ---
topic_input = st.text_input("Enter the topic you want to research:", placeholder="e.g., 'Mobil ESEMKA'")
api_key_input = st.text_input("Enter your Google AI Studio API Key:", type="password")

generate_button = st.button("Generate Report")

if generate_button:
    if not api_key_input:
        st.error("Error: Please enter your Google AI Studio API Key.")
    elif not topic_input:
        st.error("Error: Please enter a topic to research.")
    else:
        with st.spinner("Generating your report... This may take a moment."):
            report_text = generate_gemini_report(api_key_input, topic_input)
            if report_text:
                st.success("Report generated successfully!")
                st.session_state['report'] = report_text
                st.session_state['topic'] = topic_input

# --- Display Report and Download Button ---
if 'report' in st.session_state:
    st.markdown("---")
    st.subheader("Generated Report")
    st.markdown(st.session_state['report'])

    # Sanitize topic for filename
    # Replace spaces with underscores and remove characters that are not alphanumeric or spaces
    safe_topic = "".join(c for c in st.session_state['topic'] if c.isalnum() or c in (' ', '_')).rstrip()
    safe_filename = f"{safe_topic.replace(' ', '_')}.md"

    st.download_button(
        label="Download Report as MD",
        data=st.session_state['report'],
        file_name=safe_filename,
        mime="text/markdown"
    )
