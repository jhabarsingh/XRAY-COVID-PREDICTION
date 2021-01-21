# Predict COVID From Xray Report

<details>
  <summary>:zap: TECH STACK</summary>
  <div style="display:flex;justify-content:space-around">
    <img  title="Django" src="https://icon-library.com/images/django-icon/django-icon-0.jpg" width="70px" height="70px" style="margin-right:5px;" />
    <img  title="Postgresql" src="https://pbs.twimg.com/media/EGc7jg4XoAA0bez.png" height="70px" style="margin-right:5px;" />
    <img  title="PY Torch" src="https://miro.medium.com/max/2440/1*ptGydg-rxqLVD_mQxQzKlg.png" height="70px" style="margin-right:5px;" />
    <img  title="Docker" src="https://pbs.twimg.com/profile_images/1273307847103635465/lfVWBmiW_400x400.png" height="70px" style="margin-right:5px;" />
    <img  title="PY Torch" src="https://miro.medium.com/max/3006/1*U62uxIOclJe-Lyre14p_rQ.png" height="70px" style="margin-right:5px;" />
  </div>
</details>

![Covid Prediction](staticfiles/corona.png)

## About
It's a ML Model to detect covid from xray reports of the patient.

**INPUT** : **JPEG, PNG, JPG**

**OUTPUT** : **VIRAL, COVID+, COVID-**

#### **PYTORCH IMAGE CLASSIFIER** is used to implement this ML Model.
#### [DATASET](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database?select=COVID-19+Radiography+Database)

## Want To Contribute
### DOCKER SETUP
* download docker, docker-compose
* build and start the docker-compose
```bash
sudo docker-compose build
sudo docker-compose up
```
* now start working on the project

### TRAVIS-CI (CI/CD)
* PR should be accepted by Travis-Ci
* Write test cases if it is needed
* It should be linted [ PEP8 Guidelines ]


