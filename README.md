# Playing around with the Bluesky Python SDK

The [Python SDK](https://atproto.blue/en/latest/index.html) for the Bluesky app is nice! You'll want to some brief reading on how the API for the `AppView` works versus [AtProto Reference](https://atproto.com/guides/overview). Fundamentally the data is all stored in PDSes that are aggregated by a Relay which streams a firehose for different apps to consume. 

One of the best ways to understand the different data structures underlying any given account is to [use this app](https://atproto-browser.vercel.app/) and play around with it using your account. 

## Instructions

1. Get your bluesky username and password and add them to a `.env` file (see the `.env.example` file for structure)
2. pip/uv install dependencies from `pyproject.toml`
3. Hit the API by running data on your follower/follow graph to start with
4. Check the available endpoints. 






