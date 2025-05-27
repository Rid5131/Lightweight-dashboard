import streamlit as st
import pandas as pd
from streamlit_lightweight_charts import renderLightweightCharts

def plot_candlestick_chart_lightweight(df):
    # Convert 'timestamp' to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True)

    # Prepare chart data
    chart_data = [
        {
            "time": int(row["timestamp"].timestamp()),
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"])
        }
        for _, row in df.iterrows()
    ]

    # Prepare markers if 'direction' column exists
    markers = []
    if "direction" in df.columns:
        for _, row in df.iterrows():
            signal = str(row["direction"]).strip().upper()
            marker = {
                "time": int(row["timestamp"].timestamp()),
                "position": "belowBar" if signal == "LONG" else "aboveBar" if signal == "SHORT" else "inBar",
                "color": "green" if signal == "LONG" else "red" if signal == "SHORT" else "yellow",
                "shape": "arrowDown" if signal == "LONG" else "arrowUp" if signal == "SHORT" else "circle",
                "text": signal
            }
            markers.append(marker)

    # Define chart options
    chart_options = {
        "width": 700,
        "height": 400,
        "layout": {
            "background": {
                "type": "solid",
                "color": "white"
            },
            "textColor": "black"
        },
        "grid": {
            "vertLines": {
                "color": "rgba(197, 203, 206, 0.5)"
            },
            "horzLines": {
                "color": "rgba(197, 203, 206, 0.5)"
            }
        },
        "timeScale": {
            "borderColor": "rgba(197, 203, 206, 0.8)"
        }
    }

    # Define series
    series = [{
        "type": "Candlestick",
        "data": chart_data,
        "markers": markers
    }]

    # Render chart
    renderLightweightCharts([{
        "chart": chart_options,
        "series": series
    }])

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("TSLA Candlestick Chart")
    


    data_path = "C:/New folder/NEW/data/TSLA_data - Sheet1.csv"
    df = pd.read_csv(data_path)

    # Drop rows with missing data
    df = df.dropna(subset=["timestamp", "open", "high", "low", "close"])

    plot_candlestick_chart_lightweight(df)


