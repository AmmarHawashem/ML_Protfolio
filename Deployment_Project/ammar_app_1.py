# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# set the page configuration to wide
st.set_page_config(layout="wide")


# Title/Text
st.title("Auto Scout Cars Price")
st.text("Deployment Project")



# Header/Subheader
st.header('What are we?')
st.text("We are a beutiful group who created this app to give you an estimate of your dream car")
st.text("To give you an accurate price in $, please provide the following infromation")

################################################################################################################
# table  of features
#st.title("information")
#cols = st.columns(2)
#cols[0].write("make_model")
#cols[1].write("Car Model")

#cols[0].write("hp_kW")
#cols[1].write("Car power in Kilo Watt: the rate at which work is done by engines or motors")

#cols[0].write("age")
#cols[1].write("Car Age")

#cols[0].write("km")
#cols[1].write("Car mileage ")

#cols[0].write("Gears")
#cols[1].write("Possible Car gear ratio between the engine and the car’s wheels")

#cols[0].write("Displacement_cc")
#cols[1].write("Car Engine Size")
################################################################################################################


st.title("Please Fill INFO to Get the Price")
#################################################################################################################
# # 1- Make_model
# st.header('Make Model')


# # create a dictionary of car images
# car_images = {
#     'Audi A1': 'Cars_images/Audi_A1.webp',
#     'Audi A2': 'Cars_images/Audi_A2.webp',
#     'Audi A3': 'Cars_images/Audi_A3.webp',
#     'Opel Astra': 'Cars_images/Opel_Astra.webp',
#     'Opel Corsa': 'Cars_images/Opel_Corsa.webp',
#     'Opel Insignia': 'Cars_images/Opel_Insignia.webp',
#     'Renault Clio': 'Cars_images/Renault_Clio.webp',
#     'Renault Duster': 'Cars_images/Renault_Duster.webp',
#     'Renault Espace': 'Cars_images/Renault_Espace.webp',
# }

# # create a list of car names
# car_names = list(car_images.keys())

# # display the images and allow the user to choose one
# make_model = st.selectbox('Select a make model:', car_names)
# car_image = car_images[make_model]
# st.image(car_image, caption=make_model, width=400)
####################################################
import streamlit as st

# Define a list of cars
cars = [
    {"make": "Audi", "model": "A1", "image": "Cars_images/Audi_A1.webp"},
    {"make": "Audi", "model": "A2", "image": "Cars_images/Audi_A2.webp"},
    {"make": "Audi", "model": "A3", "image": "Cars_images/Audi_A3.webp"},
    {"make": "Opel", "model": "Insignia", "image": "Cars_images/Opel_Insignia.webp"},
    {"make": "Opel", "model": "Corsa", "image": "Cars_images/Opel_Corsa.webp"},
    {"make": "Opel", "model": "Astra", "image": "Cars_images/Opel_Astra.webp"},
    {"make": "Renault", "model": "Clio", "image": "Cars_images/Renault_Clio.webp"},
    {"make": "Renault", "model": "Duster", "image": "Cars_images/Renault_Duster.webp"},
    {"make": "Renault", "model": "Espace", "image": "Cars_images/Renault_Espace.webp"},
]

# Define a dictionary of images
images = {
    "Audi": "Cars_images/Audi_Logo.png",
    "Opel": "Cars_images/Opel_Logo.png",
    "Renault": "Cars_images/Renault_Logo.png",
}

# Define a dictionary of models
models = {
    "Audi": ["A1", "A2", "A3"],
    "Opel": ["Insignia", "Corsa", "Astra"],
    "Renault": ["Clio", "Duster", "Espace"],
}

# Define a form
with st.form("car_form"):
    # Select a car make
    make = st.selectbox("Select a car make", ["Audi", "Opel", "Renault"], key="make")

    # Select a car model
    if st.session_state.make != make:
        st.session_state.model = models[make][0]
    else:
        model = st.selectbox("Select a car model", models[make], key="model")

    # Submit the form
    submit_button = st.form_submit_button(label="Submit")

# Display the selected car
if submit_button:
    # Get the selected car
    make_model1 = [car for car in cars if car["make"] == make and car["model"] == st.session_state.model][0]
    make_model = make_model1["make"] + " " + make_model1["model"]
    # Display the car image
    st.image(make_model1["image"], caption=make_model, width=600)
else:
    make_model = "Audi A1"



#################################################################################################################
# 2- Gears
st.header('Gears')

# Add radio button
Gears = st.radio("Select Gears",("5","6","7", "8"))
st.write("Possible Car gear ratio between the engine and the car’s wheels are: ", Gears)


#################################################################################################################
# 3- age

st.header('Vehicle Age')


# Add radio button
age = st.radio("Select Car Age",("New",1,2, 3))
if age == "New" :
    age = 0
st.write("Car Age in years is: ", age)
#################################################################################################################
# 4- km
st.header('Driven Milage (km)')


# Your variable statistics
statistics = {
    "count": 14242,
    "mean": 32582.110,
    "std": 36856.863,
    "min": 0.000,
    "25%": 3898.000,
    "50%": 21000.000,
    "75%": 47000.000,
    "max": 310000.000,
}


# Slider for selecting a value
km = st.slider(
    "Select Car mileage",
    min_value=statistics["min"],
    max_value=statistics["max"],
    value=statistics["50%"],
    step=500.0,  # You can adjust the step size
)

# Display the selected value
st.write("Selected Value:", km)
#################################################################################################################
# 5- hp_kW
st.header('Car Power (KW)')

# Slider for selecting a value
hp_kW = st.slider(
   "Select Car power in Kilo Watt: the rate at which work is done by engines or motors:",
    min_value=40,
    max_value=290,
    value=85,
    step=10,  # You can adjust the step size
)

# Display the selected value
st.write("Selected Value:", hp_kW)



#################################################################################################################
# 6- Car Engine Size
st.header('Car Engine Size')

# Slider for selecting a value
Displacement_cc = st.slider(
   "Select Car Car Engine Size:",
    min_value=890,
    max_value=2967,
    value=1430,
    step=50,  # You can adjust the step size
)

# Display the selected value
st.write("Selected Value:", Displacement_cc )


#################################################################################################################




def sqrt_transform(X):
    X_copy = X.copy()
    X_copy["km"] = np.sqrt(X_copy["km"])
    return X_copy

import pickle
with open("deployment_model.pkl", "rb") as f:
    model = pickle.load(f)
    

# Create a dataframe using feature inputs
#make_model
my_dict = {"make_model": make_model,
           "age": age,
           "Gears": Gears,
           "km":km,
           "hp_kW":hp_kW,
           "Displacement_cc": Displacement_cc 
          }

#"


df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(round(result[0],0))
    st.write("price in $:", round(result[0],0) )
