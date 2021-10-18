# %%
# for stand-alone streamlit app - you will need
# "src/rider/data/v2a" folder for data
# and rider/files.py and rider/traks.py
from rider.files import gzip_filepaths, make_folder_path, read_json_from_gzip
from rider.tracks import track, draw

# %%
folder = make_folder_path(
    "src/rider/data/v2a", "5032b697-1a47-11e5-be74-00155dc6002b", 2021, 5, 24
)
for path in gzip_filepaths(folder):
    ride_json = read_json_from_gzip(path)
    # this is ride route, or "track"
    t = track(ride_json)
    # this is ride unique identifier
    n = ride_json["meta"]["external_order_id"]
    # does not draw in script
    # usually invoked as draw([t1, t1]) to draw two plots
    draw([t])
    print(n)
