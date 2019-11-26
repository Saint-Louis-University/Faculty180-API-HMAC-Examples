# Faculty180 API HMAC Examples <img src="https://media.trustradius.com/vendor-logos/u1/L9/FVSK019TRL9P-180x180.JPEG" align="right" width="125px" />

<br />

## Overview

This repository contains additional code samples of using the [Interfolio](https://www.interfolio.com/) [Faculty180](https://www.interfolio.com/products/faculty180/) [Application programming interface (API)](https://en.wikipedia.org/wiki/Application_programming_interface) with [Hash-based Message Authentication Code (HMAC)](https://en.wikipedia.org/wiki/HMAC) authentication beyond those provided by [Interfolio](https://www.interfolio.com/) in their [HMAC documentation](https://faculty180.interfolio.com/swagger/ui/hmac.html).

## API Access Control (HMAC)

For [authentication](https://en.wikipedia.org/wiki/Authentication), [Interfolio](https://www.interfolio.com/) uses the [HMAC](https://en.wikipedia.org/wiki/HMAC) mechanism. For [authorization](https://en.wikipedia.org/wiki/Authorization), [Interfolio](https://www.interfolio.com/) uses the tenant ID and a permissioning infrastructure that determines if the user has permission to access a particular set of data. [API](https://en.wikipedia.org/wiki/Application_programming_interface) [authorization](https://en.wikipedia.org/wiki/Authorization) requires a properly formatted [HTTP request header](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods).

## Three Informations

There are three pieces of information required for successful authentication and authorization:

1. public key (example):
	+ Y5aNy8OZRYFKlTxNzXuSxzz64M8YLQB3vrcUP1zk7wQ=
2. secret key (example):
	+ uEvu95GRt8fYw8dZkOyQGsOLy5yuB9vcUEK5cAcNuB4X6D6pTJegoIp/yRa7GaP/Lf6CQIA/xI/oP//YkayuAByx0nieazUEqp3DR7FtNf43=
3. database id (example):
	+ TestUniv

Note: this is an example key-pair. Interfolio will provide unique key-pairs.

## Process

1. Determine what API(s) you want to call (URL string)
2. Create a valid timestamp string in UTC (GMT)
3. Create a verb string composed of:
	+ The verb for the request you want to perform (GET, POST, PUT, DELETE)
	+ Three ASCII newlines
    + The timestamp string
    + Another ASCII newline
4. Take all of the content after 'faculty180.interfolio.com/api.php' from the URL string (this is the request string)
5. Create the verb request string composed of:
    + The verb string
    + The request string
6. Create an encrypted string by HMAC_SHA1 encoding your verb-request string with your secret key.
7. Base64-encode the encrypted string (this is the signed hash)
8. Submit your request to your URL string with the following authorization header and timestamp header:
    + TimeStamp: properly formatted timestamp
    + Authorization: INTF Your public key + Your signed hash
    + INTF-DatabaseID: your institution's database ID (e.g. TestUniv)

## Examples

The [Faculty180](https://www.interfolio.com/products/faculty180/) [HMAC](https://en.wikipedia.org/wiki/HMAC) documentation can be found [here](https://faculty180.interfolio.com/swagger/ui/hmac.html), but the code examples provided are only in [PHP](https://en.wikipedia.org/wiki/PHP), [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)), and [Python 2](https://en.wikipedia.org/wiki/Python_(programming_language)).

This repository contains a copy of the [Python 2](https://en.wikipedia.org/wiki/Python_(programming_language)) example as well as a port to [Python 3](https://en.wikipedia.org/wiki/Python_(programming_language)) and [R](https://en.wikipedia.org/wiki/R_(programming_language)).

## About

### Saint Louis University <img src="https://www.slu.edu/marcom/tools-downloads/imgs/logo/primary-mark/logowithyear_rgb.jpg" align="right" width="125px" />

Founded in 1818, [Saint Louis University](https://www.slu.edu) is one of
the nation’s oldest and most prestigious Catholic institutions. Rooted
in Jesuit values and its pioneering history as the first university west
of the Mississippi River, SLU offers nearly 13,000 students a rigorous,
transformative education of the whole person. At the core of the
University’s diverse community of scholars is SLU’s service-focused
mission, which challenges and prepares students to make the world a
better, more just place.
