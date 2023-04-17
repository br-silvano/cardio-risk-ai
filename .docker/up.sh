rm -rf ./services/training-microservice/packages 2>/dev/null
rm -rf ./services/prediction-microservice/packages 2>/dev/null

cp -R ./services/packages ./services/training-microservice
cp -R ./services/packages ./services/prediction-microservice

docker-compose up --build
