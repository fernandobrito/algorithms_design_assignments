library(ggplot2)
library(reshape)

setwd("~/ufpb/sorting/dynamic_greedy_lib/metaheuristics/r_scripts")
data <- read.csv('../output/output.txt', sep = ';')

meltedData = melt(data[c('iteration','rpd','temperature')], id='iteration')

qplot(data=data, x=iteration, y=rpd)
qplot(data=data, x=iteration, y=temperature)
# ggplot(data, aes(iteration, rpd)) + geom_point()

ggplot(data, aes(x = iteration)) + 
    geom_line(aes(y = rpd)) + 
    geom_line(aes(y = temperature)) + 
    ylab(label="") + 
    xlab("Iteration")

ggplot(meltedData, aes(x = iteration, y = value, colour = variable)) + 
    geom_line() +
    ylab("Distance from optimal solution (red) and temperature (blue)")
    xlab("# Iteration")