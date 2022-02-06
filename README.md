

<!-- PROJECT LOGO -->

<br />
<div align="center">
    <img src="https://www.mtpelerin.com/images/matic-coin.svg" alt="Logo" width="80" height="80">
  <h3 align="center">Polygon NFT Stats</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Application Insights</a></li>
    <li><a href="#API">API's </a></li>
    <li><a href="#ProjectLink">Project Link</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Polygon, formerly known as Matic Network, is a blockchain scalability platform 
and framework for connecting and building blockchain networks compatible
with Ethereum. The main idea behind this project to showcase what's actually happening inside the market in terms 
of NFT transactions, NFT collections, unique wallets and NFT growth. Since the real value of Polygon NFTs lies on the way market functions, 
People can start utilizing polygon in a better way by looking at the stats. 

Website link : [Polygon NFT Stats](https://share.streamlit.io/manidills/polygon_nft/main.py)


<img src="https://user-images.githubusercontent.com/91189264/152693313-38be3f76-1945-4d07-9988-b1bdc32462df.png" alt="Logo" width="1300" height="550">


<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

The frameworks/libraries explicitly used in this project are

* [Python](python.org)
* [keras](https://keras.io/)
* [pillow](https://pillow.readthedocs.io/en/stable/)
* [sklit_learn](https://scikit-learn.org/stable/)
* [streamlit](https://streamlit.io/)
* [streamlit-aggrid](https://pypi.org/project/streamlit-aggrid/)
* [requests](https://docs.python-requests.org/en/latest/)


<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

Follow these steps to install certain packages which is to be installed in this project also make your own 
API key from covalent to get access for data.

## Home page data is not complete polygon data, we can take it as approx 

1. Get a free API Key from [covalent](https://www.covalenthq.com/) and [NFT Port](https://www.nftport.xyz/)
2. Clone the repo
3. streamlit run main.py

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* altair==4.2.0
* hydralit==1.0.11
* keras==2.8.0
* numpy==1.22.1
* pandas==1.4.0
* pillow==9.0.1
* requests==2.22.0
* scikit_learn==1.0.2
* streamlit==1.4.0
* streamlit-aggrid



## Usage

The chain polygon is covered in this application with general information and predictions.
Volume exchanges per day, unique wallets per day, collection-wise unique wallets and volume, and 
so on are all included in the forecast. This will provide a clear statistic to NFT traders and buyers. 
As a result, they will be able to invest according to market conditions. This also provides a graphical view of 
how the chain works over time and how the market fluctuates.


* The home page represents the total volume and wallet prediction across the chain polygon by line chart and includes a few key metrices 
like Total volume, Average daily volume, and Average weekly volume. Time series forecasting model was built here to predict the number(LSTM).

* The collection page depicts  the overall volume and wallet prediction across all collections in the chain polygon by line chart; for example, 
we've provided a few key metrics and predictions of volume and wallet over the period of time for Chicken Derby. The metrices includes total volume, average daily volume, and average weekly volume.

* The Token page displays a list of unique tokens, tokens that are frequently traded, tokens that are sold in large quantities, and so on. 
We've also included the current owner of the token id, as well as the characteristics of the Top 4 most sold tokens by volume throughout each collection.

* The wallet page displays a list of unique wallets, as well as the top seller by volume, tokens top seller by volume, and total transactions, 
among other information. We've also compiled a list of the top 100 wallet-to-wallet transactions in the chain polygon.

* Duplicate page shows the near duplicate token minted in the same nft collections or other.

* The state page includes all of the collectios across the chain polygon, along with the market cap, transaction count, and floor price,etc.

<img src="https://user-images.githubusercontent.com/91189264/152693486-79f0d69f-077d-432d-812d-4a15a017b133.png" alt="Logo" width="1300" height="550">


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## API

We have used API's from covalent and Nft Port for listing transcation details, collection details,etc.


* COVALENTHQ API

https://api.covalenthq.com/v1/1/tokens/0xe4605d46fd0b3f8329d936a8b258d69276cba264/nft_metadata/123/?key=ckey_docs

https://api.covalenthq.com/v1/:chain_id/nft_market/?&key=

https://api.covalenthq.com/v1/:chain_id/nft_market/collection/:collection_address/?&key=

https://api.covalenthq.com/v1/:chain_id/tokens/:contract_address/nft_transactions/:token_id/?&key=

* NFTPORT API

https://api.nftport.xyz/v0/accounts/address

https://api.nftport.xyz/v0/duplicates/tokens

## ProjectLink


Project Link: (https://github.com/Manidills/polygon_NFT/blob/master)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

Would like to give credit to below teams for providing the API's

* [Covalent](https://www.covalenthq.com/)
* [NFT Port](https://www.nftport.xyz/)

<p align="right">(<a href="#top">back to top</a>)</p>





