<!-- <div align="center" id="top">
  <img src="./.github/app.gif" alt="Code_quality" /> -->

&#xa0;

  <!-- <a href="https://code_quality.netlify.app">Demo</a> -->
</div>

<h1 align="center">Code quality</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ArthDubey/code_quality?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ArthDubey/code_quality?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ArthDubey/code_quality?color=56BEB8">

  <img alt="Github issues" src="https://img.shields.io/github/issues/ArthDubey/code_quality?color=008000" />

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/ArthDubey/code_quality?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/ArthDubey/code_quality?color=56BEB8" /> -->
  <img alt="Build Status" src = "https://travis-ci.com/ArthDubey/code_quality.svg?branch=master">
  <img alt="License" src = "https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Code_quality 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/ArthDubey" target="_blank">Author</a>
</p>

<br>

## :dart: About

Code quality is a light weight quality check library for Python project or a Python file. It is heavily inspired by the
books of Robert C. Martin. It can be used as a consistent measure for readability and maintainability.

How many times have you seen bulky functions, inconsistent casing for variables, long if-else chains and thought to
yourself if there was a way to weed out such things before they make it to the Production environment...
Well here's my answer to that. Feel free to use this as a check for your projects.

Code quality will rate your projects on different parameters and also provide possible resolutions if any parameter
score is low. The vision behind this tool is to not have readability and maintainability as best practices, but an
industry standard.

## :checkered_flag: Installation and getting started

```
# Install
pip install code-quality

# Using (notice that it's code underscore quality)
python -m code_quality -d {{your project to test}}

```

## :sparkles: Features

:heavy_check_mark: Checks for readability by the principles defined by Robert C. Martin et al. Gives out a report with different scores.\
:heavy_check_mark: Very lightweight and blazing fast tests. Optimized for heavy repositories.\
:heavy_check_mark: Gives out Possible resolution in case any paramter is lower than it should be. (As this is the first version, this feature is very limited)
:heavy_check_mark: Zero configuration required. You can install and start running checks automatically.

## :rocket: Technologies

The following tools were used in this project:

- [Python](https://python.org/)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://python.org/) installed.

## :checkered_flag: Starting For Developers

```bash
# Clone this project
$ git clone https://github.com/ArthDubey/code_quality

# Access
$ cd code_quality

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python -m code_quality -d {{project_filepath}}

# Report will be generated in terminal

# Running tests
pytest
```

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/ArthDubey" target="_blank">Arth Dubey</a>

&#xa0;

<a href="#top">Back to top</a>
