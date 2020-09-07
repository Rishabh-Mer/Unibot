## open_widget
* start
    - utter_init_chat
    - utter_ask_lang

## suggestions
* suggestions
    - utter_suggestions

## language_h
* lang_h
    - utter_ask_details_h
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_h

## language_e + suggestions
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions

## id_card_application + no_changes
* apply_id
    - id_card_form
    - form{"name": "id_card_form"}
    - utter_show_details
    - form{"name": null}
    - utter_id_application_accept

## ok + yes
* ok
    - utter_yes

## id_card_change_name
* change_name
    - id_card_form
    - form{"name": "id_card_form"}
    - utter_show_details
* accept
    - form{"name": null}
    - utter_id_application_accept

## id_card_change_stream
* change_stream
    - id_card_form
    - form{"name": "id_card_form"}
    - utter_show_details
    - form{"name": null}
    - utter_id_application_accept

## id_card_change_sem
* change_sem
    - id_card_form
    - form{"name": "id_card_form"}
    - utter_show_details
* accept
    - form{"name": null}
    - utter_id_application_accept

## language_h + deny
* lang_h
    - utter_ask_details_h
* deny
    - utter_no_problem_h
    - utter_greet_h
    
## language_e + deny
* lang_e
    - utter_ask_details_e
* deny
    - utter_no_problem_e
    - utter_greet_e
    - utter_suggestions

## change langauage
* change_language
    - utter_ask_lang

## greet
* greet
    - utter_greet_e
    - utter_suggestions

## back  
* back
    - utter_back

## back 2
* back2
    - utter_back_2

## back 3
* back3
    - utter_back_3

## quote
* quote_day
    - utter_quote_day
    - utter_suggestions

## information technology
* IT
    - utter_IT

## Computer Engineering
* COMPS
    - utter_COMPS

## Civil Engineering
* CIVIL
    - utter_CIVIL

## Aritfical Intelligence and Machine Learning Engineering
* AIML
    - utter_AIML

## Data Engineering
* DATA
    - utter_DATA

## it_faculty
* it_faculties
    - utter_it_faculties

## comps_faculty
* comps_faculties
    - utter_comps_faculties

## civil_faculty
* civil_faculties
    - utter_civil_faculties

## aiml_faculty
* aiml_faculties
    - utter_aiml_faculties

## data_faculty
* data_faculties
    - utter_data_faculties

## it_syllabus
* it_syllabus
    - utter_it_syllabus

## comps_syllabus
* comps_syllabus
    - utter_comps_syllabus

## civil_syllabus
* civil_syllabus
    - utter_civil_syllabus

## aiml_syllabus
* aiml_syllabus
    - utter_aiml_syllabus

## data_syllabus
* data_syllabus
    - utter_data_syllabus

## it_newsletter
* it_newsletter
    - utter_it_newsletter

## admission_schedule_h
* admission_schedule_h
    - utter_admission_schedule_h

## admission_criteria_h
* admission_criteria_h
    - utter_admission_criteria_h

## ask_admission_criteria
* admission_criteria
    - utter_admission_criteria

## ask_admission1
* admission_documents
    - utter_admission_documents

## diploma_admission_schedule
* diploma_admissions{"diploma_admission_schedule":"diploma admission"}
    - utter_diploma_schedule

## diploma_documents
* diploma_admissions{"diploma_documents":"Documents for diploma"}
    - utter_diploma_documents

## diploma_eligibility_criteria
* diploma_admissions{"diploma_eligibility_criteria":"Diploma Eligibility Criteria"}
    - utter_diploma_criteria

## ask_admission_h
* admission_h
    - utter_admission_h
* intake_h
    - utter_intake_h
* cutoff_h
    - utter_cutoff_h
* document_h
    - utter_document_h

## ask_documents_h
* document_h
    - utter_document_h

## ask_dte
* dte_code
    - utter_dte_code
* intake
    - utter_intake
* merit
    - utter_merit 
    
## ask_dte1
* dte_code
    - utter_dte_code

## ask_admission
* admission_schedule
    - utter_admission_schedule 
    
## ask_admission_criteria
* admission_criteria
    - utter_admission_criteria

## diploma_admission_full
* diploma_admissions
    - utter_diploma_full_details
    - utter_admission_schedule

## brochure
* brochure
    - utter_brochure
    - utter_suggestions

