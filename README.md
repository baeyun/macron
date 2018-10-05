<p align="center">
  <img src="https://raw.githubusercontent.com/bukharim96/macron/master/resources/macron-logo.png">
</p>

<h1 align="center">Macron</h1>

Macron is a framework that builds cutting-edge cross-platform desktop apps using plain HTML, CSS and JavaScript! Check the official site to <a href="https://macron.netlify.com">learn more</a>.

Macron uses existing software on the platform to draw windows alongside the system's native web engine to render static content.

## Features

* **Cross-platform** - Macron currently supports Windows only. The Linux version is currently under active development. If you are interested in collabaration, check out the <a href="https://macron.netlify.com/contributing">Contributing</a> section.
* **Fast** - Speeds are unimaginable and run at close proximity with native apps.
* **Light** - Excluding the installer, the bundled app gets a overhead of about 10MB with all the necessary files included.
* **Extendable** - Macron is totally extendable with native modules. These native modules allow to be packaged with Macron.
* **Low RAM consumption** - With the development of Macron in mind, we selectively took care of not making the same mistakes other similar frameworks made by runnning an entire browser instance every time a user runs an app. Performance can never be traded for expression.
* **Hybrid development** - Working with native modules alongside your app makes it easier to present logic in the sense that you only use native modules when necessary.
* **System's web engine** - On Windows, static HTML is rendered by Trident and Webkit on Linux and MacOS.
* **Native extensions** - All common runtime modules are bundled with your app, including file-related functionalities, system and process activities amongst others.
* **Easy and simple** - Creating Macron apps that don't utilize any extra modules is dead easy. In fact, a single config file runs your entire app.

## Prerequisites

You must be running on the Windows platform to proceed. The Linux platform is currently under active development while MacOS isn't currently supported. 

- WPF (.NET) version: >=3.5/4.0
- pythonnet version: >=2.3.0
- Python version: >=3.6
- Node version: >=8.11.3

## Installation

With all the requirements met, Macron can be installed globally by running:

```
npm install -g macron
```

> **Note**: Macron must be installed globally for caching purposes. This might be changed in future versions.

## Quick Commands
```bash
# Install Macron globally from npm
$ npm install -g macron

# Create new app
$ macron init  MyCoolApp

# Integrate Macron in existing project
$ macron init

# Remotely run your app
$ macron start

# Build your awesome app
$ macron build

# Run your awesomely built app
$ macron start build
```

The rest of the commands can be found on the official site.

## Contribution & Support

We are seeking support from community members like you to fund and support the Macron project, it's development and future. A custom domain is needed for the site as well. You can become a patreon here:

<a href="https://patreon.com/macron">
  <img src="https://raw.githubusercontent.com/bukharim96/macron/master/resources/become_a_patron_button@2x.png" alt="Patreon">
</a>

As a result, we'll add your logo to our *README.md* page and also a big banner at the bottom of our site.

You can find the complete contribution guide <a href="https://macron.netlify.com/contributing">right here</a>. We are actively searching for users who can test out the latest version of Macron on Windows 7 and kindly report any perceived differences regarding general performance or RAM usage.

## Releases

The complete release notes can be found at <a href="https://macron.netlify.com/releases">this link</a>.

## Quick Links

* <a href="https://macron.netlify.com/getting-started">Getting Started</a>
* <a href="https://macron.netlify.com/advanced">Advanced Guide</a>
* <a href="https://macron.netlify.com/api">API Reference</a>

## Contact

To get in touch, send us a <a href="https://twitter.com/macronjs">direct message on Twitter</a>.

Happy hacking!
