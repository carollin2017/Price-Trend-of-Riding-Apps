import pandas as pd
import plotly.express as px

def price_when_rains(df_rain, uber='UberPool', lyft='Shared'):
    
    cond_distance = df_rain['distance'].isin([0.5, 1, 1.5, 2, 2.5, 3])
    df_data = df_rain[cond_distance]

    cond_uber = df_data['name'] == uber
    cond_lyft = df_data['name'] == lyft

    df_data = df_data[cond_uber | cond_lyft]
    df_data = df_data.sort_values(by='distance')

    fig = px.scatter(df_data, x="source_rain", y="price", color="cab_type", hover_data=['distance', 'name'], 
                 animation_frame = 'distance', color_discrete_map={'Lyft': '#FF00BF','Uber':'#000000'},
                 range_y=[0,30], labels={"source_rain": "Amount of rainfall per day (inches)"})
    fig["layout"].pop("updatemenus")
    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
    },font_color="#FFFFFF",)

    return fig

def amount_rides_in_rain(df_rain, uber='UberPool', lyft='Shared'):
    cond_uber = df_rain['name'] == uber
    cond_lyft = df_rain['name'] == lyft
    df_rain = df_rain[cond_uber | cond_lyft]
    df_rides_rain = df_rain.groupby(['cab_type', 'date']).size().reset_index()
    df_rides_rain = df_rides_rain.rename(columns={0: "amount"}) 

    fig = px.bar(df_rides_rain, 
                 x='cab_type', y='amount', 
                 color = 'cab_type',
                 color_discrete_map={'Lyft': '#FF00BF','Uber':'#000000'},
                 animation_frame = 'date'
                )
    fig["layout"].pop("updatemenus")
    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
    },font_color="#FFFFFF")
    
    return fig