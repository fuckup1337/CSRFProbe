<p align="middle"><img src='https://i.imgur.com/diK2aT7.png' /></p>  

# CSRF Probe
CSRF Probe is a advanced scanner for hunting down Cross Site Request Forgery bugs in web applications.

### Working:
The typical flow of this scanner is :-
- Spiders the target website to find all pages.
- Finds all types of forms present on the each page.
- Hunts out hidden as well as visible parameter values.
- Submits each form with normal tokens & parameter values.
- Generates random token strings and sets parameter values.
- Submits each form with the crafted tokens.
- Finds out if the tokens are sufficiently protected.
- Generates custom proof of concepts after each successful bug hunt.

<img src="https://i.imgur.com/Qd4mSqm.png" />

#### Features:

- [x] Features continuous crawling and scanning.
- [x] Support for both GET and POST requests.
- [x] Support for custom cookie values and generic headers.
- [x] Generates special crafted tokens for different parameters.
- [x] Submits forms in the normal way as well as with crafted token.
- [x] Rare chances of false positives occuring during scan.
- [x] Follows redirects when there is a 302 response.
- [x] Generates PoCs for both exploitable and not exploitable CSRFs.
- [x] Has a user-friendly interaction environment.
- [x] Everything is automated on demand.

<img src="https://i.imgur.com/aLD1GDD.png" />

#### Version:
v1.0.0

#### Warnings:
Do not use this tool on a live site!

It is because this tool is designed to perform all kinds of form submissions automatically which can be dangerous to he site. Sometimes you may screw up your database and most probably perform a DoS on the site as well.

Use on a disposable test site!

#### Drawbacks:
The scanner has the following drawbacks presently:

- Normally the scanner assumes that every form has a hidden/visible parameter and token field.
- Changing or removing that token field usually causes a 403 Forbidden response.
- Spidering is restricted to domains of startpages (so doesn't work with all domains). :(

#### Requirements:

- mechanize
- requests
- bs4
- lxml
- logging

#### Usage:

➲ Clone the script and launch it.
```
git clone https://github.com/the-Infected-Drake/CSRFProbe.git
cd CSRFProbe
```
➲ Install the dependencies.
```
pip install -r requirements
```
➲ Launch the script.
```
python csrfprobe.py
```
➲ Enter the website target.
```
https://examplesite.com
```
➲ Let the scanner load up.

➲ Keep track of PoCs which may appear (if bug exists).

➲ Report to owners if any bugs found... ; )

#### Version:

- v1.1.0

#### To Do's:
- Associate multithreading for the better.

> Thank you...

✎ @_tID
