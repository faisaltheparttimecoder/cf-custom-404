# Introduction

Example on how to setup up a custom 404 page on cloud foundry foundation if the app route does not exists.

# Setup

+ clone the repo

```
git clone https://github.com/faisaltheparttimecoder/cf-custom-404.git
```

+ Login to the CF foundation.

```
cf login -a https://api.<domain-name>
```

+ Push the app to the CF 

```
cf push
```

+ Now map all the non existing route to this app.

```
cf map-route Page404 <domain-name> -n "*"
```

+ Now any non existing app will receive this custom 404 page.
