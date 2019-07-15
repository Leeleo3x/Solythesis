import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from utils import generate_tests

m = {}


def name_mapping(name):
    if "secured" in name:
        return "S"
    if "noopt" in name:
        return "S-N"
    return "O"


for i in range(6):
    for benchmark in generate_tests(i):
        name = benchmark[0] + benchmark[2]
        idx = name_mapping(name)
        if idx not in m:
            m[idx] = {}
        res = pd.read_csv("/data/{}/{}.txt".format(name, name), sep="\s+", header=None, dtype=np.float64, skiprows=1)
        res = res[[1]]
        m[idx][benchmark[2]] = np.mean(res)[0]


corder = ["erc20", "tran", "batchTransfer", "v", "erc721", "tran"]
rorder = ["S", "S-N", "O"]


for r in rorder:
    s = " & \\textbf{{}}".format(r)
    for c in corder:
        s += "& {}\\%".format(m[r][c])
    s += "\\\\"
    print(s)
