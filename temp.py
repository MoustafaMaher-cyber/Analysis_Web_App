import streamlit as st
import pandas as pd
import seaborn as sns
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")
upload = st.file_uploader("upload your dataset")
if upload is not None:
    data=pd.read_csv(upload)
    
if upload is not None:    
    if st.checkbox("Perview Data Set"):
       if st.button("Head"):
           st.write(data.head())
       if st.button("Tail"):
           st.write(data.tail())
           
if upload is not None:
   if st.checkbox("Data Type"):
       st.text("Dtypes of DataSet")
       st.write(data.dtypes)  

if upload is not None:
   data_shape=st.radio("what is the dimension do you want to know", ('Rows','Columns')) 
   if data_shape=='Rows':
       st.text("Rows OF Your dataset")
       st.write(data.shape[0])
   if data_shape=='Columns':
       st.text("Columns OF Your dataset")
       st.write(data.shape[1])
if upload is not None:
   test=data.isnull().values.any()
   if test==True:
      if st.checkbox("Lost Data"):
         sns.heatmap(data.isnull())
         st.pyplot()
   else:
       st.success("there is no missing data")
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("there are duplicates in your dataset")
        dup=st.selectbox("remove duplicates",("select one","yes","no"))
        if dup=="yes":
            data=data.drop_duplicates()
            st.text("duplicates are removed")
        if dup=="no":
            st.text("duplicates were not removed")
    else:
        st.success("there are no duplicates")
if upload is not None:
   if st.checkbox("Summery stat"):
       st.write(data.describe(include="all"))        