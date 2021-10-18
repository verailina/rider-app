import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

from rider.files import trackpoints
from rider.routes import get_trips_and_routes
from rider.plotting import plot_one


def generate_random_df(n=3) -> pd.DataFrame:
    dfs = []
    np.random.seed(10)
    def random_track(size):
        track = [(50, 50)]
        for delta in np.random.uniform(-0.5, 1., (size, 2)):
            track.append(track[-1] + delta)
        return track

    for i in range(n):
        df = pd.DataFrame(random_track(300),
                          columns=list(["lon", "lat"]))

        df["date"] = f"2021-01-0{i}"
        df["car"] = f"car{i}"
        df["time"] = 123
        dfs.append(df)
    return pd.concat(dfs, keys=[f"track_{i}" for i in range(n)])


st.title("Треки поездок")

#points_df = pd.DataFrame.from_records(trackpoints("data"))
points_df = generate_random_df()


trips, routes = get_trips_and_routes(points_df)
first_track = st.selectbox("Выберите трек",
                           [f"track_{i}" for i in range(len(routes))])

track_df = points_df.loc[first_track]
track_df["track"] = first_track
st.write(track_df)
st.write(px.scatter(routes[int(first_track[-1])], x="lon", y="lat"))
#st.write(plot_one(routes[int(first_track[-1])]))


