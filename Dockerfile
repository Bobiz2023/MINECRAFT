FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y curl unzip libcurl4

# Set working directory
WORKDIR /bedrock

# Download and extract the Bedrock server files
ADD https://minecraft.azureedge.net/bin-linux/bedrock-server-1.20.30.02.zip .
RUN unzip bedrock-server-1.20.30.02.zip && rm bedrock-server-1.20.30.02.zip

# Expose the necessary ports
EXPOSE 19132/udp

# Start the server
CMD ./bedrock_server
