import pandas as pd
from dash import html, dcc, Dash, Input, Output, callback
import plotly.express as px
from datetime import datetime
def age_grouping(age):
    if age <= 18:
        return  'Below 18yrs'
    elif 19 <= age <= 25:
        return '19-25yrs'
    elif 26 <= age <= 35:
        return '26-35yrs'
    elif 36 <= age <= 45:
        return '36-45yrs'
    elif 46 <= age <= 55:
        return '46-55yrs'
    else:
        return 'More than 55yrs'
external_stylesheets = ['assets/style/styles.css']
app = Dash(__name__,external_stylesheets = external_stylesheets)
customer_df = pd.read_csv('P6-UK-Bank-Customers (1).csv')
customer_df['Age Group'] = customer_df['Age'].apply(age_grouping)
customer_df['Date Joined'] = pd.to_datetime(customer_df['Date Joined'],format='%d.%b.%y')


def date_grouping(date):
    if datetime(2015,1,1) <= date <= datetime(2015,3,31):
        return 'Quarter 1'
    elif datetime(2015,4,1) <= date <= datetime(2015,6,30):
        return 'Quarter 2'
    elif datetime(2015,7,1) <= date <= datetime(2015,9,30):
        return 'Quarter 3'
    else:
        return 'Quarter 4'
customer_df['Quarters'] = customer_df['Date Joined'].apply(date_grouping)
customer_df['Full Name'] = customer_df['Name'].str.cat(customer_df['Surname'], sep = " ")
#Total Customer
count_customers = customer_df['Customer ID'].nunique()

