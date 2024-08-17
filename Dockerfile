FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y curl unzip libcurl4 libssl1.0.0

# Set working directory
WORKDIR /bedrock

# Download and extract the Bedrock server files
ADD https://minecraft.azureedge.net/bin-linux/bedrock-server-<version>.zip .
RUN unzip bedrock-server-<version>.zip && rm bedrock-server-<version>.zip

# Expose the necessary ports
EXPOSE 19132/udp

# Start the server
CMD ./bedrock_server
