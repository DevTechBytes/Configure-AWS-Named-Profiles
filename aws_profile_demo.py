import boto3

aws_profile = 'bedrock-user-profile'

session = boto3.Session(profile_name=aws_profile)
bedrock_client = session.client('bedrock')

models = bedrock_client.list_foundation_models(byOutputModality='TEXT')

def get_models():
    models = bedrock_client.list_foundation_models(byOutputModality='TEXT')

    return models

def load_model_options():
    available_models = get_models()
    
    models = []
    for model in available_models['modelSummaries']:
        model_Id = model['modelId'].split(":")

        if model_Id[0] not in models:
            models.append(model_Id[0])

    return models

print(load_model_options())