server <- function(input, output) { 

  mypdf <- reactive({
      req(input$file1)
      req(input$id_no)
      
      my_mpesa <- pdftools::pdf_text(input$file1$datapath, upw = input$id_no)
      mpesa_split <-str_split(my_mpesa, fixed("\n"))
      airtime <- lapply(mpesa_split, str_subset, pattern = "Airtime Purchase")
      
      if(length(airtime)>=1){
      date_bought <- extract_dates(airtime)
      amount_bought <- airtime_and_others(airtime)
      amt_date= combine_dateAmount(date_bought, amount_bought)
      amt_df = time_categories(amt_date)
      }
  })
  
  output$pdf_view<-renderTable({
    mypdf()
  })
  
  output$mpesa_plot <-renderPlot({
    ggplot(mypdf(), aes(x=date_bought, y=whatis_bought, color = time_category))+geom_point()
  })

  
  
  
  }

