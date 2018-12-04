# User Account Creation - Serverless Function

![python](https://img.shields.io/badge/Python-3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2&style=flat-square&colorA=36363e)
![flask](https://img.shields.io/badge/flask-1.0.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Sendgrid](https://img.shields.io/badge/sendgrid-5.6.0-blue.svg?longCache=true&logo=delicious&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![Mixpanel](https://img.shields.io/badge/mixpanel-4.3.2-blue.svg?longCache=true&logo=coderwall&longCache=true&style=flat-square&logoColor=white&colorB=002992&colorA=36363e)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.2.12-red.svg?longCache=true&style=flat-square&logo=scala&logoColor=white&colorA=36363e)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2&colorA=36363e)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=36363e)
[![GitHub issues](https://img.shields.io/github/issues/toddbirchard/Link-Preview-API.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/ghosttheme-stockholm/issues)
[![GitHub stars](https://img.shields.io/github/stars/toddbirchard/Link-Preview-API.svg?style=flat-square&colorB=e3bb18&colorA=36363e)](https://github.com/toddbirchard/hackers-account-creation/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/toddbirchard/Link-Preview-API.svg?style=flat-square&colorA=36363e)](https://github.com/toddbirchard/hackers-account-creation/network)

An endpoint triggered whenever a user submits a "create account" form. Handles several intricacies which simplify signup, track analytics, and prompts a welcome email.

![Cloud Function](https://raw.githubusercontent.com/toddbirchard/hackers-account-creation/master/img/cloudfunction.png)

## Functionality

This function holds a simple core value: simplify the onboarding process as much as possible for end users. This means keeping our "sign up" form as simple as possible (currently two fields) and discerning any additional data we might like to collect through scripting.
