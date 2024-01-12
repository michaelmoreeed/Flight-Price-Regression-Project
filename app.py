import streamlit as st
import pandas as pd
import joblib
import sklearn
import category_encoders
import xgboost
Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def Make_Prdiction(Airline, Source, Destination, Total_Stops, Additional_Info,
       Day_of_Journey, Month_of_Journey, Dep_Time_Category,
       Arrival_Time_Category, Duration_minutes):
    
    df = pd.DataFrame(columns=Inputs)
    df.at[0,"Airline"] = Airline
    df.at[0,"Source"] = Source
    df.at[0,"Destination"] = Destination
    df.at[0,"Total_Stops"] = Total_Stops
    df.at[0,"Additional_Info"] = Additional_Info
    df.at[0,"Day_of_Journey"] = Day_of_Journey
    df.at[0,"Month_of_Journey"] = Month_of_Journey
    df.at[0,"Dep_Time_Category"] = Dep_Time_Category
    df.at[0,"Arrival_Time_Category"] = Arrival_Time_Category
    df.at[0,"Duration_minutes"] = Duration_minutes
    result = Model.predict(df)
    return result[0]
def main():
    st.title("Flight Price")
    Airline= st.selectbox("Airline",['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia','Vistara Premium economy', 'Jet Airways Business','Multiple carriers Premium economy']) 
    Source = st.selectbox("Source",['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" ,['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'] )
    Total_Stops = st.selectbox("Number of Stops" ,['non-stop', '1 stops', '2 stop', '3 stops'])
    Additional_Info = st.selectbox("Additional Info" , ['No info', 'In-flight meal not included','No check-in baggage included', '1 Long layover','Change airports', 'Business class'])
    Day_of_Journey = st.selectbox("Day of Journey" ,['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'] )
    Month_of_Journey = st.selectbox("Month of Journey",['March', 'May', 'June', 'April'])
    Dep_Time_Category = st.selectbox("Departure Time",['Night', 'Early Morning', 'Morning', 'Evening', 'Afternoon'])
    Arrival_Time_Category = st.selectbox("Arrival Time",['Early Morning', 'Afternoon', 'Night', 'Morning', 'Evening'])
    Duration_minutes = st.slider("Duration from Departure to Arrival(minutes)" ,  min_value=60, max_value=2900, value=100, step=1)
    if st.button("Predict"):
        Results = Make_Prdiction(Airline, Source, Destination, Total_Stops, Additional_Info,Day_of_Journey, Month_of_Journey, Dep_Time_Category,Arrival_Time_Category, Duration_minutes)
        st.text(f"The total Price is : {Results.astype(int)}")
main()
