## app.R ##
library(shiny)
library(shinydashboard)

ui <- dashboardPage(
  dashboardHeader(title = "Mpesa stat"),
  dashboardSidebar(
    menuItem("About Mpesa stat", tabName = "about", icon = icon("home")),
    menuItem("Upload pdf", tabName = "upload_pdf", icon = icon("upload")),
    menuItem("Analyze", tabName = "analyze", icon = icon("bar-chart-o")),
    menuItem("Export", tabName = "widgets", icon = icon("database"))
  ),
  dashboardBody(
    tabItems(
      tabItem(tabName = "upload_pdf", h2("Uploading your Mpesa Statement"),
              # Input: Select a file ----
              fileInput("file1", "Choose PDF File",
                        multiple = FALSE,
                        accept = c("text/pdf",
                                   ".pdf")),
              passwordInput("id_no", label = "Mpesa Statement Password",value = 27196363),
              tabsetPanel(
                tabPanel("View",
                         fluidPage(column(width=11,box(tableOutput("pdf_view"))))
                  
                )
              )
              
              ),
      tabItem(tabName = "analyze",
              
              tabsetPanel(
                tabPanel("Mpesa Statement Analytics",
                         
                         fluidPage(fluidRow(
                                            box(selectInput("select_KP1",label = h4("Select a Category"),
                                                            choices = c("Airtime purchases", "Bundle purchases","PayBills","Till payments","Funds transfer to","Funds received from"), selected = "Airtime purchases"), width = 6, status = "info")),
                                   fluidRow(column(width=11,
                                                   box(plotOutput("mpesa_plot"),width = NULL, status = "info"),
                                                   box(htmlOutput("text1"), width = NULL, background = "teal"),
                                                   downloadButton("download_all_websiteKPIs_data", "Download All KPIs Data")))))
              )
              
              
              
              
              
              
              )
      
    
    )
    
    
  )
)




