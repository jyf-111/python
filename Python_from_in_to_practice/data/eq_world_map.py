import plotly.express as px
from eq_explore_data import lons,lats 

fig = px.scatter(
    x = lons,
    y = lats,
    labels={"x":"经度","y":"维度"},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title="全球地震散点图",
)

fig.write_html("Python_from_in_to_practice/data/golbal_earthquakes.html")
fig.show()
