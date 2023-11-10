Properties 
#recommendation-systems #programming-level-1-2 #algorithms

# Recommendation systems
Popularity and "Likes"

This type of paradigm is makes a suggestion based on how many people "like" the entity.

One prime example of this, is the like button (heart) in Instagram. When you click on the heart button, Instagram records it somewhere along the other data like demographic and psychographic information. With this information, they might suggest to other users similar to you, products and services that you like. 

We implemented the Popularity/Likes paradigm with our Favourite Bubble Tea activity. 

## N-Point Rating system

N-point rating systems are used by many services particularly Amazon.

An example of an N-point rating system would be Amazon's product review system using stars.  
	The system is rated using from 1-5 stars, with 5 stars being the highest and 1 star being the lowest. 

This paradigm provides more granular information. Buyers are asked to rate the product using a 5-point scale. 


## Similarity Score Algorithm

Amazon, Meta, Netflix all use similarity scores to help drive and keep users on their platforms. 

	Example
	Amazon likes

> Ubial likes [""]
> Ubial likes ["nintendo switch", "usb pd chargers", 4k blu ray movies"]
> Ben likes ["nintendo switch", "usb pd chargers", "lego"] 
> Fido likes ["lego", "chew toys", "fuzzy slippers"]

#### figure out a way to compare the similarities between each person and then transfer the similarity score to python

#### Similarity scores indicate how similar two people are to each other. Ben and Ubial have a similarity score of 2 (they like two things that are the same.) Ubial and Fido have a similarity score of 0. Ben and Fido have a similarity score of 1. 














