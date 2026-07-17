pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat """
                cd SwagLabs_Automation
                python -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                cd SwagLabs_Automation
                python -m pytest -v
                """
            }
        }
    }
}

               Difference                          

Freestyle:                          Pipeline:

GitHub URL                          GitHub URL
      ↓                                 ↓
Build Step lo                       Jenkinsfile
pip install                             ↓
pytest
                                Jenkinsfile lo already
                                    pip install
                                      pytest



Jenkins Pipeline Quick Notes (Leelasai)
1. Jenkins enduku use chestam?

Automation tests ni automatic ga run cheyyadaniki.

Flow:

Developer
↓
Git
↓
GitHub
↓
Jenkins
↓
Pytest
↓
HTML Report

2. Jenkins Install
Java install
Jenkins install
Browser lo open
localhost:8080
Unlock Jenkins
Suggested Plugins Install
Create Admin User
Dashboard Open
3. Freestyle Project

New Item
↓
Freestyle Project
↓
GitHub Repository URL
↓
Build Steps
↓
Windows Batch Command

Command:

python -m pip install -r requirements.txt

python -m pytest -v

Build Now

Result:
PASS / FAIL

4. Git Commands

git status

git add .

git commit -m "message"

git push origin main

5. Pipeline Project

New Item

↓

Pipeline

↓

Description (Optional)

↓

Pipeline Script From SCM

↓

SCM = Git

↓

Repository URL

↓

Branch = */main

↓

Script Path

SwagLabs_Automation/Jenkinsfile

↓

Save

↓

Build Now

6. Jenkinsfile

pipeline {

agent any

stages {

stage('Install Dependencies') {

steps {

bat """

cd SwagLabs_Automation

python -m pip install -r requirements.txt

"""

}

}

stage('Run Tests') {

steps {

bat """

cd SwagLabs_Automation

python -m pytest -v

"""

}

}

}

}

7. Meaning

pipeline

Pipeline start.

agent any

Available Jenkins machine meeda run cheyyi.

stages

Pipeline ni steps ga divide cheyyi.

stage

Oka work.

Example:

Install Dependencies

Run Tests

steps

Aa stage lo execute cheyyalsina commands.

bat

Windows CMD commands.

Linux ayithe sh.

cd SwagLabs_Automation

Project folder loki vellu.

python -m pip install -r requirements.txt

Dependencies install.

python -m pytest -v

Automation test cases run.

-v

Verbose mode.

Test names display chestundi.

8. Mana Project Flow

Website

↓

Selenium

↓

Pytest

↓

Git

↓

GitHub

↓

Jenkins Pipeline

↓

Tests Run

↓

HTML Report

↓

SUCCESS

9. Interview Questions

Q. Jenkins enduku?

Automation ni automatic ga run cheyyadaniki.

Q. Pipeline ante?

Automation process ni code laga rayadam.

Q. SCM ante?

Source Code Management.

Mana project lo Git.

Q. agent any ante?

Available Jenkins node meeda pipeline run avutundi.

Q. stage ante?

Pipeline lo oka step.

Q. steps ante?

Execute cheyyalsina commands.

Q. bat enduku?

Windows commands execute cheyyadaniki.

Q. sh enduku?

Linux commands execute cheyyadaniki.

Q. pytest -v ante?

Automation tests execute chestundi.

Q. requirements.txt enduku?

Project libraries install cheyyadaniki.

10. Nenu Hands-on ga chesinavi

✔ Jenkins Install

✔ Freestyle Project

✔ GitHub Connect

✔ Git Commands

✔ Jenkins Pipeline

✔ Jenkinsfile

✔ Requirements Install

✔ Pytest Execute

✔ HTML Report

✔ Screenshot on Failure

✔ Git Push

✔ 7 Tests PASS

11. CI (Continuous Integration)

Developer

↓

Git Push

↓

GitHub

↓

Jenkins

↓

Checkout Code

↓

Install Dependencies

↓

Run Tests

↓

Report

↓

SUCCESS

Idhe mana project lo hands-on ga chesina CI process.