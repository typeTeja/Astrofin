# Use an official Node.js runtime
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the app
RUN npm run build

# Expose custom port
EXPOSE 3000

# Start Next.js
CMD ["npm", "run", "start"]
