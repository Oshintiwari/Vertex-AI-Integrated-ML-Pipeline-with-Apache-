from google.cloud import aiplatform
import json

# Load Vertex AI configuration
with open('config/vertex_ai_config.json', 'r') as config_file:
    vertex_config = json.load(config_file)

def train_and_deploy_model():
    aiplatform.init(
        project=vertex_config["project_id"],
        location=vertex_config["region"]
    )

    # Create and run training job
    training_job = aiplatform.CustomJob(
        display_name=vertex_config["training_job_name"],
        script_path=vertex_config["training_script"],
        container_uri=vertex_config["container_uri"],
        args=vertex_config["training_args"]
    )

    model = training_job.run(sync=True)

    # Deploy the model
    endpoint = model.deploy(
        machine_type=vertex_config["deployment_machine_type"]
    )

    print(f"Model deployed to endpoint: {endpoint.resource_name}")
