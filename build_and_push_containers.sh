#!/bin/bash

set -e -x

docker buildx rm secure-edge-pro || true
docker buildx create --name secure-edge-pro \
                     --config buildkitd-secure-edge-pro.toml
docker buildx use secure-edge-pro
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/inetinfo --push .

set +x
echo "-------------------------------------------------------"
echo "Don't forget to run the container in HOST networking mode:"
echo "See article https://support.ixon.cloud/s/article/Running-custom-Docker-applications-on-the-SecureEdge-Pro#h_01J0NP3YCWA0F0AV3T9257HE8R"
echo "-------------------------------------------------------"
