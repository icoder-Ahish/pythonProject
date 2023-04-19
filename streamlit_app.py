import streamlit as st

st.title("Streamlit App")
st.text("Writing Just Simple text ")
st.header('my streamlit button ')

json = {"a":"1,2,3", "b":"22,33,22"}
st.json(json)

st.markdown("***Ashish*** os3")
st.markdown("---")


st.latex(r"\begin{bmatrix}\frac{5}{6} & \frac{1}{6} & 0 \\[0.3em]\frac{5}{6} & 0 & \frac{1}{6} \\[0.3em]0 & \frac{5}{6} & \frac{1}{6}\end{bmatrix}")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown("---")
code="""
print("hello world")
def func():
  return 0; 
"""
st.code(code, language="Python")


if st.button('Clicked me'):
     st.write('Why Clicked ')
else:
     st.write('Goodbye')