## brochure_h
* brochure_h
    - utter_brochure_h
    
## merit
* merit
    - utter_merit

## merit_h
* merit_h
    - utter_merit_h

## ask_admission_h
* admission_h
    - utter_admission_h

## ask_cutoff_h
* cutoff_h
    - utter_cutoff_h

## ask_documents_h
* document_h
    - utter_document_h

## ask_docs_h
* docs_h
    - utter_docs_h
    - utter_document_h

## ask_cutoff
* cutoff
    - utter_cutoff

## ask_dte_h
* dte_h
    - utter_dte_h

## last_date_admission
* last_date_admission
    - utter_last_date_admission
    - utter_admission_schedule

## intake
* intake
    - utter_intake

## department
* department
    - utter_department

## department_h
* department_h
    - utter_department_h

## ask_minority_h
* minority_h
    - utter_minority_h
    - utter_document_h

## ask_reserved_h
* reserved_h
    - utter_reserved_h
    - utter_document_h

## reservation
* reservation
   - utter_reservation

## minority
* minority
   - utter_minority

## ask_minority_h
* minority_h
    - utter_minority_h
    - utter_document_h

## ask_reserved_h
* reserved_h
    - utter_reserved_h
    - utter_document_h

## ask_payment
* payment
    - utter_payment

## payment_date
* payment_date
    - utter_payment_date
   
## ask_payment_h
* payment_h
    - utter_payment_h
    - utter_fees_h

## ask_scholarship    
* scholarship
    - utter_scholarship   
     
## ask_scholarship_h    
* scholarship_h
    - utter_scholarship_h
    - utter_fees_h

## fees_button
* fees_h_btn
    - utter_fees_h

## fees_h
* fees_h
    - utter_fees_details
    - utter_fees_h

## fees
* fees
    - utter_fees

## NAAC
* naac_grade
    - utter_naac
    - utter_suggestions

## unaided
* college_type
    - utter_unaided

## affiliation
* affiliated
    - utter_affiliated

## course_duration
* course_duration
    - utter_course_duration

## ict_classroom
* ict_classroom
    - utter_ict_classroom

## ac_classrooms
* ac_classroom
    - utter_ac_classroom

## ucoe
* ucoe
    - utter_ucoe

## college_h
* college_h
    - utter_college_h

## notices
* notices
    - utter_notices
    - utter_suggestions

## images_h_
* images_h
    - utter_display_h

## images
* images
    - utter_display 

## images + more
* images
    - utter_display 
* more
    - utter_display 

## images + more + appraise
* images
    - utter_display 
* more
    - utter_display
* appraise
    - utter_thanks 

## images + appraise
* images
    - utter_display 
* appraise
    - utter_thanks 

## images + appraise + more
* images
    - utter_display 
* appraise
    - utter_thanks
* more
    - utter_display

## attendance
* attendance
    - utter_attendance_criteria

## attendance_h
* attendance_h
    - utter_attendance_h

## faculty_name
* faculty_name
    - utter_faculty_name

## principal
* principal
    - utter_principal

## principal_h
* principal_h
    - utter_principal_h

## college_timing
* college_timing
    - utter_college_timing

## college_timing_h
* college_timing_h
    - utter_college_timing_h   

## college_reopen
* college_reopen
  - utter_college_reopen 

## academic_calendar
* academic_calendar
    -  utter_academic_calendar
    
## academic_calendar1
* academic_calendar_h
    -  utter_academic_calendar_h

## about_college
* about_college
    - utter_about_college
    - utter_suggestions

## about_college_h
* about_college_h
    - utter_about_college_h

## transport_way
* transport_way
    - utter_transport_way

## bus_service
* bus_service
    - utter_bus_service
* bus_fees
    - utter_bus_fees

## bus_fees
* bus_fees
    - utter_bus_fees

## ask_bus_service_h
* bus_service_h
    - utter_bus_service_h

## ask_bus_h
* bus_fees_h
    - utter_bus_fees_h
    - utter_facility_h

## ask_transport_way_h
* transport_way_h
    - utter_transport_way_h
    - utter_facility_h

## bus_id
* busid_h
    - utter_busid_h
    - utter_applying_id_h

## bus_id_e
* bus_id
    - utter_bus_id

## location
* directions   
    - utter_directions

## ask_location_h
* location_search_h
    - utter_direction_h

