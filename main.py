import os
from typing import List


import streamlit as st
import pandas as pd
import tensorflow as tf

# os.environ["TF_MIN_GPU_MULTIPROCESSOR_COUNT"] = "0"

# check the GPU Precense, if this running CPU-Based, there will be some warning
strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

# @tf.function
# def apply_gradient(optimizer, loss_object, model, x, y):
#     with tf.GradientTape() as tape:
#         logits = model(x)
#         loss_value = loss_object(y_true=y, y_pred=logits)
  
#     gradients = tape.gradient(loss_value, model.trainable_weights)
#     optimizer.apply_gradients(zip(gradients, model.trainable_weights))

#     return logits, loss_value

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))