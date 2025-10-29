import numpy as np
import matplotlib.pyplot as plt

# 定義參數
a_P = 12  # 尖峰需求截距
b_P = 1   # 尖峰需求斜率
a_O = 8   # 離峰需求截距
b_O = 1   # 離峰需求斜率
c = 0
d = 0.8

# 建立價格區間
P = np.linspace(0, 15, 200)
Q = np.linspace(0, 15, 200)

# 尖峰與離峰需求曲線
D_P = a_P - b_P * P
D_O = a_O - b_O * P
S = c + d * P

# 畫圖
plt.figure(figsize=(10, 6))

# 畫需求曲線
plt.plot(P, D_P, label=r'Peak Demand: $Q_DP = a_P - b_PP$', color='lightblue',  linewidth=25)
plt.plot(P, D_O, label=r'Off-Peak Demand: $Q_DO = a_O - b_OP$', color='lightgreen',  linewidth=25)
plt.plot(P, S, label=r'Supply: $Q_S = c + dP$', color='red')

P_eq_p = (a_P - c) / (b_P + d)
Q_eq_p = a_P - b_P * P_eq_p

# 標註均衡點

plt.text(P_eq_p, Q_eq_p,
         rf'Peak Equilibrium Point.''\n'rf'($P_P^* = \frac{{a_P-c}}{{b_P+d}}$, $Q_P^* = a_P-b_PP^*$)',
         va='top', ha='left', fontsize=10)

P_eq_o = (a_O - c) / (b_O + d)
Q_eq_o = a_O - b_O * P_eq_o

plt.text(P_eq_o, Q_eq_o,
            rf'Off-Peak Equilibrium Point.''\n'rf'($P_O^* = \frac{{a_O-c}}{{b_O+d}}$, $Q_O^* = a_O-b_OP^*$)',
            va='bottom', ha='left', fontsize=10)

P_eq_avg = (P_eq_p + P_eq_o) / 2
Q_eq_avg = (Q_eq_p + Q_eq_o) / 2

# 畫供給價格水平線
plt.axvline(x=P_eq_avg, color='red', linestyle='--', label=r'Supply Price = $\frac{P_P^* + P_O^*}{2}$')

P_re_p = P_eq_avg
Q_re_p = a_P - b_P * P_re_p
plt.text(P_re_p, Q_re_p,
         rf'Peak Retail Point.''\n'r'($P_{RP}^* = \frac{{P_P^* + P_O^*}}{2}$, $Q_{RP}^* = a_P - b_PP_R^*$)',
         va='bottom', ha='left', fontsize=10)

P_re_o = P_eq_avg
Q_re_o = a_O - b_O * P_re_o
plt.text(P_re_o, Q_re_o,
         rf'Off-Peak Retail Point.''\n'r'($P_{RO}^* = \frac{{P_P^* + P_O^*}}{2}$, $Q_{RO}^* = a_O - b_OP_R^*$)',
         va='top', ha='left', fontsize=10)

# 依據Retail Point著色消費者剩餘與生產者剩餘區域

# Consumer Surplus (Peak), cut below the peak demand curve and above the peak retail price
# Consumer Surplus (Off-Peak), cut below the off-peak demand curve and above the off-peak retail price
plt.fill_between(P, D_P, S, where=(P <= P_re_p), color='lightblue', alpha=0.5, label='Consumer Surplus (Peak)')
plt.fill_between(P, D_O, S, where=(P <= P_re_o), color='lightgreen', alpha=0.5, label='Consumer Surplus (Off-Peak)')
# 標註
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Long Term Peak and Off-Peak Supply Demand Graph (Traditional Model)')
plt.legend()
plt.grid(True)
plt.xlim(0, 12)
plt.ylim(0, max(a_P, a_O))

# 刪除
plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)


# 刪除圖片白邊 (zero padding)
plt.subplots_adjust(left=0.03, right=0.99, top=0.95, bottom=0.03)


plt.show()
