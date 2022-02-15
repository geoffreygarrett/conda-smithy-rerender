import os
import \
    requests  # noqa We are just importing this to prove the dependency installed correctly
import sys


def main():
    github_token = os.environ["INPUT_WORKFLOW_GITHUB_TOKEN"]
    feedstock_url = os.environ["INPUT_FEEDSTOCK_URL"]
    modified_url = "/".join(feedstock_url.split("/")[-3:])

    result_code = 0

    GITHUB_RUN_ID = os.environ["GITHUB_RUN_ID"]
    GITHUB_SERVER_URL = os.environ["GITHUB_SERVER_URL"]
    GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]
    run_url = (f"{GITHUB_SERVER_URL}/" +
               f"{GITHUB_REPOSITORY}/" +
               f"actions/runs/{GITHUB_RUN_ID}")

    GITHUB_ACTOR = os.environ["GITHUB_ACTOR"]

    # use git to clone the feedstock url
    REMOTE_URL = f'https://{github_token}:{GITHUB_ACTOR}@{modified_url}'

    print(f"::set-output name=result_code::{result_code}")
    print(f"::set-output name=run_url::{run_url}")
    print(f"::set-output name=modified_url::{modified_url}")


if __name__ == "__main__":
    main()
