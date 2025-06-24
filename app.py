import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title='FIFA Players Dataset EDA', page_icon=':bar_chart:')
st.markdown("<h2 style='text-align: center; font-weight: bold;'> FIFA Players Dataset EDA </h2>", unsafe_allow_html=True)

df = pd.read_csv('Cleaned FIFA Players Dataset.csv')
#################################################################################################################

page=st.sidebar.radio('Pages',['Introduction','Analysis Question','Reporting'])
if page=='Introduction':
    st.title("👋 Welcome to FIFA Players Dataset EDA")
    st.image("FiFa_3.jpg")
    st.dataframe(df.head())
    st.header("Dataset Description")
    st.write('''
- **name**: The player's commonly used name or nickname, often a shorter version of their full name (e.g., "L. Messi" for Lionel Messi).
- **full_name**: The player's complete legal name, including first, middle, and last names (e.g., "Lionel Andrés Messi Cuccittini").
- **birth_date**: The player's date of birth in MM/DD/YYYY format, indicating when they were born (e.g., "6/24/1987").
- **age**: The player's age in years at the time the data was recorded, derived from their birth date.
- **height_cm**: The player's height measured in centimeters, reflecting their physical stature (e.g., 170.18 cm).
- **weight_kgs**: The player's weight measured in kilograms, indicating their body mass (e.g., 72.1 kg).
- **positions**: The on-field positions the player is capable of playing, such as striker (ST), midfielder (CM), or defender (CB), often listed with multiple roles (e.g., "CF,RW,ST").
- **nationality**: The country the player represents, typically based on citizenship or eligibility for international play (e.g., "Argentina").
- **overall_rating**: A numerical score (out of 100) representing the player's overall skill level in the game, with higher values indicating better performance.
- **potential**: A numerical score (out of 100) estimating the player's potential to improve, often higher for younger players with growth potential.
- **value_euro**: The player's estimated market value in euros, reflecting their worth in the transfer market (e.g., 110,500,000 euros).
- **wage_euro**: The player's weekly wage in euros, indicating their salary (e.g., 565,000 euros).
- **preferred_foot**: The player's dominant foot for playing, either "Left" or "Right," affecting their performance in certain actions.
- **international_reputation(1-5)**: A rating from 1 to 5 indicating the player's global fame and recognition, with 5 being the highest (e.g., 5 for world-class stars).
- **weak_foot(1-5)**: A score from 1 to 5 assessing the player's ability to use their non-preferred foot, with higher scores indicating better versatility.
- **skill_moves(1-5)**: A score from 1 to 5 representing the player's ability to perform complex skill moves or tricks, with higher scores indicating greater flair.
- **body_type**: The player's physical build, such as "Normal," "Lean," or "Stocky," which may influence their in-game performance (some players have unique body types, e.g., "Messi").
- **release_clause_euro**: The amount in euros required to buy out the player's contract from their club, if applicable (e.g., 226,500,000 euros).
- **national_team**: The national team the player represents, if they are part of one (e.g., "Argentina"); blank if not selected.
- **national_rating**: The player's rating when playing for their national team, reflecting their performance in international matches (e.g., 82).
- **national_team_position**: The player's specific position in their national team’s lineup, such as "RF" (right forward) or "GK" (goalkeeper).
- **national_jersey_number**: The jersey number assigned to the player for their national team (e.g., 10).
- **crossing**: A score (out of 100) measuring the player's ability to deliver accurate crosses from wide areas into the penalty box.
- **finishing**: A score (out of 100) indicating the player's skill in scoring goals, particularly in one-on-one situations.
- **heading_accuracy**: A score (out of 100) reflecting the player's ability to accurately direct headers, often important for aerial duels.
- **short_passing**: A score (out of 100) assessing the player's ability to make precise short passes to teammates.
- **volleys**: A score (out of 100) measuring the player's skill in striking the ball before it hits the ground.
- **dribbling**: A score (out of 100) indicating the player's ability to control the ball while moving and evading defenders.
- **curve**: A score (out of 100) reflecting the player's ability to bend the ball’s trajectory, often used in free kicks or crosses.
- **freekick_accuracy**: A score (out of 100) measuring the player's precision in taking free kicks.
- **long_passing**: A score (out of 100) assessing the player's ability to execute accurate long-range passes.
- **ball_control**: A score (out of 100) indicating the player's ability to maintain possession and manipulate the ball under pressure.
- **acceleration**: A score (out of 100) measuring how quickly the player can reach their top speed.
- **sprint_speed**: A score (out of 100) reflecting the player's maximum running speed.
- **agility**: A score (out of 100) indicating the player's ability to change direction quickly and maintain balance.
- **reactions**: A score (out of 100) assessing the player's quickness in responding to in-game situations.
- **balance**: A score (out of 100) measuring the player's ability to stay upright and stable, especially under physical challenges.
- **shot_power**: A score (out of 100) reflecting the strength behind the player's shots, affecting goal-scoring potential.
- **jumping**: A score (out of 100) indicating the player's ability to leap for headers or aerial challenges.
- **stamina**: A score (out of 100) measuring the player's endurance and ability to maintain performance throughout a match.
- **strength**: A score (out of 100) reflecting the player's physical power, useful in physical duels.
- **long_shots**: A score (out of 100) assessing the player's ability to score from long-range shots.
- **aggression**: A score (out of 100) indicating the player's physicality and intensity in challenges or duels.
- **interceptions**: A score (out of 100) measuring the player's ability to anticipate and intercept passes.
- **positioning**: A score (out of 100) reflecting the player's awareness and ability to find optimal positions on the field.
- **vision**: A score (out of 100) indicating the player's ability to spot and create passing or scoring opportunities.
- **penalties**: A score (out of 100) assessing the player's accuracy and reliability in taking penalty kicks.
- **composure**: A score (out of 100) measuring the player's calmness and decision-making under pressure.
- **marking**: A score (out of 100) reflecting the player's ability to track and stay close to opposing players.
- **standing_tackle**: A score (out of 100) indicating the player's skill in making clean tackles while standing.
- **sliding_tackle**: A score (out of 100) assessing the player's ability to execute effective sliding tackles to win the ball.

''')
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
       st.subheader("🔍 Search ")
       name = st.text_input("")
       search = st.button("Search")

    if search:
        if name == 'Mohab Allam'.lower():
            st.write(''' 
                    He was the best instructor at Epsilon AI and the lead trainer of our course.
                    Throughout the program, he was incredibly supportive and always willing to help us whenever we faced challenges.
                    His dedication, professionalism, and friendly attitude made a huge difference in our learning experience.
                    I truly wish him continued success and all the best in his future endeavors.

                           ''')
            st.balloons()
            st.snow()
            
        elif name == 'Osama Ashraf'.lower():
            st.image("Osama Ashraf.jpg")
            
            st.write(''' I am a Computer Science student at the Faculty of Computers and Information,
                     currently specializing in the  Artificial Intelligence (AI) track with a strong focus on Data Science.
                     I am actively developing my skills in data analysis, machine learning,
                     and data visualization through hands-on learning.
                    Currently, I am enrolled in a Data Science course with EpsilonAI,
                    where I am working on a mid-project focused on Exploratory Data Analysis (EDA) of FIFA Players.
                    This project allows me to apply key Data Science techniques,
                    including data cleaning, filtering, visualization, and storytelling using Python, Pandas, Seaborn, and Streamlit.
                    I am passionate about using data to generate insights and solve real-world problems,
                     and I am constantly exploring opportunities to grow in the AI and Data Science field.

                                                                             ''')
            st.balloons()
            st.snow()
        elif name == 'Epsilon AI'.lower():
            st.image("epsilon-AI-institute-Colored-joint-the-future-of-AI.png")
            
            st.write('''
                        EpsilonAI Institute is a leading educational organization specialized in training and empowering individuals in the fields of Artificial Intelligence (AI),
                        Machine Learning, Data Science, and emerging technologies. With a mission to bridge the gap between academic knowledge and industry demands, EpsilonAI provides high-quality, 
                        hands-on learning experiences designed to prepare students and professionals for real-world applications.
                        The institute offers structured training tracks, practical projects, and mentorship programs in areas such as:

                        - **Data Science**

                        - **AI & Machine Learning**

                        - **Deep Learning**

                        - **Natural Language Processing (NLP)**

                        - **Big Data & Cloud Technologies**

                     EpsilonAI stands out through its focus on project-based learning,
                     where students apply the tools and techniques learned in class to solve actual business and data problems.
                     Courses are delivered by experienced industry professionals and are tailored to match international standards.
                     Whether you are a beginner or an advanced learner, EpsilonAI provides a supportive environment to build expertise,
                     earn certifications, and become job-ready in the AI-driven futur                                                                                                         ''')
            st.balloons()
            st.snow()
        else:
            st.info("Let's go 🚀 (No special match found)")


