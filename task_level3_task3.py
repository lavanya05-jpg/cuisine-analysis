import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\lavanya\Downloads\cuisine_analysis\dataset.csv")

# ── Part 1: Price Range vs Online Delivery & Table Booking ──
delivery_by_price = df.groupby("Price range")["Has Online delivery"].apply(
    lambda x: (x == "Yes").sum() / len(x) * 100
)

booking_by_price = df.groupby("Price range")["Has Table booking"].apply(
    lambda x: (x == "Yes").sum() / len(x) * 100
)

print("Online Delivery % by Price Range:")
print(delivery_by_price)

print("\nTable Booking % by Price Range:")
print(booking_by_price)

# ── Part 2: Bar Chart ──
x = delivery_by_price.index
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
bars1 = ax.bar(x - width/2, delivery_by_price.values, width, label="Online Delivery", color="steelblue")
bars2 = ax.bar(x + width/2, booking_by_price.values, width, label="Table Booking", color="orange")

ax.set_xlabel("Price Range (1=Cheap, 4=Expensive)")
ax.set_ylabel("Percentage (%)")
ax.set_title("Price Range vs Online Delivery & Table Booking")
ax.set_xticks(x)
ax.legend()

plt.tight_layout()
plt.savefig(r"C:\Users\lavanya\Downloads\cuisine_analysis\price_vs_services.png")
plt.show()

print("\nChart saved as price_vs_services.png")