## ask_distance
* distance
    - utter_distance

## ask_near_station
* nearest_station
    - utter_nearest_station

## ask_parking
* parking
    - utter_parking

## ask_concession
* concession
    - utter_concession

## facility
* facility_h
    - utter_facility_h

## facilities
* facility
    - utter_facility

## hostel
* hostel
    - utter_hostel

## locker_facility_h
* locker_facility_h
    - utter_locker_facility_h
    - utter_facility_h

## locker_facility
* locker_facility
    - utter_locker_facility
    - utter_facility
    
## wifi_facility_h
* wifi_facility_h
    - utter_wifi_facility_h
    - utter_facility_h

## wifi_facility
* wifi_facility
    - utter_wifi_facility
    - utter_facility

## bcr_gcr_facility
* bcr_facility
    - utter_bcr_gcr
    - utter_facility

## bcr_gcr_facility
* gcr_facility
    - utter_bcr_gcr
    - utter_facility

## sports_room
* sports_room
    - utter_sports_room
    - utter_facility

## sports_room_h
* sports_room_h
    - utter_sports_room_h
    - utter_facility_h

## technical events
* technical_events
    - utter_technical_events

## events_h
* events_h
    - utter_events_h

## event
* events
    - utter_events
    
## extra_activities
* extra_activities
    - utter_extra_activities
    
## IETE
* IETE
    - utter_IETE

## IETE Schedule
* IETE_schedule
    - utter_IETE_schedule

## hackstomp1
* hackstomp
    - utter_hackstomp
    
## hackstomp2
* hackstomp
    - utter_hackstomp
* hackstomp_date
    - utter_hackstomp_date
    
## ask_vyro
* vyro
    - utter_vyro

## vyro_schedule
* vyro_schedule
    - utter_vyro_schedule
    
## ask_aurora
* aurora
    - utter_aurora

## aurora_schedule
* aurora_schedule
    - utter_aurora_schedule

## ask_hackstomp_date
* hackstomp_date
    - utter_hackstomp_date

## ask_tantrostav
* tantrostav
    - utter_tantrostav

## ask_csi
* csi
    - utter_csi

## ask_eyantra
* eyantra
    - utter_eyantra

## ask_nss
* nss
    - utter_nss

## ask_ieee
* ieee
    - utter_ieee

## ask_automation
* automation
    - utter_automation

## ask_wdcell
* wdcell
    - utter_wdcell

## ask_scouncil
* scouncil
    - utter_scouncil

## ask_speak_club
* speak_club
    - utter_speak_club

## ask_farming
* farming
    - utter_farming

## canteen_facility
* canteen
    - utter_canteen 
    
## ask_food
* food
    - utter_food
    - utter_facility

## ask_canteen_h
* canteen_h
    - utter_canteen_h

## ask_canteen_menu_h
* menu_h
    - utter_canteen_menu
    - utter_facility_h

## ask_non_veg
* non_veg
    - utter_non_veg

## ask_examination
* examination
    - utter_examination

## ask_examination_h
* examination_h
    - utter_examination   

## ask_intake_h
* intake_h
    - utter_intake_h

## about_placement
* placement
  - utter_placement

## placement_companies
* placement_companies
    - utter_placement_companies

## placed_students
* placed_student
    - utter_placed_students

## placement
* placement_h
    - utter_placement_h
 
## placement_details_h
* placement_detail_h
    - utter_placement_detail_h
    - utter_placement_h

## placement_office
* TPO_h
    - utter_TPO_h
    - utter_placement_h

## library_card_h
* library_card_h
    - utter_library_card_h
    - utter_applying_id_h

## ask_library 
* ask_library
    - utter_library

## library_timing
* library_timings
    - utter_library_timing

## library_card
* library_card
   - utter_library_card

## library_details
* library_details
    - utter_library_details

## college_id
* college_id_h
    - utter_college_id_h
    - utter_applying_id_h

## applying_id
* applying_id
    - utter_applying_id

## applying_id_h
* applying_id_h
    - utter_applying_id_h

## college_age
* how_old_college
    - utter_college_age

## college founder
* founder
    - utter_college_founder
   
## anti_ragging
* anti_ragging
   - utter_anti_ragging
   - utter_extra_activities

## who_are_you
* who_are_you
    - utter_who_am_i

## what_else
* what_else
    - utter_what_else

