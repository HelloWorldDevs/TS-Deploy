#!/bin/bash

DEPLOY_HOST="$1@wf-198-58-114-22.webfaction.com"
DEPLOY_PATH="/home/$1/webapps/$2"

ssh $DEPLOY_HOST "cd $DEPLOY_PATH && git pull"
