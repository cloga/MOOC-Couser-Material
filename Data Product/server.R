library(shiny)

shinyServer(
  function(input, output) {
    output$newHist <- renderPlot({
      hist(rbinom(input$n,100,input$prob), xlab='# of sucess', col='lightblue',main='Histogram')
      })
    
  }
)
