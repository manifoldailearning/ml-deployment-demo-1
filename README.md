
`aws lightsail create-container-service --service-name flask-service --power small --scale 1`

# Check the status

`aws lightsail get-container-services --service-name flask-service`

`aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container`

```
aws lightsail create-container-service-deployment \
--service-name flask-service \
--containers file://containers.json \
--public-endpoint file://public-endpoint.json
```