#project 2 convertor
import streamlit as st
st.markdown(
    """
    <style> 
    body {
        background-color : #1e1e2f;
        color : white;
    }
    .stApp {
        background: linear-gradient(125deg,#bcbcbc,#cfe2f3);
        padding: 30px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        border-radius: 15px;
    }
    h1{
        text-align: center;
        font-size: 36px;
        color:white;
    }
    .stButton>button{
        background: linear-gradient(45deg,#0b5394,#351c75);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        transition: background 0.3s;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.5);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg,#92fe9d,#00c9ff);
        color:black;
    }
    .result-box{
        font-size: 2opx;
        font-weight: bold;
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 10px;
        marging-top:20px;
        boc-shadow: 0px 5px 15px rgba(0,201,255,0.3)
    }
    .footer{
        text-align : center;
        marging-top: 50px;
        font-size: 14px;
        color: black
    }
    </style>
 """,
 unsafe_allow_html=True
 )

#title and description:
st.markdown("<h1> universal unit convertor </h1>",unsafe_allow_html=True)
st.write("easily between diffrent units of lenght, weight, and temperature.")

#sidebar menu
conversion_type = st.sidebar.selectbox("choose conversion type",["lenght","weight","temperature"])
value =st.number_input("Enter value", value=0.0,min_value=0.0,step=0.1)
col1,col2 = st.columns(2)

if conversion_type == "lenght":
    with col1:
        from_unit = st.selectbox("from",[ "meters","kilometers","centimeters","milimeters","miles","yards","inches","feets"])
    with col2:
        to_unit = st.selectbox ("to",["meters","kilometers","centimeters","milimeters","miles","yards","inches","feets"]) 
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox ("from",["kilogram", "grams", "miligrams", "pounds","ounces"])
    with col2:
        to_unit = st.selectbox("to",["kilogram", "grams", "miligrams", "pounds","ounces"])    
elif conversion_type == "temperature":
    with col1:
        from_unit = st.selectbox("from",["celsius","fahranheit","kelvin"])
    with col2:
        to_unit = st.selectbox("to",["celsius","fahranheit","kelvin"])    

#converted function
def length_converter(value,from_unit,to_unit):
    lenght_units = {
        'meters': 1 ,'kilometers':0.001,'centimeters': 100, 'milimeters':10000,
        'miles':0.000621371, 'yards':1.09361, 'feets':3.28, 'inches': 39.37
    }
    return(value / lenght_units[from_unit])*lenght_units[to_unit]

def weight_convertor(value,from_unit,to_unit):
    weight_units = {
        'kilogram':1,'grams':1000, 'miligrams':1000000, 'pounds': 2.2046,'ounces':35.27
    }
    return(value / weight_units[from_unit])*weight_units[to_unit]

def temp_convertor(value,from_unit,to_unit):
    if from_unit == "celsius":
        return (value *9/5 +32) if to_unit == "fahranheit" else value + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahranheit":
         return (value - 32) * 5/9 if to_unit == "celsius" else (value -32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value -273.15) * 9/5+32 if to_unit == "fahranheit" else value
    return value 

result = 0.0

#button for conversion
if st.button ("convert"):
    if conversion_type == "lenght":
        result = length_converter(value , from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_convertor(value,from_unit,to_unit)
    elif conversion_type == "temperature":
        result = temp_convertor (value,from_unit,to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",unsafe_allow_html=True)

st.markdown ("<div class='footer'>Created with love by Asad Ali </div>", unsafe_allow_html=True )