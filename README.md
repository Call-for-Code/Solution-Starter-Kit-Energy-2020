# Energy sustainability in the context of climate change

This solution starter was initially created at the United Nations Human Rights Office in Geneva, Switzerland on February 27-28, 2020, and built out over following 4 weeks. It features contributions by technologists from JPMorgan Chase, Persistent Systems, IBM, and Red Hat.

## Authors

* Vincent Batts - Red Hat
* Binu Midhun - IBM
* Mark Meiklejohn - JPMorgan Chase
* Roberto Mosqueda - Persistent Systems
* Henry Nash - IBM

## Contents

1. [Overview](#overview)
1. [Video](#video)
1. [The idea](#the-idea)
1. [How it works](#how-it-works)
1. [Diagrams](#diagrams)
1. [Documents](#documents)
1. [Datasets](#datasets)
1. [Technology](#technology)
1. [Getting started](#getting-started)
1. [Resources](#resources)
1. [License](#license)

## Overview

### What's the problem

As the population grows, so does the demand for energy. Fossil fuels like coal, oil, and gas have exacted an enormous toll on the environment — from air and water pollution to climate change. By investing in solar, wind, and thermal power, improvements in energy productivity and expanding infrastructure is key to providing clean and more efficient energy.

Read about the [UN Sustainable Development Goal on affordable and clean energy](https://www.undp.org/content/undp/en/home/sustainable-development-goals/goal-7-affordable-and-clean-energy.html).

While the switch to clean energy in our homes will make a real and important impact to the climate, energy usuage in the commercial sector is often higher than in the domestic sector (i.e. that used in homes). A key part of this commercial energy consumption goes into making products that we buy. However, while some products we buy come with an [Energy-efficiency rating](https://ec.europa.eu/info/energy-climate-change-environment/standards-tools-and-labels/products-labelling-rules-and-requirements/energy-label-and-ecodesign/about_en) (e.g. how much energy will my washing machine consume when I use it?), there is nothing provided in terms of the amount of energy (and type of energy, i.e. fossil vs renewable) that was used to manufacture the product in the first place. In fact, if you think about it, to minimize the impact on the climate of prouducts you buy, it would be great to be able to compare the *climate impact* across different manufactures' products. To be complete, this climate impact comparison might also include other things outside of energy - eg. water consumption. What is really needed is a comprehensive *Climate Impact Rating* for products, that can be presented to a consumer as some kind of labelling system.

### How can technology help

Whether it's third-party open source projects or IBM Cloud services, technologies like data analytics, visualization, Internet of Things, Open APIs, databases and blockchain can help address global environmental challenges to track energy (and other consumables) that go into making prodcts. Enabling us to select products that have the lowest climate impact can have a real reduction in our personal impact on the planet.

## Video

[ replace this with Binu's video]

[![Call for Code Solution Starter: Water sustainability in the context of climate change](https://img.youtube.com/vi/hC2b-iP6Rxc/0.jpg)](https://www.youtube.com/watch?v=hC2b-iP6Rxc)

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

This solution starter idea provides a basic architecture of you to experiment within any of the categories above, and includes:

* A CouchDB NoSQL database layer holding both individual product rating, as well as sumamry data
* A basic API server that allows data to insert and extract data from the database. This API is expressed as a Swagger (OpenAPI) document, so you can build your own clients.
* Deployment tools to stand up the above on the IBM Cloud, within the free-tier plan (i.e. so it is free for you to experiment)

The database is populated with some inital example data, to get you started.

[ Need to add someting about summary data here, dpending on what Binu comes up with ]

## Diagrams

![Cloud Impact Rating Starter Architecture](TBA?raw=true "Cloud Impact Rating Starter Architecture")

## Documents

* [Data Tools & Maps](https://www.eia.gov/tools/)
* [Existing Energystar Ratings System](https://www.energystar.gov/)
* [EU Energy Ratings System](https://ec.europa.eu/info/energy-climate-change-environment/standards-tools-and-labels/products-labelling-rules-and-requirements/energy-label-and-ecodesign/about_en)
* [Traffic Light Food Labelling](https://en.wikipedia.org/wiki/Traffic_light_rating_system)

## Datasets

* [World consumption averages, and break down per capita](https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption)
* [Power plant information](https://www.eia.gov/state/maps.php)

## Technology

* TBA

## Getting started

### Prerequisites

You should have a basic understanding of calling APIs via http. You could also learn more about using [Swagger/OpenAPI](https://swagger.io/docs/specification/about/).

Also, you'll need an [IBM Cloud account](https://cloud.ibm.com), with the latest IBM Cloud tools on your local machine.

### Steps

1. [Provision a CouchDB instance using Cloudant](#1-provision-mysql)
1. [Deploy the API server to the IBM Cloud](#2-create-openwhisk-actions-and-mappings)
1. [Test API endpoints](#3-test-api-endpoints)

### 1. Provision a CouchDB instance using Cloudant

Log into the IBM Cloud and provision a [CouchDB instance using Cloudant](TBD). Cloudant has a free tier for simple testing.

[add more here]

### 2. Deploy the API server to the IBM Cloud

`deploy.sh` is a convenience script reads the environment variables from `local.env` that.....

```bash
./deploy.sh --install
```

### 3. Test API endpoints

There are helper scripts that simulate HTTP API clients to create, get, update and delete entities against the `/v1/cir` endpoint.

```bash
# GET /v1/cir?barcode=1
client/cat-get.sh 1
```

## Resources

* TBA

## License

This solution starter is made available under the [Apache 2 License](LICENSE).
