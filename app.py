import joblib
from flask import Flask, reques, app, jsonify, url_for, render_template
import tensorflow
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

app=Flask(_name_)