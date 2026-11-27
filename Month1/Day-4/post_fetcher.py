
import requests
import json

post_id = input("Enter post ID (1-100): ")

url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if "id" not in data:
            print("Post not found.")
        else:
            print("\nTitle:", data["title"])
            print("Body:", data["body"])

            with open("post.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\nPost saved successfully!")

    elif response.status_code == 404:
        print("Post not found.")

    else:
        print("API error:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)
