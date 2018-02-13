#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(lubridate)

ui <- fluidPage(
   
   titlePanel("Date Calculation in Singapore Date format"),
   
   sidebarLayout(
      sidebarPanel(
        dateInput("dated", "Start Date", format = "dd/mm/yyyy"),
        numericInput("numer", "Number of Days/Weeks/ Months", 2),
        selectInput("Typeofdate", "Select Days/Weeks/Months", 
                    c("Days", "Weeks", "Months"), selected = "Weeks")
      ),
      
      mainPanel(
        h4(textOutput("change_date_1"))
        
      )
   )
)


server <- function(input, output) {
  final_date <- reactive({
    ifelse(input$Typeofdate == "Days", as.character(input$dated + days(input$numer)),
           ifelse(input$Typeofdate == "Weeks", as.character(input$dated + weeks(input$numer)),
                  ifelse(input$Typeofdate == "Months", as.character(input$dated %m+% months(input$numer)), "")))
    
  })
  
 final_date_1 <- reactive({
   paste(substr(final_date(), 9, 10), substr(final_date(), 6,7), substr(final_date(), 1,4), sep = "/")
 })
  
 output$change_date_1 <- renderText({
     paste("End Date: " , final_date_1())
})

}

shinyApp(ui = ui, server = server)

