try:
    tala = int(input("Sláðu inn heiltölu: "))
    print("Þetta var heiltala. Takk.")
except ValueError:
    print("Þetta var ekki heiltala.")
