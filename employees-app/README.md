# Employees alkalmazás

SonarScanner futtatása:

```shell
docker run --rm -e SONAR_HOST_URL="http://host.docker.internal:9000" -e SONAR_TOKEN="sqa_fb0cc06af7def29c42e28696b373a3ed836642d7" -v ".:/usr/src" sonarsource/sonar-scanner-cli
```