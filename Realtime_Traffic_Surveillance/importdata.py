# !pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Mo9c2Rg6ODta4k7MqF3H")
project = rf.workspace("bike-helmets").project("bike-helmet-detection-2vdjo")
version = project.version(2)
dataset = version.download("yolo26")


#also add local data/custom data for realtime accuracy
                