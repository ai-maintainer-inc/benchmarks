# Usage

You can use the benchmarks locally with docker-compose, see the [platform-dockerized repo](https://github.com/ai-maintainer-inc/platform-dockerized) for instructions.

# About

Contains folders representing repositories. Each "repo" contains a .benchmark folder that has information about the task as well as a dockerfile that checks whether or not the task was resolved successfully.

Benchmarks are automatically loaded into the postgres database and git-server with the [slurper](https://github.com/ai-maintainer-inc/slurper) script.