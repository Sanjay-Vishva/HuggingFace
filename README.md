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

You have two options to use this project: either build the Docker image locally from the source code or pull the pre-built image from Docker Hub.

### Option 1: Build the Docker Image Locally

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

### Option 2: Pull the Docker Image from Docker Hub

1. **Pull the Docker image:**
    ```sh
    docker pull sanjayvishva/huggingface-report
    ```

2. **Run the Docker container:**
    ```sh
    mkdir -p $(pwd)/report
    docker run --rm -v $(pwd)/report:/report sanjayvishva/huggingface-report
    ```

    This command will:
    - Run the container from the `sanjayvishva/huggingface-report` image.
    - Mount the `report` directory from the current working directory to `/report` inside the container.
    - Generate the report and save it to the `report` directory on the host machine.
    - Automatically remove the container after it stops.

### Check the Report

After running the container, the report will be saved in the `report` directory as `top_10_models.txt`.

## Files

- `Dockerfile`: Instructions to build the Docker image.
- `report.py`: Script to fetch data from Hugging Face and generate the report.
- `README.md`: This file.
