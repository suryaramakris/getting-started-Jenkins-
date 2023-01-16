import streamlit as st 
import pickle

model = pickle.load(open('model.pkl', 'rb'))
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

def welcome():
    return "Index Page"


def predict(sl,sw,pl,pw):
    prediction=model.predict([[sl,sw,pl,pw]])
    return labels[prediction[0]]
def main():
    st.title("IRIS Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit IRIS Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sl = st.text_input("Sepal Length","Type Here")
    sw = st.text_input("Sepal Width","Type Here")
    pl = st.text_input("Petal Length","Type Here")
    pw = st.text_input("Petal Width","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(sl,sw,pl,pw)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

main()
