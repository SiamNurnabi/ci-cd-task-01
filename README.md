# ci-cd-task-01
1. Create a script (in Python or Bash) that:
Fetches the list of commits from any public GitHub repository (e.g., torvalds/linux or another repo of your choice).
Prints the commit messages and author names in the console.
2. Dockerize the script:
Write a Dockerfile that runs your script inside a container.
3. CI/CD with GitHub Actions:
Create a GitHub Actions workflow that:
Builds the Docker image.
Pushes it to Docker Hub (you can use a personal Docker Hub account).
