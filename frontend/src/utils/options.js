export const OPTIONS={
checking_status:['<0','0<=X<200','>=200','no checking'],
credit_history:['critical','poor','existing paid','delayed','all paid'],
purpose:['car_new','car_used','furniture','radio_tv','education','business','repairs','domestic_appliances'],
savings_status:['<100','100<=X<500','500<=X<1000','>=1000','unknown'],
employment:['unemployed','<1','1<=X<4','4<=X<7','>=7'],
personal_status:['male_single','female','male_married','male_divorced'],other_parties:['none','co_applicant','guarantor'],property_magnitude:['real_estate','life_insurance','car_other','unknown'],other_payment_plans:['none','bank','stores'],housing:['own','rent','free'],job:['unskilled','skilled','management','highly_skilled'],own_telephone:['yes','none'],foreign_worker:['yes','no']};
export const emptyProfile={applicant_id:'CL-NEW',checking_status:'0<=X<200',duration:24,credit_history:'existing paid',purpose:'car_new',credit_amount:5000,savings_status:'500<=X<1000',employment:'1<=X<4',installment_commitment:2,personal_status:'male_single',other_parties:'none',residence_since:3,property_magnitude:'real_estate',age:32,other_payment_plans:'none',housing:'own',existing_credits:2,job:'skilled',num_dependents:1,own_telephone:'yes',foreign_worker:'yes'};
