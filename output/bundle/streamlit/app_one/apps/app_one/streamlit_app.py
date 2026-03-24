import streamlit as st
import traceback

try:
    # ---- your entire app code goes here ----
    import pandas as pd
    
    st.title("My App")
    df = pd.DataFrame({"a": [1, 2, 3]})
    st.dataframe(df)
    # ---- end of app code ----

except TypeError as e:
    st.error("TypeError occurred!")
    st.code(traceback.format_exc())     # shows full traceback in UI

except Exception as e:
    st.error(f"Unexpected error: {e}")
    st.code(traceback.format_exc())     # shows full traceback in UI