# Setting up AWS Named Profiles

This repo is contains the commands ran in the following YouTube video <a href="https://youtu.be/6qXKlcApG8Q">🔐 Master AWS Named Profiles: Named Profiles Setup Tutorial! 🔑</a>

## Installing AWS CLI

Run the following command for installing the AWS CLI.

`
pip install awscli
`

## Configuring your AWS Profiles

You will run the following command to configure you individual profiles. See video referenced above if you are unsure how to set the values for the commands ran below.

`
aws configure --profile demo-user-1-profile
`

`
aws configure --profile demo-user-2-profile
`

## Test Named Profiles with AWS CLI

This is the list of commands for testing your named profiles via the command-line.

`
aws s3 ls --profile s3-user-profile
`

`
aws bedrock list-foundation-models --profile bedrock-user-profile
`