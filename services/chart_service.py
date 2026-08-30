import os
import matplotlib.pyplot as plt

def generate_chart(scores):
    os.makedirs('outputs/charts', exist_ok=True)
    if not scores:
        return None
    labels=list(scores.keys())
    values=list(scores.values())
    plt.figure(figsize=(8,4))
    plt.bar(labels, values)
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    path='outputs/charts/chart.png'
    plt.savefig(path)
    plt.close()
    return path