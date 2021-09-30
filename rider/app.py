import streamlit as st
import pandas as pd
import numpy as np

from rider.files import trackpoints
from rider.routes import get_trips_and_routes
from rider.plotting import plot_one


def generate_random_df(n=3) -> pd.DataFrame:
    dfs = []

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
    return pd.concat(dfs)


st.title("Треки поездок")

#points_df = pd.DataFrame.from_records(trackpoints("data"))
points_df = generate_random_df()
st.write(points_df.head())

trips, routes = get_trips_and_routes(points_df)
first_track = st.selectbox("Выберите трек",
                           [str(int(i)) for i in range(len(routes))])

st.write(plot_one(routes[int(first_track)]))


