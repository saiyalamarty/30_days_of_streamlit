import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1 - Its basic use case is to display text and Markdown-formatted text:

st.write("Hello, *World!* :sunglasses:")

# Example 2 - As mentioned above, it can also be used to display other data formats such as numbers:

st.write(1234)

# Example 3 - DataFrames can also be displayed as follows:

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

# Example 4 - You can pass in multiple arguments:

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# Example 5 - Finally, you can also display plots as well by passing it to a variable as follows:

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(c)
