from rpy2.robjects.packages import importr, data
utils = importr('utils')
base = importr('base')
#utils.install_packages('stats')
#utils.install_packages('lme4')
stats = importr('stats')
lme4 = importr('lme4')