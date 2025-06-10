#!/usr/bin/env bash

ACTION=$1
SCRIPT_DIR=$( dirname "$(realpath "$0")" )

shift

if [ "$ACTION" == "install" ]; then
  docker-compose --project-directory "$SCRIPT_DIR"/ up -d
elif [ "$ACTION" == "logs" ]; then
  docker-compose --project-directory "$SCRIPT_DIR"/ logs -f -t
elif [ "$ACTION" == "generate" ]; then
  docker exec -it kaggle bash -c "cd .. && python -m downloader.main $*"
elif [ "$ACTION" == "tests" ]; then
  docker exec -it kaggle bash -c "pytest"
elif [ "$ACTION" == "mypy" ]; then
  docker exec -it kaggle bash -c "cd .. && mypy -m downloader.main"
elif [ "$ACTION" == "destroy" ]; then
  docker stop kaggle && docker rm kaggle && docker rmi kaggle
fi
