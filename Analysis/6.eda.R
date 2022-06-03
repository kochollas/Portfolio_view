library(dplyr)
da <- read.csv('~/Documents/upwork/Nayda/survey.csv')

colnames(da)[2]

data.frame(table(da$What.state.do.you.live.in.))

data.frame(table(da$What.is.your.Gender.identity.))
sum(is.na(da$What.is.your.Gender.identity.))

data.frame(table(da$How.many.drinks.on.average.do.you.consume.a.week.))
sum(is.na(da$How.many.drinks.on.average.do.you.consume.a.week.))

data.frame(table(da$What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.))

data.frame(table(da$What.is.your.ethnicity.race.))

sum(is.na(da$What.is.your.ethnicity.race.))

data.frame(table(da$What.is.your.average.annual.household.income.))

data.frame(table(da$What.is.your.marital.status.))

data.frame(table(da$What.is.your.sexual.orientation.))

data.frame(table(da$What.kind.of..drinker..would.you.say.you.identify.as.))

data.frame(table(da$How.many.days.in.the.week.on.average.do.you.NOT.drink.))

data.frame(table(da$What.would.you.say.is.your.biggest.trigger.for.drinking.))

data.frame(table(da$What.best.describes.your.education.level.))

data.frame(table(da$Do.you.work.from.home.))

data.frame(table(da$What.industry.do.you.work.in.))

data.frame(table(da$How.often.do.you.feel.the.effects.of.a.hangover.))

data.frame(table(da$What.is.your.age.))

data.frame(table(da$On.a.scale.of.1.to.10..how.would.you.rate.your.level.of..happiness.))

data.frame(table(da$Do.you.go.to.therapy.))

data.frame(table(da$How.often.do.you.exercise.))

data.frame(table(da$Do.you.have.any.children.))

data.frame(table(da$What.political.party.do.you.most.closely.affiliate.with.))

