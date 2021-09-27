from libraries import *
from credentials import *

#Specify date range below it is daily by default. You can change to 'weekly'

def ga_Query_Calls(duration='daily'):
  start_date, end_date= date_range(duration)
  

  #sessions
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:sessions'}], 
          }]
        }
    ).execute()

  sessions = get_report(analytics,start_date,end_date)



  #users
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:users'}], 
          }]
        }
    ).execute()

  users = get_report(analytics,start_date,end_date)


  #entrances

  #users
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}], 
          }]
        }
    ).execute()

  entrances = get_report(analytics,start_date,end_date)


  print(entrances)


  #Organic search channel sessions


  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{'name': 'ga:channelGrouping'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  sessions_by_Organic_search  = get_report(analytics,start_date,end_date)

  print(sessions_by_Organic_search)

  #Organic search channel users
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:newUsers'}],
            'dimensions': [{'name': 'ga:channelGrouping'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  users_by_Organic_search  = get_report(analytics,start_date,end_date)

  print(users_by_Organic_search)



  #Organic search entrances

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:channelGrouping'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  entrances_by_Organic_search  = get_report(analytics,start_date,end_date)

  print(entrances_by_Organic_search)


  #Paid Search entrances
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:channelGrouping'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Paid Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  entrances_paid  = get_report(analytics,start_date,end_date)

  print(entrances_paid)

  #Paid Social entrances
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:channelGrouping'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Social"
                  ]
              }]}]


          }]
        }
    ).execute()


  entrances_social  = get_report(analytics,start_date,end_date)

  print(entrances_social)

  # sessions of landing page
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{"name": "ga:landingPagePath"}]
            
          }]
        }
    ).execute()

  sessions_landpage = get_report(analytics,start_date,end_date)

  # users of landing page
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:users'}],
            'dimensions': [{"name": "ga:landingPagePath"}]
            
          }]
        }
    ).execute()

  users_landpage = get_report(analytics,start_date,end_date)


  # entrances of landing page
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{"name": "ga:landingPagePath"}]
            
          }]
        }
    ).execute()

  entrances_landpage = get_report(analytics,start_date,end_date)

  #sessions from various URLS of interest

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{'name': 'ga:pagePath'}]



          }]
        }
    ).execute()

  sessions_by_urls  = get_report(analytics,start_date,end_date)


  #users by urls
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [ {'expression': 'ga:users'}],
            'dimensions': [{'name': 'ga:pagePath'}]



          }]
        }
    ).execute()

  users_by_urls  = get_report(analytics,start_date,end_date)

  #entrances by urls
  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [ {'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:pagePath'}]



          }]
        }
    ).execute()

  entrances_by_urls  = get_report(analytics,start_date,end_date)

  #Organic search entrances Destination pages

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:pagePath'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  organic_entrances_url  = get_report(analytics,start_date,end_date)


  #Organic search sessions page url

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{'name': 'ga:pagePath'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  organic_sessions_url  = get_report(analytics,start_date,end_date)


  #Organic search entrances page url

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:entrances'}],
            'dimensions': [{'name': 'ga:pagePath'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  organic_entrances_url  = get_report(analytics,start_date,end_date)



  #Organic search users page url

  def get_report(analytics,start,end):
    return analytics.reports().batchGet(
        body={
          'reportRequests': [
          {
            'viewId': VIEW_ID,
            'pageSize': 10000,
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'metrics': [{'expression': 'ga:users'}],
            'dimensions': [{'name': 'ga:pagePath'}],
            "dimensionFilterClauses":[{
                  "filters":[{
                  "dimensionName":"ga:channelGrouping",
                  "operator":"EXACT",
                  "expressions":[
                  "Organic Search"
                  ]
              }]}]


          }]
        }
    ).execute()

  organic_users_url  = get_report(analytics,start_date,end_date)

  





  READY_TO_CREATE_DATAFRAMES =True

  if READY_TO_CREATE_DATAFRAMES:
    print("**********************************************")
    print("--- ALL REQUIRED DATA PULLED SUCCESSFULLY---")
    print("**********************************************")

  #----------------------- Perform data aggregation------------------------------------------------------
  #single value output for various metrics  --PART A
  sessionVal = single_metric_output(sessions, "sessions")
  usersVal = single_metric_output(users, "users")
  entrancesVal = single_metric_output(entrances, "entrances")
  sessionsOrganicVal =single_metric_output(sessions_by_Organic_search, "sessions")
  usersOrganicVal =single_metric_output(users_by_Organic_search, "users")
  entrancesOrganicVal = single_metric_output(entrances_by_Organic_search, "entrances")
  entrancesPaidVal = single_metric_output(entrances_paid, "entrances")
  entrancesSocialVal = single_metric_output(entrances_social, "entrances")

  #sessions landing page with virtual --- PART B
  sessionsLandpage_df = single_metric_single_dimension_output(sessions_landpage,"session", "url")
  SessionslandPageWithVirtual_dict = landing_page_include_virtual(sessionsLandpage_df)
  SLPV = SessionslandPageWithVirtual_dict['landingPage containing virtual']
  ExcludingVirtualVal_sessions = int(sessionVal)- SLPV
  #users_landingpagewithvirtual
  usersLandpage_df = single_metric_single_dimension_output(users_landpage,"users", "url")
  UserslandPageWithVirtual_dict = landing_page_include_virtual(usersLandpage_df)
  ULPV = UserslandPageWithVirtual_dict['landingPage containing virtual']
  ExcludingVirtualVal_users = int(usersVal)- ULPV
  #Entrances land page virtual
  entranceLandpage_df = single_metric_single_dimension_output(entrances_landpage,"entrances", "url")
  entranceslandPageWithVirtual_dict = landing_page_include_virtual(entranceLandpage_df)
  ELPV = entranceslandPageWithVirtual_dict['landingPage containing virtual']
  ExcludingVirtualVal_entrances = int(entrancesVal)- ELPV

  #sessions organic search excluding virtual -organic_sessions_url

  session_organic_pagepath_df = single_metric_single_dimension_output(organic_sessions_url,"sessions", "url")

  session_organic_pagepathWithVirtual_dict = landing_page_include_virtual(session_organic_pagepath_df)
  SOIV = session_organic_pagepathWithVirtual_dict['landingPage containing virtual']
  SOEV = int(sessionsOrganicVal) - SOIV

  #uentrances organic search excluding virtual - organic_entrances_url

  entrances_organic_pagepath_df = single_metric_single_dimension_output(organic_entrances_url,"entrances", "url")

  entrances_organic_pagepathWithVirtual_dict = landing_page_include_virtual(entrances_organic_pagepath_df)
  EOIV = entrances_organic_pagepathWithVirtual_dict['landingPage containing virtual']
  EOEV = int(entrancesOrganicVal) - EOIV

  #users organic search excluding virtual
  users_organic_pagepath_df = single_metric_single_dimension_output(organic_users_url,"users", "url")

  users_organic_pagepathWithVirtual_dict = landing_page_include_virtual(users_organic_pagepath_df)
  UOIV = users_organic_pagepathWithVirtual_dict['landingPage containing virtual']
  UOEV = int(usersOrganicVal) - UOIV


  # All the destination queries ---------PART C
  sessionDestinationdf  = single_metric_single_dimension_output(sessions_by_urls,"sessions", "url")
  usersDestinationdf  = single_metric_single_dimension_output(users_by_urls,"users", "url")
  entrancessDestinationdf  = single_metric_single_dimension_output(entrances_by_urls,"entrances", "url")


  destinations = ['colorado','new-york-city','hawaii','new-orleans','asheville','tennessee','gatlinburg',
                  'nashville', 'florida', 'orlando','key-west','miami','st-augustine','georgia','savannah',
                  'atlanta', 'chicago', 'seattle','ohio','cincinnati','oregon','portland','las-vegas',
                  'california','san-francisco','san-diego', 'lake-tahoe','big-sur','idaho','boise','sun-valley',
                  'texas','houston','dallas','austin','washingtondc','arizona','sedona','grand-canyon']
  SessionDestination_dict = destination_data(destinations, sessionDestinationdf)
  usersDestination_dict = destination_data(destinations, usersDestinationdf)
  entrancesDestination_dict = destination_dataEntrance(destinations, entrancessDestinationdf)

  # Organic entrances to all pages with elopement-packages/ -- Destination pages  ---PART D
  entrancesOrganic_url_df = single_metric_single_dimension_output(organic_entrances_url,"entrances", "url")
  destPagesEntrance_dict = elopement_packages(entrancesOrganic_url_df, 'elopement-packages/')
  DPVal = destPagesEntrance_dict['Destination Pages entrances']


  # Table Names 
  virtual_column_names = ['from_date', 'to_date','metric','metric_count','segment']
  primary_metrics_colnames = ['from_date', 'to_date','metric','dimension','metric_count']
  marketwise_traffic_colnames = ['from_date', 'to_date','destination','metric','metric_count']

  # creat a dictionary to hold data for --PART A

  def primaryKPIs(myMetric, myDim, myVal):
      primary_KPIs = {}
      primary_KPIs['From'] = start_date
      primary_KPIs['To'] = end_date
      primary_KPIs['Metric'] = myMetric
      primary_KPIs['Dimension'] = myDim
      primary_KPIs['Value'] = myVal
      return primary_KPIs

  vals = [sessionVal,usersVal,entrancesVal,sessionsOrganicVal,usersOrganicVal,entrancesOrganicVal,entrancesPaidVal,entrancesSocialVal]
  mets = ["sessions", "users", "entrances","sessions","users","entrances","entrances","entrances"]
  dims = ["Total","Total","Total","Organic Search","Organic Search","Organic Search","Paid Search","Social"]



  def KPIs_dict_to_DF(mets,dims,vals):
      complete_dic = pd.DataFrame()
      for i in range(len(vals)):
          complete_dic = complete_dic.append(primaryKPIs(mets[i],dims[i],vals[i]), ignore_index=True)
      return complete_dic


          
  dataA = KPIs_dict_to_DF(mets,dims,vals)
  dataA_todb = dataA.loc[:,["From","To","Metric","Dimension","Value"]]
  dataA_todb.columns = primary_metrics_colnames



  # PART B Data
  valsB = [ExcludingVirtualVal_sessions,ExcludingVirtualVal_users,ExcludingVirtualVal_entrances]
  metsB = ["sessions", "users", "entrances"]
  dimsB = ["Excluding people who land on virtual","Excluding people who land on virtual","Excluding people who land on virtual"]

  dataB = KPIs_dict_to_DF(metsB,dimsB,valsB)
  dataB_todb = dataB.loc[:,["From","To","Metric","Dimension","Value"]]
  dataB_todb["Segment"] = dataB_todb.loc[:,["Dimension"]]
  dataB_todb = dataB_todb.drop('Dimension',axis=1)
  # Renaming columns to match database recent changes
  dataB_todb.columns = virtual_column_names


  # --- PART D DATA
  ValsD = [DPVal,SOEV,EOEV,UOEV]
  metsD = ["entrances", "sessions","entrances","users"]
  dimsD = ["Organic Search - Destination Pages", "Organic Search Non virtual","Organic Search Non virtual","Organic Search Non virtual"]

  dataD = KPIs_dict_to_DF(metsD,dimsD,ValsD)
  dataD_todb = dataD.loc[:,["From","To","Metric","Dimension","Value"]]
  dataD_todb["Segment"] = dataD_todb.loc[:,["Dimension"]]
  dataD_todb = dataD_todb.drop('Dimension',axis=1)
  dataD_todb.columns = virtual_column_names


  #PART C
  def dest_KPIs(mydate1,mydate2,mydest, myMetric, myVal):
      primary_KPIs = {}
      primary_KPIs['From'] = mydate1
      primary_KPIs['To'] = mydate2
      primary_KPIs['Destination'] = mydest
      primary_KPIs['Metric'] = myMetric
      primary_KPIs['Value'] = myVal
      return primary_KPIs


  def destination_df(dest_dict,metricKPI):
      place = []
      Value = []
      for key, val in dest_dict.items():
          #print(key,val)
          place.append(key)
          Value.append(val)
      N = len(destinations)
      From = []
      To = []
      Metric = []
      #metricKPI = "sessions"
      for i in range(N):
          From.append(start_date)
          To.append(end_date)
          Metric.append(metricKPI)
      destinationDF = dest_KPIs(From,To,place,Metric,Value)
      return destinationDF


  dict_dest1 = destination_df(SessionDestination_dict,"sessions")
  dict_dest2 = destination_df(usersDestination_dict,"users")
  dict_dest3 = destination_df(entrancesDestination_dict,"entrances")

  data1C =pd.DataFrame(dict_dest1)
  data1C = data1C.loc[:,["From","To","Destination","Metric","Value"]]
  data1C.columns = marketwise_traffic_colnames = ['from_date', 'to_date','destination','metric','metric_count']
  data2C =pd.DataFrame(dict_dest2)
  data2C = data2C.loc[:,["From","To","Destination","Metric","Value"]]
  data2C.columns = marketwise_traffic_colnames = ['from_date', 'to_date','destination','metric','metric_count']
  data3C =pd.DataFrame(dict_dest3)
  data3C = data3C.loc[:,["From","To","Destination","Metric","Value"]]
  data3C.columns = marketwise_traffic_colnames = ['from_date', 'to_date','destination','metric','metric_count']

  # part E to handle referrals urls

  def pull_url_part(urlsData, pattern='/referral/', col ="sessions"):
    landpageView = {} 
    df1 = urlsData.loc[urlsData["url"].str.contains(pattern, flags =re.I, regex=True)]  
    #df2 = df1.loc[df1["url"].str.contains('/demo/', flags =re.I, regex=True)] 
    landpageView[col]=pd.to_numeric(df1.iloc[:,0]).sum() #- pd.to_numeric(df2.iloc[:,0]).sum()
    return landpageView
  
  referral_session = pull_url_part(sessionDestinationdf)
  referral_entrances = pull_url_part(entrancessDestinationdf,col="entrances")
  referral_users =  pull_url_part(usersDestinationdf, col ="users")

  david_sessions = pull_url_part(sessionDestinationdf, pattern='Davids' )
  davids_entrances = pull_url_part(entrancessDestinationdf,pattern='Davids',col="entrances")
  david_users = pull_url_part(sessionDestinationdf, pattern='Davids', col ="users")

  rustic_sessions = pull_url_part(sessionDestinationdf, pattern='rustic' )
  rustic_entrances = pull_url_part(entrancessDestinationdf, pattern='rustic',col="entrances")
  rustic_users = pull_url_part(sessionDestinationdf, pattern='rustic', col ="users")  

  valsE = [referral_session['sessions'],referral_entrances['entrances'],referral_users['users'],
  david_sessions['sessions'],davids_entrances['entrances'],david_users['users'],
  rustic_sessions['sessions'],rustic_entrances['entrances'],rustic_users['users'] ]
  metsE = ["sessions","entrances", "users", "sessions","entrances","users","sessions","entrances","users"]
  dimsE = ["Referral page","Referral page","Referral page","Davids bridal","Davids bridal","Davids bridal","rusticwedding","rusticwedding","rusticwedding"]
  
  dataE = KPIs_dict_to_DF(metsE,dimsE,valsE)
  dataE_todb = dataE.loc[:,["From","To","Metric","Dimension","Value"]]
  dataE_todb.columns = primary_metrics_colnames

  print(dataE_todb.head(10))
  return [dataA_todb,dataB_todb,data1C,data2C,data3C,dataD_todb, dataE_todb]

