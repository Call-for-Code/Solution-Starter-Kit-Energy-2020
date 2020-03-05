# Energy sustainability in the context of climate change

This solution starter was created by at the United Nations Human Rights Office in Geneva, Switzerland on February 27-28, 2020. It features contributions by technologists from JPMorgan Chase, Persistent Systems, IBM, and Red Hat. 

## Authors

* Mark Meiklejohn - JPMorgan Chase
* Roberto Mosqueda - Persistent Systems
* Vincent Batts - Red Hat
* Binu Midhun - IBM
* Henry Nash - IBM

## Contents

1. [Overview](#overview)
2. [Video](#video)
3. [The idea](#the-idea)
4. [How it works](#how-it-works)
5. [Diagrams](#diagrams)
6. [Documents](#documents)
7. [Datasets](#datasets)
8. [Technology](#technology)
9. [Getting started](#getting-started)
9. [Resources](#resources)
10. [License](#license)

## Overview

### What's the problem?

As the population grows, so does the demand for energy. Fossil fuels like coal, oil, and gas have exacted an enormous toll on the environment — from air and water pollution to climate change. By investing in solar, wind, and thermal power, improvements in energy productivity and expanding infrastructure is key to providing clean and more efficient energy.

Read about the [UN Sustainable Development Goal on affordable and clean energy](https://www.undp.org/content/undp/en/home/sustainable-development-goals/goal-7-affordable-and-clean-energy.html).

While the switch to clean energy in our homes will make a real and important impact to the climate, energy usuage in the commercial sector is often higher than in the domestic sector (i.e. that used in homes). A key part of this commercial energy consumption goes into making products that we buy. However, while some products we buy come with an [Energy-efficiency rating](https://ec.europa.eu/info/energy-climate-change-environment/standards-tools-and-labels/products-labelling-rules-and-requirements/energy-label-and-ecodesign/about_en) (e.g. how much energy will my washing machine consume when I use it?), there is nothing provided in terms of the amount of energy (and type of energy, i.e. fossil vs renewable) that was used to manufacture the product in the first place. In fact, if you think about it, to minimize the impact on the climate of prouducts you buy, it would be great to be able to compare the *climate impact* across different manufactures' products. To be complete, this climate impact comparison might also include other things outside of energy - eg. water consumption. What is really needed is a comprehensive *Climate Impact Rating* for products, that can be presented to a consumer as some kind of labelling system.

### How can technology help?

Whether it's third-party open source projects or IBM Cloud services, technologies like data analytics, visualization, Internet of Things, Open APIs, databases and blockchain can help address global environmental challenges to track energy (and other consumables) that go into making prodcts. Enabling us to select products that have the lowest climate impact can have a real reduction in our personal impact on the planet.

## Video

[ replace this with Binu's video]

[![Call for Code Solution Starter: Water sustainability in the context of climate change ](https://img.youtube.com/vi/hC2b-iP6Rxc/0.jpg)](https://www.youtube.com/watch?v=hC2b-iP6Rxc)

## The idea

The idea is to expand the global product labelling system, to include a comprehensive *Climate Impact Rating (CIR)*, which will be visible at the point-of-sale (POS) by consumers (be that in-store or on-line). Such a Climate Impact Rating could eventually include:

* Energy Efficiency while in use (this exists today for many products)
* Energy (and energy mix) to produce, potentially expressed as CO2 emitted
* Expected lifetime of product (enabling better comparison between production energy vs in-use energy)
* Other (non-CO2) green-house gas emmissions (e.g. from fertilizer)
* Other comsumables, e.g. water
* Recyclability

One of the key challenges of any such labelling system is that it be, first and foremost, understandable by the intended reader - as well as comprehensive in terms of what it includes. We envisage that eventually this would actuially be printed on products (much like today's Energy Efficiency or Food labelling), but ahead of that we would like to enable POS scanning using smart phones to transalate barcodes into a visible rating.

One further item that would be benficial to build in would be to include an estimate of the climate impact of the transporation of the product to the Point-of-Sale (POS). By definition, this could most likely not be printed on the product (since the value at each POS might be different) - but perhaps be looked up be displayed via a smart phone (which would know the location), or online.

Creating such a labelling system is a large and global undertaking, which will require many underlying components, technologies and agreements to come together. For the Call for Code 2020 challenge on Energy we are encouraging you to experiment with building out some of these components - so these can be brought together to enable this overall labelling system. These components fall into a number of categories:

|   |   |
| - | - |
| Core-Architecture | Use the provided starter kit to get a basic system up and running that supports Consumer APIs. Maybe you can develop a better architecure? Develop new and interesting ways of displaying the CIR, e.g. via Augmented Reality (AR) on a mobile deice, within search engines, on product listings etc. |
| Data Science | How best to map raw data into the chosen label. For example, is it better to represent energy as CO2 produced (i.e. it combines amount of energy and use of renewables) or keep these separate? How might we include summary data (e.g. by CO2 per country/region) ahead of having detailed information for a significant number of products? |
| Labelling Design | Experiment (and maybe user test) and then propose design  of the label that is both comprehensive and understandable by consumers. Use the experience from food labelling and existing Energy Ratings as examples |
| Additional Storyboards | Develop additional storyboards (and interfaces) for users who are manufactures, administrators and auditors |

## How it works

The goal of this solution is to provide a better feedback loop that empowers local municipalities, small business owners, and members of the community, especially the most vulnerable. The team approached this problem by looking how a solution could benefit three potential end users who need access to information about the current situation, resources available to them, and how to better prepare next time:

1. A disaster victim, who seeks information on how to improve her community by best matching her skills to volunteer opportunities.
1. A small business owner who needs to open her shop as soon as possible to restart cash flow.
1. A local elected government official, who needs to generate damage assessments and rebuilding recommendations quickly.

By combining cloud-native infrastructure with event-driven data processing and intelligent modeling, this solution could help predict when and where a disaster may strike next and extrapolate the impact. Furthermore, it could allow stakeholders to derive the most promising course of action with the greatest improvement to plans and processes possible.

## Diagrams

![Challenge 1 Architecture](/images/Challenge_1_Architecture.png?raw=true "Challenge 1 Architecture")

This solution starter idea provides a basic architecture of you to experiment within any of the categories, and includes:

* A CouchDB NoSQL database layer holding both individual product rating, as well as sumamry data
* A basic API server that allows data to insert and extract data from the database. This API is expressed as a Swagger (OpenAPI) document, so you can build your own clients.
* Deployment tools to stand up the above on the IBM Cloud, within the free-tier plan (i.e. so it is free for you to experiment)

## Documents

- [Data Tools & Maps](https://www.eia.gov/tools/)
- [Existing Energystar Ratings System](https://www.energystar.gov/)
- [EU Energy Ratings System](https://ec.europa.eu/info/energy-climate-change-environment/standards-tools-and-labels/products-labelling-rules-and-requirements/energy-label-and-ecodesign/about_en)
- [Traffic Light Food Labelling](hhttps://en.wikipedia.org/wiki/Traffic_light_rating_system)

## Datasets

- [World consumption averages, and break down per capita](https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption)
- [Power plant information](https://www.eia.gov/state/maps.php)

## Technology

- TBA

## Getting started

### Prerequisite

You should have a basic understanding of the OpenWhisk programming model. If not, [try the action, trigger, and rule demo first](https://github.com/IBM/openwhisk-action-trigger-rule).

Also, you'll need an IBM Cloud account and the latest [OpenWhisk command line tool (`ibmcloud fn`) installed and on your PATH](https://github.com/IBM/openwhisk-action-trigger-rule/blob/master/docs/OPENWHISK.md).

As an alternative to this end-to-end example, you might also consider the more [basic "building block" version](https://github.com/IBM/openwhisk-rest-api-trigger) of this sample.

### Steps

1. [Provision MySQL](#1-provision-mysql)
2. [Create OpenWhisk actions and mappings](#2-create-openwhisk-actions-and-mappings)
3. [Test API endpoints](#3-test-api-endpoints)
4. [Delete actions and mappings](#4-delete-actions-and-mappings)
5. [Recreate deployment manually](#5-recreate-deployment-manually)

### 1. Provision MySQL

Log into the IBM Cloud and provision a [ClearDB](https://console.ng.bluemix.net/catalog/services/cleardb-mysql-database/) or a [Compose for MySQL](https://console.ng.bluemix.net/catalog/services/compose-for-mysql/) database instance. ClearDB has a free tier for simple testing, while Compose has tiers for larger workloads.

- For [ClearDB](https://console.ng.bluemix.net/catalog/services/cleardb-mysql-database/), log into the ClearDB dashboard, and select the default database created for you. Get the user, password and host information under "Endpoint Information".

- For [Compose](https://console.ng.bluemix.net/catalog/services/compose-for-mysql/), get the information from the `Service Credentials` tab in the IBM Cloud console.

Copy `template.local.env` to a new file named `local.env` and update the `MYSQL_HOSTNAME`, `MYSQL_USERNAME`, `MYSQL_PASSWORD` and `MYSQL_DATABASE` for your MySQL instance.

### 2. Create OpenWhisk actions and mappings

`deploy.sh` is a convenience script reads the environment variables from `local.env` and creates the OpenWhisk actions and API mappings on your behalf. Later you will run these commands yourself.

```bash
./deploy.sh --install
```

> **Note**: If you see any error messages, refer to the [Troubleshooting](#troubleshooting) section below. You can also explore [Alternative deployment methods](#alternative-deployment-methods).

### 3. Test API endpoints

There are four helper scripts that simulate HTTP API clients to create, get, update and delete entities against the `/v1/cat` endpoint.

```bash
# POST /v1/cat {"name": "Tarball", "color": "Black"}
client/cat-post.sh Tarball Black

# GET /v1/cat?id=1
client/cat-get.sh 1 # Or whatever integer ID was returned by the command above

# PUT /v1/cat {"id": 1, "name": "Tarball", "color": "Gray"}
client/cat-put.sh 1 Tarball Gray

# DELETE /v1/cat?id=1
client/cat-delete.sh 1
```

### 4. Delete actions and mappings

Use `deploy.sh` again to tear down the OpenWhisk actions and mappings. You will recreate them step-by-step in the next section.

```bash
./deploy.sh --uninstall
```

## Resources

- [Words into Action guidelines: Build back better in recovery, rehabilitation and reconstruction](https://www.unisdr.org/we/inform/publications/53213)
- [Sendai Framework Priority 4: Build Back Better](https://www.youtube.com/watch?v=mRTlS3ZfljM)
- [Building Back Better: How to Cut Natural Disaster Losses by a Third](https://www.worldbank.org/en/news/press-release/2018/06/18/building-back-better-how-to-cut-natural-disaster-losses-by-a-third)

## License

This solution starter is made available under the [Apache 2 License](LICENSE).
