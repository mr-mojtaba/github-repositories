# Need to install ( pip install requests )
import requests


# ---------- Function ----------

def get_trending_repositories(language, num_repositories):

    repositories = []
    page = 1

    while len(repositories) < num_repositories:
        url = f"https://github.com/search?q={language}&type=repositories&s=stars&o=desc&p={page}"
        response = requests.get(url)

        if response.status_code == 200:

            # Converting the responses to JSON.
            data = response.json()

            # Taking elements from the response.
            page_repositories = data["payload"]["results"]

            # Adding the elements to the list.
            repositories.extend(page_repositories)

            page += 1
        else:
            print("Error!")
            return []
    return repositories[:num_repositories]


# ---------- Inputs ----------

language = input("Enter language: ")
num_repositories = int(input("Number of repositories: "))


# ---------- Main condition ----------

# Variable to store the collected repositories.
repositories = get_trending_repositories(language, num_repositories)

if repositories:
    output = f"trending_{language}_repositories.txt"

    with open(output, mode="w", encoding="utf-8") as file:
        file.write(f"Top {num_repositories} {language} repositories on GitHub:\n")
        file.write(50 * "*")
        file.write(f"\n")
        for i, repo in enumerate(repositories, start=1):
            file.write(f"#{i} {repo['hl_name']} - {repo['hl_trunc_description']}\n"
                       f"URL: https://github.com/{repo['repo']['repository']['owner_login']}"
                       f"/{repo['repo']['repository']['name']}\n")
            file.write(50 * "-")
            file.write("\n")
        print(f"Result saved to {output}")
else:
    print("No repositories found!")
