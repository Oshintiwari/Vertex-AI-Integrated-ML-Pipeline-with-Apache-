from beam_pipeline import run_beam_pipeline
from vertex_ai_integration import train_and_deploy_model

if __name__ == "__main__":
    # Run the Apache Beam pipeline
    run_beam_pipeline()
    
    # Train and deploy the model on Vertex AI
    train_and_deploy_model()
