import pandas as pd
import streamlit as st

def main():
    st.set_page_config(page_title='Software Engineers Salaries in Egypt', page_icon='logo.png')

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



    df = pd.read_csv("https://docs.google.com/spreadsheets/d/1R8aoZV-O5p4dIBdNzsSwQ17rvhxnXld8Wxp0vK5xgwc/export?format=csv")
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

   
    st.write("## Egypt's Tech Scene (Salaries, Technologies and Trends)")


    plot(plot_option)

    table()

    st.write("An overview of both the salaries and technologies in Egypt's tech market")
    st.write("### Introduction")
    st.write("Egypt's tech market is a bit vague. You can't access information regarding salaries, popular technologies, and companies' environment without finding yourself having to get in contact with employees working inside the company. Famous reviews websites like Glassdoor aren't much of a help since most employees don't disclose their salaries even anonymously and only angry employees decide to write reviews on Glassdoor.")
    st.write("This unintelligibility makes anyone who wants to value themselves in the market fail to do so. A lot of people often ask me: Which technologies should we learn to increase our chances in the market? Or how much should I ask for? And so on. While it's true that some companies are technology agnostic when it comes to hiring where they test you in your Problem Solving and Design skills, most companies, in Egypt, favour hiring someone who is already comfortable with their tech stack.")
    st.write("Disclaimer: This by no means is a comprehensive overview of the market, it's biased toward my network and the companies I'm interested in. Having said that, I assure you that I made an effort trying to clean the data and make it fair. I didn't include anyone working for a remote company, all the data that we analyse here are shared by Software Engineers working in companies operating in Egypt.")


    st.caption('[Join us in The Survey](https://forms.gle/Tkk1SXwFbRQDWwsd8)')


if __name__ == "__main__":
#     try:
    main()
#     except:
#         st.error('Erorr 404 Please Contact The Deveoloper sherifabdalla2005@gmail.com')
