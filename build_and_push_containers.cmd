@echo off
setlocal enabledelayedexpansion

docker buildx rm secure-edge-pro 2>nul || echo Buildx instance not found, continuing...
docker buildx create --name secure-edge-pro --config buildkitd-secure-edge-pro.toml
if errorlevel 1 (
    echo Failed to create buildx instance
    exit /b 1
)

docker buildx use secure-edge-pro
if errorlevel 1 (
    echo Failed to use buildx instance
    exit /b 1
)
docker buildx build --platform linux/arm64/v8 --tag 192.168.140.1:5000/inetinfo --push .
if errorlevel 1 (
    echo Failed to build and push container
    cd ..
    exit /b 1
)

endlocal 