app.layout = (
    html.Div(
        children = [
        html.Div(
            children=[
                html.H1('UK Bank Customer Report - 2015', style={'background-color': 'black', 'text-align': 'center', 'color': 'crimson','vertical-align':'top','margin-top':'0px'})
            ]
        ),
        #dropdowns
        html.Div(
           style ={'display':'flex'},
           children=[
               html.Div(
                   children=[
                       html.H1('Total Customers',style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 10%'}),
                       html.H1(count_customers,id='card',
                               style={ 'text-align': 'center','padding': '0 10%'})
                   ],
                   style={'flex':1}
               ),
               html.Div(
                   children=[
                       html.H1('Job Classification',
                               style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 10%'}),
                       dcc.Dropdown(customer_df['Job Classification'].unique(), id='job-dropdown',searchable=True,placeholder='Search Job Class',style= {'color':'crimson'})
                   ],
                   style={'flex': 1}
               ),
               html.Div(
                   children=[
                       html.H1('Gender',
                               style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 10%'}),
                       dcc.Dropdown(customer_df['Gender'].unique(), id='gender-dropdown',searchable=True,placeholder='Search Gender',style= {'color':'crimson'})
                   ],
                   style={'flex': 1}
               ),
               html.Div(
                   children=[
                       html.H1('Age',
                               style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 10%'}),
                       dcc.Dropdown(customer_df['Age Group'].unique(), id='age-dropdown', searchable=True,placeholder='Search Age',style= {'color':'crimson'})
                   ],
                   style={'flex': 1}
               ),
               html.Div(
                   children=[
                       html.H1('Region',
                               style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 10%'}),
                       dcc.Dropdown(customer_df['Region'].unique(),id= 'region-dropdown',searchable=True,placeholder='Search Region',style= {'color':'crimson'})
                   ],
                   style={'flex':1}
               )
           ]
       ),
        #piecharts and Donutcharts
        html.Div(
           children=[
               html.Div(style={'display': 'flex'},
                   children=[
                       html.Div(
                           children=[
                               html.H1('Total balance of customer by Region',
                                       style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 5%'}),
                               dcc.Graph(style={'width': '90%', 'padding': '0 5%'},id='donut-chart')
                           ],
                           style={'flex':1}
                       ),
                       html.Div(
                           children=[
                               html.H1('Count of Customers by Region',
                                       style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 5%'}),
                               dcc.Graph(id='pie-chart',
                                         style={'width': '90%', 'padding': '0 5%'})
                           ],
                           style={'flex':1}
                       ),
                       html.Div(
                           children=[
                               html.H1('Count of customer per Quarter',
                                       style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 5%'}),
                               dcc.Graph(style={'width': '90%', 'padding': '0 5%'},id='quarter-graph')
                           ],
                           style={'flex':1}
                       ),
                       html.Div(
                           children=[
                               html.H1('Average of age by Job Classification',
                                       style={'background-color': 'black', 'font-size': '130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 5%'}),
                               dcc.Graph(style={'width': '90%', 'padding': '0 5%'},id='agejob-graph')
                           ],
                           style={'flex':1}
                       )
                   ]
               )
           ]
       ),
         html.Div(style={'display':'flex'},
             children=[
                 html.Div(
                     children=[
                         html.H1('Balance by Job classification and gender',style={'background-color': 'black','font-size':'130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 20%'}),
                         dcc.Graph(id='jobgender-stack',style={'width': '90%', 'padding': '0 5%'})
                     ],
                    style={'flex':1}
                 ),
                 html.Div(
                     children=[
                         html.H1('Balance of age group and gender',style={'background-color': 'black','font-size':'130%', 'color': 'crimson','border':'2px solid crimson','padding': '0 20%'}),
                         dcc.Graph(id= 'agegender-stack',style={'width': '90%', 'padding': '0 5%'})
                     ],
                    style={'flex':1}
                 ),
                 html.Div(
                     children=[
                         html.H1('Full name by job and gender',style={'background-color': 'black','font-size':'130%','color': 'crimson','border':'2px solid crimson','padding': '0 20%'}),
                         dcc.Graph(id='namejobgender-stack' ,style={'width': '90%', 'padding': '0 5%'})
                     ],
                    style={'flex':1}
                 )
             ]
         )
    ]
    )
)
#Count of customer per Quarter
@callback(
    Output('quarter-graph','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value'),
    Input('region-dropdown','value')
)
def update_graph(job,gender,age_group,region):
    if job is None:
        if gender is None:
            if age_group is None:
                if region is None: #job,gender,age_group,region = None
                    customer_quater_df = customer_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #job,gender,age_group = None and region = value
                    filter_df = customer_df[customer_df['Region']==region]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
            else:
                if region is None: #job,gender,region = None and age_group = value
                    filter_df = customer_df[customer_df['Age Group']== age_group]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #job,gender = None and age_group,region = value
                    filter_df = customer_df[(customer_df['Age Group']== age_group) & (customer_df['Region']== region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
        else:
            if age_group is None:
                if region is None: #job,age_group,region = None and gender = value
                    filter_df = customer_df[customer_df['Gender'] == gender]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #job,age_group = None and gender,region = value
                    filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Region'] == region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
            else:
                if region is None: #job,region = None and gender,age_group = value
                    filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Age Group'] == age_group)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #job = None and gender,age_group,region = value
                    filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
    else:
        if gender is None:
            if age_group is None:
                if region is None: #gender,age_group,region = none and job = value
                    filter_df = customer_df[customer_df['Job Classification'] == job]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #gender,age_group= none and job,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Region'] == region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
            else:
                if region is None: #gender,region= none and job,age_group  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #gender= none and job,age_group,region  = value
                    filter_df = customer_df[ (customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group) & (customer_df['Region']==region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
        else:
            if age_group is None:
                if region is None: #age_group,region= none and job,gender  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #age_group= none and job,gender,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender) & (customer_df['Region'] == region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
            else:
                if region is None: #region= none and job,gender,age_group  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender) & (customer_df['Age Group'] == age_group)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
                else: #job,gender,age_group,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender) & (customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    customer_quater_df = filter_df.groupby('Quarters').agg(Totalcustomer=('Full Name', 'count'))
    fig5 = px.bar(customer_quater_df, x=customer_quater_df.index, y='Totalcustomer',labels={'Totalcustomer': 'Count of Customers', 'Quarters': 'Quarter'}, color=customer_quater_df.index,color_discrete_map={'Quarter 1': 'crimson', 'Quarter 2': 'crimson', 'Quarter 3': 'crimson','Quarter 4': 'crimson'},text_auto='0.2s')
    fig5.update_layout(
        yaxis_title='Count of Customers',
        showlegend=False
    )
    fig5.update_traces(textangle=0, textposition="outside", cliponaxis=False)
    return fig5

#Average of age by Job Classification
@callback(
    Output('agejob-graph','figure'),
    Input('region-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value')
)
def update_graphb(region,gender,age_group):
    if region is None:
        if gender is None:
            if age_group is None: #age,gender,region= None
                age_job_df = customer_df.groupby('Job Classification').agg(AverageAge = ('Age','mean'))
            else: #gender,region= None and age = Value
                filter_df = customer_df[customer_df['Age Group']==age_group]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
        else:
            if age_group is None: #age,region= None and gender = Value
                filter_df = customer_df[customer_df['Gender'] == gender]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
            else: #region= None and age,gender = Value
                filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Age Group']==age_group)]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
    else:
        if gender is None:
            if age_group is None:#age,gender = None and region= Value
                filter_df = customer_df[customer_df['Region'] == region]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
            else: #gender = None and region,age= Value
                filter_df = customer_df[(customer_df['Region'] == region) & (customer_df['Age Group'] == age_group)]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
        else:
            if age_group is None: #region,gender= Value and age = None
                filter_df = customer_df[(customer_df['Region'] == region) & (customer_df['Gender'] == gender)]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
            else: #region,age,gender= Value
                filter_df = customer_df[(customer_df['Region'] == region) & (customer_df['Age Group'] == age_group) & (customer_df['Gender'] == gender)]
                age_job_df = filter_df.groupby('Job Classification').agg(AverageAge=('Age', 'mean'))
    fig6 = px.bar(age_job_df, x=age_job_df.index, y='AverageAge', labels={'AverageAge': 'Average Age'},color=age_job_df.index,color_discrete_map={'Blue Collar': 'crimson', 'Other': 'crimson', 'White Collar': 'crimson'},text_auto='0.2s')
    fig6.update_layout(
        yaxis_title='Count of full name',
        showlegend=False
    )
    fig6.update_traces(textangle=0, textposition="outside", cliponaxis=False)
    return fig6
# Donut chart
@callback(
    Output('donut-chart','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value')
)
def update_donut(job,gender,age_group):
    if job is None:
        if gender is None:
            if age_group is None: #age,gender,job= None
                donut_df = customer_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
            else: #gender,job= None and age = Value
                filter_df = customer_df[customer_df['Age Group']==age_group]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
        else:
            if age_group is None: #age,job= None and gender = Value
                filter_df = customer_df[customer_df['Gender'] == gender]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
            else: #job= None and age,gender = Value
                filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Age Group']==age_group)]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
    else:
        if gender is None:
            if age_group is None:#age,gender = None and job= Value
                filter_df = customer_df[customer_df['Job Classification'] == job]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
            else: #gender = None and job,age= Value
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group)]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
        else:
            if age_group is None: #job,gender= Value and age = None
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender)]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
            else: #job,age,gender= Value
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group) & (customer_df['Gender'] == gender)]
                donut_df = filter_df.groupby(['Region']).agg(Totalbalance=('Balance', 'sum')).round()
    fig = px.pie(donut_df,values='Totalbalance', names=donut_df.index, hole=0.5,labels={'Totalbalance':'Total Balance'})
    fig.update_layout()
    return fig

#Pie chart
pie_df = customer_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
@callback(
    Output('pie-chart','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value')
)
def update_donut(job,gender,age_group):
    if job is None:
        if gender is None:
            if age_group is None: #age,gender,job= None
                pie_df = customer_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
            else: #gender,job= None and age = Value
                filter_df = customer_df[customer_df['Age Group']==age_group]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
        else:
            if age_group is None: #age,job= None and gender = Value
                filter_df = customer_df[customer_df['Gender'] == gender]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
            else: #job= None and age,gender = Value
                filter_df = customer_df[(customer_df['Gender'] == gender) & (customer_df['Age Group']==age_group)]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
    else:
        if gender is None:
            if age_group is None:#age,gender = None and job= Value
                filter_df = customer_df[customer_df['Job Classification'] == job]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
            else: #gender = None and job,age= Value
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group)]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
        else:
            if age_group is None: #job,gender= Value and age = None
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Gender'] == gender)]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
            else: #job,age,gender= Value
                filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Age Group'] == age_group) & (customer_df['Gender'] == gender)]
                pie_df = filter_df.groupby(['Region']).agg(Totalcount=('Customer ID', 'count'))
    fig1 = px.pie(pie_df,values='Totalcount',names=pie_df.index,labels={'Totalcount':'Total count'})
    fig1.update_layout()
    return fig1
#Balance by Job classification and gender
@callback(
    Output('jobgender-stack','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value'),
    Input('region-dropdown','value')
)
def update_fig(job,gender,age_group,region):
    if job is None:
        if gender is None:
            if age_group is None:
                if region is None: #job,gender,age_group,region = None
                    job_gender_df = customer_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #job,gender,age_group = None and region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender',values='Balance', aggfunc='sum')
            else:
                if region is None: #job,gender,region = None and age_group = value
                    filter_df = customer_df[customer_df['Age Group']== age_group]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender',values='Balance', aggfunc='sum')
                else: #job,gender = None and age_group,region = value
                    filter_df = customer_df[(customer_df['Age Group']== age_group) & (customer_df['Region']== region)]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender',values='Balance', aggfunc='sum')
        else:
            if age_group is None:
                if region is None: #job,age_group,region = None and gender = value
                    job_gender_df = customer_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #job,age_group = None and gender,region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
            else:
                if region is None: #job,region = None and gender,age_group = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #job = None and gender,age_group,region = value
                    filter_df = customer_df[(customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
    else:
        if gender is None:
            if age_group is None:
                if region is None: #gender,age_group,region = none and job = value
                    job_gender_df = customer_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #gender,age_group= none and job,region  = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
            else:
                if region is None: #gender,region= none and job,age_group  = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #gender= none and job,age_group,region  = value
                    filter_df = customer_df[ (customer_df['Age Group'] == age_group) & (customer_df['Region']==region)]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
        else:
            if age_group is None:
                if region is None: #age_group,region= none and job,gender  = value
                    job_gender_df = customer_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #age_group= none and job,gender,region  = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
            else:
                if region is None: #region= none and job,gender,age_group  = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
                else: #job,gender,age_group,region  = value
                    filter_df = customer_df[(customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    job_gender_df = filter_df.pivot_table(index='Job Classification', columns='Gender', values='Balance',aggfunc='sum')
    fig2 = px.bar(job_gender_df, x=job_gender_df.index, y=['Male', 'Female'], barmode='stack',
                      labels={'value': 'Total Balance', 'color': 'Gender', 'variable': 'Gender'},
                      color_discrete_map={'Male': 'crimson', 'Female': 'pink'},text_auto='0.2s')
    fig2.update_layout(
    )
    return fig2
#Balance of age group and gender
@callback(
    Output('agegender-stack','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value'),
    Input('region-dropdown','value')
)
def update_fig(job,gender,age_group,region):
    if job is None:
        if gender is None:
            if age_group is None:
                if region is None: #job,gender,age_group,region = None
                    age_gender_df = customer_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
                else: #job,gender,age_group = None and region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
            else:
                if region is None: #job,gender,region = None and age_group = value
                    age_gender_df = customer_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
                else: #job,gender = None and age_group,region = value
                    filter_df = customer_df[customer_df['Region']== region]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
        else:
            if age_group is None:
                if region is None: #job,age_group,region = None and gender = value
                    age_gender_df = customer_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
                else: #job,age_group = None and gender,region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
            else:
                if region is None: #job,region = None and gender,age_group = value
                    age_gender_df = customer_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
                else: #job = None and gender,age_group,region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
    else:
        if gender is None:
            if age_group is None:
                if region is None: #gender,age_group,region = none and job = value
                    filter_df = customer_df[customer_df['Job Classification'] == job]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
                else: #gender,age_group= none and job,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Region'] == region)]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
            else:
                if region is None: #gender,region= none and job,age_group  = value
                    filter_df = customer_df[customer_df['Job Classification'] == job]
                    age_gender_df = filter_df.pivot_table(index='Age Group', columns='Gender', values='Balance',aggfunc='mean')
                else: #gender= none and job,age_group,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Region'] == region)]
                    age_gender_df = filter_df.pivot_table(index='Age Group',columns='Gender',values='Balance',aggfunc='mean')
        else:
            if age_group is None:
                if region is None: #age_group,region= none and job,gender  = value
                    filter_df = customer_df[customer_df['Job Classification'] == job]
                    age_gender_df = filter_df.pivot_table(index='Age Group', columns='Gender', values='Balance',aggfunc='mean')
                else: #age_group= none and job,gender,region  = value
                    filter_df = customer_df[(customer_df['Job Classification'] == job) & (customer_df['Region'] == region)]
                    age_gender_df = filter_df.pivot_table(index='Age Group', columns='Gender', values='Balance',aggfunc='mean')
            else:
                if region is None: #region= none and job,gender,age_group  = value
                    filter_df = customer_df[customer_df['Job Classification'] == job]
                    age_gender_df = filter_df.pivot_table(index='Age Group', columns='Gender', values='Balance',aggfunc='mean')
                else: #job,gender,age_group,region  = value
                    filter_df = customer_df[
                        (customer_df['Job Classification'] == job) & (customer_df['Region'] == region)]
                    age_gender_df = filter_df.pivot_table(index='Age Group', columns='Gender', values='Balance',aggfunc='mean')
    fig3 = px.bar(age_gender_df,x=['Male','Female'],y=age_gender_df.index,labels={'value':'Average Balance','color':'Gender','variable':'Gender'},color_discrete_map={'Male': 'crimson', 'Female': 'pink'},text_auto='0.2s')
    fig3.update_layout()
    return fig3
#count of full name by job classification and gender
@callback(
    Output('namejobgender-stack','figure'),
    Input('job-dropdown','value'),
    Input('gender-dropdown','value'),
    Input('age-dropdown','value'),
    Input('region-dropdown','value')
)
def update_graph(job,gender,age_group,region):
    if job is None:
        if gender is None:
            if age_group is None:
                if region is None: #job,gender,age_group,region = None
                    name_job_df = customer_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #job,gender,age_group = None and region = value
                    filter_df = customer_df[customer_df['Region']==region]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
            else:
                if region is None: #job,gender,region = None and age_group = value
                    filter_df = customer_df[customer_df['Age Group']== age_group]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #job,gender = None and age_group,region = value
                    filter_df = customer_df[(customer_df['Age Group']== age_group) & (customer_df['Region']== region)]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
        else:
            if age_group is None:
                if region is None: #job,age_group,region = None and gender = value
                    name_job_df = customer_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #job,age_group = None and gender,region = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
            else:
                if region is None: #job,region = None and gender,age_group = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #job = None and gender,age_group,region = value
                    filter_df = customer_df[(customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
    else:
        if gender is None:
            if age_group is None:
                if region is None: #gender,age_group,region = none and job = value
                    name_job_df =  customer_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #gender,age_group= none and job,region  = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
            else:
                if region is None: #gender,region= none and job,age_group  = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #gender= none and job,age_group,region  = value
                    filter_df = customer_df[(customer_df['Age Group'] == age_group) & (customer_df['Region']==region)]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
        else:
            if age_group is None:
                if region is None: #age_group,region= none and job,gender  = value
                    name_job_df =  customer_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #age_group= none and job,gender,region  = value
                    filter_df = customer_df[customer_df['Region'] == region]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
            else:
                if region is None: #region= none and job,gender,age_group  = value
                    filter_df = customer_df[customer_df['Age Group'] == age_group]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
                else: #job,gender,age_group,region  = value
                    filter_df = customer_df[(customer_df['Age Group'] == age_group) & (customer_df['Region'] == region)]
                    name_job_df = filter_df.pivot_table(index='Job Classification',columns='Gender',values='Full Name',aggfunc='size')
    fig4 = px.bar(name_job_df,x=name_job_df.index,y=['Male','Female'],barmode='stack',color_discrete_map={'Male':'crimson','Female':'pink'},labels={'variable':'Gender','value':'Count'},text_auto=True)
    fig4.update_layout(
    yaxis_title = 'Count of Full Name',
    legend_title = 'Gender'
)
    return fig4
if __name__ == ('__main__'):
    app.run(debug=False)
