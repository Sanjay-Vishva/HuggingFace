import requests

def fetch_data():
    response = requests.get("https://huggingface.co/api/models?sort=downloads")
    models = response.json()
    top_10_models = models[:10]
    return top_10_models

def generate_report():
    top_10_models = fetch_data()
    with open('/report/top_10_models.txt', 'w') as file:
        for model in top_10_models:
            file.write(f"{model['modelId']}: {model['downloads']}\n")

if __name__ == "__main__":
    generate_report()
