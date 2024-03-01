# Setting up local AWS IAM Profile - Cheat Sheet

This repo is a companion to the YouTube video located <a href="">here</a>

## Activating Python virtual environment
You can activate your Python virtual environment by calling the following command in yout terminal. We are using Anaconda which can be found [here](https://www.anaconda.com/download)

If you don't already have a virtual Python environment already setup you can refer to this video [How to Set Up a Dedicated OpenAI Python Environment with Anaconda](https://youtu.be/lZ2OnOkd1Rk) if you are unsure how to setup your environment.

`
conda activate <you-environment-name>
`

## Installing Python packages
`
pip3 install awscli boto3
`

## Configuring your AWS Profiles
You will run the following command to configure you individual profiles. See video referenced above if you are unsure how to set the values for the commands ran below.

`
aws configure --profile demo-user-1-profile
`

`
aws configure --profile demo-user-2-profile
`