elif page =='Analysis Question':
    st.title("Analysis Question")
    st.write(''' - **Univariate Analysis**''')
    st.header(" 1- What is the distribution of age_category?")
    df_age_category=df['age_category'].value_counts().reset_index()
    st.plotly_chart(px.bar(df_age_category,x='age_category',y='count',title='Age Category Distribution',text_auto=True ))
    st.header("2- What is the distribution of position_count ? ")
    position_count_dist=df['position_count'].value_counts().reset_index()
    st.plotly_chart(px.pie(position_count_dist,names='position_count',values='count',title='Position Count Distribution'))
    st.header("3- What is the distribution of Body_Type ? ")
    body_type_dist=df['body_type'].value_counts().reset_index()
    st.plotly_chart(px.bar(body_type_dist,x='body_type',y='count',title='Body Type Distribution',text_auto=True))
    st.header("4- What is the distribution of Finishing ? ")
    st.plotly_chart(px.histogram(df,x='finishing',title='Finishing Distribution'))
    st.header("5- What is the distribution of Crossing ? ")
    st.plotly_chart(px.histogram(df,x='crossing',title='Crossing Distribution'))
    st.header("6- What is the distribution of Heading Accuracy ? ")
    st.plotly_chart(px.histogram(df,x='heading_accuracy',title='Heading Accuracy Distribution'))
    st.write(''' - **Bivariate Analysis**''')
    st.header("7- What are the names of players who are under 20 years old and valued at more than €10 million?")
    d180=df[(df['age']<20)&(df['value_euro']>10000000)][['full_name','value_euro','age']].sort_values(by='value_euro',ascending=False)
    st.plotly_chart(px.bar(d180,x='full_name',y='value_euro',title='Players who are under 20 years old and have a value of more than 10 million euros',text_auto=True))
    st.header("8 - Who players it's positions is GK , and height>= 185 cm , reactions>=70,agility>=55 , growth_ratio_potential_overall_rating>1 , age_category is promising, sort by release_clause_euro ASC ?")
    d27=df[(df['positions']=='GK')&(df['height_cm']>=185)&(df['reactions']>=70)
      &(df['agility']>=60)
      &(df['growth_ratio_potential_overall_rating']>1)&(df['age_category']=='Promising')]

    d27=d27[['full_name','age','value_euro','release_clause_euro','nationality']].sort_values(by='release_clause_euro',ascending=True)
    st.plotly_chart(px.bar(d27,x='full_name',y='release_clause_euro',title='Top 4 Players with positions GK with release_clause_euro',text_auto=True))
    st.header("9 - What is the average stamina for each body_type in the CM  position?")
    d3=df[df['positions']=='CM']
    d3=d3.groupby('body_type')['stamina'].mean().sort_values(ascending=False).reset_index()
    st.plotly_chart(px.pie(d3,values='stamina',names='body_type',title='Body Type with Average Stamina for CM'))
    st.header("10 - Who players it's positions is CB and height>=180 cm,marking>=60, standing_tackle>=65, sliding_tackle>=65, interceptions>=68,heading_accuracy>=68, strength>=68,jumping>=70, aggression>=70,  short_passing>=72,long_passing>=70, age_category is Peak ,sort by value_euro ASC ? ")
    d44=df[(df['positions']=='CB')&(df['height_cm']>=180)&(df['interceptions']>=68)&(df['marking']>=60)
      &(df['standing_tackle']>=65)&(df['sliding_tackle']>=65)&(df['short_passing']>=72)&(df['long_passing']>=70)
      &(df['strength']>=68)& (df['jumping']>=70)&(df['aggression']>=70)&(df['heading_accuracy']>=68)&(df['age_category']=='Peak')]
   
    d44=d44[['full_name','age','potential','value_euro','nationality']].sort_values(by='value_euro',ascending=True).head(10)
    st.plotly_chart(px.bar(d44,x='full_name',y='value_euro',title='Top 10 Players with value_euro is sorted ASC',text_auto=True))
    st.header("11 - What is the Highest release_clause_euro in each age_category for players whose position is LB ?")
    d5=df[df['positions']=='LB']
    d5=d5.groupby('age_category')['release_clause_euro'].max().sort_values(ascending=False).reset_index()
    st.plotly_chart(px.bar(d5,x='age_category',y='release_clause_euro',title='Age Category with Maximum Release Clause for LB',text_auto=True))
    st.header("12 - What is the total value_euro for each nationality for players whose position is LW or RW?  ")
    d13=df[df['positions'].isin(['LW', 'RW'])]
    d13=d13.groupby('nationality')['value_euro'].sum().sort_values(ascending=False).head(10).reset_index()
    st.plotly_chart(px.bar(d13,x='nationality',y='value_euro',title='Top 10 Nationalities with Most Value',text_auto=True))
    st.header("13 - Show the relation between the age and wage_euro ")
    st.plotly_chart(px.scatter(df, x='age', y='wage_euro', title='Age vs Wage (Euro)',size='wage_euro',
         labels={'age': 'Age', 'wage_euro': 'Wage (Euro)'},trendline='ols'))
    st.header("14- What is the relationship between overall_rating and value_euro in the FIFA dataset, and how can Plotly Express add a regression line to explore this trend? ")
    st.plotly_chart(px.scatter(df, 
                x='overall_rating', 
                y='value_euro', 
                hover_data=['full_name'], 
                title='Relationship between Overall Rating and Value (Euro)',
                labels={'overall_rating': 'Overall Rating', 'value_euro': 'Value (Euro)'},
                trendline='ols' # Add OLS regression line
                ))
    st.header("15- What is the relationship between height_cm and weight_kgs for players, and how can a scatter plot  in Plotly Express enhance this analysis?")
    st.plotly_chart(px.scatter(df,
                 x='height_cm',
                 y='weight_kgs',
                 hover_data=['full_name'],
                 title='Relationship between Height(cm) and Weight (Kg)',
                 labels={'height_cm': 'Height', 'weight_kgs': 'Weight'},
                 trendline='ols' # Add OLS regression line
                ))
    st.header("16- What is the relationship between age and potential in the FIFA dataset, and how can Plotly Express use hover data to include full_name and nationality?")
    st.plotly_chart(px.scatter(df,
                 x='age',
                 y='potential',
                 hover_data=['full_name','nationality'],
                 title='Relationship between Age  and Potential',
                 labels={'age': 'Age', 'potential': 'Potential'},
                 trendline='ols' # Add OLS regression line
                ))
    st.header("17- What is the relationship between age and acceleration for players, and how can a scatter plot in Plotly Express with a trendline reveal any patterns?")
    st.plotly_chart(px.scatter(df,
                 x='age',
                 y='acceleration',
                 hover_data=['full_name','nationality'],
                 title='Relationship between Age  and Acceleration',
                 labels={'age': 'Age', 'acceleration': 'Acceleration'},
                 trendline='ols' # Add OLS regression line
                ))
    st.header("18- What is the relationship between age and stamina for FIFA players, and how can Plotly Express")
    st.plotly_chart(px.scatter(df,
                 x='age',
                 y='stamina',
                 hover_data=['full_name','nationality'],
                 title='Relationship between Age  and Stamina',
                 labels={'age': 'Age', 'stamina': 'Stamina'},
                 trendline='ols' # Add OLS regression line
                ))
    st.write(''' - **Multivariate Analysis**''')
    st.header("19 - Who are the players with position_count greater than or equal to 3 , age_category equal to 'Promising' and potential greater than or equal to 85?")
    d12=df[(df['position_count']>=3) & (df['age_category']=='Promising')& (df['potential']>=85)]
    d12=d12[['full_name','age','potential']].sort_values(by='potential',ascending=False).head(10)
    st.plotly_chart(px.bar(d12,x='full_name',y='potential',color='age',title='Top 10 Promising Players with position_count>=3',text_auto=True))
    st.header("20 - Who players it's positions is ST and height>=180 cm,finishing>=82, positioning>=70, shot_power>=69, volleys>=68,heading_accuracy>=72, ball_control>=65,strength>=62, jumping>=72, reactions>=70,short_passing>=62")
    d91=df[(df['positions']=='ST')&(df['height_cm']>=180)&(df['finishing']>=82)&(df['positioning']>=70)
      &(df['shot_power']>=69)&(df['volleys']>=68)&(df['heading_accuracy']>=72)&(df['ball_control']>=65)
      &(df['strength']>=65)& (df['jumping']>=72)&(df['reactions']>=70)&(df['short_passing']>=62)]
    d91=d91[['full_name','age','potential','positions','nationality']].sort_values(by='age',ascending=False).head(10)
    st.plotly_chart(px.bar(d91,x='full_name',y='age',color='potential',title='Top 10 Players with positions ST with age',text_auto=True))
    st.header("21 - Who are the players earning more than €250K in weekly wages and age is between 22 and 28?")
    d190=df[(df['wage_euro']>250000)& df['age'].isin(range(22,29))][['full_name','age','wage_euro','nationality']].sort_values(by='wage_euro',ascending=False)
    st.plotly_chart(px.bar(d190,x='full_name',y='wage_euro',color='age',title='Top 9 Players with wages more than 250000 with age',text_auto=True))
    st.header('22 - What is the average crossing and finishing for each preferred_foot in positions LW ')
    d33=df[df['positions']=='LW']
    d33=d33.groupby('preferred_foot')[['finishing','crossing']].mean().sort_values(by=['finishing'],ascending=False).reset_index()
    st.plotly_chart(px.bar(d33,x='preferred_foot',y='finishing',color='crossing',title='Preferred Foot with Average Finishing and Crossing for LW',text_auto=True))
    st.header("23 - What is the average crossing and finishing for each preferred_foot in positions RW ")
    d34=df[df['positions']=='RW']
    d34=d34.groupby('preferred_foot')[['finishing','crossing']].mean().sort_values(by=['finishing'],ascending=False).reset_index()
    st.plotly_chart(px.bar(d34,x='preferred_foot',y='finishing',color='crossing',title='Preferred Foot with Average (Finishing and Crossing)  for RW',text_auto=True))
    st.header("24 - Players(LB,RB),marking>=80, standing_tackle>=70, sliding_tackle>=70, interceptions>70,crossing>=80, stamina>=75,sprint_speed>=75,acceleration>=70 ?")
    d9=df[(df['positions'].isin(['LB','RB'])) & (df['marking']>=80)&(df['standing_tackle']>=70)&(df['sliding_tackle']>=70)
       &(df['interceptions']>=70)&(df['crossing']>=80)&(df['stamina']>=75)&(df['sprint_speed']>=75)&(df['acceleration']>=70)]
    d9=d9[['full_name','age','potential','positions']].sort_values(by='potential',ascending=False)
    st.plotly_chart(px.bar(d9,x='full_name',y='potential',color='age',title='Top 6 Players with Potential>=85',text_auto=True))
    st.header("25 - What is the correlation between all columns ? ")
    df_corr=(df.drop(['name','full_name','positions','nationality','birth_date','preferred_foot','body_type','position_category','age_category'],axis=1)).corr()
    st.plotly_chart(px.imshow(
    df_corr,
    text_auto='.2f',  # عرض القيم بدقة رقمين عشريين
    color_continuous_scale='RdBu_r', # Scale of color
    title='Correlation Matrix of FIFA Players Dataset',
    labels=dict(x='Features', y='Features', color='Correlation'),
    width=1200,
    height=800
       ))


