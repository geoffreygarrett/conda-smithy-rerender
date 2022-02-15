import os
import \
    requests  # noqa We are just importing this to prove the dependency installed correctly
import sys

def main():
    github_token = os.environ["INPUT_WORKFLOW_GITHUB_TOKEN"]
    feedstock_url = os.environ["INPUT_FEEDSTOCK_URL"]
    modified_url = "/".join(feedstock_url.split("/")[-3:])

    result_code = ...
    run_url = ("${{ github.server_url }}/" +
               "${{ github.repository }}/" +
               "actions/runs/${{ github.run_id }}")

    # use git to clone the feedstock url
    REMOTE_URL = f'https://{github_token}:${{ github.actor }}@{modified_url}'

    print(f"::set-output name=result_code::{result_code}")
    print(f"::set-output name=run_url::{run_url}")
    print(f"::set-output name=modified_url::{modified_url}")


if __name__ == "__main__":
    main()