#Q1
q1 <- data.frame(da %>% select(What.is.your.Gender.identity., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())

write.csv(q1, '~/Documents/upwork/Nayda/q1.csv')

#Q2
q2 <- data.frame(da %>% select(What.industry.do.you.work.in., What.kind.of..drinker..would.you.say.you.identify.as.)%>%table())

q2 <- q2 %>% filter(What.kind.of..drinker..would.you.say.you.identify.as. == 'Excessive drinker') %>% arrange(desc(Freq))

write.csv(q2, '~/Documents/upwork/Nayda/q2.csv')

#Q3
q3 <- q1 <- data.frame(da %>% select(What.is.your.marital.status., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
write.csv(q3, '~/Documents/upwork/Nayda/q3.csv')

#4
q4 <- q1 <- data.frame(da %>% select(What.is.your.average.annual.household.income., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
write.csv(q4, '~/Documents/upwork/Nayda/q4.csv')

q4 <- q1 <- data.frame(da %>% select(What.is.your.average.annual.household.income., How.many.days.in.the.week.on.average.do.you.NOT.drink.)%>%table())
write.csv(q4, '~/Documents/upwork/Nayda/q4.csv')


#q5
da$gender <- ifelse(da$What.is.your.Gender.identity.=="Male", "Male",
                    ifelse(da$What.is.your.Gender.identity.=="Female", "Female", "Others"))
q5 <- data.frame(da %>% select(gender, What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)%>%table())
write.csv(q5, '~/Documents/upwork/Nayda/q5.csv')

q6 <- data.frame(da %>% select(What.state.do.you.live.in., What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)%>%table())
write.csv(q6, '~/Documents/upwork/Nayda/q6.csv')

q6b <- data.frame(da %>% select(What.state.do.you.live.in., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
q6b <- q6b %>% filter(Freq > 0)
write.csv(q6b, '~/Documents/upwork/Nayda/q6b.csv')

q7 <- data.frame(da %>% select(What.is.your.sexual.orientation., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
write.csv(q7, '~/Documents/upwork/Nayda/q7.csv')


da$straight_or_not <-ifelse(da$What.is.your.sexual.orientation. == "Straight (Heterosexual)", "Straight","Not Straight") 
q10 <- data.frame(da %>% select(straight_or_not, How.many.days.in.the.week.on.average.do.you.NOT.drink.)%>%table())
write.csv(q10, '~/Documents/upwork/Nayda/q10.csv')


q11 <- data.frame(table(da$What.would.you.say.is.your.biggest.trigger.for.drinking.))
q11 <-q11 %>% arrange(desc(Freq))
write.csv(q11, '~/Documents/upwork/Nayda/q11.csv')


q16<- data.frame(da %>% select(Do.you.work.from.home., How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
write.csv(q16, '~/Documents/upwork/Nayda/q16.csv')


q17<- data.frame(da %>% select(What.industry.do.you.work.in., How.often.do.you.feel.the.effects.of.a.hangover.)%>%table())
q17 <- q17 %>% arrange(How.often.do.you.feel.the.effects.of.a.hangover., desc(Freq))
write.csv(q17, '~/Documents/upwork/Nayda/q17.csv')


q18<- data.frame(da %>% select(Do.you.have.any.children.,How.often.do.you.exercise.)%>%table())
write.csv(q18, '~/Documents/upwork/Nayda/q18.csv')

q25<- data.frame(da %>% select(On.a.scale.of.1.to.10..how.would.you.rate.your.level.of..happiness.,How.many.drinks.on.average.do.you.consume.a.week.)%>%table())
q25 <- q25%>%arrange(desc(On.a.scale.of.1.to.10..how.would.you.rate.your.level.of..happiness.))
write.csv(q25, '~/Documents/upwork/Nayda/q25.csv')

q26 <- da%>%select(straight_or_not, What.state.do.you.live.in., How.many.drinks.on.average.do.you.consume.a.week.)
q26 <- q26%>%group_by(What.state.do.you.live.in.,straight_or_not)%>%count(How.many.drinks.on.average.do.you.consume.a.week.)
write.csv(q26, '~/Documents/upwork/Nayda/q26.csv')

q32 <- da%>%select(Do.you.go.to.therapy., How.many.drinks.on.average.do.you.consume.a.week.)
q32 <- q32%>%group_by(Do.you.go.to.therapy.)%>%count(How.many.drinks.on.average.do.you.consume.a.week.)
write.csv(q32, '~/Documents/upwork/Nayda/q32.csv')

#recoding the ages
da$age_grp <- ifelse(da$What.is.your.age.>=21 & da$What.is.your.age. <=30, '21-30',
                     ifelse(da$What.is.your.age.>=31 & da$What.is.your.age. <=40, '31-40',
                            ifelse(da$What.is.your.age.>=41 & da$What.is.your.age. <=50, '41-50',
                                   ifelse(da$What.is.your.age.>=51 & da$What.is.your.age. <=60, '51-60',
                                          ifelse(da$What.is.your.age.>=61 & da$What.is.your.age. <=70, '61-70',
                                                 ifelse(da$What.is.your.age.>=71 & da$What.is.your.age. <=80, '71-80','80+'))))))




q8 <- da%>%select(age_grp, What.is.your.Gender.identity., What.kind.of..drinker..would.you.say.you.identify.as.)
q8 <- q8%>%group_by(What.is.your.Gender.identity.,age_grp)%>%count(What.kind.of..drinker..would.you.say.you.identify.as.)%>%
  arrange(desc(n))
write.csv(q8, '~/Documents/upwork/Nayda/q8.csv')


q9 <- da%>%select(age_grp, What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)
q9 <- q9 %>% group_by(age_grp)%>%count(What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)
write.csv(q9, '~/Documents/upwork/Nayda/q9.csv')


q42 <- da%>%select(age_grp, gender, What.political.party.do.you.most.closely.affiliate.with.,How.many.drinks.on.average.do.you.consume.a.week.)
q42 <- q42 %>% group_by(gender, age_grp,What.political.party.do.you.most.closely.affiliate.with.)%>%count(How.many.drinks.on.average.do.you.consume.a.week.)
write.csv(q42, '~/Documents/upwork/Nayda/q42.csv')


#da$drink_weekly <- ifelse(da$How.many.drinks.on.average.do.you.consume.a.week.)
#Q12

q12 <- da%>%select(gender, What.would.you.say.is.your.biggest.trigger.for.drinking.)
q12 <- q12 %>% group_by(gender)%>%count(What.would.you.say.is.your.biggest.trigger.for.drinking.)%>%arrange(desc(n))
write.csv(q12, '~/Documents/upwork/Nayda/q12.csv')

q13 <- da%>%select(gender, What.is.your.marital.status.,   What.would.you.say.is.your.biggest.trigger.for.drinking.)
q13 <- q13 %>% group_by(gender, What.is.your.marital.status.)%>%count(What.would.you.say.is.your.biggest.trigger.for.drinking.)%>%arrange(desc(n))
write.csv(q13, '~/Documents/upwork/Nayda/q13.csv')

q14 <- da%>%select(age_grp,   What.would.you.say.is.your.biggest.trigger.for.drinking.)
q14 <- q14 %>% group_by(age_grp)%>%count(What.would.you.say.is.your.biggest.trigger.for.drinking.)%>%arrange(desc(n))
write.csv(q14, '~/Documents/upwork/Nayda/q14.csv')


q15 <- da%>%select(What.is.your.sexual.orientation.,   What.would.you.say.is.your.biggest.trigger.for.drinking.)
q15 <- q15 %>% group_by(What.is.your.sexual.orientation.)%>%count(What.would.you.say.is.your.biggest.trigger.for.drinking.)%>%arrange(desc(n))
write.csv(q15, '~/Documents/upwork/Nayda/q15.csv')


q19 <- da%>%select(Do.you.have.any.children., How.many.drinks.on.average.do.you.consume.a.week.)
q19 <- q19 %>% group_by(Do.you.have.any.children.)%>%count(How.many.drinks.on.average.do.you.consume.a.week.)%>%arrange(desc(n))
write.csv(q19, '~/Documents/upwork/Nayda/q19.csv')


q20 <- da%>%select(Do.you.have.any.children., What.kind.of..drinker..would.you.say.you.identify.as.)
q20 <- q20 %>% group_by(Do.you.have.any.children.)%>%count(What.kind.of..drinker..would.you.say.you.identify.as.)%>%arrange(desc(n))
write.csv(q20, '~/Documents/upwork/Nayda/q20.csv')

q21 <- da%>%select(Do.you.have.any.children., What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)
q21 <- q21 %>% group_by(Do.you.have.any.children.)%>%count(What.type.of.alcohol.do.you.usually.consume...select.all.that.apply.)%>%arrange(desc(n))
write.csv(q21, '~/Documents/upwork/Nayda/q21.csv')


da$consumption_groups <- ifelse(da$How.many.drinks.on.average.do.you.consume.a.week.== '0', '10 and less',
                                ifelse(da$How.many.drinks.on.average.do.you.consume.a.week. == '1-5','10 and less',
                                       ifelse(da$How.many.drinks.on.average.do.you.consume.a.week. == '6-10','10 and less',
                                              'More than 10')))


q23 <- da%>%select(consumption_groups, How.many.days.in.the.week.on.average.do.you.NOT.drink.)
q23 <- q23 %>% group_by(consumption_groups)%>%count(How.many.days.in.the.week.on.average.do.you.NOT.drink.)%>%arrange(desc(n))
write.csv(q23, '~/Documents/upwork/Nayda/q23.csv')


q27 <- da%>%select(How.many.drinks.on.average.do.you.consume.a.week., On.a.scale.of.1.to.10..how.would.you.rate.your.level.of..happiness.)
q27 <- q27 %>% group_by(How.many.drinks.on.average.do.you.consume.a.week.)%>%count(On.a.scale.of.1.to.10..how.would.you.rate.your.level.of..happiness.)%>%arrange(desc(n))
write.csv(q27, '~/Documents/upwork/Nayda/q27.csv')

q28 <- da%>%select(How.many.drinks.on.average.do.you.consume.a.week., What.is.your.average.annual.household.income.)
q28 <- q28 %>% group_by(How.many.drinks.on.average.do.you.consume.a.week.)%>%count(What.is.your.average.annual.household.income.)%>%arrange(desc(n))
write.csv(q28, '~/Documents/upwork/Nayda/q28.csv')


q29 <- da%>%select(How.many.drinks.on.average.do.you.consume.a.week., What.is.your.marital.status.)
q29 <- q29 %>% group_by(How.many.drinks.on.average.do.you.consume.a.week.)%>%count(What.is.your.marital.status.)
write.csv(q29, '~/Documents/upwork/Nayda/q29.csv')


q30 <- da%>%select(How.many.drinks.on.average.do.you.consume.a.week., What.industry.do.you.work.in.)
q30 <- q30 %>% group_by(How.many.drinks.on.average.do.you.consume.a.week.)%>%count(What.industry.do.you.work.in.)
write.csv(q30, '~/Documents/upwork/Nayda/q30.csv')


q31 <- da%>%select(How.many.drinks.on.average.do.you.consume.a.week.,Do.you.work.from.home.)
q31 <- q31 %>% group_by(How.many.drinks.on.average.do.you.consume.a.week.)%>%count(Do.you.work.from.home.)
write.csv(q31, '~/Documents/upwork/Nayda/q31.csv')




q33 <- da%>%select(What.would.you.say.is.your.biggest.trigger.for.drinking.,Do.you.go.to.therapy.)
q33 <- q33 %>% group_by(What.would.you.say.is.your.biggest.trigger.for.drinking.)%>%count(Do.you.go.to.therapy.)
write.csv(q33, '~/Documents/upwork/Nayda/q33.csv')


q34 <- da%>%select(How.often.do.you.feel.the.effects.of.a.hangover.,How.often.do.you.exercise.)
q34 <- q34 %>% group_by(How.often.do.you.exercise.)%>%count(How.often.do.you.feel.the.effects.of.a.hangover.)
write.csv(q34, '~/Documents/upwork/Nayda/q34.csv')


q40 <- da%>%select(What.best.describes.your.education.level.,How.many.drinks.on.average.do.you.consume.a.week.)
q40 <- q40 %>% group_by(What.best.describes.your.education.level.)%>%count(How.many.drinks.on.average.do.you.consume.a.week.)
write.csv(q40, '~/Documents/upwork/Nayda/q40.csv')


q41 <- da%>%select(What.best.describes.your.education.level.,What.kind.of..drinker..would.you.say.you.identify.as.)
q41 <- q41 %>% group_by(What.best.describes.your.education.level.)%>%count(What.kind.of..drinker..would.you.say.you.identify.as.)
write.csv(q41, '~/Documents/upwork/Nayda/q41.csv')


states <- da%>%select(What.state.do.you.live.in.)%>%group_by(What.state.do.you.live.in.)%>%count()%>%arrange()%>%data.frame()
write.csv(states, '~/Documents/upwork/Nayda/states.csv')



