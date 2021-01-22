<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">gitega</h3>

  <p align="center">
    Keep a local copy of the stats of all your public github repos.
    <br />
    <br />
    <a href="https://github.com/b3nj5m1n/gitega/issues">Report Bug</a>
    ·
    <a href="https://github.com/b3nj5m1n/gitega/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)



<!-- ABOUT THE PROJECT -->
## About The Project

Regularly execute a python script to keep a local copy of the stats of all your public github repos.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python3.7
```sh
sudo apt install python3.7
sudo pacman install python3.7
```
* Github personal access token (Settings -> Developer Settings -> Personal Access Tokens -> Generate new token) with all repo permissions.


### Installation

1. Clone the repo
```sh
git clone https://github.com/b3nj5m1n/gitega.git
```
2. Install requirements packages
```sh
pip install -r requirements.txt
```


<!-- USAGE EXAMPLES -->
## Usage

Navigate into the directory and add an account:
```sh
python addAccount.py --name YourUserName --token YourAccessToken
```

Use update.sh to automatically update all your accounts and send a report to you via email. Call the script with the path to your .gitega directory and your email (Will be used to send & receive, requires you to have msmtp set up) Put something like this (This one will run at 17:00 every day) in your crontab file (Using crontab -e): `0 17 * * * bash /home/YourUserName/Documents/Github/gitega/update.sh "/home/YourUserName/.gitega" "YourEmailAdress"`

Regularly run update.py to update all traffic data for all repositorys of an account. python update.py --name YourUserName

This will also parse the data and store it in an sql lite database.



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/b3nj5m1n/gitega?style=flat-square
[contributors-url]: https://github.com/b3nj5m1n/b3nj5m1n/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/b3nj5m1n/gitega.svg?style=flat-square
[forks-url]: https://github.com/b3nj5m1n/gitega/network/members
[stars-shield]: https://img.shields.io/github/stars/b3nj5m1n/gitega.svg?style=flat-square
[stars-url]: https://github.com/b3nj5m1n/gitega/stargazers
[issues-shield]: https://img.shields.io/github/issues/b3nj5m1n/gitega.svg?style=flat-square
[issues-url]: https://github.com/b3nj5m1n/gitega/issues
[license-shield]: https://img.shields.io/github/license/b3nj5m1n/gitega.svg?style=flat-square
[license-url]: https://github.com/b3nj5m1n/gitega/blob/master/LICENSE.txt
[product-screenshot]: https://socialify.git.ci/b3nj5m1n/gitega/image?font=Inter&language=1&owner=1&pattern=Circuit%20Board&theme=Light
