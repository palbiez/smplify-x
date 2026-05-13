import numpy as np

path = r"C:\Users\firew\Documents\python_scripts\openpose_pipeline\dataset\smplx\SMPLX_FEMALE.npz"
data = np.load(path, allow_pickle=True)
print(sorted(list(data.keys()))[:50])
print("hands_componentsl" in data.keys(), "hands_componentsr" in data.keys())