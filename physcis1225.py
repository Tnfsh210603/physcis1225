import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math


# Streamlit 標題
st.title("金屬板電磁阻尼探究")
st.text("這是一個針對阻尼震盪的模擬網站，透過使用者調整參數來生成軌跡圖，但不考慮震幅過大導致物體與銅板產生碰撞的情況。")


# 輸入
mass = st.slider('質量 (kg)', min_value=0.1, max_value=0.25, value=0.1, step=0.01)
amplitude = st.slider('原始震幅 (m)', min_value=0.01, max_value=0.1, value=0.01, step=0.01)
thickness = st.slider('銅板厚度 (mm)', min_value=2.0, max_value=10.0, value=2.0, step=0.1)
height = st.slider('高度 (m)', min_value=0.01, max_value=0.08, value=0.01, step=0.01)
spring_constant = st.slider('彈力常數 (N/m)', min_value=10, max_value=20, value=10, step=1)


# 數學計算
T = (2*math.pi*(mass/spring_constant)**0.5)  # 周期
k = 0.000002991722221
b = k * (height ** -3) * (mass ** -0.75) * (np.e ** (-0.263/thickness))


# 圖表生成
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_title('Y-T Plot')
ax.set_xlabel('Time(s)')
ax.set_ylabel('Displacement (m)')
ax.grid(True)


# 數據動態更新
time_values = np.linspace(0, 15, 1500)
displacement_values = amplitude * np.exp(-b * time_values) * np.cos(2 * np.pi * time_values / T)
ax.plot(time_values, displacement_values, label="Displacement")
ax.legend()


# 展示圖表
st.pyplot(fig)
