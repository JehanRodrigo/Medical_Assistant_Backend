# Medical_Assistant_Backend
* Simply this repository is for testing Backends for the "Medical_Assistant" Project.

Our Frontend URL: https://medical-assistant-deploy.vercel.app/

### Commands
* gunicorn command for running python file
```
gunicorn medi_backend_pipe:app
```
<br/>

* install from requirements.txt
```
pip install -r requirements.txt
```
<br/>

* docker command to build docker image locally
```
docker build -t jehanrodrigo/medi_back_gpt2_pipe:0.1 .
```
<br/>

* docker command to run docker image locally with port mapping
```
docker run -p 5000:5000 jehanrodrigo/medi_back_gpt2_pipe:0.1
```
<br/>

### Backend Deployments
* The deployed backend with [GPT2.](https://medicalback-34822786368.asia-south1.run.app/)
* The deployed backend with [BioGPT.](https://biosuggimg-1081715976745.asia-south1.run.app)

### Others
* Requirements that we installed time to time:
  * gunicorn
    * gunicorn==23.0.0
  * protobuf 
    * protobuf-5.28.3
  * sacremoses
    * joblib-1.4.2
    * sacremoses-0.1.1
  * flask==3.0.3
  * flask-cors==5.0.0
  * transformers==4.45.2
  * torch==2.5.0


### References
* BioGPT Documentation Link: [here](https://huggingface.co/docs/transformers/main/en/model_doc/biogpt#transformers.BioGptModel)
