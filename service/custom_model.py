import os
import sys
import logging
from pathlib import Path
from typing import List, Self
from dataclasses import dataclass

import pandas as pd
from pandas import DataFrame, Series
import tensorflow as tf

class CustomDataPreparations:
    def __init__(self, data: DataFrame | Series, is_generate: bool) -> None:
        super(CustomDataPreparations, self).__init__()
        self.data = data
        self.is_generate = is_generate
        
    def __initial_data(self) -> DataFrame:
        PATH = Path.absolute() + "data/"
        df = pd.read_csv()
        
        return df
    
    def header_to_class(self) -> None:
        return self.data
    
    
class ClaimModel(tf.keras.Model):
    # CLASSES = CustomDataPreparations().header_to_class
    def __init__(self):
        super(ClaimModel, self).__init__()
        self._conv1a = tf.keras.layers.Conv2D(kernel_size=3, filters=16, padding='same', activation='relu')
        self._conv1b = tf.keras.layers.Conv2D(kernel_size=3, filters=30, padding='same', activation='relu')
        self._maxpool1 = tf.keras.layers.MaxPooling2D(pool_size=2)
        self._pooling = tf.keras.layers.GlobalAveragePooling2D()
        self._classifier = tf.keras.layers.Dense(self.CLASSES, activation='softmax')
        

@tf.function
def apply_gradient(optimizer, loss_object, model, x, y):
    with tf.GradientTape() as tape:
        logits = model(x)
        loss_value = loss_object(y_true=y, y_pred=logits)
  
    gradients = tape.gradient(loss_value, model.trainable_weights)
    optimizer.apply_gradients(zip(gradients, model.trainable_weights))

    return logits, loss_value