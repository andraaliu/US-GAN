# Metrics

This folder contains support code for evaluating our model.

## Face Verification Score (FVS)
Returns a score of similarity between faces. Uses [Face++ comparison API](https://console.faceplusplus.com/documents/5679308).

Notes: Currently sending images via Base64 encoding -- seems like we are limited to 64x64 images this way. If we want to send bigger images, look into ways to upload entire file, or host remotely.

## Emotion Score
TODO

## Gram matrix 
TODO