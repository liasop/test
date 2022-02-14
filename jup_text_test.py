# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # jupytest test
# some text

import numpy as np
x = np.arange(0,100,2)

def my_fun(x):
    return x*2


y = my_fun(x)
y

z = np.arange(9,10)


