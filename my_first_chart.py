import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic" 
 # 윈도우는 Malgun Gothic
w = [17,15,6,6,10,9,13]
d = ["월","화","수","목","금","토","일"]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(d,w)

for i, p in enumerate(w):
    ax.annotate(
        f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 2.5), ha="center"
    )
ax.set_title("이번 주 최저 기온")
fig.savefig("my_first_chart.png")
