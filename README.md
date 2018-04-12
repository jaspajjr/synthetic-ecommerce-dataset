# Synthetic eCommerce Dataset

As the name suggests this is not a real dataset. However I often find that my dev work would be easier if I had a dataset which had similar features to those that occur in actual eCommerce environments. 

I'm going to add a few more things into this:
    - Customer ID
    - Instructions on how to build and run, and save a csv using docker
    - More user agent fields

I'm open to suggestions and pull requests. This data is completely made up, use at your own risk.

`docker build -t dataset-generation .`
`docker run -it -v $(pwd):/output dataset-generation`