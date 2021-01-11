import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

pio.renderers.default = "browser"  # <- determines how plots are displayed using Plotly

import payments2

df = (payments2.do_rollup()
      .sort_values("date", ascending=False)
      .assign(date=lambda x: x.date.dt.date,
              winnings=lambda x: x.profit.apply(lambda i: f"${i:.2f}"),
              overall=lambda x: x.total.apply(lambda i: f"${i:.2f}"),
              ))

people = {"Alex": "blue",
          "Britt": "orange",
          "Colin": "green",
          "Danny": "red",
          "Matthew": "purple",
          "Michael": "darkred",
          "Tucker": "pink",
          "Zach": "gray"}

fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.1,
    specs=[[{"type": "scatter"}],
           [{"type": "table"}]]
)

for name, my_df in df.groupby("name"):
    fig.append_trace(go.Scatter(x=my_df["date"], y=my_df["total"], name=name,
                                mode='lines+markers', line=dict(color=people[name])),
                     row=1, col=1)

#fig.update_layout(yaxis_range=[-500,500], row=1, col=1)
fig.update_yaxes(range=[-500,500], row=1, col=1)


fig.add_trace(
    go.Table(
        header=dict(
            values=["Date", "Name", "Winnings", "Overall"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df[k].tolist() for k in ["date", "name", "winnings", "overall"]],
            align="left")
    ),
    row=2, col=1
)
fig.update_layout(
    height=800,
    title_text="Poker results",
)

pio.write_html(fig, file='index.html', auto_open=True)
