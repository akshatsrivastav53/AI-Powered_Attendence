import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background:
                        linear-gradient(135deg, rgba(194, 65, 12, 0.88), rgba(251, 146, 60, 0.84)),
                        url("https://images.unsplash.com/photo-1588072432836-e10032774350?auto=format&fit=crop&w=1600&q=80") center/cover fixed !important;
                }

                .stApp::before {
                    content: "";
                    position: fixed;
                    inset: 0;
                    pointer-events: none;
                    background:
                        url("https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80") left 8% bottom 8%/260px auto no-repeat,
                        url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=900&q=80") right 7% top 16%/300px auto no-repeat;
                    opacity: 0.28;
                    filter: saturate(1.08);
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:rgba(255, 247, 237, 0.93) !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background:
                        linear-gradient(135deg, rgba(255, 237, 213, 0.92), rgba(254, 215, 170, 0.9)),
                        url("https://images.unsplash.com/photo-1588072432836-e10032774350?auto=format&fit=crop&w=1600&q=80") center/cover fixed !important;
                }

                .stApp::before {
                    content: "";
                    position: fixed;
                    inset: 0;
                    pointer-events: none;
                    background:
                        url("https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80") left 4% bottom 8%/240px auto no-repeat,
                        url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=900&q=80") right 5% top 12%/280px auto no-repeat;
                    opacity: 0.18;
                    filter: saturate(1.05);
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            .brand-title-home {
                text-align:center;
                color:#fff7ed;
                font-size:2.7rem !important;
                line-height:1.08 !important;
                text-shadow: 0 3px 18px rgba(124, 45, 18, 0.38);
            }

            .brand-title-dashboard {
                text-align:left;
                color:#c2410c;
                font-size:1.55rem !important;
                line-height:1.05 !important;
                margin:0 !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #ea580c !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #f97316 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #7c2d12 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)
