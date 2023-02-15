import argparse
import os
import requests


def openai_request(
    prompt,
    openai_secret_key,
    max_tokens=100,
    temp=0.5,
    model="text-davinci-003",
    url="https://api.openai.com/v1/completions",
    n=1,
    top_p=None,
    stop=None,
):
    headers = {"Authorization": f"Bearer {openai_secret_key}"}

    json_data = {
        "model": model,
        "prompt": prompt,
        "temperature": temp,
        "max_tokens": max_tokens,
        "n": n,
    }
    if temp is not None:
        json_data["temperature"] = temp
    if top_p is not None:
        json_data["top_p"] = top_p
    if stop is not None:
        json_data["stop"] = stop

    response = requests.post(url, headers=headers, json=json_data)
    return response


if __name__ == "__main__":
    oai_key = os.environ.get("OAI_SECRET_KEY")
    if oai_key is None:
        print("ERROR: Environment variable OAI_SECRET_KEY is not set!")
        print("You can sign up for an OpenAI API key at https://openai.com/api/")
        print("Then run `export OAI_SECRET_KEY='xxx'` before running yo again :)")
        exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default=None)
    parser.add_argument("--N", type=int, default=1)
    args = parser.parse_args()
    # e.g.: "find all files whose filename contains the string 'good' and size is less than 1mb"
    if not len(args.query):
        print("No query provided")
        exit(0)
    prompt = f"Hi, what command should I run in terminal to list all files in current dir that are 30mb or larger?\n\n Try this:\n```find . -size +30M\n```"
    prompt += f"\nHi, what command should I run in terminal to {args.query}?\n\nThis command should do it:\n```\n"
    response = openai_request(prompt, oai_key, n=args.N, stop="```")
    resp_json = response.json()
    try:
        texts = [i["text"] for i in resp_json["choices"]]
    except Exception as e:
        print(f"response from OpenAI:\n{resp_json}")
        raise e
    print()
    plural = "s" if args.N > 1 else ""
    print(f"Suggested command{plural}:\n")
    for text in texts:
        print(text.strip("\n"))
        print()
