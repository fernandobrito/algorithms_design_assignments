library(ggplot2)

setwd("~/ufpb/sorting/dynamic_greedy_lib/metaheuristics/r_scripts")
data <- read.csv('../output/output.txt', sep = ';')

qplot(data=data, x=iteration, y=rpd)
qplot(data=data, x=iteration, y=temperature)
# ggplot(data, aes(iteration, rpd)) + geom_point()
