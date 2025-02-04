import streamlit as st
from PIL import Image
from datetime import datetime, time
import pandas as pd
from datetime import date
from functions import create_new_datafile
import calendar, os

# Page Configuration
st.set_page_config(
    page_title="Time-Sheet",
    page_icon=Image.open("extrafiles/1695795692729-removebg-preview.png"),
    initial_sidebar_state="collapsed",
    layout="wide"
)

# Variables
all_months = ["January", "February", "March", "April", "May", "June", "July", "September",
              "October", "November", "December"]

# Popup dialoge
@st.dialog(" ")
def popup(message="Done!"):
    st.text(message)

# Sidebar
with st.sidebar:
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        main_icon = st.image("extrafiles/1695795692729-removebg-preview.png", width=100)
        title = st.header("Diya Infotech TimeSheet")
    month = st.selectbox(label="Month",options=all_months, index=datetime.now().month-1)
    year = st.text_input(label="Year", max_chars=15, value = datetime.now().year)
    if st.button("Create"):
        path = f'CSVs/{month}-{year}.csv'
        if os.path.exists(path):
            popup("Timestamps are already created!")
        else:
            month_num = list(calendar.month_name).index(month)
            create_new_datafile(month_num, int(year))
            popup(f"File created for {month}-{year}")


# Main Page
st.header('TimeSheet')
st.text("")
col1, col2, col3 = st.columns([1,1,10])
with col1:
    month = st.selectbox(label="Choose Month",options=all_months, index=datetime.now().month-1)
with col2:
    year = st.number_input(label="Choose Year",
                        min_value =2024,
                        max_value = 2050,
                        step = 1,
                        # format = "%f",
                        value = datetime.now().year)

path =  f'CSVs/{month}-{year}.csv'


if st.button("Go"):
    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        popup("Timestamp didn't find! \nPlease create one.")

#Configurate column
column_configurator = {    
                        "date" : st.column_config.DateColumn(
                            "Date",
                            min_value=date(2023, 1, 1),
                            max_value=date(2050, 1, 1),
                            format="MMM DD, YYYY",
                            step=1,
                            disabled=True,
                            width = "small",
                        ),
                        "punch_in" : st.column_config.TimeColumn(
                            "Punch in Time",
                            min_value=time(8, 0, 0),
                            max_value=time(18, 0, 0),
                            format="hh:mm a",
                            step=30,
                            width = "small",
                        ),
                        "punch_out" : st.column_config.TimeColumn(
                            "Punch out Time",
                            min_value=time(8, 0, 0),
                            max_value=time(18, 0, 0),
                            format="hh:mm a",
                            step=30,
                            width = "small",
                        ),
                        "day" : st.column_config.TextColumn(
                            "Day",
                            disabled=True,
                            width = "small",
                        ),
                        "early-leave" : st.column_config.CheckboxColumn(
                            "Left Early?",
                            default=False,
                            width = "small",   
                        ),
                        'total-earning' : st.column_config.TextColumn(
                            "Total Earning",
                            width = "medium",
                            disabled="True",
                        ),
                        "notes" : st.column_config.TextColumn(
                            "Notes",
                            help = "If you want to add something to explain yourself in future about the time stamps.",
                            width = "large"
                        ),    
                      }



if os.path.exists(path):
    df = pd.read_csv(path)
    df['date'] = df['date'].astype('datetime64[ns]')
    df['punch_in'] = df['punch_in'].astype('datetime64[ns]').dt.time
    df['punch_out'] = df['punch_out'].astype('datetime64[ns]').dt.time
    df['early-leave'] = df['early-leave'].astype('bool')
    df['notes'] = df['notes'].astype('str')
    df['total-earning'] = df['total-earning'].astype('str')


    data = st.data_editor(df, 
                        hide_index=True, 
                        use_container_width=True,
                        column_config = column_configurator,
                        )
    col1, col2, col3 = st.columns([1, 10, 1])
    with col3:
        if st.button("Apply"):
            # data['punch_in'] = data['punch_in']
            data.to_csv(path, header=True,index=False)
else:
    st.divider()
    st.text("Timesheet is not created yet! \nThis is sample TimeSheet.")
    st.divider()
    path = "CSVs/test.csv"
    df = pd.read_csv(path)
    df['date'] = df['date'].astype('datetime64[ns]')
    df['punch_in'] = df['punch_in'].astype('datetime64[ns]').dt.time
    df['punch_out'] = df['punch_out'].astype('datetime64[ns]').dt.time
    df['early-leave'] = df['early-leave'].astype('bool')
    df['notes'] = df['notes'].astype('str')
    df['total-earning'] = df['total-earning'].astype('str')


    data = st.data_editor(df, 
                        hide_index=True, 
                        use_container_width=True,
                        column_config = column_configurator,
                        )
    


