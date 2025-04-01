# Phidata-Agents-Video_Summarizer Setup
Video Summarizer application with help of Phidata agents

1. Create a venv and activate it
```bash
conda create -n phidata python=3.11 -y

conda activate phidata
```

2. Install required dependencies packages
```bash
pip install -r requirements.txt
```

3. create .env file and store required API keys
```bash
GOOGLE_API_KEY= '####----#####'
GROQ_API_KEY= '####----#####'
PHI_API_KEY= '####----#####'
OPENAI_API_KEY= '####----####
```

# Deployment of streamlit app using AWS-EC2

### 1. Login with your AWS console and launch an EC2 instance

### 2. Run the following commands
Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"

move to working directory 'cd your-project'

```

```bash
docker build -t manirathinam21/stapp:latest . 

```

```bash
docker images -a   

```
```bash
docker run -d -p 8501:8501 manirathinam21/stapp   
```

```bash
docker ps     
```

```bash
docker stop container_id  
```


```bash
docker rm $(docker ps -a -q)  
```

```bash
docker login    
```

```bash
docker push manirathinam21/stapp:latest   
```

```bash
docker rmi manirathinam21/stapp:latest
```

```bash
docker pull manirathinam21/stapp
```

```bash
   
```