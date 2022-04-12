import importlib.util
import os
import re
import sys

import streamlit as st

fake_module_count = 0


# Functions
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(data, key=alphanum_key)


def load_module(filepath):
    """
    Create module from filepath and put in sys.modules, so Streamlit knows to watch it for changes.

    :param filepath:
    :return:
    """

    global fake_module_count

    modulename = "_dont_care_%s" % fake_module_count
    spec = importlib.util.spec_from_file_location(modulename, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[modulename] = module

    fake_module_count += 1


# Parse command-line arguments.
if len(sys.argv) > 1:
    folder = os.path.abspath(sys.argv[1])
else:
    folder = os.path.abspath(os.getcwd())


# Get the day to app path mapping.
sub_folders = [f for f in os.scandir(folder) if f.is_dir() and "day" in f.name]  # Get only the day folders

day_app = {}  # Dictionary of day number to app.

# Loop through the sub folders and get the day number and app.
for sub_folder in sub_folders:
    for file in os.listdir(sub_folder.path):
        if file.endswith(".py"):
            day_app[sub_folder.name.replace("_", " ").title()] = os.path.join(sub_folder.path, file)

# Make a UI to run different files.
file_name_to_run = st.sidebar.selectbox("Select an app", sorted_alphanumeric(day_app.keys()))


# Run the selected file.
with open(day_app[file_name_to_run]) as f:
    load_module(day_app[file_name_to_run])
    file_body = f.read()

exec(file_body, {})
