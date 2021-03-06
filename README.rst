.. image:: http://www.repostatus.org/badges/latest/wip.svg
    :target: http://www.repostatus.org/#wip
    :alt: Project Status: WIP — Initial development is in progress, but there
          has not yet been a stable, usable release suitable for the public.

.. image:: https://img.shields.io/github/license/jwodder/ghutil.svg?maxAge=2592000
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

The ``ghutil`` package provides a command-line program for interacting with &
managing GitHub repositories, issues, gists, etc.

This is a work in progress; while the program should be usable at any given
point in time, many API features are not yet present, and those features that
are present may have their interface modified at any time.


Installation
============
``ghutil`` requires Python 3.3 or higher to run and `pip
<https://pip.pypa.io>`_ 6.0+, `Setuptools <https://setuptools.readthedocs.io>`_
30.3.0+, & `wheel <https://pypi.python.org/pypi/wheel>`_ to install.  `Once you
have those
<https://packaging.python.org/installing/#install-pip-setuptools-and-wheel>`_,
you can install ``ghutil`` and its dependencies by running::

    python3 -m pip install git+https://github.com/jwodder/ghutil.git


Basic Usage
===========

Authentication
--------------
Store your GitHub username & password in ``~/.netrc`` like so::

    machine api.github.com
    login YOUR_USERNAME_HERE
    password YOUR_PASSWORD_HERE

(Make sure the file permissions on ``~/.netrc`` are set to 0600!)

Commands
--------
Most commands output JSON.

``gh gist [list]``
   List your gists

``gh gist show <gist-id> ...``
   Show gist details

``gh gist new [-d <description>] [-f <filename>] [-P|--private] <file>``
   Create a gist from a given file

``gh issue new [-T <title>] [--body <file>] [-a <assignee>] [-l <label>] [-m <milestone>] [<repo>]``
   Create an issue in the given repository

``gh issue show <issue> ...``
   Show details on the given issues

``gh issue [list [--filter assigned|created|mentioned|subscribed|all] [--state open|closed|all]]``
   List your issues

``gh plus1 <issue_url>|<comment_url> ...``
   Give a thumbs-up to an issue, pull request, or comment thereon

``gh release [<tag>]``
   Create or edit the release for the given tag (default: the most recent
   reachable tag)

``gh repo clone <repo> [<dir>]``
   Locally clone a GitHub repository

``gh repo delete [<repo>]``
   Delete a GitHub repository

``gh repo edit [<repo>]``
   Edit a GitHub repository's details

``gh repo fans [<repo>]``
   List users that have forked, starred, or watched the given repository

``gh repo fork <repo>``
   Fork the given repository

``gh repo [list]``
   List your repositories

``gh repo list-forks [<repo>]``
   List a repository's forks

``gh repo network [<repo> ...]``
   Show a repository's network of forks as a tree

``gh repo new [-d <description>] [-H <homepage>] [-P|--private] <name>``
   Create a new repository

``gh repo search <search-term> ...``
   Search for repositories on GitHub

``gh repo show [<repo> ...]``
   Show details on the given repositories

``gh repo star [<repo> ...]``
   Star the given repositories

``gh repo starred``
   List starred repositories

``gh repo unstar [<repo> ...]``
   Unstar the given repositories

``gh request [--accept <MIME type>] [--data <data>] [-X <method>] <path>``
   Make an arbitrary GitHub API request to ``<path>``
