library(shiny)
shinyUI(pageWithSidebar(
  headerPanel("Binomial Distribution Histogram"),
  sidebarPanel(    
    sliderInput('n', 'Number of Observations',value = 30, min = 5, max = 100, step = 5,),
    sliderInput('prob', 'Probability',value = 0.5, min = 0.1, max = 0.9, step = 0.1,),
    p('A simple App to imitate binomial distribution.'),
    p('number of trials is 100.'),
    p('You could slide bar below to change number of observations & probability.'),
    p('Have a fan!')
  ),
  mainPanel(
    plotOutput('newHist')
  )
))
