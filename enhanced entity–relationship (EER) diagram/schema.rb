# This file is auto-generated from the current state of the database. Instead of editing this file, 
# please use the migrations feature of ActiveRecord to incrementally modify your database, and
# then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your database schema. If you need
# to create the application database on another system, you should be using db:schema:load, not running
# all the migrations from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 24) do

  create_table "attendances", :force => true do |t|
    t.integer  "event_id"
    t.integer  "member_id"
    t.string   "predicted_attendance"
    t.boolean  "actual_attendance"
    t.string   "excused_conflict_reason"
    t.integer  "attendance_short_term_camping_nights", :default => 0
    t.integer  "attendance_long_term_camping_nights",  :default => 0
    t.integer  "attendance_service_hours",             :default => 0
    t.datetime "created_on"
    t.datetime "updated_on"
    t.boolean  "provided_transportation",              :default => false
    t.boolean  "before_contacted"
    t.boolean  "before_deciding"
    t.boolean  "before_going"
    t.boolean  "after_didnt_go"
    t.boolean  "before_not_going"
  end

  create_table "authusers", :force => true do |t|
    t.string   "login"
    t.string   "email"
    t.string   "crypted_password",          :limit => 40
    t.string   "salt",                      :limit => 40
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "remember_token"
    t.datetime "remember_token_expires_at"
  end

  create_table "content_pages", :force => true do |t|
    t.string    "title"
    t.string    "name",            :default => "", :null => false
    t.integer   "markup_style_id"
    t.text      "content"
    t.integer   "permission_id",                   :null => false
    t.timestamp "created_at",                      :null => false
    t.timestamp "updated_at",                      :null => false
  end

  add_index "content_pages", ["permission_id"], :name => "fk_content_page_permission_id"
  add_index "content_pages", ["markup_style_id"], :name => "fk_content_page_markup_style_id"

  create_table "controller_actions", :force => true do |t|
    t.integer "site_controller_id",                 :null => false
    t.string  "name",               :default => "", :null => false
    t.integer "permission_id"
  end

  add_index "controller_actions", ["permission_id"], :name => "fk_controller_action_permission_id"
  add_index "controller_actions", ["site_controller_id"], :name => "fk_controller_action_site_controller_id"

  create_table "displayedpatrols", :force => true do |t|
    t.integer "patrollookup_id"
  end

  create_table "emails", :force => true do |t|
  end

  create_table "events", :force => true do |t|
    t.string   "short_description"
    t.string   "location"
    t.string   "full_description"
    t.date     "start_date"
    t.date     "end_date"
    t.integer  "smic_id"
    t.integer  "adult_leader_2_id"
    t.integer  "parent_coordinator_id"
    t.integer  "troop_short_term_camping_nights"
    t.integer  "troop_long_term_camping_nights"
    t.integer  "troop_service_hours"
    t.datetime "created_on"
    t.datetime "updated_on"
    t.boolean  "service_project"
    t.boolean  "camping"
    t.boolean  "non_camping_outing"
    t.boolean  "meeting"
    t.boolean  "misc_troop_activity"
  end

  create_table "jobassignments", :force => true do |t|
    t.integer "joblookup_id",        :null => false
    t.integer "member_id",           :null => false
    t.date    "date_start"
    t.date    "date_end"
    t.string  "obe_specific_patrol"
    t.integer "patrollookup_id"
  end

  create_table "joblookups", :force => true do |t|
    t.string  "job_abbr"
    t.string  "job_full_title"
    t.string  "appropriate_generation"
    t.boolean "jlo",                    :default => false
    t.boolean "plc",                    :default => false
    t.boolean "patrol_level",           :default => false
    t.boolean "smasm",                  :default => false
    t.boolean "patrol_advisor",         :default => false
    t.boolean "troop_committee",        :default => false
  end

  create_table "markup_styles", :force => true do |t|
    t.string "name", :default => "", :null => false
  end

  create_table "mbcounselors", :force => true do |t|
    t.integer "mblookup_id"
    t.integer "member_id"
    t.date    "application_paperwork_submitted"
    t.boolean "is_active"
  end

  create_table "mbearneds", :force => true do |t|
    t.integer "mblookup_id"
    t.integer "member_id"
    t.integer "mbcounselor_id"
    t.date    "date_begun"
    t.date    "date_earned"
    t.date    "date_awarded_troop_mtg"
    t.date    "date_awarded_coh"
  end

  create_table "mblookups", :force => true do |t|
    t.string  "mb_name"
    t.integer "mb_bsa_number"
    t.date    "date_mb_rqmts_last_updated"
    t.string  "link_to_online_rqmts"
    t.date    "defunct_as_of_date"
    t.boolean "eagle_required"
    t.string  "link_to_image"
    t.string  "mb_category"
  end

  create_table "medformlookups", :force => true do |t|
    t.string  "med_form_class"
    t.integer "form_valid_duration_years"
    t.string  "comments",                  :limit => 500
  end

  create_table "medformsubmittals", :force => true do |t|
    t.integer "medformlookup_id", :null => false
    t.integer "member_id",        :null => false
    t.date    "date_effective",   :null => false
    t.date    "date_expires"
  end

  create_table "members", :force => true do |t|
    t.string   "first_name"
    t.string   "middle_name"
    t.string   "last_name"
    t.string   "preferred_name"
    t.integer  "father_pointer"
    t.integer  "mother_pointer"
    t.string   "school_name"
    t.integer  "grade_in_school"
    t.date     "grade_in_school_as_of"
    t.string   "religious_affiliation"
    t.date     "birthday"
    t.boolean  "obe_youth",                   :default => true
    t.boolean  "obe_adult",                   :default => false
    t.boolean  "active_member",               :default => true
    t.string   "db_username"
    t.string   "db_password"
    t.string   "db_rights_permission_access"
    t.integer  "db_login_count"
    t.date     "db_last_login"
    t.datetime "created_on"
    t.datetime "updated_on"
    t.string   "home_street_address"
    t.string   "home_city"
    t.string   "home_state"
    t.string   "home_zip"
    t.string   "home_phone"
    t.string   "cell1"
    t.string   "cell2"
    t.string   "pager"
    t.string   "fax"
    t.string   "home_email"
    t.string   "work_occupation"
    t.string   "work_company"
    t.string   "work_address"
    t.string   "work_office_phone"
    t.string   "work_phone2"
    t.string   "work_email"
    t.string   "generation",                  :default => "scout"
    t.string   "emergency_contact"
  end

  create_table "menu_items", :force => true do |t|
    t.integer "parent_id"
    t.string  "name",                 :default => "", :null => false
    t.string  "label",                :default => "", :null => false
    t.integer "seq"
    t.integer "controller_action_id"
    t.integer "content_page_id"
  end

  add_index "menu_items", ["controller_action_id"], :name => "fk_menu_item_controller_action_id"
  add_index "menu_items", ["content_page_id"], :name => "fk_menu_item_content_page_id"
  add_index "menu_items", ["parent_id"], :name => "fk_menu_item_parent_id"

  create_table "old_jobs", :force => true do |t|
    t.string   "job_title",         :limit => 50, :default => "", :null => false
    t.datetime "created_on"
    t.datetime "updated_on"
    t.string   "job_title_acronym", :limit => 30, :default => ""
  end

  create_table "old_jobs_people", :id => false, :force => true do |t|
    t.integer "job_id",    :default => 0, :null => false
    t.integer "person_id", :default => 0, :null => false
  end

  create_table "old_people", :force => true do |t|
    t.string   "lastname",   :limit => 30, :default => "", :null => false
    t.string   "firstname",  :limit => 30, :default => "", :null => false
    t.string   "middlename", :limit => 30, :default => "", :null => false
    t.datetime "created_on"
    t.datetime "updated_on"
  end

  create_table "old_schema_info", :id => false, :force => true do |t|
    t.integer "version"
  end

  create_table "old_testgroups", :force => true do |t|
    t.string "name", :limit => 30
  end

  create_table "old_testusers", :force => true do |t|
    t.string "name", :limit => 30
  end

  create_table "old_users", :force => true do |t|
    t.string   "login"
    t.string   "email"
    t.string   "crypted_password",          :limit => 40
    t.string   "salt",                      :limit => 40
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "remember_token"
    t.datetime "remember_token_expires_at"
  end

  create_table "patrolassignments", :force => true do |t|
    t.integer "patrollookup_id"
    t.integer "member_id"
    t.date    "date_joined_patrol"
    t.date    "date_left_patrol"
  end

  create_table "patrollookups", :force => true do |t|
    t.string  "patrol_name"
    t.boolean "is_active",         :default => true
    t.date    "date_activated"
    t.date    "date_disbanded"
    t.boolean "new_scout"
    t.integer "patrol_sort_order"
    t.boolean "adult_leaders"
    t.boolean "sluggish"
  end

  create_table "permissions", :force => true do |t|
    t.string "name", :default => "", :null => false
  end

  create_table "plugin_schema_info", :id => false, :force => true do |t|
    t.string  "plugin_name"
    t.integer "version"
  end

  create_table "roles", :force => true do |t|
    t.string    "name",                            :default => "", :null => false
    t.integer   "parent_id"
    t.string    "description",     :limit => 1024, :default => "", :null => false
    t.integer   "default_page_id"
    t.text      "cache"
    t.timestamp "created_at",                                      :null => false
    t.timestamp "updated_at",                                      :null => false
  end

  add_index "roles", ["parent_id"], :name => "fk_role_parent_id"
  add_index "roles", ["default_page_id"], :name => "fk_role_default_page_id"

  create_table "roles_permissions", :force => true do |t|
    t.integer "role_id",       :null => false
    t.integer "permission_id", :null => false
  end

  add_index "roles_permissions", ["role_id"], :name => "fk_roles_permission_role_id"
  add_index "roles_permissions", ["permission_id"], :name => "fk_roles_permission_permission_id"

  create_table "rqmtlookups", :force => true do |t|
    t.string  "rank_name"
    t.integer "rank_number",               :limit => 4
    t.string  "badge_image_path"
    t.string  "rqmtno"
    t.string  "short_text"
    t.string  "complete_text"
    t.date    "start_effectivity"
    t.date    "end_effectivity"
    t.string  "link_to_online_rank_rqmts"
    t.boolean "sm_conf_board_of_review"
    t.boolean "rank_complete"
    t.boolean "presentation_placeholder"
  end

  create_table "rqmtsignoffs", :force => true do |t|
    t.integer "rqmtlookup_id"
    t.integer "member_id"
    t.string  "signing_adult"
    t.date    "signoff_date"
    t.string  "location_comments"
    t.integer "mblookup_id"
    t.string  "event_results"
    t.boolean "rqmt_not_applicable"
  end

  create_table "sessions", :force => true do |t|
    t.string    "session_id", :default => "", :null => false
    t.text      "data"
    t.timestamp "created_at",                 :null => false
    t.timestamp "updated_at",                 :null => false
  end

  create_table "site_controllers", :force => true do |t|
    t.string  "name",                        :default => "", :null => false
    t.integer "permission_id",                               :null => false
    t.integer "builtin",       :limit => 10, :default => 0
  end

  add_index "site_controllers", ["permission_id"], :name => "fk_site_controller_permission_id"

  create_table "storedparameters", :force => true do |t|
    t.string  "text_identifier", :limit => 45
    t.integer "stored_integer"
    t.string  "stored_text"
  end

  create_table "system_settings", :force => true do |t|
    t.string  "site_name",                 :default => "", :null => false
    t.string  "site_subtitle"
    t.string  "footer_message",            :default => ""
    t.integer "public_role_id",            :default => 0,  :null => false
    t.integer "session_timeout",           :default => 0,  :null => false
    t.integer "default_markup_style_id",   :default => 0
    t.integer "site_default_page_id",      :default => 0,  :null => false
    t.integer "not_found_page_id",         :default => 0,  :null => false
    t.integer "permission_denied_page_id", :default => 0,  :null => false
    t.integer "session_expired_page_id",   :default => 0,  :null => false
    t.integer "menu_depth",                :default => 0,  :null => false
  end

  add_index "system_settings", ["public_role_id"], :name => "fk_system_settings_public_role_id"
  add_index "system_settings", ["site_default_page_id"], :name => "fk_system_settings_site_default_page_id"
  add_index "system_settings", ["not_found_page_id"], :name => "fk_system_settings_not_found_page_id"
  add_index "system_settings", ["permission_denied_page_id"], :name => "fk_system_settings_permission_denied_page_id"
  add_index "system_settings", ["session_expired_page_id"], :name => "fk_system_settings_session_expired_page_id"

  create_table "traininglookups", :force => true do |t|
    t.string  "training_name",            :default => "", :null => false
    t.date    "training_date_start"
    t.date    "training_date_end"
    t.boolean "training_good_forvever"
    t.integer "training_valid_for_years"
    t.string  "offering_organization"
    t.string  "training_location"
  end

  create_table "trainingtakens", :force => true do |t|
    t.integer "member_id"
    t.integer "traininglookup_id"
    t.date    "date_earned"
    t.date    "date_expires"
  end

  create_table "users", :force => true do |t|
    t.string  "name",                   :default => "", :null => false
    t.string  "password", :limit => 40, :default => "", :null => false
    t.integer "role_id",                                :null => false
  end

  add_index "users", ["role_id"], :name => "fk_user_role_id"

end