## say welcome
* thankyou
    - utter_welcome
     
## say goodbye + acceptfeed
* goodbye
    - utter_goodbye
    - utter_ask_feed
* accept
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}

## say goodbye + denyfeed
* goodbye
    - utter_goodbye
    - utter_ask_feed
* deny
    - utter_no_problem_e

## feed_h + acceptfeed
* feed_h
    - utter_ask_feed_h
* accept
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_back

## feed_h + denyfeed
* feed_h
    - utter_ask_feed_h
* deny
    - utter_no_problem_h
    - utter_back
    
## ask about
* askabout
    - utter_sayabout

## ask work
* askwork
    - utter_work

## handleinsult
* handleinsult
    - utter_bad 

## askbuilder
* ask_builder
    - utter_ask_builder

## askweather    
* ask_weather
    - utter_ask_weather

## askhowdoing
* ask_howdoing 
    - utter_sayabout

## asklanguages
* ask_languagesbot
    - utter_ask_languagesbot

## askhowold
* ask_howold
    - utter_ask_howold

## askrest
* ask_restaurant 
    - utter_ask_restaurant 

## asktime
* ask_time
    - utter_ask_time 

## askwherefrmom
* ask_wherefrom
    - utter_ask_wherefrom 

## askwhoami
* ask_whoami 
    - utter_ask_whoami  

## joke
* telljoke
    - utter_telljoke 

## askname
* ask_whatismyname
    - utter_ask_whatismyname

## story1_english_yes
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions
* quote_day
    - utter_quote_day
    - utter_suggestions
* about_college
    - utter_about_college
    - utter_suggestions
* notices
    - utter_notices
    - utter_suggestions

## story1_english_no
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* deny
    - utter_no_problem_e
    - utter_greet_e
    - utter_suggestions
* quote_day
    - utter_quote_day
    - utter_suggestions
* about_college
    - utter_about_college
    - utter_suggestions
* notices
    - utter_notices
    - utter_ask_feed
* deny
    - utter_no_problem_e
    - utter_suggestions
* department
    - utter_department
* intake
    - utter_intake
* cutoff
    - utter_ask_feed
* deny
    - utter_no_problem_e
    - utter_cutoff

## bus + feedback
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions
* bus_service
    - utter_bus_service
* bus_fees
    - utter_bus_fees
* transport_way
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_transport_way

## dept + feed
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions
* department
    - utter_department
* IT
    - utter_IT
* it_faculties
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_it_faculties

## deptc + feed
* department
    - utter_department
* COMPS
    - utter_COMPS
* comps_syllabus
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_comps_syllabus

## deptai + feed
* department
    - utter_department
* AIML
    - utter_AIML
* aiml_faculties
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_aiml_faculties

## admission + feed
* admission_schedule
    - utter_admission_schedule
* admission_documents
    - utter_admission_documents
* admission_criteria
    - utter_admission_criteria
* last_date_admission
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_last_date_admission

## notice + feed
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions
* quote_day
    - utter_quote_day
    - utter_suggestions
* about_college
    - utter_about_college
    - utter_suggestions
* notices
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_notices
    - utter_suggestions

## nss + feed
* start
    - utter_init_chat
    - utter_ask_lang
* lang_e
    - utter_ask_details_e
* accept
    - user_form
    - form{"name": "user_form"}
    - form{"name": null}
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}
    - utter_greet_e
    - utter_suggestions
* anti_ragging
   - utter_anti_ragging
   - utter_extra_activities
* csi
    - utter_csi
* ieee
    - utter_ieee
* nss
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_nss

## placement + feed
* placement
  - utter_placement
* placed_student
    - utter_placed_students
* placement_companies
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_placement_companies

## facility + feed
* facility
    - utter_facility
* locker_facility
    - utter_locker_facility
    - utter_facility
* wifi_facility
    - utter_wifi_facility
    - utter_facility
* sports_room
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_sports_room
    - utter_facility

## canteen + feed
* canteen
    - utter_canteen 
* food
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_food
    - utter_facility

## library + feed
* ask_library
    - utter_library
* library_timings
    - utter_library_timing
* library_card
   - utter_library_card
* library_details
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_library_details

## founder + principal + feed
* principal
    - utter_principal
* founder
    - feedback_form
    - form{"name": "feedback_form"}
    - form{"name": null}
    - utter_college_founder


















