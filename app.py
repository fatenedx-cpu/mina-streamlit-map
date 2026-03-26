import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(page_title="خريطة جبال الهملايا التفاعلية", layout="wide")

st.title("🏔️ خريطة قمر صناعي تفاعلية (من جبال الهملايا)")
st.markdown("تم إنشاء هذه الخريطة بناءً على كود Google Colab.")

m = leafmap.Map(center=[28.468, 84.15], zoom=10)
m.add_basemap("SATELLITE")
m.to_streamlit(height=700)
