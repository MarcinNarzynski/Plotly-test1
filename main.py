import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import kaleido


def calculate_relative_value(input_data: dict[str: list]):
    data_as_list = input_data["performance"]
    result = []
    for elem in data_as_list:
        result.append(round(100 * elem / data_as_list[-1] if data_as_list[-1] != 0 else 0, ndigits=1))

    return {"performance [%]": result,
            "build": input_data["build"]}


def main():


    # Constructing DataFrame from a dictionary including Series:
    #
    # >>> d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    # >>> pd.DataFrame(data=d, index=[0, 1, 2, 3])
    #    col1  col2
    # 0     0   NaN
    # 1     1   NaN
    # 2     2   2.0
    # 3     3   3.0

    my_data = {"performance": [10, 11, 13, 12, 10, 8, 7, 8, 10, 9],
               "build": ["1.1.10", "1.1.11", "1.1.12", "1.1.13", "1.1.14", "1.1.15", "1.1.16", "1.1.17", "1.2.0", "1.2.1"]}
    processed_data = calculate_relative_value(my_data)
    prepared_data = pd.DataFrame(data=processed_data)
    fig = px.line(prepared_data, x="build", y="performance [%]", title='Performance changes', text="performance [%]",
                  labels={"performance [%]": "performance [%]", "build": "build no"})

    fig.update_traces(
        textposition="bottom right",
        line=dict(color='#4A4', width=1, dash='dot'),
        marker=dict(size=10, line=dict(width=1, color='#222')),
        textfont=dict(size=12, color='#000')
    )

    fig.update_layout(
        margin=dict(l=0, r=5, t=25, b=0),
        paper_bgcolor="LightSteelBlue",
        title_font_size=13,
        autosize=True,
    )

    # fig.show()


    # my_data = px.data.stocks()
    # px.line(my_data, x='AAPL', labels={'x': 'AAPL', 'y': '???'}, title='Mój tytuł')
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=my_data.date, y=my_data.AAPL))

    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=prepared_data, y="col1"))

    # fig.update_layout(
    #     xaxis=dict(
    #         showline=True,
    #         showgrid=False,
    #         showticklabels=True,
    #         linecolor='rgb(204, 204, 204)',
    #         linewidth=2,
    #         ticks='outside',
    #         tickfont=dict(
    #             family='Arial',
    #             size=10,
    #             color='rgb(82, 82, 82)',
    #         ),
    #
    #     ),
    #     yaxis=dict(
    #         showline=False,
    #         showgrid=False,
    #         showticklabels=False,
    #         zeroline=False
    #     ),
    #     autosize=False,
    #     margin=dict(
    #         autoexpand=False,
    #         l=100,
    #         r=20,
    #         t=110,
    #     ),
    #     showlegend=False,
    #     plot_bgcolor='white',
    #     title="Marcin",
    #     titlefont=dict(
    #             family='Arial',
    #             size=16,
    #             color='rgb(82, 82, 82)',
    #         ),
    # )

    print("Generating html...")

    with open("Result.html", "wt") as file:
        file.write(fig.to_html())

    # print("Generating image...")
    #
    # image = fig.to_image(
    #     format='svg',
    #     width=600,
    #     height=480
    # )
    #
    # with open("Result.svg", "wb") as file:
    #     file.write(image)


if __name__ == '__main__':
    main()
