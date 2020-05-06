# Github Webhook Framework dockerized Container
<a id="markdown-Github%20Webhook%20Framework%20dockerized%20Container" name="Github%20Webhook%20Framework%20dockerized%20Container"></a>

A simple container to quickly and easily transfer web-based applications into a productive operation. The container allows a fast development of a Web service by simple exchange of the application files.

## Purpose
<a id="markdown-Purpose" name="Purpose"></a>

This repository was developed from the project [github-webhooks-framework](https://github.com/generaliinformatik/github-webhooks-framework), which needed a standardized Docker Container for productive operation. Since the app developed in this project was based on Python and Flask, an environment was needed that would allow the operation of such an app.


## Table of content
<a id="markdown-Table%20of%20content" name="Table%20of%20content"></a>
<!-- TOC -->

- [Purpose](#purpose)
- [Table of content](#table-of-content)
- [Requirements](#requirements)
- [To-dos](#to-dos)
- [Installation](#installation)
    - [Cloning the Github repository](#cloning-the-github-repository)
- [Deploy](#deploy)
    - [Docker](#docker)
- [License](#license)
- [Credits](#credits)

<!-- /TOC -->

## Requirements
<a id="markdown-Requirements" name="Requirements"></a>
- Docker / OpenShift
- Python
    - Flask

## To-dos
<a id="markdown-To-dos" name="To-dos"></a>
- tba

## Installation
<a id="markdown-Installation" name="Installation"></a>

### Cloning the Github repository
<a id="markdown-Cloning%20the%20Github%20repository" name="Cloning%20the%20Github%20repository"></a>

    git clone https://github.com/generaliinformatik/docker-github-webhook-framework.git
    cd docker.github-webhook-framework

## Deploy
<a id="markdown-Deploy" name="Deploy"></a>

### Docker
<a id="markdown-Docker" name="Docker"></a>

To deploy in a Docker container you have to expose the port 5000, for example with the following command:

    git clone http://github.com/generaliinformatik/docker-github-webhooks-framework.git
    docker build --pull -t generaliinformatik/docker-github-webhooks-framework docker-rad-container
    docker run -d --name docker-rad-container -p 5000:5000 generaliinformatik/docker-github-webhooks-framework

You can also mount volume to setup the ``hooks/`` directory, and the file ``config.json``:

    docker run -d --name docker-rad-container \
      -v /path/to/my/app:/app \
      -p 5000:5000 \
      docker-rad-container

## License
<a id="markdown-License" name="License"></a>

MIT, see [LICENSE](LICENSE)


## Credits
<a id="markdown-Credits" name="Credits"></a>

- tba

Thanks.
