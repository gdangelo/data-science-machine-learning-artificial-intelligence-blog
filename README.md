# :warning: Not yet available --> Coming soon! :warning:

> This is my personal blog on Data Science, Machine Learning, and Artificial Intelligence. It is built using the Pelican framework. Articles are written with Jupyter Notebook.

## Features

* [Python](https://www.python.org/);
* [Virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/);
* [Pelican](http://docs.getpelican.com/en/stable/);
* ... 
* See [requirements.txt](https://github.com/gdangelo/data-science-machine-learning-artificial-intelligence-blog/blob/master/requirements.txt) for all dependencies;

## Quickstart

```
# Clone the repo
git clone https://github.com/gdangelo/data-science-machine-learning-artificial-intelligence-blog
cd data-science-machine-learning-artificial-intelligence-blog/
git submodule update --init --recursive

# Install virtualenv via pip
pip install virtualenv

# Create a virtual environment and activate it
virtualenv venv
source venv/bin/activate (UNIX)
venv\Scripts\activate.bat (WINDOWS)

# Install all the dependencies
pip install -r requirements.txt

# Generate site
make regenerate

# Start the server
make serve
```

That will regenerate files upon modification and serve site at `http://localhost:8000`.

## File Structure

```
root/
 ├── content/                            * Contains all the written articles
 |── output/   
 |── plugins/                            * Contains all the additional plugins
 |── themes/
 |    ├── static/                        * Contains all the static assets
 |    |   ├── css/
 |    |   ├── fonts/
 |    |   ├── img/
 |    |   ├── js/
 |    |   └── particlesjs-config.json    * Config file used to display particles
 |    |   
 |    └── templates/
 |        ├── about.html                 * To display the about page
 |        ├── article.html               * Processed for each article
 |        ├── base.html                  * Header section for each page
 |        ├── contact.html               * To display the contact page
 |        ├── footer.html                * Footer section for each page
 |        ├── category.html              * Processed for each category
 |        ├── index.html                 * To display the home page
 |        ├── page.html                  * Processed for each page
 |        ├── search.html                * To display the search page
 |        └── tag.html                   * Processed for each tag
 |
 ├── venv/                               * Python virtual environment
 ├── develop_server.sh 
 ├── fabfile.py                          * Automation tool (Fabric) for generation and publication tasks  
 ├── Makefile                            * Automation tool (Make) for generation and publication tasks  
 ├── pelicanconf.py                      * Main settings file
 ├── publishconf.py                      * Settings to use when ready to publish
 ├── README.md 
 └── requirements.txt                    * List of package dependencies
```
