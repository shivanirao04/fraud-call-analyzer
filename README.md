# Fraud Call Analyzer API

This project is a FastAPI-based backend service built for a hackathon challenge.
It simulates an AI-powered fraud call analyzer that accepts audio input and returns
a fraud risk classification.

The API is designed to be:
- Easy to run locally
- Stable on low-resource machines
- Compatible with hackathon testing servers

---

## 🚀 Live Deployed API (Optional)

If you just want to test the API without running code:

Swagger UI:
https://fraud-call-analyzer.onrender.com/docs

---

## 🛠 Requirements

Make sure you have the following installed:

- Python **3.9 or above**
- VS Code (recommended but optional)
- Internet connection

To check Python version:
```bash
python --version
fraud-call-analyzer
├── app.py
├── requirements.txt
└── README.md



M Shivani Rao <msh23cs@cmrit.ac.in>
12:43 PM (2 minutes ago)
to me

mvn archetype:generate ...
cd my_app
mvn package
java -cp target/my_app-1.0-SNAPSHOT.jar coll.cmrit.App

git config --global user.email "email"
git config --global user.name "Student"

git init
git add .
git commit -m "Initial commit"

ls -al ~/.ssh
ssh-keygen -t ed25519 -C "email"
cat ~/.ssh/id_ed25519.pub

git remote add origin git@github.com: username/repo.git
git config --global push.autoSetupRemote true
git push origin main

http://localhost:8080
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

pipeline {
 agent any
 stages {

  stage('Checkout') {
   steps {
    git branch: 'main',
    url: 'https://github.com/username/repository.git'
   }
  }

  stage('Build') {
   steps {
    sh 'mvn clean package'
   }
  }

  stage('Test') {
   steps {
    sh 'mvn test'
   }
  }

 }
}
