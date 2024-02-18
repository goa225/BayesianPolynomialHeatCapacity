# Amanda Gin
# agin@colostate.edu
# MATH435 Project 1

# https://github.com/goa225/MnHeatCapacity

# BAYESIAN POLYNOMIAL REGRESSION OF MAGNETIC-FIELD-DEPENDENT HEAT CAPACITY IN 
# MONONUCLEAR ENCAPSULATED Mn(II) COMPLEXES


# # Adapted from https://rpubs.com/SergioMarrero/352161

# Requires base, cmdstanr, datasets, devtolls, digest, graphics, grDevices, 
# methods, parallel, posterior, rethinking, stats, usethis, and utils packages.

## Load Heat Capacity Data and Plot on Original Log Scales
d <- read.csv("/Users/amandagin/Downloads/HeatCapacity_0T.csv")
str(d)
plot(HeatCap ~ Temperature, data = d, log='xy', xlab="Temperature (K)", 
     ylab=parse(text='Heat~Capacity~"(J"~mol^{-1}~K^{-1}*")"'),lwd=0,pch=6)
points(d$Temperature[1:30], d$HeatCap[1:30], col = "blue",lwd=1.5,pch=6)
points(d$Temperature[31:60], d$HeatCap[31:60], col = "orange",lwd=1.5,pch=6)
points(d$Temperature[61:90], d$HeatCap[61:90], col = "green",lwd=1.5,pch=6)
legend("bottomright", legend = c("1","2","3"), col = c("blue","orange","green"), pch = 6)
title(main = "0 T")

# # Standardize Temperature Data & Plot
d$Temperature.s <- (d$Temperature - mean(d$Temperature)) /sd(d$Temperature)
plot(HeatCap ~ Temperature.s, data = d, lwd=0,pch=6)
points(d$Temperature.s[1:30], d$HeatCap[1:30], col = "blue",lwd=1.5,pch=6)
points(d$Temperature.s[31:60], d$HeatCap[31:60], col = "orange",lwd=1.5,pch=6)
points(d$Temperature.s[61:90], d$HeatCap[61:90], col = "green",lwd=1.5,pch=6)
legend("bottomright", legend = c("1","2","3"), col = c("blue","orange","green"), pch = 6)
title(main = "0 T Normalized")

# # Fitting the Data with Cubic Regression
d$Temperature.s2 <- d$Temperature.s^2
d$Temperature.s3 <- d$Temperature.s^3

m4.6 <- map(
  alist(
    HeatCap ~ dnorm(mu, sigma),
    mu <- a + b1*Temperature.s + b2*Temperature.s2 + b3*Temperature.s3,
    # Set your priors here
    a ~ dnorm(0,10),
    b1 ~ dnorm(0,10),
    b2 ~ dnorm(0,10),
    b3 ~ dnorm(0,10),
    sigma ~ dunif(0, 1)), 
  data = d)

# Table Summary 
precis(m4.6, corr = TRUE)

# Plot Cubic Regression
Temperature.seq <- seq(from = -2, to = 2.6, length.out = 30)
pred_dat <- list(Temperature.s = Temperature.seq, Temperature.s2 = Temperature.seq^2, Temperature.s3 = Temperature.seq^3 )
mu <- link(m4.6 , data = pred_dat)
mu.mean <- apply(mu, 2, mean)
mu.PI <- apply(mu, 2, PI, prob = 0.95)
sim.HeatCap <- sim(m4.6, data = pred_dat)
HeatCap.PI <- apply(sim.HeatCap, 2, PI, prob = 0.95)
  # Convert axis back to original
plot(HeatCap ~ Temperature.s, d, pch=6, lwd=0, xaxt="n",
     xlab="Temperature (K)", ylab=parse(text='Heat~Capacity~"(J"~mol^{-1}~K^{-1}*")"'))
points(d$Temperature.s[1:30], d$HeatCap[1:30], col = "blue",lwd=1.5,pch=6)
points(d$Temperature.s[31:60], d$HeatCap[31:60], col = "orange",lwd=1.5,pch=6)
points(d$Temperature.s[61:90], d$HeatCap[61:90], col = "green",lwd=1.5,pch=6)
legend("bottomright", legend = c("1","2","3"), col = c("blue","orange","green"), pch = 6)
title(main = "0 T Cubic Model")
at <- c(-2, -1, 0, 1, 2)
labels <- at*sd(d$Temperature) + mean(d$Temperature)
axis(side = 1, at = at, labels = round(labels,1))
lines(Temperature.seq, mu.mean)
shade(mu.PI, Temperature.seq, col = "red")
shade(HeatCap.PI, Temperature.seq)

# # Fitting the Data with Quadratic Regression
d$Temperature.s2 <- d$Temperature.s^2
d$Temperature.s3 <- d$Temperature.s^3
d$Temperature.s4 <- d$Temperature.s^4

m4.7 <- map(
  alist(
    HeatCap ~ dnorm(mu, sigma),
    mu <- a + b1*Temperature.s + b2*Temperature.s2 + b3*Temperature.s3 + b4*Temperature.s4,
    # Set your priors here
    a ~ dnorm(0, 10),
    b1 ~ dnorm(0, 10),
    b2 ~ dnorm(0, 10),
    b3 ~ dnorm(0, 10),
    b4 ~ dnorm(0, 10),
    sigma ~ dunif(0, 1)), 
  data = d)

# Table Summary 
precis(m4.7, corr = TRUE)

# Plot Quadratic Regression
Temperature.seq <- seq(from = -2, to = 2.6, length.out = 30)
pred_dat <- list(Temperature.s = Temperature.seq, Temperature.s2 = Temperature.seq^2, Temperature.s3 = Temperature.seq^3, Temperature.s4 = Temperature.seq^4)
mu <- link(m4.7 , data = pred_dat)
mu.mean <- apply(mu, 2, mean)
mu.PI <- apply(mu, 2, PI, prob = 0.95)
sim.HeatCap <- sim(m4.7, data = pred_dat)
HeatCap.PI <- apply(sim.HeatCap, 2, PI, prob = 0.95)
# Convert axis back to original
plot(HeatCap ~ Temperature.s, d, pch=6,lwd=0, xaxt="n",
     xlab="Temperature (K)", ylab=parse(text='Heat~Capacity~"(J"~mol^{-1}~K^{-1}*")"'))
points(d$Temperature.s[1:30], d$HeatCap[1:30], col = "blue",lwd=1.5,pch=6)
points(d$Temperature.s[31:60], d$HeatCap[31:60], col = "orange",lwd=1.5,pch=6)
points(d$Temperature.s[61:90], d$HeatCap[61:90], col = "green",lwd=1.5,pch=6)
legend("bottomright", legend = c("1","2","3"), col = c("blue","orange","green"), pch = 6)
title(main = "0 T Quadratic Model")
at <- c(-2, -1, 0, 1, 2)
labels <- at*sd(d$Temperature) + mean(d$Temperature)
axis(side = 1, at = at, labels = round(labels,1))
lines(Temperature.seq, mu.mean)
shade(mu.PI, Temperature.seq, col = "red")
shade(HeatCap.PI, Temperature.seq)