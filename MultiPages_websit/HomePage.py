import streamlit as st

#Removing Hamburger and footer
####################################
st.markdown("""
<style>
  .css-1rs6os.edgvbvh3
  {
      visibility: hidden;
  }
  </style>
""", unsafe_allow_html= True)
####################################
st.markdown("""
<style>
  .css-cio0dv.egzxvld1
  {
      visibility: hidden;
  }
</style>
""", unsafe_allow_html= True)

# Custom navbar
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #f8f9fa;
        box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.25);
        border-radius: 4px;
    }
    .navbar-title {
        color: black;
        font-size: 24px;
        font-weight: bold;
    }
    .search-input {
        width: 300px;
        padding: 8px 12px;
        border: 2px solid #ced4da;
        border-radius: 4px;
        font-size: 16px;
        transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    }
    .search-input:focus {
        outline: none;
        border-color: #80bdff;
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
    }
    </style>
    <div class="navbar">
        <div class="navbar-title">
            My MultiPage App
        </div>
        <form>
            <input class="search-input" type="text" placeholder="Search...">
        </form>
    </div>
    """,
    unsafe_allow_html=True
)

# Your app code here
