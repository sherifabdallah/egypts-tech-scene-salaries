import pandas as pd
import streamlit as st

def main():



    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            button[title="View fullscreen"] {
            display: none;
            }
            button[title="View fullscreen"]:hover {
            display: none;
            }
            summary{
                display: none;
            }
            summary:hover{
                display: none;
            }
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    sheet_id = '1F72dM1-kD129wt8xctacsgD_q7ja9c77hZh-JhMJFlI'
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    df.head()

    survey_option = st.sidebar.selectbox('Choose a Data', 
                    ("Years of Experience" , "Job Title", "Current Company", "Salary range"))

    plot_option = st.sidebar.selectbox('Choose a Data', 
                    ("Bar chart" ,"Line chart" , "Area chart", "Arrow bar chart", "Arrow area chart", "Arrow line chart", "Legacy area chart"))

    table_option = st.sidebar.radio("Show Table", ('Turn Off', 'Turn On'))

    data = df[survey_option].value_counts()

    def table(): 
        if table_option == "Turn On":
            st.table(data)
        else:
            pass

    def plot(plot):
        if plot == "Line chart":
            st.line_chart(data)
        elif plot == "Area chart":
            st.area_chart(data)
        elif plot == "Arrow bar chart":
            st._arrow_bar_chart(data)
        elif plot == "Arrow area chart":
            st._arrow_area_chart(data)
        elif plot == "Arrow line chart":
            st._arrow_line_chart(data)
        elif plot == "Legacy area chart":
            st._legacy_area_chart(data)
        elif plot == "Bar chart":
            st.bar_chart(data)

    plot(plot_option)


    table()
    st.caption('[Share us in The Survey](https://forms.gle/Tkk1SXwFbRQDWwsd8)')


if __name__ == "__main__":
    try:
        main()
    except:
        st.error('Erorr 404 Please Contact The Deveoloper sherifabdalla2005@gmail.com')