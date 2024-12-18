# Medical_Assistant_Backend
* Simply this repository is for testing Backends for the "Medical_Assistant" Project.

Our Frontend URL: https://medical-assistant-deploy.vercel.app/

##### Commands
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



##### References
* BioGPT Documentation Link: [here](https://huggingface.co/docs/transformers/main/en/model_doc/biogpt#transformers.BioGptModel)
