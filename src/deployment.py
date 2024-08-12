def deploy_model(model, platform='aws'):
    """Deploy the model to the specified cloud platform (AWS/GCP)."""
    if platform == 'aws':
        print("Deploying model to AWS...")
        # Code to deploy model on AWS
    elif platform == 'gcp':
        print("Deploying model to GCP...")
        # Code to deploy model on GCP
    else:
        print("Unsupported platform!")
