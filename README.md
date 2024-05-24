# Hugging Face Model Report Generator

This project creates a Docker container that fetches data from the Hugging Face model hub, compiles a list of the top 10 downloaded models, and generates a report. The container is designed to be easily downloadable and runnable on a Linux machine.

## Features

- Fetches data from Hugging Face API.
- Compiles a list of the top 10 downloaded models.
- Generates a report and saves it to the host machine.
- Automatically stops and removes the container after generating the report.

## Prerequisites

- Docker installed on your machine.

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/huggingface-report-generator.git
    cd huggingface-report-generator
    ```

2. **Build the Docker image:**
    ```sh
    docker build -t huggingface-report .
    ```

3. **Run the Docker container:**
    ```sh
    mkdir -p $(pwd)/report
    docker run --rm -v $(pwd)/report:/report huggingface-report
    ```

    This command will:
    - Run the container from the `huggingface-report` image.
    - Mount the `report` directory from the current working directory to `/report` inside the container.
    - Generate the report and save it to the `report` directory on the host machine.
    - Automatically remove the container after it stops.

4. **Check the report:**
    The report will be saved in the `report` directory as `top_10_models.txt`.

## Files

- `Dockerfile`: Instructions to build the Docker image.
- `report.py`: Script to fetch data from Hugging Face and generate the report.
- `README.md`: This file.
