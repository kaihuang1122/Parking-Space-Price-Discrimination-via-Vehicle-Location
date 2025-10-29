import numpy as np
import matplotlib.pyplot as plt

# 定義參數
a_P = 12  # 尖峰需求截距
b_P = 1   # 尖峰需求斜率
a_O = 8   # 離峰需求截距
b_O = 1   # 離峰需求斜率
c = 0
d = 0.8

# 建立需求與供給的數量區間
Q = np.linspace(0, 15, 200)

# 反求價格函數
P_Dp = (a_P - Q) / b_P   # Peak demand 反函數 P(Q) = (a_P - Q) / b_P
P_Do = (a_O - Q) / b_O   # Off-peak demand 反函數 P(Q) = (a_O - Q) / b_O
P_S = (Q - c) / d        # Supply 反函數 P(Q) = (Q - c) / d

# 計算均衡點
# 原本的均衡價格與數量
P_eq_p = (a_P - c) / (b_P + d)
Q_eq_p = a_P - b_P * P_eq_p

P_eq_o = (a_O - c) / (b_O + d)
Q_eq_o = a_O - b_O * P_eq_o

# 繪圖
plt.figure(figsize=(10, 6))

# 畫需求與供給曲線（價格在縱軸，數量在橫軸）
plt.plot(Q, P_Dp, label='Peak Demand: $P = \\frac{a_P - Q}{b_P}$', color='lightblue', linewidth=25)
plt.plot(Q, P_Do, label='Off-Peak Demand: $P = \\frac{a_O - Q}{b_O}$', color='lightgreen', linewidth=25)
plt.plot(Q, P_S,  label='Supply: $P = \\frac{Q - c}{d}$', color='red')

# 標註均衡點
plt.scatter([Q_eq_p], [P_eq_p], color='blue')
plt.text(Q_eq_p, P_eq_p,
         rf'Peak Equilibrium Point.''\n'rf'($P_P^* = \frac{{a_P-c}}{{b_P+d}}$, $Q_P^* = a_P-b_PP^*$)',
         va='bottom', ha='right', fontsize=10)

plt.scatter([Q_eq_o], [P_eq_o], color='green')
plt.text(Q_eq_o, P_eq_o,
         rf'Off-Peak Equilibrium Point.''\n'rf'($P_O^* = \frac{{a_O-c}}{{b_O+d}}$, $Q_O^* = a_O-b_OP^*$)',
         va='top', ha='left', fontsize=10)

P_eq_avg = (P_eq_p + P_eq_o) / 2
Q_eq_avg = (Q_eq_p + Q_eq_o) / 2

# 畫供給價格水平線
plt.axhline(y=P_eq_avg, color='red', linestyle='--', label=r'Supply Price = $\frac{P_P^* + P_O^*}{2}$')

P_re_p = P_eq_avg
Q_re_p = a_P - b_P * P_re_p
plt.scatter([Q_re_p], [P_re_p], color='blue')
plt.text(Q_re_p, P_re_p,
         rf'Peak Retail Point.''\n'r'($P_{RP}^* = \frac{{P_P^* + P_O^*}}{2}$, $Q_{RP}^* = a_P - b_PP_R^*$)',
         va='bottom', ha='left', fontsize=10)

P_re_o = P_eq_avg
Q_re_o = a_O - b_O * P_re_o
plt.scatter([Q_re_o], [P_re_o], color='green')
plt.text(Q_re_o, P_re_o,
         rf'Off-Peak Retail Point.''\n'r'($P_{RO}^* = \frac{{P_P^* + P_O^*}}{2}$, $Q_{RO}^* = a_O - b_OP_R^*$)',
         va='top', ha='right', fontsize=10)


# # 畫零網格線，用於零刻度
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)

# 填充消費者剩餘區域（峰時與離峰分開）
# 峰時：需求曲線之上、均衡價之上，從 Q=0 到 Q_eq_p
plt.fill_between(Q, P_Dp, P_eq_avg, where=(Q <= Q_eq_avg) & (P_Dp >= P_eq_p),
                 color='lightblue', hatch = '\\\\', alpha=0.7, label='Consumer Surplus (Peak)')
# 離峰：需求曲線之上、均衡價之上，從 Q=0 到 Q_eq_o
plt.fill_between(Q, P_Do, P_eq_avg, where=(Q <= Q_eq_avg) & (P_Do >= P_eq_avg),
                 color='green', hatch = '//', alpha=0.3, label='Consumer Surplus (Off-Peak)')

# 填充生產者剩餘區域
# 生產者剩餘峰時：供給曲線之下、均衡價之下，從 Q=0 到 Q_eq_avg
plt.fill_between(Q, P_S, P_eq_avg, where=(Q <= Q_eq_avg) & (P_S <= P_eq_avg),
                 color='lightcoral', hatch = '\\\\', alpha=0.5, label='Producer Surplus (Peak)')
# 生產者剩餘離峰：供給曲線之下、均衡價之下，從 Q=0 到 Q_eq_avg
plt.fill_between(Q, P_S, P_eq_avg, where=(Q <= Q_re_o) & (P_S <= P_re_o),
                 color='orange', hatch = '//', alpha=0.5, label='Producer Surplus (Off-Peak)')


# 標籤與圖片設定
plt.xlabel('Quantity (Q)')
plt.ylabel('Price (P)')
plt.title('Supply and Demand (Price on Vertical Axis)')
plt.xlim(0, 10)
plt.ylim(0, max(a_P, a_O) + 1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend( loc='upper right')

# 移除多餘刻度（如果不需要顯示刻度）
plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# 去除白邊
plt.subplots_adjust(left=0.03, right=0.99, top=0.95, bottom=0.03)

plt.show()