########################################################################################################################
elif page=='Reporting':
    
    filter_columns = [
        "nationality", "positions", "age", "age_category", "position_category", "position_count",
        "height_cm", "weight_kgs", "overall_rating", "potential", "value_euro", "wage_euro",
        "preferred_foot", "international_reputation(1-5)", "weak_foot(1-5)", "skill_moves(1-5)",
        "body_type", "release_clause_euro", "crossing", "short_passing", "dribbling", "curve",
        "freekick_accuracy", "long_passing", "long_shots", "interceptions", "balance", "vision",
        "penalties", "finishing", "positioning", "shot_power", "volleys", "heading_accuracy",
        "ball_control", "strength", "jumping", "reactions", "agility", "stamina", "acceleration",
        "sprint_speed", "aggression", "composure", "marking", "standing_tackle", "sliding_tackle",
        "growth_ratio_potential_overall_rating", "value_to_wage_ratio", "bmi"
    ]

    selected_filters = {}
    for col in filter_columns:
        options = ["All"] + sorted(df[col].dropna().unique().tolist())
        choice = st.sidebar.selectbox(col, options)
        if choice != "All":
            selected_filters[col] = choice

    # تطبيق الفلاتر فقط إذا تم اختيار قيم محددة
    filtered_df = df.copy()
    for key, value in selected_filters.items():
        filtered_df = filtered_df[filtered_df[key] == value]

    st.subheader("📃 Filtered Data")
    st.write(filtered_df)
    st.plotly_chart(px.bar(filtered_df,x="full_name",y="age",color="value_euro",title="The Names , Ages and Value_Euro of Players after Filtering",text_auto=True))
    #st.plotly_chart(px.bar(filtered_df,x="full_name",y="growth_ratio_potential_overall_rating",color="body_type",title="The Names , Growth and Body_Type of Players after Filtering",text_auto=True))
    #st.plotly_chart(px.bar(filtered_df,x='full_name',y='position_count',color='positions',title="The Relation that shows who players are playing in more positions and its positions",text_auto=True))

    
