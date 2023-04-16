# Predicting APS Failures in Scania Trucks using Machine Learning

This project uses machine learning to predict APS (Air Pressure System) failures in Scania trucks. It provides an end-to-end solution that covers all aspects of the machine learning workflow, from data preparation to model deployment. The project is deployed on AWS using Docker, and implements a CI/CD pipeline and MLOps to automate and streamline the workflow. Additionally, GitHub Actions is used to automate the deployment process.

## Deployment

The project is deployed on AWS using Docker. The Docker image is stored in an ECR (Elastic Container Registry) repository. The deployment is fully automated using a CI/CD pipeline.

## Docker

Docker is used to create a containerized version of the project that can be easily deployed and run on any machine. The Docker container includes all the necessary dependencies and libraries needed to run the project.

## CI/CD Pipeline

A CI/CD (Continuous Integration/Continuous Deployment) pipeline is used to automate the building, testing, and deployment of the project. The pipeline is triggered automatically when new changes are pushed to the project's GitHub repository. The pipeline includes steps for building the Docker image, running tests, and deploying the image to the ECR repository.

## MLOps

MLOps is used to automate and streamline the machine learning workflow. The project uses Airflow to schedule batch predictions and training pipelines. The trained model is stored in an S3 bucket.

## Dataset
The dataset used in this project is the APS Failure at Scania Trucks dataset, which contains data on air pressure system failures in Scania trucks. The dataset was sourced from the UCI Machine Learning Repository and can be found at the following link: https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks.

The dataset includes various sensor readings and operational parameters for each truck, as well as a binary classification of whether or not the truck experienced an air pressure system (APS) failure during testing. The goal of this project is to use machine learning techniques to predict APS failures in Scania trucks based on these sensor readings and parameters.

## Environment Variables

The following environment variables are required to run the project:

- `AWS_ACCESS_KEY_ID`: The AWS access key ID for your AWS account.
- `AWS_SECRET_ACCESS_KEY`: The AWS secret access key for your AWS account.
- `AWS_REGION`: The AWS region where you will be deploying your application.
- `AWS_ECR_LOGIN_URI`: The URI used to login to the Elastic Container Registry.
- `ECR_REPOSITORY_NAME`: The name of the Elastic Container Registry repository where the Docker image will be pushed.
- `BUCKET_NAME`: The name of the S3 bucket where the trained model and prediction results will be stored.
- `MONGO_DB_URL`: The URL of the MongoDB database used in the project.


## Installation

To install and run the project, follow these steps:

1. Clone the GitHub repository to your local machine
```bash
git clone https://github.com/skprasad117/Predicting-APS-Failures-in-Scania-Trucks-using-Machine-Learning.git
```
2. Set the required environment variables
3. Install all requirements
```bash
pip install -r requirements.txt
```
4. Run main.py file
```bash
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

