# Webfaction Deployment
#### By _**Joseph Karasek**_ for _**Hello World Devs**_

### Version 0.1

## Description

_This deployment script is meant to be used with [WebFaction](https://www.webfaction.com/) and was built as a development tool for the Tyson Steele projects. This script handles two tasks: 1) setting up the initial configuration on Webfaction for a static site (including the webapp, domain, and website) and 2) pulling the latest version of a site if the website already exists._

_This is the first python application I have ever written. Please feel free to give me feedback._

## Prerequisites

_You will need the following things properly installed on your computer._

* Python 2.7

## Installation

* It is highly suggested (but not required) that you place the script in the root directory of the project you are working on.
* Open the `example.siteConfig.py` file. Follow the instruction to create a `siteConfig.py` file
  * Note: This file will need to be in the same directory as the deploy.py script
* It's suggested you add the following entries to you .gitignore file
```
siteConfig.py
*.pyc
```

## How to use

Simply run... `python deploy.py`. This command will both initialize a project and pull in the latest version.

## Features to add

* Setup of DNS through Name Cheap
* Better UI feedback, including prompts

## Known Bugs

_Deployment and updates to the repo are handled with Git. Currently this causes the script to exist with an error message, despite the actions being successful._

## Resources

* [WebFaction API Docs](https://docs.webfaction.com/xmlrpc-api/apiref.html)

## Support and contact details

_If you have any questions, concerns, or feedback, please contact the authors through_ [gitHub](https://github.com/joekarasek/).

## Technologies Used

* _Python_
* _WebFaction API_

### License

MIT License.

Copyright (c) 2016 **_Joseph Karasek_**
