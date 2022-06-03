# THIS APP WILL RESIDE IN ONE FILE BUT BIGGER APPS NEED SEPARATE UI AND SERVER SECTIONS
# WRITTEN BY MICHAEL.
# USED TO ANALYZE DOG BREEDS IN COMPARISON TO EACH OTHER.
# LOAD REQUIRED LIBRARIES.

# runApp("~/Documents/dogBreed/")  data1 <- melt(id= "Breed", breed_traits)
library(shiny)
library(shinydashboard)
library(dplyr)
library(ggplot2)
library(reshape2)

#pull the dataset
breed_traits <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-02-01/breed_traits.csv')
write.csv(breed_traits,"breed_traits.csv")
breed_traits <- read.csv("breed_traits.csv")
breed_traits <-data.frame(breed_traits)

my_css <- "
 h1 {
        font-weight: bold; font-size : 15px;
 }
#compare{padding:5px 70px; 
    background:yellow; 
    border:0 none;
    cursor:pointer;
    -webkit-border-radius: 5px;
    border-radius: 5px; 
    font-weight: bold;
    align:center;
}

#dogplot{background:black; font-weight: bold; font-size : 15px}
"

 # add this after title within UI tags$style(my_css)



header <- dashboardHeader(title = h1("DOG BREED ANALYTICS"))

sidebar <- dashboardSidebar(
  selectInput('dogbreed', 'Select two Dog Breeds', choices = unique(breed_traits$Breed),multiple = TRUE, selected = c("Retrievers (Labrador)","French Bulldogs")),
  #picked only numeric class variables for this drop down
  selectInput('dogbreed_x', 'Select Dog Breed Features', choices = colnames(breed_traits)[c(3:8,11:length(colnames(breed_traits)))],selected = c("Affectionate.With.Family","Good.With.Young.Children"),multiple = TRUE),
  br(), 
  actionButton("compare", "COMPARE")
  )

body <- dashboardBody(
  fluidRow(
    valueBox(
      width = 6,
      value = textOutput('dogA_star'), 
      subtitle = textOutput('dogA'), 
      icon = icon("dog"), color = "green"
    ),
    valueBox(
      width = 6,
      value = textOutput('dogB_star'), 
      subtitle = textOutput('dogB'),
      icon = icon("dog"), color = "yellow"
    )
  ),
  fluidRow(
  mainPanel(width = 12,
    tabsetPanel(
      tabPanel('Table', DT::DTOutput('dogtable')),
      tabPanel('Plot', plotOutput('dogplot')))
)))


# Create the UI using the header, sidebar, and body
ui <- dashboardPage(
  tags$head(
    tags$style(my_css
    )
  ),
  
  skin = "black",header = header,
                    sidebar = sidebar,
                    body = body)

server <- function(input, output) {
 checks <- reactive({
  validate(
    need(
      input$dogbreed_x != "Coat Type" | input$dogbreed_x != "Coat Length", 
      "Make a selection of Numeric variables for Now..."
    )
  )})

  data <- reactive({
    breed_filtered = subset(breed_traits, Breed %in% input$dogbreed)%>%select('Breed', input$dogbreed_x)
    
  })
  
  output$dogA <- renderText({
    data.frame(data())[1,"Breed"]
  })
  
  output$dogB <- renderText({
    data.frame(data())[2,"Breed"]
  })
  

  output$dogA_star <-renderText({
    input$compare
    isolate({
      
      N = length(colnames(data()))
      total_star1 = sum(data()[1,c(2:N)])
      total_star1 = paste(total_star1, "Points")
    })
    
  })
  

  output$dogB_star <-renderText({
    input$compare
    isolate({
      N = length(colnames(data()))
      total_star2 = sum(data()[2,c(2:N)])
      total_star2 = paste(total_star2, "Points")
    })
    
  })
  
  
  output$dogtable <- DT::renderDT({
    input$compare
    isolate({
      data()

    })
    
  })
  
  output$dogplot <- renderPlot({
    input$compare
    isolate({
      df <- melt(data(),id="Breed")
      g <- ggplot(df, aes(x=Breed, y=value ))+geom_point()+facet_grid(cols = vars(factor(variable))) 
      g+theme_bw()
      
    })
    
  })
}

shinyApp(ui, server)