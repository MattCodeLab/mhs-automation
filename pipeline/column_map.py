"""
Column mapping for BNM MHS datasets.

COLUMNS   : table_id → list of raw parsed column names (auto-extracted)
RENAME    : table_id → {raw_col: desired_col}  (fill in desired names)
METADATA  : table_id → metadata placeholder dict
"""

COLUMNS: dict[str, list[str]] = {
    # Reserve Money
    '1.1': ['reserve_money', 'total_reserve_money', 'currency_in_circulation', 'required_reserves', 'excess_reserves', 'deposits_of_the_private_sector', 'wang_rizab_reserve_money_faktor_faktor_yang_mempengaruhi_wang_rizab_factors_affecting_reserve_money_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total', 'claims_on_government', 'less_deposits_of_government', 'claims_on_the_private_sector', 'external_operations', 'other_influences'],

    # Banking System: Loan/Financing Applied by Purpose
    '1.10': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing_applied'],

    # Banking System: Loans Applied by Purpose (prev)
    '1.10a': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans_applied'],

    # Banking System: Loan/Financing Applied by Sector
    '1.11': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_loan_financing_applied_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_loan_financing_applied'],

    # Banking System: Loan/Financing Applied by Type
    '1.11.1': ['type', 'overdraft_facilities', 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_total', 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_loan_financing_applied'],

    # Banking System: Loans Applied by Sector (prev)
    '1.11a': ['merchant_or_investment_banks', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_hotels', 'construction', 'real_estate', 'transport_storage_and_communication', 'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_intermediation', 'renting_business_activities', 'research_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'total_loans_applied'],

    # Banking System: Loan/Financing Approved
    '1.12': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing_approved'],

    # Banking System: Loans Approved by Purpose (prev)
    '1.12a': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans_approved'],

    # Banking System: Loan/Financing Approved by Sector
    '1.13': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_loan_financing_approved_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_loan_financing_approved'],

    # Banking System: Loans Approved by Sector (prev2)
    '1.13.1': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total', 'construction', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communication', 'finance_insurance_and_business_services', 'financial_services', 'insurance', 'business_services', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_passenger_cars', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_lain_lain_others', 'total_loans_approved'],

    # Banking System: Loan/Financing Approved by Type
    '1.13.2': ['type', 'overdraft_facilities', 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_total', 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_loan_financing_approved'],

    # Banking System: Loans Approved by Sector (prev)
    '1.13a': ['merchant_or_investment_banks', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_hotels', 'construction', 'real_estate', 'transport_storage_and_communication', 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_intermediation', 'renting_business_activities', 'research_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'total_loans_approved'],

    # Banking System: Loan/Financing Disbursed by Purpose
    '1.14': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing_disbursed'],

    # Banking System: Loans Disbursed by Purpose (prev)
    '1.14a': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans_disbursed'],

    # Banking System: Loan/Financing Disbursed by Sector
    '1.15': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_loan_financing_disbursed_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_loan_financing_disbursed'],

    # Banking System: Loans Disbursed by Sectors (prev2)
    '1.15.1': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total', 'construction', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communication', 'finance_insurance_and_business_services', 'financial_services', 'insurance', 'business_services', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_passenger_cars', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_lain_lain_others', 'total_loans_approved'],

    # Banking System: Loan/Financing Disbursed by Type
    '1.15.2': ['type', 'overdraft_facilities', 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_total', 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'foreign_currency_loans_financing', 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_loan_financing_disbursed'],

    # Banking System: Loans Disbursed by Sector (prev)
    '1.15a': ['merchant_or_investment_banks', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_hotels', 'construction', 'real_estate', 'transport_storage_and_communication', 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_intermediation', 'renting_business_activities', 'research_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'total_loans_disbursed'],

    # Banking System: Loan/Financing Repaid by Purpose
    '1.16': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing_repaid'],

    # Banking System: Loans Repaid by Purpose (prev)
    '1.16a': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans_repaid'],

    # Banking System: Loan/Financing Repaid by Sector
    '1.17': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_loan_financing_repaid_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_loan_financing_repaid'],

    # Banking System: Loans Repaid by Sectors (prev2)
    '1.17.1': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total', 'construction', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communication', 'finance_insurance_and_business_services', 'financial_services', 'insurance', 'business_services', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_passenger_cars', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_lain_lain_others', 'total_loans_approved'],

    # Banking System: Loan/Financing Repaid by Type
    '1.17.2': ['type', 'overdraft_facilities', 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_total', 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'foreign_currency_loans_financing', 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_loan_financing_repaid'],

    # Banking System: Loans Repaid by Sector (prev)
    '1.17a': ['merchant_or_investment_banks', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurants_hotels', 'construction', 'real_estate', 'transport_storage_and_communication', 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_intermediation', 'renting_business_activities', 'research_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'total_loans_repaid'],

    # Banking System: Loan/Financing by Type
    '1.18': ['type', 'overdraft_facilities', 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_total', 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'up_to_one_year', 'more_than_one_year', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'foreign_currency_loans_financing', 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_loan_financing'],

    # Islamic Banking: Financing by Type
    '1.18.1': ['type', 'overdraft_facilities', 'islamic_banking_system_financing_by_type_rm_million_term_financing_total', 'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_financing', 'factoring_receivables', 'personal_financing', 'housing_financing', 'other_term_financing', 'up_to_one_year', 'more_than_one_year', 'bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'foreign_currency_financing', 'islamic_banking_system_financing_by_type_rm_million_term_financing_lain_lain_others', 'total_financing'],

    # Islamic Banking: Financing by Type (prev)
    '1.18.1a': ['ibs_of_investment_merchant_banks', 'overdraft', 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_sewa_beli_hire_purchase_jumlah_total', 'of_which_passenger_cars', 'leasing', 'block_discounting', 'bridging_financing', 'syndicated_financing', 'factoring', 'personal_financing', 'housing_financing', 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_lain_lain_others', 'up_to_one_year', 'more_than_one_year', 'bill_financing', 'trust_receipts', 'revolving_credit', 'foreign_currency_financing', 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_lain_lain_others', 'total_financing'],

    # Islamic Banking: Financing by Shariah Contract
    '1.18.2': ['industry', 'bai_inah', 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_total', 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_total', 'ijarah_thumma_al_bai', 'ijarah_mawsufah_fi_zimmah', 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_others', 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_lain_lain_others', 'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_total', 'parallel_istisna', 'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_lain_lain_others', 'mudarabah_venture', 'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_total', 'murabahah_to_the_purchase_orderer', 'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_lain_lain_others', 'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_total', 'musyarakah_mutanaqisah', 'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_lain_lain_others', 'musyarakah_venture', 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_total', 'qard_standalone', 'qard_with_rahn', 'qard_with_ujrah', 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others', 'tawarruq', 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others_1', 'total_financing'],

    # Islamic Banking: Financing by Concept (prev)
    '1.18.2a': ['ibs_of_investment_merchant_banks', 'bai_bithaman_ajil', 'ijarah', 'ijarah_thumma_al_bai', 'murabahah', 'musyarakah', 'mudharabah', 'istisna', 'sistem_perbankan_islam_pembiayaan_mengikut_konsep_islamic_banking_system_financing_by_concept_lain_lain_others', 'total_financing'],

    # Banking System: Loan/Financing by Location
    '1.18.3': ['location', 'banking_system_loan_financing_by_location_rm_million_inside_malaysia_jumlah_total', 'johor', 'kedah', 'kelantan', 'melaka', 'negeri_sembilan', 'pahang', 'pulau_pinang', 'perak', 'perlis', 'sabah', 'sarawak', 'selangor', 'terengganu', 'wilayah_persekutuan_kuala_lumpur', 'wilayah_persekutuan_labuan', 'wilayah_persekutuan_putrajaya', 'outside_malaysia', 'total_loan_financing'],

    # Banking System: Classification of Loans by Type (prev)
    '1.18a': ['merchant_banks', 'overdraft', 'total', 'of_which_passenger_cars', 'leasing', 'block_discounting', 'bridging_loans', 'syndicated_loans', 'factoring', 'personal_loans', 'housing_loans', 'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_pinjaman_berjangka_term_loans_lain_lain_others', 'up_to_one_year', 'more_than_one_year', 'trade_bills', 'trust_receipts', 'revolving_credit', 'spi_loans', 'foreign_currency_loans', 'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_lain_lain_others', 'total_loans'],

    # Banking System: Loan/Financing by Purpose
    '1.19': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total', 'cost_300k', 'cost_300k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'of_which_housing_loan_financing_sold_to_cagamas', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total', 'purchase_of_industrial_building_factories', 'purchase_of_land_only', 'purchase_of_commercial_complexes', 'purchase_of_shophouses_shoplots', 'purchase_of_other_non_residential_property', 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing'],

    # Islamic Banking: Financing by Purpose and Sectors
    '1.19.1': ['industry', 'purchase_of_securities', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_total', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_total', 'purchase_of_consumer_durable_goods', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_lain_lain_others', 'credit_card', 'pembinaan_construction', 'working_capital', 'other_purposes', 'jumlah_pembiayaan_total_financing', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'personal_uses_pembinaan_construction', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'finance_insurance_real_estate_and_business_activities_jumlah_pembiayaan_total_financing'],

    # Islamic Banking: Financing by Purpose and Sectors (prev)
    '1.19.1a': ['ibs_of_investment_merchant_banks', 'purchase_of_securities', 'sistem_perbankan_islam_pembiayaan_mengikut_tujuan_dan_sektor_islamic_banking_system_financing_by_purpose_and_sectors_purpose_pembelian_kenderaan_pengangkutan_purchase_of_transport_vehicles_jumlah_total', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_use', 'credit_card', 'purchase_of_consumer_durables', 'pembinaan_construction', 'working_capital', 'other_purpose', 'total_financing', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'sector_pembinaan_construction', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_activities', 'education_health_and_others', 'household_sector', 'other_sector_n_e_c'],

    # Islamic Banking: Loans by Purpose and Sector (prev)
    '1.19.2': ['akhir_tempoh_end_of_period_1', 'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_purpose_and_sector', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_use', 'credit_card', 'purchase_of_consumer_durables', 'pembinaan_construction', 'working_capital', 'other_purpose', 'total_loans', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'loans_by_sector_pembinaan_construction', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_activities', 'education_health_and_others', 'household_sector', 'sector'],

    # Islamic Banking: Loans by Type and Sector (prev)
    '1.19.3': ['akhir_tempoh_as_at_end_of_1', 'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector', 'agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_and_water', 'wholesale_retail_hotels_and_restaurants', 'construction', 'residential_property', 'non_residential_property', 'real_estate', 'transport_storage_and_communications', 'financial_insurance_and_business_services', 'personal_uses', 'purchase_of_consumer_durable_goods', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'sistem_perbankan_skim_perbankan_islam1_2_format_terdahulu_pinjaman_mengikut_jenis_dan_sektor_banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector_pembiayaan_mengikut_sektor_financing_by_sector_lain_lain_others', 'total_financing', 'overdrafts', 'term_financing', 'bill_financing', 'other_financing'],

    # Commercial & Islamic Banks: Loans/Financing by Purpose
    '1.19.4': ['purchase_of_securities', 'purchase_of_transport_vehicles', 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'industrial_buildings_and_factories', 'land', 'commercial_complexes', 'shophouses', 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans'],

    # Investment Banks: Classification of Loans by Purpose
    '1.19.5': ['purchase_of_securities', 'purchase_of_transport_vehicles', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'industrial_buildings_and_factories', 'land', 'commercial_complexes', 'shophouses', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'total_loans'],

    # Banking System: Household Loan/Financing by Purpose
    '1.19.6': ['purpose', 'purchase_of_securities', 'purchase_of_passenger_cars', 'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total', 'cost_300k', 'cost_300k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'purchase_of_non_residential_property', 'personal_uses', 'credit_card', 'other_purposes', 'total_loan_financing'],

    # Banking System: Household Loan/Financing by Purpose (prev)
    '1.19.6a': ['purpose', 'purchase_of_securities', 'purchase_of_passenger_cars', 'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total', 'cost_250k', 'cost_250k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'purchase_of_non_residential_property', 'personal_uses', 'credit_card', 'other_purposes', 'total_loan_financing'],

    # Banking System: Loans by Purpose (prev)
    '1.19a': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_use', 'credit_card', 'purchase_of_consumer_durables', 'construction', 'working_capital', 'other_purpose', 'total_loans'],

    # Banking System: Loans by Purpose (prev2)
    '1.19b': ['merchant_or_investment_banks', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'of_which_purchase_of_passenger_cars', 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'industrial_buildings_and_factories', 'land', 'commercial_complexes', 'shophouses', 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_use', 'credit_card', 'purchase_of_consumer_durables', 'construction', 'working_capital', 'other_purpose', 'total_loans'],

    # Banking System: Loan/Financing by Purpose (prev3)
    '1.19c': ['purpose', 'purchase_of_securities', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total', 'cost_250k', 'cost_250k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'of_which_housing_loan_financing_sold_to_cagamas', 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total', 'purchase_of_industrial_building_factories', 'purchase_of_land_only', 'purchase_of_commercial_complexes', 'purchase_of_shophouses_shoplots', 'purchase_of_other_non_residential_property', 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_loan_financing'],

    # Currency in Circulation by Denomination
    '1.2': ['currency_in_circulation_by_denomination', 'mata_wang_dalam_edaran_currency_in_circulation', 'rm1', 'rm2', 'rm5', 'rm10', 'rm20', 'rm50', 'rm100', 'rm5002', 'rm10002', 'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_notes_currency_in_circulation_others', '1_sen', '5_sen', '10_sen', '20_sen', '50_sen', 'rm14', 'coins_currency_in_circulation', 'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_rm_million_others'],

    # Banking System: Loan/Financing by Sector
    '1.20': ['sector', 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_jumlah_total', 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_total', 'growing_of_oil_palm', 'growing_of_cocoa', 'growing_of_rubber_trees', 'animal_production', 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_others', 'forestry_and_logging', 'fishing_and_aquaculture', 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_jumlah_total', 'extraction_of_crude_petroleum_and_natural_gas', 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_total', 'mining_of_tin_ores', 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_others', 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_lain_lain_others', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_jumlah_total', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_total', 'palm_oil_processing', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_others', 'beverages', 'tobacco_products', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_reproduction_of_recorded_media', 'chemicals_and_chemical_products', 'rubber_and_plastic_products', 'non_metallic_mineral_products', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_total', 'basic_iron_and_steel', 'tin_smelting', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_others', 'fabricated_metal_products', 'electrical_machinery_and_apparatus_n_e_c', 'machinery_and_equipment_n_e_c', 'transport_equipment', 'banking_system_loan_financing_by_sector_rm_million_manufacturing_lain_lain_others', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'banking_system_loan_financing_by_sector_rm_million_construction_jumlah_total', 'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_total', 'residential', 'non_residential', 'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_others', 'civil_engineering', 'specialised_construction_activities', 'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_jumlah_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_jumlah_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_loan_financing'],

    # Commercial & Islamic Banks: Loans/Financing by Sector
    '1.20.1': ['bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_jumlah_total', 'manufacture_of_rubber_and_plastic_products', 'manufacturing_timah_tin', 'food_beverages_and_tobacco', 'of_which_palm_oil_processing', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_publishing_and_allied_industries', 'industrial_chemicals', 'non_metallic_mineral_products', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_lain_lain_others', 'electricity_gas_and_water_supply', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_jumlah_total', 'civil_engineering', 'industrial_buildings_and_factories', 'infrastructure', 'commercial_complexes', 'residential', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_lain_lain_others', 'real_estates', 'transport_storage_and_communication', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_intermediation', 'business_activities', 'research_and_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector', 'total_loans'],

    # Commercial & Islamic Banks: Loans by Sector (prev)
    '1.20.2': ['bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total', 'rubber_processing_and_rubber_products', 'manufacturing_timah_tin', 'palm_oil_processing', 'food_beverages_and_tobacco', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_pulishing_and_allied_industries', 'industrial_chemicals', 'plastic_products', 'non_metallic_mineral_products', 'building_materials', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others', 'electricity_gas_and_water_supply', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_jumlah_total', 'civil_engineering', 'industrial_buldings_and_factories', 'infrastructure', 'kompleks_perniagaan_commercial_complexes', 'residential', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'industrial_buildings_and_factories', 'land', 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes', 'shophouses', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'real_estates', 'transport_storage_and_communication', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_services', 'insurance', 'business_services', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_lain_lain_others', 'total_loans', 'of_which_loans_to_government'],

    # Investment Banks: Classification of Loans by Sector
    '1.20.3': ['bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_jumlah_total', 'manufacture_of_rubber_and_plastic_products', 'manufacturing_timah_tin', 'food_beverages_and_tobacco', 'of_which_palm_oil_processing', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_publishing_and_allied_industries', 'industrial_chemicals', 'non_metallic_mineral_products', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_lain_lain_others', 'electricity_gas_and_water_supply', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_jumlah_total', 'civil_engineering', 'industrial_buildings_and_factories', 'infrastructure', 'commercial_complexes', 'residential', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_lain_lain_others', 'real_estates', 'transport_storage_and_communication', 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_intermediation', 'business_activities', 'research_and_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector', 'total_loans'],

    # Merchant Banks: Loans by Sector (prev)
    '1.20.4': ['bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total', 'rubber_processing_and_rubber_products', 'manufacturing_timah_tin', 'palm_oil_processing', 'food_beverages_and_tobacco', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_publishing_and_allied_industries', 'industrial_chemicals', 'plastic_products', 'non_metallic_mineral_products', 'building_materials', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others', 'electricity_gas_and_water_supply', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total', 'civil_engineering', 'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories', 'infrastructure', 'kompleks_perniagaan_commercial_complexes', 'residential', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories', 'land', 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes', 'shophouses', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'real_estates', 'transport_storage_and_communication', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_services', 'insurance', 'business_services', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_lain_lain_others', 'total_loans', 'of_which_loans_to_government'],

    # Finance Companies: Loans by Sector (prev)
    '1.20.5': ['syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total', 'rubber_processing_and_rubber_products', 'manufacturing_timah_tin', 'palm_oil_processing', 'food_beverages_and_tobacco', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_publishing_and_allied_industries', 'industrial_chemicals', 'plastic_products', 'non_metallic_mineral_products', 'building_materials', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others', 'electricity_gas_and_water_supply', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total', 'civil_engineering', 'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories', 'infrastructure', 'kompleks_perniagaan_commercial_complexes', 'residential', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150k_to_250k', '250k', 'housing_loans_sold_to_cagamas', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total', 'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories', 'land', 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes', 'shophouses', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others', 'real_estates', 'transport_storage_and_communication', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_services', 'insurance', 'business_services', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'community_social_and_personal_services', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_lain_lain_others', 'total_loans', 'of_which_loans_to_government'],

    # Finance Companies: Loans by Sector (historical)
    '1.20.6': ['sector_pertanian_agriculture_jumlah_total', 'rubber', 'oil_palm', 'forestry_and_logging', 'fisheries_and_livestock', 'other_agriculture', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'tin', 'quarrying', 'other_minerals', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_jumlah_total', 'food_beverages_and_tobacco', 'textiles_and_wearing_apparel', 'wood_and_woods_products', 'printing_publishing_paper_etc', 'metal_and_metal_products', 'machinery_appliances_and_transport_equipment', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_lain_lain_others', 'construction', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perdagangan_am_general_commerce_jumlah_total', 'import_export_and_wholesale_trade', 'retail_trade', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_jumlah_total', 'housing', 'consumption_credit', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_lain_lain_others', 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_pelbagai_hal_miscellaneous_jumlah_total', 'transport_and_storage', 'real_estate', 'business_services', 'all_other', 'jumlah_pinjaman_total_loans', 'foreign_loans', 'rm_juta_rm_million_jumlah_pinjaman_total_loans'],

    # Banking System: Loans by Sector (prev)
    '1.20a': ['merchant_or_investment_banks', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'wholesale_retail_restaurants_and_hotels', 'construction', 'real_estate', 'transport_storage_and_communication', 'financing_insurance_and_business_services', 'education_health_others', 'household_sector', 'other_sector', 'total_loans'],

    # Banking System: Loans by Sector (prev2)
    '1.20b': ['merchant_or_investment_banks', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_jumlah_total', 'rubber', 'oil_palm', 'cocoa', 'livestock', 'forestry_and_logging', 'fisheries', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_lain_lain_others', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total', 'timah_tin', 'crude_petroleum_and_natural_gas', 'quarrying', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_jumlah_total', 'manufacture_of_rubber_and_plastic_products', 'manufacturing_including_agro_based_timah_tin', 'food_beverages_and_tobacco', 'of_which_palm_oil_processing', 'textiles_wearing_apparel_and_leather', 'wood_and_wood_products_incl_furniture', 'paper_and_paper_products', 'printing_and_publishing_and_allied_industries', 'industrial_chemicals', 'non_metallic_mineral_products', 'iron_and_steel_products', 'metal_products', 'machinery_non_electrical', 'electrical_machinery_and_appliances', 'transport_equipment', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_lain_lain_others', 'electricity_gas_and_water_supply', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total', 'wholesale_trade', 'retail_trade', 'restaurants_and_hotels', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_jumlah_total', 'civil_engineering', 'industrial_buildings_and_factories', 'infrastructure', 'commercial_complexes', 'residential', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_lain_lain_others', 'real_estate', 'transport_storage_and_communication', 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total', 'financial_intermediation', 'business_activities', 'research_and_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector', 'total_loans'],

    # Banking System: Loans by MFRS 9 Stages and Provisions
    '1.21': ['industry', 'banking_system_total_loan_financing_by_malaysian_financial_reporting_standards_9_mfrs_9_stages_and_total_provisions_rm_million_total_loan_financing_jumlah_total', '12_months_expected_credit_losses_stage_1', 'lifetime_expected_credit_losses_not_credit_impaired_stage_2', 'lifetime_expected_credit_losses_credit_impaired_stage_3', 'total_provisions', 'ratio_of_gross_impaired_loan_financing_to_gross_total_financing', 'ratio_of_net_impaired_financing_to_net_total_financing'],

    # Islamic Banking: Financing by MFRS 9 Stages and Provisions
    '1.21.1': ['industry', 'islamic_banking_system_total_financing_by_mfrs_9_stages_and_total_provisions_rm_million_total_financing_jumlah_total', '12_months_expected_credit_losses_stage_1', 'lifetime_expected_credit_losses_not_credit_impaired_stage_2', 'lifetime_expected_credit_losses_credit_impaired_stage_3', 'total_provisions', 'ratio_of_gross_impaired_financing_to_gross_total_financing', 'ratio_of_net_impaired_financing_to_net_total_financing'],

    # Islamic Banking: NPL/Impaired and Provisions (prev)
    '1.21.1a': ['ibs_of_investment_merchant_banks', 'non_performing_financing_impaired_financing', 'pendapatan_tergantung_income_in_suspense', 'peruntukan_jejas_nilai_individu_individual_impairment_provisions', 'collective_impairment_provisions', 'pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing', 'pembiayaan_bersih_net_total_financing', 'nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing', 'ratio_of_total_provisions_impairment_provisions_to_net_non_performing_financing_impaired_financing', 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing', 'impaired_financing', '6_months_pendapatan_tergantung_income_in_suspense', '6_months_peruntukan_jejas_nilai_individu_individual_impairment_provisions', 'general_provisions_collective_impairment_provisions', '6_months_pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing', '6_months_pembiayaan_bersih_net_total_financing', '6_months_nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing', 'impairment_provisions_to_net_non_performing_financing_impaired_financing', '6_months_nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing', 'total_financing'],

    # Islamic Banking: Impaired Financing and Provisions (prev)
    '1.21.1b': ['islamic_banking_scheme_ibs', 'impaired_financing', 'individual_impairment_provisions', 'collective_impairment_provisions', 'ratio_of_net_impaired_financing_to_net_total_financing', 'ratio_of_total_impairment_provisions_to_total_impaired_financing', 'ratio_of_collective_impairment_provisions_to_net_total_financing'],

    # Islamic Banking: Impaired Financing and Provisions (prev2)
    '1.21.1c': ['industry', 'impaired_financing', 'total_provisions', 'ratio_of_net_impaired_financing_to_net_total_financing', 'ratio_of_total_provisions_to_total_financing'],

    # Islamic Banking: Impaired Financing and Provisions (prev3)
    '1.21.1d': ['industry', 'impaired_loan_financing', 'total_provisions', 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing', 'ratio_of_total_provisions_to_total_loan_financing'],

    # Commercial & Islamic Banks: NPL/Impaired Loans
    '1.21.2': ['pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', 'faedah_tergantung_interest_in_suspense', 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans', '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', '6_months_faedah_tergantung_interest_in_suspense', '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans'],

    # Commercial & Islamic Banks: Impaired Loans (prev)
    '1.21.2a': ['impaired_loans', 'individual_impairment_provisions', 'collective_impairment_provisions', 'ratio_of_net_impaired_loans_to_net_total_loans', 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans'],

    # Commercial & Islamic Banks: Impaired Loans (prev2)
    '1.21.2b': ['impaired_loan_financing', 'total_provisions', 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing', 'ratio_of_total_provisions_to_total_loan_financing'],

    # Investment Banks: NPL/Impaired Loans
    '1.21.3': ['pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', 'faedah_tergantung_interest_in_suspense', 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans', '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', '6_months_faedah_tergantung_interest_in_suspense', '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans'],

    # Investment Banks: Impaired Loans (prev)
    '1.21.3a': ['impaired_loans', 'individual_impairment_provisions', 'collective_impairment_provisions', 'ratio_of_net_impaired_loans_to_net_total_loans', 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans'],

    # Investment Banks: Impaired Loans (prev2)
    '1.21.3b': ['impaired_loan_financing', 'total_provisions', 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing', 'ratio_of_total_provisions_to_total_loan_financing'],

    # Finance Companies: Loan Provisions and NPL
    '1.21.4': ['pinjaman_tak_berbayar_non_performing_loans', 'faedah_tergantung_interest_in_suspense', 'peruntukan_khas_specific_provisions', 'peruntukan_am_general_provisions', 'jumlah_pinjaman1_3_total_loans1_3', 'pinjaman_tak_berbayar4_non_performing_loans4', 'jumlah_pinjaman_bersih2_net_total_loans2', '6_months_pinjaman_tak_berbayar_non_performing_loans', '6_months_faedah_tergantung_interest_in_suspense', '6_months_peruntukan_khas_specific_provisions', '6_months_peruntukan_am_general_provisions', '6_months_jumlah_pinjaman1_3_total_loans1_3', '6_months_pinjaman_tak_berbayar4_non_performing_loans4', 'rm_million_jumlah_pinjaman_bersih2_net_total_loans2'],

    # Banking System: NPL/Impaired Loans and Provisions (prev)
    '1.21a': ['pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', 'faedah_tergantung_interest_in_suspense', 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans', '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans', '6_months_faedah_tergantung_interest_in_suspense', '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions', '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions', 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans', '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans', 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans'],

    # Banking System: Impaired Loans and Provisions (prev)
    '1.21b': ['impaired_loans', 'individual_impairment_provisions', 'collective_impairment_provisions', 'ratio_of_net_impaired_loans_to_net_total_loans', 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans'],

    # Banking System: Impaired Loans and Provisions (prev2)
    '1.21c': ['impaired_loan_financing', 'total_provisions', 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing', 'ratio_of_total_provisions_to_total_loan_financing'],

    # Banking System: Impaired Loans and Provisions (prev3)
    '1.21d': ['industry', 'impaired_loan_financing', 'total_provisions', 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing', 'ratio_of_total_provisions_to_total_loan_financing'],

    # Banking System: Impaired Loan/Financing by Purpose
    '1.22': ['purpose', 'purchase_of_securities', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total', 'cost_300k', 'cost_300k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total', 'purchase_of_industrial_building_factories', 'purchase_of_land_only', 'purchase_of_commercial_complexes', 'purchase_of_shophouses_shoplots', 'purchase_of_other_non_residential_property', 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total', 'purchase_of_consumer_durable_goods', 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_impaired_loan_financing'],

    # Commercial & Islamic Banks: NPL by Purpose
    '1.22.1': ['purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150_to_250k', '250k', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total', 'industrial_building_factories', 'land', 'commercial_complexes', 'shophouse', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'impaired_loans'],

    # Investment Banks: NPL/Impaired Loans by Purpose
    '1.22.2': ['purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150_to_250k', '250k', 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total', 'industrial_building_factories', 'land', 'commercial_complexes', 'shophouse', 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'impaired_loans'],

    # Banking System: NPL/Impaired Loans by Purpose (prev)
    '1.22a': ['purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'impaired_loans'],

    # Banking System: NPL/Impaired Loans by Purpose (prev2)
    '1.22b': ['purpose', 'purchase_of_securities', 'purchase_of_transport_vehicle', 'of_which_purchase_of_passenger_cars', 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total', '25k', '25k_to_60k', '60k_to_100k', '100k_to_150k', '150_to_250k', '250k', 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total', 'industrial_building_factories', 'land', 'commercial_complexes', 'shophouse', 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_uses', 'credit_cards', 'purchase_of_consumer_durable_goods', 'construction', 'working_capital', 'other_purpose', 'impaired_loans'],

    # Banking System: Impaired Loans by Purpose (prev)
    '1.22c': ['purpose', 'purchase_of_securities', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total', 'cost_250k', 'cost_250k_to_500k', 'cost_500k_to_1m', 'cost_1m', 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total', 'purchase_of_industrial_building_factories', 'purchase_of_land_only', 'purchase_of_commercial_complexes', 'purchase_of_shophouses_shoplots', 'purchase_of_other_non_residential_property', 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_total', 'purchase_of_consumer_durable_goods', 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others', 'credit_card', 'construction', 'working_capital', 'other_purposes', 'total_impaired_loan_financing'],

    # Banking System: Impaired Loan/Financing by Sector
    '1.23': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others', 'accommodation_and_food_service_activities', 'transportation_and_storage', 'information_and_communication', 'banking_system_impaired_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'household_sector', 'other_sector', 'total_impaired_loan_financing'],

    # Commercial & Islamic Banks: NPL by Sector
    '1.23.1': ['primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurant_hotels', 'construction', 'transport_storage_and_communication', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_imtermediation', 'real_estate_renting_and_business_activities', 'reseach_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'impaired_loans'],

    # Commercial & Islamic Banks: NPL by Sector (prev)
    '1.23.2': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'construction', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_services', 'consump_tion_credit', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tidak_berbayar_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_non_performing_loans_by_sector_previous_format_purpose_or_group_borrowers_lain_lain_others', 'total_non_performing_loans'],

    # Investment Banks: NPL/Impaired Loans by Sector
    '1.23.3': ['primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurant_hotels', 'construction', 'transport_storage_and_communication', 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_imtermediation', 'real_estate_renting_and_business_activities', 'reseach_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'impaired_loans'],

    # Merchant Banks: NPL by Sector (prev)
    '1.23.4': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufac_turing', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'construc_tion', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_services', 'consump_tion_credit', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'bank_saudagar_pinjaman_tidak_berbayar_mengikut_sektor_merchant_bank_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others', 'total_non_performing_loans'],

    # Finance Companies: Non-Performing Loans by Sector
    '1.23.5': ['agriculture_hunting_forestry_and_fishing', 'mining_and_quarrying', 'manufactu_ring', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'construc_tion', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_services', 'consump_tion_credit', 'purchase_of_securities', 'purchase_of_transport_vehicles', 'syarikat_kewangan_pinjaman_tidak_berbayar_mengikut_sektor_finance_companies_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others', 'total_non_performing_loans'],

    # Banking System: Impaired Loan/Financing by Type
    '1.23.6': ['type', 'overdraft_facilities', 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_total', 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total', 'purchase_of_passenger_cars', 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others', 'leasing_receivables', 'block_discounting_receivables', 'bridging_loans_financing', 'factoring_receivables', 'personal_loans_financing', 'housing_loans_financing', 'other_term_loans_financing', 'trade_bills_bill_financing', 'trust_receipts', 'revolving_credit', 'credit_charge_card', 'foreign_currency_loans_financing', 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others', 'total_impaired_loan_financing'],

    # Banking System: NPL/Impaired Loans by Sector (prev)
    '1.23a': ['primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_restaurants_hotels', 'construction', 'transport_storage_and_communication', 'finance_insurance_and_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'impaired_loans'],

    # Banking System: NPL/Impaired Loans by Sector (prev2)
    '1.23b': ['sector', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total', 'wholesale_trade', 'retail_trade', 'restaurant_hotels', 'construction', 'transport_storage_and_communication', 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total', 'financial_imtermediation', 'real_estate_renting_and_business_activities', 'reseach_development', 'other_business_activities', 'education_health_others', 'household_sector', 'other_sector_n_e_c', 'impaired_loans'],

    # Banking System: Total Deposits by Type
    '1.24': ['demand_deposits', 'fixed_deposits_special_investment_account_and_general_investment_account', 'saving_deposits', 'negotiable_instruments_of_deposits_issued', 'foreign_currency_deposit', 'tawarruq_fixed_deposits', 'others_deposit_accepted', 'banking_system_total_deposits_by_type_and_repurchase_agreements_rm_million_total_deposit_total', 'repurchase_agreements', 'total_deposits_and_repurchase_agreements'],

    # Islamic Banking: Deposits by Type
    '1.24.1': ['islamic_banking_system_deposits_by_type_discontinued', 'rm_special_investment_deposits', 'fx_special_investment_deposits', 'rm_general_investment_deposits', 'fx_general_investment_deposits', 'rm_demand_deposits', 'fx_demand_deposits', 'rm_saving_deposits', 'fx_saving_deposits', 'negotiable_instruments_of_deposits_issued', 'rm_tawarruq_fixed_deposits', 'fx_tawarruq_fixed_deposits', 'rm_others_deposit_accepted', 'fx_others_deposit_accepted', 'islamic_banking_system_deposits_by_type_discontinued_rm_million_total'],

    # Islamic Banking: Deposits by Type & Holder
    '1.24.2': ['islamic_banking_system_deposits_by_type_and_holder', 'kerajaan_persekutuan_federal_government', 'kerajaan_negeri_state_government', 'badan_berkanun_statutory_agency', 'institusi_kewangan_financial_institution', 'perusahaan_perniagaan_business_enterprises', 'individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_jumlah_total', 'fx_special_investment_deposits_kerajaan_persekutuan_federal_government', 'fx_special_investment_deposits_kerajaan_negeri_state_government', 'fx_special_investment_deposits_badan_berkanun_statutory_agency', 'fx_special_investment_deposits_institusi_kewangan_financial_institution', 'fx_special_investment_deposits_perusahaan_perniagaan_business_enterprises', 'fx_special_investment_deposits_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_jumlah_total', 'rm_general_investment_deposits_kerajaan_persekutuan_federal_government', 'rm_general_investment_deposits_kerajaan_negeri_state_government', 'rm_general_investment_deposits_badan_berkanun_statutory_agency', 'rm_general_investment_deposits_institusi_kewangan_financial_institution', 'rm_general_investment_deposits_perusahaan_perniagaan_business_enterprises', 'rm_general_investment_deposits_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_jumlah_total', 'fx_general_investment_deposits_kerajaan_persekutuan_federal_government', 'fx_general_investment_deposits_kerajaan_negeri_state_government', 'fx_general_investment_deposits_badan_berkanun_statutory_agency', 'fx_general_investment_deposits_institusi_kewangan_financial_institution', 'fx_general_investment_deposits_perusahaan_perniagaan_business_enterprises', 'fx_general_investment_deposits_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_jumlah_total', 'rm_demand_deposits_by_customer_kerajaan_persekutuan_federal_government', 'rm_demand_deposits_by_customer_kerajaan_negeri_state_government', 'rm_demand_deposits_by_customer_badan_berkanun_statutory_agency', 'rm_demand_deposits_by_customer_institusi_kewangan_financial_institution', 'rm_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises', 'rm_demand_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_jumlah_total', 'fx_demand_deposits_by_customer_kerajaan_persekutuan_federal_government', 'fx_demand_deposits_by_customer_kerajaan_negeri_state_government', 'fx_demand_deposits_by_customer_badan_berkanun_statutory_agency', 'fx_demand_deposits_by_customer_institusi_kewangan_financial_institution', 'fx_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises', 'fx_demand_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_jumlah_total', 'rm_saving_deposits_by_customer_institusi_kewangan_financial_institution', 'rm_saving_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_jumlah_total', 'fx_saving_deposits_by_customer_institusi_kewangan_financial_institution', 'fx_saving_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_jumlah_total', 'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_persekutuan_federal_government', 'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_negeri_state_government', 'rm_negotiable_instruments_of_deposits_issued_by_customer_badan_berkanun_statutory_agency', 'rm_negotiable_instruments_of_deposits_issued_by_customer_institusi_kewangan_financial_institution', 'rm_negotiable_instruments_of_deposits_issued_by_customer_perusahaan_perniagaan_business_enterprises', 'rm_negotiable_instruments_of_deposits_issued_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_jumlah_total', 'rm_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government', 'rm_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government', 'rm_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency', 'rm_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution', 'rm_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises', 'rm_tawarruq_fixed_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_jumlah_total', 'fx_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government', 'fx_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government', 'fx_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency', 'fx_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution', 'fx_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises', 'fx_tawarruq_fixed_deposits_by_customer_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_jumlah_total', 'rm_others_deposits_kerajaan_persekutuan_federal_government', 'rm_others_deposits_kerajaan_negeri_state_government', 'rm_others_deposits_badan_berkanun_statutory_agency', 'rm_others_deposits_institusi_kewangan_financial_institution', 'rm_others_deposits_perusahaan_perniagaan_business_enterprises', 'rm_others_deposits_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_jumlah_total', 'fx_others_deposits_kerajaan_persekutuan_federal_government', 'fx_others_deposits_kerajaan_negeri_state_government', 'fx_others_deposits_badan_berkanun_statutory_agency', 'fx_others_deposits_institusi_kewangan_financial_institution', 'fx_others_deposits_perusahaan_perniagaan_business_enterprises', 'fx_others_deposits_individu_individuals', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_lain_lain_others', 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_jumlah_total'],

    # Islamic Banking: Deposits by Type and Holder (prev)
    '1.24.3': ['akhir_tempoh_as_at_end_of_1', 'banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder', 'kerajaan_government', 'institusi_kewangan_financial_institutions', 'badan_perniagaan_business_enterprises', 'individu_individuals', 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_permintaan_demand_deposits_jumlah_total', 'investment_deposits_kerajaan_government', 'investment_deposits_institusi_kewangan_financial_institutions', 'investment_deposits_badan_perniagaan_business_enterprises', 'investment_deposits_individu_individuals', 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_pelaburan_investment_deposits_jumlah_total', 'saving_deposits_institusi_kewangan_financial_institutions', 'saving_deposits_individu_individuals', 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_rm_million_jumlah_total'],

    # Banking System: Total Deposits by Holder
    '1.25': ['federal_government', 'state_government', 'statutory_agency', 'financial_institution', 'business_enterprises', 'individuals', 'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_others', 'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_total'],

    # Banking System: Demand Deposits by Holder
    '1.25.1': ['holder', 'banking_system_demand_deposits_by_holder', 'federal_government', 'state_government', 'statutory_agency', 'financial_institution', 'business_enterprises', 'individuals', 'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_others', 'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_total'],

    # Banking System: Savings and Fixed Deposits by Holder
    '1.25.2': ['holder', 'federal_government', 'state_government', 'statutory_agency', 'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_financial_institution', 'business_enterprises', 'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_individuals', 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_others', 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_total', 'saving_deposit_by_customer_financial_institution', 'saving_deposit_by_customer_individuals', 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_others', 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_total'],

    # Banking System: Repurchase Agreements by Holder
    '1.25.3': ['holder', 'banking_system_repurchase_agreements_by_holder', 'federal_government', 'state_government', 'statutory_agency', 'financial_institution', 'business_enterprises', 'individuals', 'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_others', 'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_total'],

    # Banking System: NIDs by Holder
    '1.25.4': ['holder', 'banking_system_negotiable_instruments_of_deposits_by_holder', 'federal_government', 'state_government', 'statutory_agency', 'financial_institution', 'business_enterprises', 'individuals', 'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_others', 'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_total'],

    # Banking System: Foreign Currency and Other Deposits by Holder
    '1.25.5': ['holder', 'banking_system_foreign_currency_and_other_deposits_by_holder', 'federal_government', 'state_government', 'statutory_agency', 'financial_institution', 'business_enterprises', 'individuals', 'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_others', 'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_total', 'other_deposits_accepted', 'total_deposits'],

    # Banking System: Fixed Deposits by Original Maturity
    '1.25.6': ['original_maturity', 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity', 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_total', 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_up_to_1_year_in_months_total', 'le_1_month', 'gt_1_month_to_3_months', 'gt_3_months_to_6_months', 'gt_6_months_to_9_months', 'gt_9_months_to_12_months', 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_exceeding_1_year_in_years_total', 'gt_1_year_to_3_years', 'gt_3_years_to_4_years', 'gt_4_years_to_5_years', 'gt_5_years'],

    # Statutory Reserve Requirement and Liquidity Ratio
    '1.26': [],

    # Statutory Reserve and Liquid Asset Requirement
    '1.27': ['rizab_berkanun_statutory_reserve', 'tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities', 'islamic_banks_rizab_berkanun_statutory_reserve', 'islamic_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities', 'investment_banks_rizab_berkanun_statutory_reserve', 'investment_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities'],

    # New Liquidity Framework
    '1.28': ['keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'lebihan_pematuhan_bersih_net_compliance_surplus', 'maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus', 'tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'islamic_banks_tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'maturity_le_1_week_lebihan_pematuhan_bersih_net_compliance_surplus', 'islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'rm_million_islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus', 'maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'tempoh_matang_kurang_daripada_3_hari_maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'maturity_le_3_days_lebihan_pematuhan_bersih_net_compliance_surplus', 'maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'tempoh_matang_lebih_daripada_3_hari_hingga_1_bulan_maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm', 'maturity_gt_3_days_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus'],

    # Liquidity Coverage Ratio
    '1.28a': ['nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio', 'aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets', 'aliran_keluar_tunai_bersih²_net_cash_outflows²', 'commercial_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio', 'commercial_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets', 'commercial_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²', 'islamic_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio', 'islamic_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets', 'islamic_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²', 'investment_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio', 'investment_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets', 'investment_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²'],

    # Banking System: Constituents of Capital
    '1.29': ['tier_1_capital', 'tier_2_capital', 'total_capital', 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital', 'capital_base', 'aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1', 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2', 'total_risk_weighted_assets', 'risk_weighted_capital_ratio', 'core_capital_ratio'],

    # Islamic Banking System: Constituents of Capital
    '1.29.1': ['akhir_tempoh_as_at_end_of_1', 'ibs_of_investment_merchant_banks', 'core_capital', 'tier_2_capital', 'total_capital', 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital', 'capital_base', 'aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1', 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2', 'total_risk_weighted_assets', 'risk_weighted_capital_ratio', 'core_capital_ratio'],

    # Islamic Banking System: Constituents of Capital (v2)
    '1.29.1a': ['islamic_banking_scheme_ibs', 'cet1_capital', 'tier_1_capital', 'total_capital', 'total_risk_weighted_assets', 'cet1_capital_ratio', 'tier_1_capital_ratio', 'total_capital_ratio'],

    # Commercial & Islamic Banks: Constituents of Capital
    '1.29.2': ['akhir_tempoh_end_of_period_1', 'tier_1_capital', 'tier_2_capital', 'total_capital', 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital', 'capital_base', 'aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1', 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2', 'total_risk_weighted_assets', 'capital_ratio', 'core_capital_ratio'],

    # Commercial & Islamic Banks: Capital (prev)
    '1.29.2a': ['cet1_capital', 'tier_1_capital', 'total_capital', 'total_risk_weighted_assets', 'cet1_capital_ratio', 'tier_1_capital_ratio', 'total_capital_ratio'],

    # Finance Companies: Constituents of Capital
    '1.29.3': ['akhir_tempoh_end_of_period_1', 'tier_1_capital', 'tier_2_capital', 'total_capital', 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital', 'capital_base', 'aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1', 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2', 'total_risk_weighted_assets', 'risk_weighted_capital_ratio', 'core_capital_ratio'],

    # Investment Banks: Constituents of Capital
    '1.29.4': ['tier_1_capital', 'tier_2_capital', 'total_capital', 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital', 'capital_base', 'aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight', 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1', 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2', 'total_risk_weighted_assets', 'risk_weighted_capital_ratio', 'core_capital_ratio'],

    # Investment Banks: Constituents of Capital (prev)
    '1.29.4a': ['cet1_capital', 'tier_1_capital', 'total_capital', 'total_risk_weighted_assets', 'cet1_capital_ratio', 'tier_1_capital_ratio', 'total_capital_ratio'],

    # Banking System: Constituents of Capital (v2)
    '1.29a': ['bank_pelaburan_investment_banks', 'cet1_capital', 'tier_1_capital', 'total_capital', 'total_risk_weighted_assets', 'cet1_capital_ratio', 'tier_1_capital_ratio', 'total_capital_ratio'],

    # Banking System: Constituents of Capital (prev)
    '1.29b': ['cet1_capital', 'tier_1_capital', 'total_capital', 'total_risk_weighted_assets', 'cet1_capital_ratio', 'tier_1_capital_ratio', 'total_capital_ratio'],

    # Monetary Aggregates: M1, M2 and M3
    '1.3': ['monetary_aggregates_m1_m2_and_m', 'total_m', 'jumlah_total_m', 'm_jumlah_total_m', 'currency_m', 'demand_m', 'narrow_qm', 'savings_deposits', 'fixed_deposits', 'nids', 'repos', 'fx_deposits', 'other_deposits', 'deposits_placed_with_other_banking_institutions'],

    # Broad Money, M3
    '1.3.1': ['wang_secara_luas_m_broad_money_m_m_jumlah_total', 'wang_secara_luas_m_broad_money_m_m_baki_urus_niaga_transaction_balances_jumlah_total', 'currency_in_circulation', 'demand_deposits', 'wang_secara_luas_m_broad_money_m_m_separuh_wang_secara_luas_broad_quasi_money_jumlah_total', 'savings_deposits', 'fixed_deposits', 'nids', 'repos', 'foreign_currency_deposits', 'other_deposits'],

    # Factors Affecting M3
    '1.3.2': ['faktor_penentu_m_factors_affecting_m_jumlah_total', 'faktor_penentu_m_factors_affecting_m_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total', 'claims_on_government', 'government_deposits', 'faktor_penentu_m_factors_affecting_m_tuntutan_ke_atas_sektor_swasta_claims_on_the_private_sector_jumlah_total', 'loans', 'securities', 'faktor_penentu_m_factors_affecting_m_aset_asing_bersih_net_foreign_assets_jumlah_total', 'bnm', 'banking_system', 'other_influences'],

    # Credit Card Operations in Malaysia
    '1.30': ['no_of_card_transactions¹', 'in_malaysia_local_cardholders²', 'in_malaysia_foreign_cardholders³', 'abroad_local_cardholders²', 'total_cash_advances_in_malaysia_local_cardholders²', 'total_cash_advances_in_malaysia_foreign_cardholders³', 'total_cash_advances_abroad_local_cardholders²', 'principal_cards', 'supplementary_cards', 'amount_of_credit_line_extended', 'current_balances', '3_months', '3_to_6_months', '6_months'],

    # Debit Card Transactions
    '1.30.1': ['number_of_card_transactions', 'total_purchases_in_malaysia', 'total_purchases_abroad', 'total_cash_withdrawals_via_pos_terminal_in_malaysia', 'total_cash_withdrawals_via_pos_terminal_abroad', 'total_fund_transfer_in_malaysia', 'total_cash_withdrawals_via_atm_in_malaysia', 'rm_million_unit_million_abroad'],

    # Banking System: Loan to Fund Ratio and Liquidity
    '1.31': ['deposit_rm_billion', 'debt', 'equity', 'loan', 'loan_to_fund_ratio', 'loan_to_fund_and_equity_ratio', 'money_market_borrowings_excluding_repos_rm_billion', 'repo', 'bnm_debt_securities', 'srr', 'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_lain_lain_others', 'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_jumlah_total'],

    # Islamic Banking: Total Investment Account by Type and Holder
    '1.32': ['islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_restricted_investment_account¹_total', 'financial_institution', 'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_unrestricted_investment_account¹_total', 'business_enterprises', 'individuals', 'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_jumlah_total'],

    # Islamic Banking: Assets funded through Investment Account
    '1.32.1': ['loans_and_advances', 'amount_due_from_designated_financial_institutions', 'other_assets', 'total_assets'],

    # Islamic Banking: Financing through Investment Account by Type
    '1.32.2': ['syndicated_financing', 'housing_financing', 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others', 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others_1', 'total_financing'],

    # Islamic Banking: Financing through Investment Account by Concept
    '1.32.3': ['bai_bithaman_ajil', 'murabahah', 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_concept_rm_million_others', 'total_financing'],

    # Islamic Banking: Financing through Investment Account by Purpose
    '1.32.4': ['purchase_of_securities', 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_purpose_and_sectors_rm_million_purpose_purchase_of_transport_vehicles_total', 'of_which_purchase_of_passenger_cars', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'purchase_of_fixed_assets_other_than_land_and_building', 'personal_use', 'pembinaan_construction', 'working_capital', 'other_purpose', 'total_financing', 'primary_agriculture', 'mining_and_quarrying', 'manufacturing_including_agro_based', 'electricity_gas_and_water_supply', 'wholesale_retail_trade_and_hotels_restaurants', 'sector_pembinaan_construction', 'real_estate', 'transport_storage_and_communications', 'finance_insurance_and_business_activities', 'education_health_and_others', 'household_sector', 'other_sector_n_e_c'],

    # Islamic Banking: Total Investment Account by Original Maturity
    '1.32.5': ['islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_jumlah_total', 'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_up_to_1_year_in_months_total', 'le_1_month', 'gt_1_month_to_3_months', 'gt_3_months_to_6_months', 'gt_6_months_to_9_months', 'gt_9_months_to_12_months', 'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_exceeding_1_year_in_years_total', 'gt_1_year_to_3_years', 'gt_3_years_to_4_years', 'gt_4_years_to_5_years', 'gt_5_years'],

    # Financial Institution: SME Loan/Financing by Sector
    '1.33': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'total_outstanding_loan_financing'],

    # Financial Institution: SME Loan/Financing Applied by Sector
    '1.33.1': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'financing_applied'],

    # Financial Institution: SME Loan/Financing Approved by Sector
    '1.33.2': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'financing_approved'],

    # Financial Institution: SME Loan/Financing Disbursed by Sector
    '1.33.3': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'financing_disbursed'],

    # Financial Institution: SME Loan/Financing Repaid by Sector
    '1.33.4': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'financing_repaid'],

    # Financial Institution: Impaired SME Loan/Financing by Sector
    '1.33.5': ['sector', 'agriculture_forestry_and_fishing', 'mining_and_quarrying', 'manufacturing', 'electricity_gas_steam_and_air_conditioning_supply', 'water_supply_sewerage_waste_management_and_remediation_activities', 'construction', 'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total', 'wholesale_trade_except_of_motor_vehicles_and_motorcycles', 'retail_trade_except_of_motor_vehicles_and_motorcycles', 'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others', 'accommodation_and_food_service_activities', 'transportation_storage', 'information_communication', 'financial_and_insurance_takaful_activities', 'real_estate_activities', 'professional_scientific_and_technical_activities', 'administrative_and_support_service_activities', 'education_health_and_others', 'other_sector', 'financing'],

    # Financial Institutions: SME Loan/Financing by Purpose
    '1.34': ['purpose', 'purchase_of_securities', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total', 'purchase_of_passenger_cars', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others', 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others', 'purchase_of_residential_property', 'purchase_of_non_residential_property', 'construction', 'working_capital', 'other_purposes', 'financing', 'memo_item_credit_card'],

    # Financial Institution: SME Loan/Financing by SME Size
    '1.35': ['sme_size', 'individual_for_business', 'micro', 'small', 'medium', 'financing'],

    # Financial Institution: SME Loans Applied and Approved by Size
    '1.35.1': ['sme_size', 'individu_bagi_tujuan_perniagaan_individual_for_business', 'mikro_micro', 'kecil_small', 'sederhana_medium', 'financing_applied', 'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business', 'rm_million_mikro_micro', 'rm_million_kecil_small', 'rm_million_sederhana_medium', 'financing_approved'],

    # Financial Institution: SME Loans Disbursed and Repaid by Size
    '1.35.2': ['sme_size', 'individu_bagi_tujuan_perniagaan_individual_for_business', 'mikro_micro', 'kecil_small', 'sederhana_medium', 'financing_disbursed', 'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business', 'rm_million_mikro_micro', 'rm_million_kecil_small', 'rm_million_sederhana_medium', 'financing_repaid'],

    # Financial Institution: Impaired SME Loans by Size
    '1.35.3': ['sme_size', 'individual_for_business', 'micro', 'small', 'medium', 'financing'],

    # Financial Institution: SME Loan/Financing by Loan Size
    '1.36': ['loan_size', 'rm', 'rm1_million', 'rm1_juta_hingga_rm5_juta_rm5_million', 'rm5_juta_rm5_million', 'total_outstanding_loan_financing'],

    # BNM: Statement of Assets
    '1.4': ['pada_akhir_tempoh_end_of_period_1', 'bank_negara_malaysia_statement_of_assets', 'gold_and_foreign_exchange', 'imf_reserve_tranche_position', 'holdings_of_special_drawing_rights', 'malaysian_government_papers', 'bills_discounted', 'deposits_with_financial_institutions', 'loans_and_advances', 'deferred_expenditure', 'properties_land_and_buildings', 'other_assets', 'total_assets'],

    # BNM: Statement of Capital and Liabilities
    '1.5': ['bank_negara_malaysia_statement_of_capital_and_liabilities', 'paid_up_capital', 'reserves', 'currency_in_circulation', 'financial_institutions', 'federal_government', 'bank_negara_malaysia_penyata_modal_dan_liabiliti_bank_negara_malaysia_statement_of_capital_and_liabilities_deposit_deposits_lain_lain_others', 'bank_negara_bills_and_bonds', 'allocation_of_special_drawing_rights', 'other_liabilities', 'total_liabilities'],

    # BNM: Statement of Capital and Liabilities (prev)
    '1.5.1': ['bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format', 'paid_up_capital', 'general_reserve_fund', 'other_reserves', 'currency_in_circulation', 'financial_institutions', 'federal_government', 'bank_negara_malaysia_penyata_modal_dan_liabiliti_format_terdahulu_bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format_deposit_deposits_lain_lain_others', 'bank_negara_bills_and_bonds', 'allocation_of_special_drawing_rights', 'other_liabilities', 'total_liabilities'],

    # Banking System: Statement of Assets
    '1.7': ['assets', 'wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents', 'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia', 'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos', 'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia', 'residents_bank_negara_malaysia', 'residents_commercial_banks', 'residents_islamic_banks', 'residents_investment_banks', 'residents_other_banking_institutions', 'bukan_pemastautin_non_residents', 'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions', 'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held', 'bil_perbendaha_raan_treasury_bills', 'sekuriti_kerajaan_¹_government_securities_¹', 'sekuriti_lain_other_securities', 'pinjaman_dan_pendahuluan_loans_and_advances', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain_other_assets', 'jumlah_aset_total_assets', 'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents', 'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia', 'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos', 'deposits_placed_and_reverse_repos_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia', 'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia', 'amount_due_from_designated_financial_institutions_residents_commercial_banks', 'amount_due_from_designated_financial_institutions_residents_islamic_banks', 'amount_due_from_designated_financial_institutions_residents_investment_banks', 'amount_due_from_designated_financial_institutions_residents_other_banking_institutions', 'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents', 'amount_due_from_designated_financial_institutions_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions', 'amount_due_from_designated_financial_institutions_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held', 'malaysian_securities_bil_perbendaha_raan_treasury_bills', 'malaysian_securities_sekuriti_kerajaan_¹_government_securities_¹', 'malaysian_securities_sekuriti_lain_other_securities', 'malaysian_securities_pinjaman_dan_pendahuluan_loans_and_advances', 'malaysian_securities_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'malaysian_securities_aset_lain_other_assets', 'malaysian_securities_jumlah_aset_total_assets', 'rm_million_jumlah_aset_total_assets'],

    # Islamic Banking System: Statement of Assets
    '1.7.1': ['assets', 'cash_and_cash_equivalents', 'balances_in_current_account_with_bank_negara_malaysia', 'other_deposits_placed_and_reverse_repos', 'statutory_deposits_with_bank_negara_malaysia', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'non_residents', 'investment_account_due_from_designated_financial_institutions', 'negotiable_instrument_deposits_held', 'treasury_bills', 'government_securities¹', 'other_securities', 'loans_and_advances', 'property_plant_and_equipment', 'other_assets', 'total_assets'],

    # Commercial & Islamic Banks: Statement of Assets
    '1.7.2': ['cash_and_cash_equivalents', 'balances_in_current_account_with_bank_negara_malaysia', 'other_deposits_placed_and_reverse_repos', 'statutory_deposits_with_bank_negara_malaysia', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'non_residents', 'investment_account_due_from_designated_financial_institutions', 'negotiable_instrument_deposits_held', 'treasury_bills', 'government_securities_¹', 'other_securities', 'loans_and_advances', 'property_plant_and_equipment', 'other_assets', 'total_assets'],

    # Commercial & Islamic Banks: Assets (prev)
    '1.7.2.1': [],

    # Commercial & Islamic Banks: Domestic & Foreign Assets
    '1.7.3': ['wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents', 'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia', 'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos', 'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia', 'residents_bank_negara_malaysia', 'residents_commercial_banks', 'residents_islamic_banks', 'residents_investment_banks', 'residents_other_banking_institutions', 'bukan_pemastautin_non_residents', 'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions', 'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held', 'bil_perbendaha_raan_treasury_bills', 'sekuriti_kerajaan1_government_securities1', 'sekuriti_lain_other_securities', 'pinjaman_dan_pendahuluan_loans_and_advances', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain_other_assets', 'jumlah_aset_total_assets', 'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents', 'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia', 'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos', 'bank_asing_foreign_banks_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia', 'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia', 'amount_due_from_designated_financial_institutions_residents_commercial_banks', 'amount_due_from_designated_financial_institutions_residents_islamic_banks', 'amount_due_from_designated_financial_institutions_residents_investment_banks', 'amount_due_from_designated_financial_institutions_residents_other_banking_institutions', 'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents', 'bank_asing_foreign_banks_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions', 'bank_asing_foreign_banks_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held', 'malaysian_securities_bil_perbendaha_raan_treasury_bills', 'malaysian_securities_sekuriti_kerajaan1_government_securities1', 'bank_asing_foreign_banks_sekuriti_lain_other_securities', 'bank_asing_foreign_banks_pinjaman_dan_pendahuluan_loans_and_advances', 'bank_asing_foreign_banks_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'bank_asing_foreign_banks_aset_lain_other_assets', 'bank_asing_foreign_banks_jumlah_aset_total_assets'],

    # Commercial & Islamic Banks: Domestic & Foreign Assets (prev)
    '1.7.3.1': ['cash', 'balances_with_the_central_bank_of_malaysia', 'statutory_reserve_with_the_central_bank_of_malaysia', 'money_at_call_in_malaysia', 'other_banks', 'finance_companies', 'merchant_banks', 'outside_malaysia', 'negotiable_instruments_of_deposit_held', 'treasury_bills', 'government_securities', 'other_securities', 'overdrafts_and_other_advances', 'more_than_1_year_to_4_years', 'more_than_4_years', 'of_which_outside_malaysia', 'bankers_acceptances', 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_bil_bil_perdagangan_trade_bills_kena_bayar_di_malaysia_payable_in_malaysia_lain_lain_other', 'payable_outside_malaysia', 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_jumlah_total', 'cheques_purchased', 'fixed_and_other_assets_in_malaysia', 'other_foreign_assets', 'total_assets'],

    # Investment Banks: Statement of Assets
    '1.7.4': ['cash_and_cash_equivalents', 'balances_in_current_account_with_bank_negara_malaysia', 'other_deposits_placed_and_reverse_repos', 'statutory_deposits_with_bank_negara_malaysia', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'non_residents', 'negotiable_instrument_deposits_held', 'treasury_bills', 'government_securities', 'other_securities', 'loans_and_advances', 'property_plant_and_equipment', 'other_assets', 'total_assets'],

    # Finance Companies: Statement of Assets
    '1.7.5': ['cash', 'balances_with_bank_negara_malaysia', 'statutory_reserves_with_bank_negara_malaysia', 'other_deposits_placed_and_reverse_repos', 'money_at_call_in_malaysia', 'central_bank_of_malaysia', 'commercial_banks', 'finance_companies', 'merchant_banks', 'other_banking_institutions', 'di_luar_malaysia_outside_malaysia', 'negotiable_instruments_of_deposit_held', 'treasury_bills', 'government_securities', 'other_securities', 'loans_and_advances', 'fixed_assets', 'in_malaysia', 'in_malaysia_di_luar_malaysia_outside_malaysia', 'total_assets'],

    # Banking System: Statement of Assets (prev)
    '1.7a': ['assets', 'cash_and_cash_equivalents', 'balances_in_current_account_with_bank_negara_malaysia', 'other_deposits_placed_and_reverse_repos', 'statutory_deposits_with_bank_negara_malaysia', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'non_residents', 'investment_account_due_from_designated_financial_institutions', 'negotiable_instrument_deposits_held', 'treasury_bills', 'government_securities_¹', 'other_securities', 'loans_and_advances', 'property_plant_and_equipment', 'other_assets', 'total_assets'],

    # Banking System: Statement of Capital and Liabilities
    '1.9': ['equities_and_liabilities', 'modal_dan_rizab_total_equities', 'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund', 'akaun_deposit_khas_special_deposit_account', 'banking_system_statement_of_equities_and_liabilities_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others', 'residents_bank_negara_malaysia', 'residents_commercial_banks', 'residents_islamic_banks', 'residents_investment_banks', 'residents_other_banking_institutions', 'bukan_pemastautin_non_residents', 'akaun_pelaburan_dari_pengguna_investment_account_of_customers', 'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions', 'penerimaan_belum_bayar_acceptances_payable', 'pemastautin_residents', 'bills_payable_bukan_pemastautin_non_residents', 'tanggungan_lain_other_liabilities', 'bank_tempatan_domestic_banks_total_equities_and_liabilities', 'bank_asing_foreign_banks_modal_dan_rizab_total_equities', 'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund', 'total_deposits_akaun_deposit_khas_special_deposit_account', 'banking_system_statement_of_equities_and_liabilities_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others', 'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia', 'amount_due_to_designated_financial_institutions_residents_commercial_banks', 'amount_due_to_designated_financial_institutions_residents_islamic_banks', 'amount_due_to_designated_financial_institutions_residents_investment_banks', 'amount_due_to_designated_financial_institutions_residents_other_banking_institutions', 'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents', 'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers', 'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions', 'total_investment_account_penerimaan_belum_bayar_acceptances_payable', 'bills_payable_pemastautin_residents', 'total_liabilities_bills_payable_bukan_pemastautin_non_residents', 'bills_payable_tanggungan_lain_other_liabilities', 'bank_asing_foreign_banks_total_equities_and_liabilities', 'rm_million_total_equities_and_liabilities'],

    # Islamic Banking System: Statement of Capital & Liabilities
    '1.9.1': ['equities_and_liabilities', 'total_equities', 'deposits_under_the_new_investment_fund', 'special_deposit_account', 'islamic_banking_system_statement_of_equities_and_liabilities_rm_million_total_liabilities_total_deposits_lain_lain_others', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'bukan_pemastautin_non_residents', 'investment_account_of_customers', 'investment_account_due_to_designated_financial_institutions', 'miscellaneous_borrowing', 'miscellaneous_debt_securities_issued', 'acceptances_payable', 'residents', 'bills_payable_bukan_pemastautin_non_residents', 'other_liabilities', 'total_equities_and_liabilities'],

    # Commercial & Islamic Banks: Statement of Liabilities
    '1.9.2': ['total_equities', 'deposits_under_the_new_investment_fund', 'special_deposit_account', 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'bukan_pemastautin_non_residents', 'investment_account_of_customers', 'investment_account_due_to_designated_financial_institutions', 'acceptances_payable', 'residents', 'bills_payable_bukan_pemastautin_non_residents', 'other_liabilities', 'total_equities_and_liabilities'],

    # Commercial & Islamic Banks: Liabilities (prev)
    '1.9.2.1': ['capital_and_reserves', 'demand', 'fixed', 'savings', 'bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_previous_format_deposit_deposits_jumlah_total', 'negotiable_instruments_of_deposits_issued', 'deposits_under_the_new_investment_fund', 'special_deposit_account', 'other_banks', 'finance_companies', 'merchant_banks', 'di_luar_malaysia_outside_malaysia', 'bankers_acceptances_outstanding', 'di_malaysia_in_malaysia', 'in_malaysia_di_luar_malaysia_outside_malaysia', 'other_liabilities_di_malaysia_in_malaysia', 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia', 'total_liabilities'],

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities
    '1.9.3': ['modal_dan_rizab_total_equities', 'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund', 'akaun_deposit_khas_special_deposit_account', 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others', 'residents_bank_negara_malaysia', 'residents_commercial_banks', 'residents_islamic_banks', 'residents_investment_banks', 'residents_other_banking_institutions', 'bukan_pemastautin_non_residents', 'akaun_pelaburan_dari_pengguna_investment_account_of_customers', 'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions', 'penerimaan_belum_bayar_acceptances_payable', 'pemastautin_residents', 'bills_payable_bukan_pemastautin_non_residents', 'tanggungan_lain_other_liabilities', 'jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities', 'bank_asing_foreign_banks_modal_dan_rizab_total_equities', 'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund', 'total_deposits_akaun_deposit_khas_special_deposit_account', 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others', 'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia', 'amount_due_to_designated_financial_institutions_residents_commercial_banks', 'amount_due_to_designated_financial_institutions_residents_islamic_banks', 'amount_due_to_designated_financial_institutions_residents_investment_banks', 'amount_due_to_designated_financial_institutions_residents_other_banking_institutions', 'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents', 'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers', 'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions', 'total_liabilities_penerimaan_belum_bayar_acceptances_payable', 'bills_payable_pemastautin_residents', 'total_liabilities_bills_payable_bukan_pemastautin_non_residents', 'total_liabilities_tanggungan_lain_other_liabilities', 'total_liabilities_jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities'],

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities (prev)
    '1.9.3.1': ['capital_and_reserves', 'permintaan_demand', 'tetap_fixed', 'tabungan_savings', 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_deposits_jumlah_total', 'instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued', 'deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds', 'akaun_deposit_khas_special_deposit_account', 'bank_bank_lain_other_banks', 'syarikat_kewangan_finance_companies', 'bank_saudagar_merchant_banks', 'di_luar_malaysia_outside_malaysia', 'penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding', 'di_malaysia_in_malaysia', 'in_malaysia_di_luar_malaysia_outside_malaysia', 'other_liabilities_di_malaysia_in_malaysia', 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia', 'jumlah_tanggungan_total_liabilities', 'bank_asing_foreign_banks', 'deposits_permintaan_demand', 'in_malaysia_tetap_fixed', 'in_malaysia_tabungan_savings', 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_amounts_due_to_deposits_in_malaysia_jumlah_total', 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued', 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds', 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_akaun_deposit_khas_special_deposit_account', 'in_malaysia_bank_bank_lain_other_banks', 'in_malaysia_syarikat_kewangan_finance_companies', 'in_malaysia_bank_saudagar_merchant_banks', 'amounts_due_to_di_luar_malaysia_outside_malaysia', 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding', 'bills_payable_di_malaysia_in_malaysia', 'bills_payable_in_malaysia_di_luar_malaysia_outside_malaysia', 'tanggungan_lain_other_liabilities_di_malaysia_in_malaysia', 'amounts_due_to_other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia', 'rm_juta_rm_million_jumlah_tanggungan_total_liabilities'],

    # Investment Banks: Statement of Liabilities
    '1.9.4': ['total_equities', 'deposits_under_the_new_investment_fund', 'special_deposit_account', 'merchant_banks_investment_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'bukan_pemastautin_non_residents', 'acceptances_payable', 'residents', 'bills_payable_bukan_pemastautin_non_residents', 'other_liabilities', 'total_equities_and_liabilities'],

    # Finance Companies: Statement of Liabilities
    '1.9.5': ['capital_and_reserves', 'total_deposits', 'deposits_under_the_new_investment_fund', 'special_deposits_account', 'central_bank_of_malaysia', 'commercial_banks', 'finance_companies', 'merchant_banks', 'other_banking_institutions', 'di_luar_malaysia_outside_malaysia', 'bankers_acceptances_outstanding', 'di_malaysia_in_malaysia', 'in_malaysia_di_luar_malaysia_outside_malaysia', 'other_liabilities_di_malaysia_in_malaysia', 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia', 'total_liabilities'],

    # Finance Companies: Assets and Liabilities (prev)
    '1.9.5.1': ['cash', 'statutory_reserve_with_bnm', 'money_at_call', 'demand', 'tetap_fixed', 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_dengan_bank_deposits_with_banks_di_malaysia_in_malaysia_jumlah_total', 'di_luar_malaysia_outside_malaysia', 'treasury_bills', 'government_securities', 'subsidiary_and_other_companies', 'loans_to_financial_institutions', 'hire_purchase', 'leasing', 'housing', 'other_purposes', 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_pelannggan_lain_other_customer_jumlah_total', 'receivables_under_refinancing', 'fixed_and_other_assets', 'total_assets_liabilities', 'capital_and_reserves', 'deposits_of_customers_other_than_banks_tetap_fixed', 'savings', 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_pelanggan_selain_bank_other_customer_deposits_of_customers_other_than_banks_in_malaysia_jumlah_total', 'special_deposit_account', 'in_malaysia', 'in_malaysia_di_luar_malaysia_outside_malaysia', 'liabilities_under_refinancing', 'other_liabilities'],

    # Banking System: External Assets and Liabilities
    '1.9.6': ['amount_due_from_designated_financial_institutions', 'stock_and_shares', 'investments', 'loans_financing_and_advances', 'other_external_assets', 'banking_system_external_assets_and_external_liabilities_rm_million_total_external_assets_total', 'amount_due_to_designated_financial_institutions', 'deposits_accepted', 'bills_payable', 'other_external_liabilities', 'banking_system_external_assets_and_external_liabilities_rm_million_total_external_liabilities_total', 'net_external_liabilities'],

    # Banking System: Capital and Liabilities (prev)
    '1.9a': ['equities_and_liabilities', 'total_equities', 'deposits_under_the_new_investment_fund', 'special_deposit_account', 'banking_system_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others', 'bank_negara_malaysia', 'commercial_banks', 'islamic_banks', 'investment_banks', 'other_banking_institutions', 'bukan_pemastautin_non_residents', 'investment_account_of_customers', 'investment_account_due_to_designated_financial_institutions', 'acceptances_payable', 'residents', 'bills_payable_bukan_pemastautin_non_residents', 'other_liabilities', 'total_equities_and_liabilities'],

    # Interest Rates: Banking Institutions
    '2.1': ['interest_rates_banking_institutions', 'fixed_deposit_rates_period_in_months', 'kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'weighted_average_fixed_deposit_rates_period_in_months', 'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'savings_deposit_rate', 'weighted_average_savings_deposit_rate', 'base_rate2_br', 'weighted_average_br', 'base_lending_rate_blr', 'weighted_average_blr', 'kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans', 'weighted_alr_on_outstanding_loans', 'investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_1', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_2', 'percent_per_annum_kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans'],

    # Funds Raised in Capital Market (by Private Sector)
    '2.10': ['initial_public_offers', 'rights_issues', 'restricted_offer_for_sale', 'special_issues', 'preference_shares', 'warrants', 'new_issues_of_shares_war_rants', 'straight_bonds', 'bonds_with_war_rants', 'conver_tible_bonds', 'islamic_bonds', 'asset_backed_bonds', 'medium_term_notes', 'bon_cagamas_cagamas_bonds', 'new_issues_of_corporate_bond_and_or_sukuk', 'corporate_bond_and_or_sukuk', 'redemptions_bon_cagamas_cagamas_bonds', 'net_issues_of_corporate_bond_and_or_sukuk', 'net_funds_raised_by_the_private_sector'],

    # New Issues of Corporate Bond and/or Sukuk
    '2.11': ['agriculture_foresty_and_fishing', 'construction', 'electricity_gas_and_water', 'finance_insurance_real_estate_and_business_services', 'government_and_other_services', 'manufacturing', 'mining_and_quarrying', 'transport_storage_and_communications', 'wholesale_retail_trade_hotels_and_restaurants', 'terbitan_baru_bon_korporat_dan_atau_sukuk1_kecuali_bon_cagamas_mengikut_sektor_new_issues_of_corporate_bond_and_or_sukuk1_excluding_cagamas_bonds_by_sector_rm_million_jumlah_total'],

    # Turnover of Conventional and Islamic Money Market
    '2.14': ['antara_bank_interbank', 'korporat_corporate', 'banker_s_acceptance_antara_bank_interbank', 'banker_s_acceptance_korporat_corporate', 'negotiable_instrument_of_deposit_antara_bank_interbank', 'negotiable_instrument_of_deposit_korporat_corporate', 'mudharabah_deposits_antara_bank_interbank', 'mudharabah_deposits_korporat_corporate', 'commodity_murabahah_deposits_antara_bank_interbank', 'commodity_murabahah_deposits_korporat_corporate', 'wakalah_deposits_antara_bank_interbank', 'wakalah_deposits_korporat_corporate', 'other_deposit_antara_bank_interbank', 'other_deposit_korporat_corporate', 'islamic_bankers_acceptance_antara_bank_interbank', 'islamic_bankers_acceptance_korporat_corporate', 'islamic_negotiable_instrument_of_deposit_antara_bank_interbank', 'rm_million_equivalent_korporat_corporate'],

    # Turnover of Derivatives Transactions
    '2.15': ['warrants', 'opsyen_options', 'klibor_futures', 'swap', 'interest_rate_related_opsyen_options', 'futures', 'credit_default_swap', 'pusing_ganti_derivatif_turnover_of_derivatives_transactions_konvensional_conventional_lain_lain_others', 'profit_rate_swap'],

    # Turnover of Debt Securities and Sukuk
    '2.16': ['turnover_of_debt_securities_and_sukuk', 'bank_negara_monetary_note', 'malaysian_treasury_bills', 'malaysian_government_securities', 'bank_negara_monetary_note_islamic', 'malaysian_islamic_treasury_bills', 'government_investment_issues', 'government_housing_sukuk', 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_conventional_jumlah_total', 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_sukuk_jumlah_total', 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_rm_million_equivalent_jumlah_total'],

    # Turnover of Foreign Currency Market Transactions
    '2.17': ['fx_spot', 'fx_swap', 'fx_forward', 'fx_options'],

    # Credit to the Private Non-Financial Sector
    '2.18': ['outstanding_rm_million', 'of_which_household_a', 'of_which_business_b', 'credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c', 'total_credit_to_the_private_non_financial_sector_total_a_b_c', 'of_which_credit_to_businesses_b_c', 'annual_growth', 'outstanding_loans_to_the_private_non_financial_sector_of_which_household_a', 'outstanding_loans_to_the_private_non_financial_sector_of_which_business_b', 'kredit_kepada_sektor_swasta_bukan_kewangan_credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c', 'credit_to_the_private_non_financial_sector_total_credit_to_the_private_non_financial_sector_total_a_b_c', 'total_credit_to_the_private_non_financial_sector_of_which_credit_to_businesses_b_c'],

    # Net Financing through Banking, DFIs and Corporate Bonds (prev)
    '2.18a': ['outstanding_rm_million', 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds', 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing', 'monthly_change_rm_million', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing', 'pertumbuhan_tahunan_annual_growth', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds_1', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_1', 'net_financing_pertumbuhan_tahunan_annual_growth', 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_1', 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_2'],

    # Interest Rates: Banking Institutions (prev)
    '2.1a': ['interest_rates_banking_institutions_discontinued', 'tempoh_dalam_bulan_period_in_months', 'fixed_deposits_tempoh_dalam_bulan_period_in_months', 'deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'interest_rates_banking_institutions_discontinued_commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'savings_deposit', 'weighted_base_rate', 'base_lending_rate', 'kadar_berian_pinjaman_purata2_average_lending_rate', 'weighted_average_lending_rate', 'deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months', 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months_1', 'kadar_berian_pinjaman_purata_average_lending_rate'],

    # Islamic Banking: Financing and Profit Rates
    '2.2': ['islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders', 'fixed_deposit_rates_period_in_months', 'kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'weighted_average_fixed_deposit_rates_period_in_months', 'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months', 'investment_account_period_in_months', 'akaun_pelaburan_investment_account_period_in_months', 'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'savings_deposit_rate', 'weighted_average_savings_deposit_rate', 'base_rate', 'weighted_average_base_rate_br', 'base_financing_rate', 'weighted_average_base_financing_rate_bfr', 'average_financing_rate_on_outstanding_financing', 'weighted_average_financing_rate_afr_on_outstanding_financing', 'investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months', 'percent_per_annum'],

    # Islamic Banking: Financing and Profit Rates (prev)
    '2.2a': ['islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued', 'investment_deposit_tawarruq_fixed_deposits_period_in_months', 'deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'investment_account_period_in_months', 'akaun_pelaburan_investment_account_period_in_months', 'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months', 'savings_deposit', 'base_rate', 'base_financing_rate', 'average_financing_rate', 'investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months', 'percent_per_annum'],

    # Interest Rates: Interbank Money Market
    '2.3': ['tempoh_period_1', 'interest_rates_interbank_money_market', 'as_at_period_end', 'julat_range', 'overnight_money_julat_range', 'wang_semalaman_overnight_money_julat_range', 'purata_avg', '1_week_julat_range', '1_minggu_1_week_julat_range', 'weighted_average_interbank_rates_1_minggu_1_week_julat_range', '1_week_purata_avg', '1_month_julat_range', '1_bulan_1_month_julat_range', 'weighted_average_interbank_rates_1_bulan_1_month_julat_range', '1_month_purata_avg', '3_month_julat_range', '3_bulan_3_month_julat_range', 'weighted_average_interbank_rates_3_bulan_3_month_julat_range', '3_month_purata_avg', '6_month_julat_range', '6_bulan_6_month_julat_range', 'weighted_average_interbank_rates_6_bulan_6_month_julat_range', '6_month_purata_avg', '12_month_julat_range', '12_bulan_12_month_julat_range', 'weighted_average_interbank_rates_12_bulan_12_month_julat_range', 'percent_per_annum_purata_avg', '12_month_purata_avg'],

    # Interest Rates: Treasury Bills and Bank Negara Bills
    '2.4': ['interest_rates_treasury_bills_and_bank_negara_bills', 'average_discount_rate_on_treasury_bills_period_in_months', 'kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months', 'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months', 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months', 'average_discount_rate_on_bank_negara_bills_period_in_months', 'kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months', 'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months', 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months', 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months_1', 'percent_per_annum'],

    # Treasury Bills, MGS and Khazanah Bonds: Tender Results
    '2.4.1': [],

    # Market Indicative Yield: Malaysian Government Securities
    '2.5': ['market_indicative_yield1_malaysian_government_securities', 'market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_1', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_2', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_3', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_4', 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_5', 'percent_per_annum'],

    # Exchange Rates: Malaysian Ringgit
    '2.6': ['exchange_rates_malaysian_ringgit', 'end_of_period', 'rm_per_unit_of_usd', 'rm_per_unit_of_gbp', 'rm_per_unit_of_euro', 'rm_per_unit_of_100_sf', 'rm_per_unit_of_100_hkd', 'rm_per_unit_of_100_jpy', 'rm_per_unit_of_cny', 'rm_per_unit_of_sgd', 'rm_per_unit_of_100_idr', 'rm_per_unit_of_100_thb', 'average_for_period', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_usd', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_gbp', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_euro', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_sf', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_hkd', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_jpy', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_cny', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_sgd', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_idr', 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_thb'],

    # Exchange Rates: Malaysian Ringgit (Daily)
    '2.6.1': ['tempoh_period_1', 'june', 'sdr', 'end_of_period', 'gbp', 'eur', 'sf', '100_hkd', '100_jpy', 'cny', 'sgd', '100_idr', '100_thb'],

    # Volume of Transaction in Interbank Money Market
    '2.7': ['volume_of_transactions_in_interbank_money_market', 'overnight', 'weekend', '1_week', '1_month', '2_months', '3_months', '6_months', '1_year', 'jumlah_dana_diniagakan_dalam_pasaran_wang_antara_bank_volume_of_transactions_in_interbank_money_market_deposit_antara_bank_interbank_deposit_lain_lain_others', 'jumlah_kecil_sub_total', 'malaysian_government_securities', 'khazanah_bonds', 'cagamas_bonds', 'malaysian_treasury_bills', 'bank_negara_bills', 'cagamas_notes', 'negotiable_instrument_of_deposit', 'banker_s_acceptance', 'money_market_instrument_jumlah_kecil_sub_total', 'grand_total'],

    # Volume of Interbank Transactions in KL FX Market
    '2.8': ['usd_rm_spot', 'usd_rm_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_rm_jumlah_total', 'usd_sgd_spot', 'usd_sgd_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_sgd_jumlah_total', 'usd_jpy_spot', 'usd_jpy_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_jpy_jumlah_total', 'gbp_usd_spot', 'gbp_usd_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_gbp_usd_jumlah_total', 'eur_usd_spot', 'eur_usd_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_eur_usd_jumlah_total', 'usd_chf_spot', 'usd_chf_swap', 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_rm_juta_rm_million_jumlah_total'],

    # Funds Raised in Capital Market (by Public Sector)
    '2.9': ['funds_raised_in_the_capital_market_by_public_sector', 'malaysian_government_securities_mgs', 'mgs_advanced_subscriptions', 'khazanah_bonds_kb', 'malaysian_government_investment_issues_mgii', 'bon_simpanan_savings_bonds', 'sukuk_perumahan_kerajaan_government_housing_sukuk', 'new_issues_of_debt_securities', 'mgs', 'kb', 'mgii', 'redemptions_bon_simpanan_savings_bonds', 'redemptions_sukuk_perumahan_kerajaan_government_housing_sukuk', 'less_government_holdings', 'net_funds_raised_by_the_public_sector'],

    # Federal Government Finance
    '3.1': ['federal_government_finance', 'revenue', 'operating_expenditure', 'kurangan_deficit', 'gross_development_expenditure', 'less_loan_recoveries', 'net_development_expenditure', 'covid_19_fund', 'kurangan_keseluruhan_deficit', 'gross_domestic_borrowing', 'less_domestic_repayment', 'net_domestic_borrowing', 'gross_foreign_borrowing', 'less_foreign_repayment', 'net_foreign_borrowing', 'use_of_assets'],

    # Federal Government Revenue
    '3.1.1': ['hasil_kerajaan_persekutuan_federal_government_revenue_jumlah_total', 'jumlah_kecil_sub_total', 'companies_income_tax', 'petroleum_income_tax', 'individuals_income_tax', 'stamp_duties', 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_langsung_direct_taxes_lain_lain_others', 'indirect_taxes_jumlah_kecil_sub_total', 'export_duties', 'import_duties', 'excise_duties', 'goods_and_services_tax', 'sales_tax', 'service_tax', 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_tidak_langsung_indirect_taxes_lain_lain_others', 'non_tax_revenue_jumlah_kecil_sub_total', 'licences_and_permits', 'petroleum_royalty', 'interest_and_returns_on_investment', 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_bukan_cukai_tax_revenue_non_tax_revenue_indirect_taxes_lain_lain_others', 'non_revenue_receipts'],

    # Federal Government Operating Expenditure by Object
    '3.1.2': ['perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_jumlah_total', 'emoluments', 'retirement_charges', 'perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_bayaran_khidmat_hutang_debt_service_charges_jumlah_total', 'domestic', 'external', 'supplies_and_services', 'subsidies_and_social_assistance', 'asset_acquisition', 'grants_and_transfers', 'other_expenditure'],

    # Federal Government Development Expenditure
    '3.1.3': ['perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_jumlah_total', 'defence_and_security', 'jumlah_kecil_sub_total', 'agriculture_and_rural_development', 'trade_and_industry', 'transport', 'public_utilities', 'perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_perkhidmatan_ekonomi_economic_services_lain_lain_others', 'social_services_jumlah_kecil_sub_total', 'education', 'health', 'housing', 'social_and_community_services', 'general_administration'],

    # Federal Government Debt by Remaining Maturity
    '3.1.4': ['hutang_kerajaan_persekutuan_pengkelasan_mengikut_tempoh_baki_matang_federal_government_debt_classification_by_remaining_maturity_jumlah_total', 'jumlah_kecil_sub_total', 'treasury_bills', 'malaysian_government_investment_issues_jumlah_kecil_sub_total', 'kurang_dari_3_tahun_less_than_3_years', '5_tahun_5_years', '10_tahun_10_years', '15_tahun_15_years', 'malaysian_government_investment_issues_15_tahun_15_years', 'malaysian_government_securities_jumlah_kecil_sub_total', 'malaysian_government_securities_kurang_dari_3_tahun_less_than_3_years', 'malaysian_government_securities_5_tahun_5_years', 'malaysian_government_securities_10_tahun_10_years', 'malaysian_government_securities_15_tahun_15_years', 'sekuriti_kerajaan_malaysia_malaysian_government_securities_15_tahun_15_years', 'other_loans', 'external_debt4_jumlah_kecil_sub_total', 'non_resident_holdings_of_rm_denominated_debt', 'market_loans', 'project_loans'],

    # Federal Government Domestic Debt by Holder
    '3.1.5': ['hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_jumlah_total', 'jumlah_kecil_sub_total', 'bank_negara_malaysia_central_bank_of_malaysia', 'institusi_perbankan_banking_institutions', 'pemilik_pemilik_asing_foreign_holders', 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_bil_bil_perbendaharaan_treasury_bills_lain_lain_other', 'malaysia_government_investment_issues_jumlah_kecil_sub_total', 'kumpulan_wang_simpanan_pekerja_employees_provident_fund', 'kumpulan_wang_amanah_persaraan_kwap', 'syarikat_syarikat_insurans_insurance_companies', 'financial_sector_bank_negara_malaysia_central_bank_of_malaysia', 'financial_sector_institusi_perbankan_banking_institutions', 'institusi_kewangan_pembangunan_development_financial_institutions', 'lain_lain_institusi_bukan_kewangan_non_bank_financial_institutions', 'malaysia_government_investment_issues_pemilik_pemilik_asing_foreign_holders', 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_terbitan_pelaburan_kerajaan_malaysia_malaysia_government_investment_issues_lain_lain_other', 'malaysian_government_securities_jumlah_kecil_sub_total', 'social_security_institutions_kumpulan_wang_simpanan_pekerja_employees_provident_fund', 'social_security_institutions_kumpulan_wang_amanah_persaraan_kwap', 'malaysian_government_securities_syarikat_syarikat_insurans_insurance_companies', 'sektor_kewangan_financial_sector_bank_negara_malaysia_central_bank_of_malaysia', 'sektor_kewangan_financial_sector_institusi_perbankan_banking_institutions', 'financial_sector_institusi_kewangan_pembangunan_development_financial_institutions', 'lain_lain_institusi_kewangan_non_bank_financial_institutions', 'malaysian_government_securities_pemilik_pemilik_asing_foreign_holders', 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_sekuriti_kerajaan_malaysia_malaysian_government_securities_lain_lain_other', 'other_loans'],

    # Federal Government Debt by Currency and Remaining Maturity
    '3.1.6': ['federal_government_debt_classification_by_currency_and_remaining_maturity', 'total_rm_million_equivalent', 'rm', 'usd', 'yen', 'hutang_kerajaan_persekutuan_pengkelasan_mengikut_matawang_dan_tempoh_baki_matang_federal_government_debt_classification_by_currency_and_remaining_maturity_hutang_yang_belum_dijelaskan_kerajaan_persekutuan_mengikut_matawang_outstanding_federal_government_debt_by_currency_lain_lain_others', 'others_rm_million_equivalent'],

    # RENTAS: Foreign Holdings in Debt Securities and Sukuk
    '3.2': ['rentas_foreign_holdings_in_debt_securities_and_sukuk', 'bank_negara_monetary_note', 'malaysian_treasury_bills', 'malaysian_government_securities', 'bank_negara_monetary_note_islamic', 'malaysian_islamic_treasury_bills', 'bank_negara_malaysia_sukuk_ijarah', 'malaysian_government_investment_issues', 'government_housing_sukuk', 'corporate_bonds', 'sukuk', 'denominated_debt_securities', 'denominasi_sekuriti_hutang_denominated_debt_securities'],

    # Labour Market Indicators for the Financial Services Sector
    '3.5.12a': ['labour_market_indicators_for_the_financial_services_sector', 'total_number_of_employees', 'number_of_job_vacancies', 'new_job_created', 'new_hires_and_recalls', 'penunjuk_pasaran_pekerja_bagi_sektor_perkhidmatan_kewangan_labour_market_indicators_for_the_financial_services_sector_separations_total', 'quits_and_resignation_except_retirement', 'layoffs_and_discharges', 'other_separations'],

    # Selected Statistics on Cheques Cleared and Returned
    '3.5.14': ['no_million', 'rm_billion', 'no_000_no_000', 'rm_milion_rm_million', 'of_which_returned_cheques_due_to_insufficient_funds_no_000_no_000', 'of_which_returned_cheques_due_to_insufficient_funds_rm_milion_rm_million'],

    # Selected Statistics on Dishonoured Cheques (prev)
    '3.5.14a': ['no', 'annual_change', 'no_million', 'rm_bilion_rm_billion', 'cheques_cleared_rm_bilion_rm_billion'],

    # Banking System: Cross-Border Position vs Non-Resident
    '3.6.19': ['pinjaman_dan_deposit_loans_and_deposits', 'sekuriti_hutang_debt_securities', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_lain_lain_others', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_jumlah_total', 'liabilities_pinjaman_dan_deposit_loans_and_deposits', 'liabilities_sekuriti_hutang_debt_securities', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_lain_lain_others', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_jumlah_total', 'assets_pinjaman_dan_deposit_loans_and_deposits', 'assets_sekuriti_hutang_debt_securities', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_lain_lain_others', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_jumlah_total', 'liabiliti_liabilities_pinjaman_dan_deposit_loans_and_deposits', 'liabiliti_liabilities_sekuriti_hutang_debt_securities', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_liabiliti_liabilities_lain_lain_others', '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_rm_million_jumlah_total'],

    # Gross Imports by Economic Function
    '3.6.7': ['food', 'consumer_durables', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_lain_lain_others', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_jumlah_total', 'machinery', 'transport_equipment', 'metal_products', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_lain_lain_others', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_jumlah_total', 'for_manufacturing', 'for_construction', 'for_agriculture', 'crude_petroleum', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_lain_lain_others', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_jumlah_total', 'retained_imports', 'imports_for_re_exports', 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_rm_million_jumlah_total'],

    # External Debt
    '3.7': ['hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_jumlah_total', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_peminjaman_luar_pesisir2_offshore_borrowing_jumlah_total', 'federal_government', 'public_enterprise', 'sektor_perbankan_banking_sector', 'sektor_bukan_bank_non_bank_sector', 'short_term_sektor_perbankan_banking_sector', 'private_sector_sektor_bukan_bank_non_bank_sector', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_jumlah_total', 'sekuriti_kerajaan_government_securities', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_sederhana_dan_panjang_medium_and_long_term_lain_lain_others', 'short_term_sekuriti_kerajaan_government_securities', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_pendek_short_term_lain_lain_others', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_deposit_bukan_pemastautin_non_resident_deposits_jumlah_total', 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_lain_lain_others_jumlah_total', 'medium_and_long_term', 'term', 'debt_service_ratio7', 'medium_and_long_term_debt', 'term_debt'],

    # External Reserves
    '3.8': ['external_reserves', 'rizab_luar_negeri_external_reserves_central_bank_of_malaysia_gross_international_reserves_jumlah_total', 'special_drawing_rights', 'imf_reserves_position', 'gold_and_foreign_exchange', 'external_liabilities', 'net_international_reserves', 'other_official_reserves', 'net_official_reserves'],

    # Life/General Insurance and Takaful Funds: Statement of Assets
    '4.1': ['number_of_life_family_and_general_insurance_takaful_funds', 'total_assets', 'property_plant_and_equipment', 'investment_properties', 'loans_financing', 'malaysian_government_papers2_guaranteed_loans', 'corporate_debt_securities', 'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_lain_lain_others', 'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_jumlah_total', 'foreign_assets', 'cash_and_deposits', 'other_assets'],

    # Insurance Key Indicators
    '4.10': ['indicator', 'value'],

    # Life Insurance Business: Valuation Result and Surplus Distribution
    '4.10.1': ['indicator', 'value'],

    # Takaful Key Indicators
    '4.11': ['indicator', 'value'],

    # Insurance Broking Business: Operating Results
    '4.12': ['indicator', 'value'],

    # Insurance Broking Business: Total Premiums Transacted
    '4.12.1': ['marine_aviation_and_transit_direct_premiums_rm_million', 'general_marine_aviation_and_transit_direct_premiums_rm_million', 'fire', 'fire_direct_premiums_rm_million', 'motor', 'motor_direct_premiums_rm_million', 'miscellaneous', 'miscellaneous_direct_premiums_rm_million', 'life', 'life_miscellaneous_direct_premiums_rm_million', 'table_4_12_insurance_broking_total_premiums_transacted_total', 'total_miscellaneous_direct_premiums_rm_million'],

    # Loss Adjusting Business: Operating Results
    '4.13': ['indicator', 'value'],

    # Loss Adjusting Business: Cases Handled by Adjusters
    '4.13.1': ['motor_no', 'cases_handled_by_adjusters_motor_no', 'motor_change', 'cases_handled_by_adjusters_motor_change', 'motor_share', 'cases_handled_by_adjusters_motor_share', 'non_motor_no', 'cases_handled_by_adjusters_non_motor_no', 'non_motor_change', 'cases_handled_by_adjusters_non_motor_change', 'non_motor_share', 'cases_handled_by_adjusters_non_motor_share', 'total_no', 'cases_handled_by_adjusters_total_no', 'total_change', 'cases_handled_by_adjusters_total_change'],

    # Insurance: Assets and Liabilities
    '4.2': ['penanggung_insurans_hayat_langsung_life_direct_insurers', 'modal_berbayar_paid_up_capital', 'akaun_premium_saham_share_premium_account', 'rizab_reserves', 'keuntungan_kerugian_tertahan_retained_profit_loss', 'ekuiti_pemegang_syer_shareholders_equity_jumlah_total', 'rizab_penilaian_semula_aset_assets_revaluation_reserves', 'liabiliti_lain_other_liabilities', 'jumlah_liabiliti_total_liabilities', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'pinjaman_loans', 'malaysian_government_papers_guaranteed_loans', 'corporate_debt_securities', 'pelaburan_lain_other_investments', 'pelaburan_investments_jumlah_total', 'harta_benda_pelaburan_investment_properties', 'wang_tunai_dan_simpanan_cash_and_deposits', 'aset_lain1_other_assets', 'aset_asing_foreign_assets', 'jumlah_aset_total_assets'],

    # Takaful: Assets and Liabilities
    '4.3': ['pengendali_takaful_keluarga_langsung_family_direct_takaful_operators', 'modal_berbayar_paid_up_capital', 'akaun_premium_saham_share_premium_account', 'rizab_reserves', 'keuntungan_kerugian_tertahan_retained_profit_loss', 'ekuiti_pemegang_syer_shareholders_equity_jumlah_total', 'rizab_penilaian_semula_aset_assets_revaluation_reserves', 'liabiliti_lain_other_liabilities', 'jumlah_liabiliti_total_liabilities', 'wang_tunai_dan_simpanan_cash_and_deposits', 'government_islamic_papers_malaysian_government_guaranteed_financing', 'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities', 'pelaburan_lain_other_investments', 'pelaburan_investments_jumlah_total', 'pelaburan_harta_benda_investment_properties', 'pembiayaan_financing', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain_other_assets', 'aset_asing_foreign_assets', 'jumlah_aset_total_assets'],

    # Insurance: Capital Adequacy Ratio
    '4.4': ['penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available', 'penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required', 'penanggung_insurans_hayat_life_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio', 'penanggung_insurans_am_general_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available', 'penanggung_insurans_am_general_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required', 'penanggung_insurans_am_general_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio', 'jumlah_modal_sedia_ada4_total_capital_available', 'jumlah_modal_dikehendaki4_total_capital_required', 'penanggung_insurans_komposit2_composite2_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio', 'jumlah_modal_sedia_ada_total_capital_available', 'jumlah_modal_dikehendaki_total_capital_required', 'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio'],

    # Takaful: Capital Adequacy Ratio
    '4.5': ['pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_sedia_ada_total_capital_available', 'pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_dikehendaki_total_capital_required', 'pengendali_takaful_keluarga_family_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio', 'pengendali_takaful_am_general_takaful_operators_jumlah_modal_sedia_ada_total_capital_available', 'pengendali_takaful_am_general_takaful_operators_jumlah_modal_dikehendaki_total_capital_required', 'pengendali_takaful_am_general_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio', 'jumlah_modal_sedia_ada3_total_capital_available', 'jumlah_modal_dikehendaki3_total_capital_required', 'pengendali_takaful_komposit2_composite2_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio', 'keseluruhan_industri_consolidated_industry_jumlah_modal_sedia_ada_total_capital_available', 'keseluruhan_industri_consolidated_industry_jumlah_modal_dikehendaki_total_capital_required', 'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio'],

    # Life Insurance: New Business and Business in Force
    '4.6': ['perniagaan_dalam_malaysia_business_within_malaysia', 'nilai_diinsuranskan_sums_insured_rm_juta_rm_million', 'tahunan_annual', 'tunggal_single', 'jumlah_total', 'unit_unit', 'perniagaan_berkuat_kuasa_business_in_force_nilai_diinsuranskan_sums_insured_rm_juta_rm_million', 'premium_tahunan_annual_premium'],

    # Life Insurance: No. of New Business Policies
    '4.6.1': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'seumur_hidup_whole_life_jumlah_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total', 'anuiti_annuity_individu_individual', 'anuiti_annuity_lain_lain_others_kumpulan_group', 'anuiti_annuity_lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'jumlah_total_lain_lain_others_jumlah_total'],

    # Life Insurance: No. of Policies in Force
    '4.6.2': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'seumur_hidup_whole_life_jumlah_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total', 'anuiti_annuity_individu_individual', 'anuiti_annuity_lain_lain_others_kumpulan_group', 'anuiti_annuity_lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'unit_unit_jumlah_total'],

    # Life Insurance: No. of Policies Terminated
    '4.6.3': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'cukup_tempoh_maturity_individu_individual', 'cukup_tempoh_maturity_kumpulan_group', 'cukup_tempoh_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'unit_unit_jumlah_total'],

    # Life Insurance: Distribution of New Business Premiums
    '4.6.4': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_seumur_hidup_whole_life_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_endowmen_endowment_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_sementara_temporary_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_lain_lain_others_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_berkaitan_pelaburan_investment_linked_lain_lain_others_total', 'anuiti_annuity_individu_individual', 'anuiti_annuity_lain_lain_others_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_anuiti_annuity_lain_lain_others_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_rm_juta_rm_million_total'],

    # Life Insurance: Distribution of Annual Premiums in Force
    '4.6.5': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'seumur_hidup_whole_life_jumlah_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Life Insurance: Distribution of New Sums Insured
    '4.6.6': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'seumur_hidup_whole_life_jumlah_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total', 'anuiti_annuity_individu_individual', 'anuiti_annuity_lain_lain_others_kumpulan_group', 'anuiti_annuity_lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Life Insurance: Distribution of Sums Insured in Force
    '4.6.7': ['perniagaan_dalam_malaysia_business_within_malaysia', 'seumur_hidup_whole_life_kumpulan_group', 'seumur_hidup_whole_life_jumlah_total', 'endowmen_endowment_individu_individual', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group', 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total', 'anuiti_annuity_individu_individual', 'anuiti_annuity_lain_lain_others_kumpulan_group', 'anuiti_annuity_lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_lain_lain_others_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Life Insurance: Terminations of Annual Premiums
    '4.6.8': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'kematangan_maturity_individu_individual', 'kematangan_maturity_kumpulan_group', 'kematangan_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total', 'other_causes_including_expiry_individu_individual', 'other_causes_including_expiry_kumpulan_group', 'other_causes_including_expiry_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Life Insurance: Terminations of Sums Insured
    '4.6.9': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'cukup_tempoh_maturity_individu_individual', 'cukup_tempoh_maturity_kumpulan_group', 'cukup_tempoh_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group', 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Life Insurance: Income and Outgo
    '4.6.a': ['perniagaan_dalam_malaysia_business_within_malaysia', 'pendapatan_pelaburan_bersih_net_investment_income', 'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income', 'pendapatan_income_jumlah_total', 'faedah_polisi_bersih_net_policy_benefits', 'imbuhan_agensi_agency_remuneration', 'perbelanjaan_pengurusan_management_expenses', 'kerugian_dari_pelupusan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo', 'perbelanjaan_outgo_jumlah_total', 'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo'],

    # Life Insurance: Assets of Life Insurance Funds
    '4.6.b': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kertas_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_guaranteed_loans', 'sekuriti_hutang_korporat_corporate_debt_securities', 'pelaburan_investments_lain_lain_others', 'pelaburan_investments_jumlah_total', 'pelaburan_harta_benda_investment_properties', 'gadai_janji_mortgages', 'polisi_policy', 'pinjaman_loans_lain_lain_others', 'pinjaman_loans_jumlah_total', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain2_other_assets', 'aset_asing_foreign_assets', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Premium Income
    '4.7': ['perniagaan_dalam_malaysia_business_within_malaysia', 'premium_langsung_kasar_gross_direct_premiums', 'premium_bersih_net_premiums', 'nisbah_bendungan_retention_ratio'],

    # General Insurance: Distribution of Gross Direct Premiums
    '4.7.1': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'general1_insurance_distribution_of_gross_direct_premiums_jumlah_total'],

    # General Insurance: Claims Ratio
    '4.7.10': ['col', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'perniagaan_dalam_malaysia_business_within_malaysia_jumlah_total'],

    # General Insurance: Claims Ratio for Direct Insurers
    '4.7.10.a': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'insurans_am1_nisbah_tuntutan2_penanggung_insurans_am_langsung_jumlah_total'],

    # General Insurance: Reinsurance Accepted Premiums
    '4.7.11': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Net Premiums for Professional Reinsurers
    '4.7.12': ['marin_udara_dan_transit_marine_aviation_and_transit', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Claims Ratio for Professional Reinsurers
    '4.7.13': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'miscellaneous', 'general1_insurance_claims_ratio2_for_professional_general_reinsurers_jumlah_total'],

    # General Insurance: Earned Premium Income
    '4.7.14': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Gross Claims Paid for Direct Business
    '4.7.15': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Gross Claims Paid for Reinsurance Accepted
    '4.7.16': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Claim Recoveries from Licensed Insurers
    '4.7.17': ['marin_udara_dan_transit_marine_aviation_and_transit', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Claim Recoveries from Foreign Insurers
    '4.7.18': ['marin_udara_dan_transit_marine_aviation_and_transit', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Net Claims Paid
    '4.7.19': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Distribution of Net Premiums
    '4.7.2': ['marin_udara_dan_transit_marine_aviation_and_transit', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Net Claims Incurred
    '4.7.20': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Combined Net Retention Ratio
    '4.7.3': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'general1_insurance_combined_direct_insurers_and_professional_reinsurers_net_retention_ratio_jumlah_total'],

    # General Insurance: Net Retention Ratio for Direct Insurers
    '4.7.4': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'general1_insurance_net_retention_ratio_for_direct_insurers_jumlah_total'],

    # General Insurance: Net Retention Ratio for Reinsurers
    '4.7.5': ['perniagaan_dalam_malaysia_business_within_malaysia', 'contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'miscellaneous', 'general1_insurance_net_retention_ratio_for_professional_reinsurers_jumlah_total'],

    # General Insurance: Reinsurance Position for Premiums Ceded
    '4.7.6': ['perniagaan_dalam_malaysia_business_within_malaysia', 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'miscellaneous', 'general1_insurance_reinsurance_position_for_premiums_ceded_and_retroceded_overseas_jumlah_total'],

    # General Insurance: Reinsurance Claims Recoveries
    '4.7.7': ['marin_dan_penerbangan_udara_marine_and_aviation_hull', 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Reinsurance Profit Commissions
    '4.7.8': ['marin_dan_penerbangan_udara_marine_and_aviation_hull', 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Net Reinsurance Position
    '4.7.9': ['aliran_masuk_bersih_atau_aliran_keluar_bersih_net_inflow_or_outflow', 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_million_jumlah_total'],

    # General Insurance: Underwriting and Operating Results
    '4.7.a': ['perniagaan_dalam_malaysia_business_within_malaysia', 'tuntutan_bersih_kena_dibayar_net_claims_incurred', 'commissions', 'management_expenses', 'underwriting_profit', 'investment_income', 'capital_gains', 'pendapatan_lain_other_income', 'capital_losses', 'other_outgo', 'operating_profit'],

    # General Insurance: Assets of General Insurance Funds
    '4.7.b': ['perniagaan_dalam_malaysia_business_within_malaysia', 'amaun_tertunggak_daripada_pelanggan_pengantara_penanggung_insurans_semula_amount_due_from_clients_intermediaries_reinsurers', 'kertas_dan_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_and_guaranteed_loans', 'sekuriti_dan_hutang_korporat_corporate_debt_and_securities', 'lain_lain_others', 'pelaburan_investments_jumlah_total', 'pelaburan_harta_benda_investment_properties', 'pinjaman_loans', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain2_other_assets', 'aset_asing_foreign_assets', 'rm_juta_rm_million_jumlah_total'],

    # General Insurance: Technical Reserves
    '4.7.c': ['perniagaan_dalam_malaysia_business_within_malaysia', 'liabiliti_premium_premium_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium', 'liabiliti_tuntutan_claims_liabilities_rm_juta_rm_million', 'liabiliti_tuntutan_claims_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium', 'rizab_teknikal_technical_reserves_rm_juta_rm_million', 'rizab_teknikal_technical_reserves_peratusan_daripada_premium_bersih_percentage_of_net_premium'],

    # Family Takaful: New Business and Business in Force
    '4.8': ['bilangan_sijil_no_of_certificates_unit_unit', 'jumlah_penyertaan_sum_participated_rm_juta_rm_million', 'tunggal_single', 'tahunan_annual', 'jumlah_total', 'perniagaan_berkuat_kuasa_business_in_force_bilangan_sijil_no_of_certificates_unit_unit', 'perniagaan_berkuat_kuasa_business_in_force_jumlah_penyertaan_sum_participated_rm_juta_rm_million', 'caruman_contributions'],

    # Family Takaful: No. of New Business Certificates
    '4.8.1': ['perniagaan_dalam_malaysia_business_within_malaysia', 'keluarga_biasa_ordinary_family_group', 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_keluarga_biasa_ordinary_family_total', 'berkaitan_pelaburan_investment_linked_individual', 'berkaitan_pelaburan_investment_linked_group', 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_berkaitan_pelaburan_investment_linked_total', 'anuiti_annuity_individual', 'anuiti_annuity_group', 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_anuiti_annuity_total', 'jumlah_total_individual', 'jumlah_total_group', 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_jumlah_total_total'],

    # Family Takaful: Annual Contributions of Terminated Certificates
    '4.8.10': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'kematangan_maturity_individu_individual', 'kematangan_maturity_kumpulan_group', 'kematangan_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'other_causes_including_expiry_individu_individual', 'other_causes_including_expiry_kumpulan_group', 'other_causes_including_expiry_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: Distribution of Sum Participated of New Business
    '4.8.2': ['perniagaan_dalam_malaysia_business_within_malaysia', 'keluarga_biasa_ordinary_family_group', 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_keluarga_biasa_ordinary_family_total', 'berkaitan_pelaburan_investment_linked_individual', 'berkaitan_pelaburan_investment_linked_group', 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_berkaitan_pelaburan_investment_linked_total', 'anuiti_annuity_individual', 'anuiti_annuity_group', 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_anuiti_annuity_total', 'jumlah_total_individual', 'jumlah_total_group', 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_rm_juta_rm_million_total'],

    # Family Takaful: Distribution of New Business Contributions
    '4.8.3': ['perniagaan_dalam_malaysia_business_within_malaysia', 'keluarga_biasa_ordinary_family_group', 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_keluarga_biasa_ordinary_family_total', 'berkaitan_pelaburan_investment_linked_individual', 'berkaitan_pelaburan_investment_linked_group', 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_berkaitan_pelaburan_investment_linked_total', 'anuiti_annuity_individual', 'anuiti_annuity_group', 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_anuiti_annuity_total', 'jumlah_total_individual', 'jumlah_total_group', 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_rm_juta_rm_million_total'],

    # Family Takaful: Distribution of New Business Contributions by Plan
    '4.8.4': ['pendidikan_education', 'endowmen_endowment_lain_lain_others', 'endowmen_endowment_jumlah_total', 'gadai_janji_mortgage', 'sementara_temporary_lain_lain_others', 'sementara_temporary_jumlah_total', 'perubatan_dan_kesihatan_medical_and_health', 'keluarga_biasa_ordinary_family_lain_lain_others', 'keluarga_biasa_ordinary_family_jumlah_total', 'berkaitan_pelaburan_investment_linked', 'anuiti_annuity', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: No. of Certificates In Force
    '4.8.5': ['perniagaan_dalam_malaysia_business_within_malaysia', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'keluarga_biasa_ordinary_family_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group', 'berkaitan_pelaburan_investment_linked_jumlah_total', 'annuiti_annuity_individu_individual', 'annuiti_annuity_jumlah_total_kumpulan_group', 'annuiti_annuity_jumlah_total', 'bilangan_sijil_no_of_certificates_jumlah_total_individu_individual', 'bilangan_sijil_no_of_certificates_jumlah_total_kumpulan_group', 'unit_unit_jumlah_total'],

    # Family Takaful: Distribution of Sum Participated In Force
    '4.8.6': ['perniagaan_dalam_malaysia_business_within_malaysia', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'keluarga_biasa_ordinary_family_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group', 'berkaitan_pelaburan_investment_linked_jumlah_total', 'annuiti_annuity_individu_individual', 'annuiti_annuity_jumlah_total_kumpulan_group', 'annuiti_annuity_jumlah_total', 'jumlah_penyertaan_sum_participated_jumlah_total_individu_individual', 'jumlah_penyertaan_sum_participated_jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: Distribution of Annual Contributions In Force
    '4.8.7': ['perniagaan_dalam_malaysia_business_within_malaysia', 'endowmen_endowment_kumpulan_group', 'endowmen_endowment_jumlah_total', 'sementara_temporary_individu_individual', 'sementara_temporary_kumpulan_group', 'sementara_temporary_jumlah_total', 'lain_lain_others_individu_individual', 'lain_lain_others_kumpulan_group', 'lain_lain_others_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'keluarga_biasa_ordinary_family_jumlah_total', 'berkaitan_pelaburan_investment_linked_individu_individual', 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group', 'berkaitan_pelaburan_investment_linked_jumlah_total', 'annuiti_annuity_individu_individual', 'annuiti_annuity_jumlah_total_kumpulan_group', 'annuiti_annuity_jumlah_total', 'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_individu_individual', 'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: No. of Certificates Terminated
    '4.8.8': ['perniagaan_dalam_malaysia_business_within_malaysia', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'kematangan_maturity_individu_individual', 'kematangan_maturity_kumpulan_group', 'kematangan_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'unit_unit_jumlah_total'],

    # Family Takaful: Sum Participated of Terminated Certificates
    '4.8.9': ['kematian_death_individu_individual', 'kematian_death_kumpulan_group', 'kematian_death_jumlah_total', 'kematangan_maturity_individu_individual', 'kematangan_maturity_kumpulan_group', 'kematangan_maturity_jumlah_total', 'serahan_surrender_individu_individual', 'serahan_surrender_kumpulan_group', 'serahan_surrender_jumlah_total', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group', 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total', 'jumlah_total_individu_individual', 'jumlah_total_kumpulan_group', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: Income and Outgo
    '4.8.a': ['perniagaan_dalam_malaysia_business_within_malaysia', 'pendapatan_pelaburan_bersih_net_investment_income', 'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income', 'pendapatan_income_jumlah_total', 'manfaat_sijil_bersih_net_certificate_benefits', 'komisen_bersih_net_commissions', 'perbelanjaan_pengurusan2_management_expenses', 'kerugian_atas_jualan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo', 'perbelanjaan_outgo_jumlah_total', 'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo'],

    # Family Takaful: Assets of Family Takaful Funds
    '4.8.b': ['perniagaan_dalam_malaysia_business_within_malaysia', 'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market', 'sekuriti_islam_kerajaan_government_islamic_papers', 'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities', 'pelaburan_lain_other_investments', 'pelaburan_investments_jumlah_total', 'pelaburan_harta_benda_investment_properties', 'pembiayaan_financing', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain_other_assets', 'aset_asing_foreign_assets', 'rm_juta_rm_million_jumlah_total'],

    # Family Takaful: Valuation Result
    '4.8.c': ['indicator', 'value'],

    # General Takaful: Distribution of Gross Contributions
    '4.9': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Distribution of Net Contributions
    '4.9.1': ['marin_udara_dan_transit_marine_aviation_and_transit', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering', 'kebakaran_fire', 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Domestic Retention
    '4.9.2': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'general_takaful1_domestic_retention_ratio_of_direct_takaful_operators_business_jumlah_total'],

    # General Takaful: Gross Claims Paid
    '4.9.3': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Net Claims Paid
    '4.9.4': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Claims Ratio
    '4.9.5': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'general_takaful1_claims_ratio_of_direct_takaful_operators_jumlah_total'],

    # General Takaful: Earned Contribution Income
    '4.9.6': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Net Claims Incurred
    '4.9.7': ['perniagaan_dalam_malaysia_business_within_malaysia', 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering', 'kebakaran_fire', 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident', 'perlindungan_akta_act_cover', 'lain_lain_others', 'motor_motor_jumlah_total', 'liabiliti_liability', 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability', 'pelbagai_miscellaneous', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Underwriting and Operating Results
    '4.9.a': ['perniagaan_dalam_malaysia_business_within_malaysia', 'tuntutan_bersih_kena_dibayar_net_claims_incurred', 'komisen_bersih_net_commissions', 'perbelanjaan_pengurusan2_management_expenses', 'keuntungan_pengunderaitan_underwriting_profit', 'keuntungan_pelaburan_investment_income', 'keuntungan_modal_capital_gains', 'pendapatan_lain_other_income', 'kerugian_modal_capital_losses', 'perbelanjaan_lain_other_outgo', 'keuntungan_kendalian_operating_profit'],

    # General Takaful: Assets of General Takaful Funds
    '4.9.b': ['perniagaan_dalam_malaysia_business_within_malaysia', 'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market', 'sekuriti_islam_kerajaan_government_islamic_papers', 'sekuriti_hutang_swasta_dan_ekuiti_islam_islamic_private_debt_securities_and_equities', 'pelaburan_lain_other_investments', 'pelaburan_investments_jumlah_total', 'pelaburan_harta_benda_investment_properties', 'pembiayaan_financing', 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment', 'aset_lain_other_assets', 'aset_asing_foreign_assets', 'rm_juta_rm_million_jumlah_total'],

    # General Takaful: Technical Reserves
    '4.9.c': ['perniagaan_dalam_malaysia_business_within_malaysia', 'rizab_caruman_tidak_diperoleh_unearned_contributions_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions', 'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_rm_juta_rm_million', 'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_peratusan_daripada_caruman_bersih_percentage_of_net_contributions', 'rizab_teknikal_technical_reserves_rm_juta_rm_million', 'rizab_teknikal_technical_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions'],

    # General Takaful: Contributions Income
    '4.9.d': ['perniagaan_dalam_malaysia_business_within_malaysia', 'caruman_langsung_kasar_gross_direct_contributions', 'caruman_bersih_net_contributions', 'nisbah_bendungan_retention_ratio'],

    # List of Banking Institutions
    '5.1': [],

    # Leasing and Factoring Companies: Statement of Assets and Liabilities
    '5.2': ['cash_and_bank_balances', 'investments', 'leasing_factoring', 'syarikat_pemajakan1_dan_pemfaktoran2_penyata_aset_dan_tanggungan_leasing1_and_factoring2_companies_statement_of_assets_and_liabilities_harta_assets_akan_diterima_receivables_lain_lain_others', 'syarikat_pemajakan_leasing_companies', 'total_assets_liabilities', 'capital_reserves_and_retained_earnings', 'borrowings_from_financial_institutions', 'inter_company_borrowings', 'other_liabilities'],

}

RENAME: dict[str, dict[str, str]] = {
    # Reserve Money
    '1.1': {
        'reserve_money': 'reserve_money',  # TODO: rename
        'total_reserve_money': 'total_reserve_money',  # TODO: rename
        'currency_in_circulation': 'currency_in_circulation',  # TODO: rename
        'required_reserves': 'required_reserves',  # TODO: rename
        'excess_reserves': 'excess_reserves',  # TODO: rename
        'deposits_of_the_private_sector': 'deposits_of_the_private_sector',  # TODO: rename
        'wang_rizab_reserve_money_faktor_faktor_yang_mempengaruhi_wang_rizab_factors_affecting_reserve_money_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total': 'wang_rizab_reserve_money_faktor_faktor_yang_mempengaruhi_wang_rizab_factors_affecting_reserve_money_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total',  # TODO: rename
        'claims_on_government': 'claims_on_government',  # TODO: rename
        'less_deposits_of_government': 'less_deposits_of_government',  # TODO: rename
        'claims_on_the_private_sector': 'claims_on_the_private_sector',  # TODO: rename
        'external_operations': 'external_operations',  # TODO: rename
        'other_influences': 'other_influences',  # TODO: rename
    },

    # Banking System: Loan/Financing Applied by Purpose
    '1.10': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_applied_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_total': 'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_applied_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing_applied': 'total_loan_financing_applied',  # TODO: rename
    },

    # Banking System: Loans Applied by Purpose (prev)
    '1.10a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans_applied': 'total_loans_applied',  # TODO: rename
    },

    # Banking System: Loan/Financing Applied by Sector
    '1.11': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'banking_system_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_loan_financing_applied_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total': 'banking_system_loan_financing_applied_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loan_financing_applied': 'total_loan_financing_applied',  # TODO: rename
    },

    # Banking System: Loan/Financing Applied by Type
    '1.11.1': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_total': 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_loan_financing_applied_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_loan_financing_applied': 'total_loan_financing_applied',  # TODO: rename
    },

    # Banking System: Loans Applied by Sector (prev)
    '1.11a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_hotels': 'restaurants_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'sistem_perbankan_pinjaman_yang_dipohon_mengikut_sektor_banking_system_loans_applied_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'renting_business_activities': 'renting_business_activities',  # TODO: rename
        'research_development': 'research_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'total_loans_applied': 'total_loans_applied',  # TODO: rename
    },

    # Banking System: Loan/Financing Approved
    '1.12': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_approved_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_total': 'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_approved_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing_approved': 'total_loan_financing_approved',  # TODO: rename
    },

    # Banking System: Loans Approved by Purpose (prev)
    '1.12a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans_approved': 'total_loans_approved',  # TODO: rename
    },

    # Banking System: Loan/Financing Approved by Sector
    '1.13': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'banking_system_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_loan_financing_approved_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total': 'banking_system_loan_financing_approved_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loan_financing_approved': 'total_loan_financing_approved',  # TODO: rename
    },

    # Banking System: Loans Approved by Sector (prev2)
    '1.13.1': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_lain_lain_others': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_format_terdahulu_banking_system_loans_approved_by_sector_previous_format_kredit_penggunaan_lain_lain_others',  # TODO: rename
        'total_loans_approved': 'total_loans_approved',  # TODO: rename
    },

    # Banking System: Loan/Financing Approved by Type
    '1.13.2': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_total': 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_loan_financing_approved_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_loan_financing_approved': 'total_loan_financing_approved',  # TODO: rename
    },

    # Banking System: Loans Approved by Sector (prev)
    '1.13a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_hotels': 'restaurants_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'sistem_perbankan_pinjaman_yang_diluluskan_mengikut_sektor_banking_system_loans_approved_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'renting_business_activities': 'renting_business_activities',  # TODO: rename
        'research_development': 'research_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'total_loans_approved': 'total_loans_approved',  # TODO: rename
    },

    # Banking System: Loan/Financing Disbursed by Purpose
    '1.14': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_total': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_disbursed_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing_disbursed': 'total_loan_financing_disbursed',  # TODO: rename
    },

    # Banking System: Loans Disbursed by Purpose (prev)
    '1.14a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans_disbursed': 'total_loans_disbursed',  # TODO: rename
    },

    # Banking System: Loan/Financing Disbursed by Sector
    '1.15': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'banking_system_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total': 'banking_system_loan_financing_disbursed_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loan_financing_disbursed': 'total_loan_financing_disbursed',  # TODO: rename
    },

    # Banking System: Loans Disbursed by Sectors (prev2)
    '1.15.1': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_lain_lain_others': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_format_terdahulu_banking_system_loans_disbursed_by_sector_previous_format_kredit_penggunaan_lain_lain_others',  # TODO: rename
        'total_loans_approved': 'total_loans_approved',  # TODO: rename
    },

    # Banking System: Loan/Financing Disbursed by Type
    '1.15.2': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_total': 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'foreign_currency_loans_financing': 'foreign_currency_loans_financing',  # TODO: rename
        'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_loan_financing_disbursed_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_loan_financing_disbursed': 'total_loan_financing_disbursed',  # TODO: rename
    },

    # Banking System: Loans Disbursed by Sector (prev)
    '1.15a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_hotels': 'restaurants_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'sistem_perbankan_pinjaman_yang_dikeluarkan_mengikut_sektor_banking_system_loans_disbursed_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'renting_business_activities': 'renting_business_activities',  # TODO: rename
        'research_development': 'research_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'total_loans_disbursed': 'total_loans_disbursed',  # TODO: rename
    },

    # Banking System: Loan/Financing Repaid by Purpose
    '1.16': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_repaid_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_total': 'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_repaid_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing_repaid': 'total_loan_financing_repaid',  # TODO: rename
    },

    # Banking System: Loans Repaid by Purpose (prev)
    '1.16a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans_repaid': 'total_loans_repaid',  # TODO: rename
    },

    # Banking System: Loan/Financing Repaid by Sector
    '1.17': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'banking_system_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_loan_financing_repaid_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total': 'banking_system_loan_financing_repaid_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loan_financing_repaid': 'total_loan_financing_repaid',  # TODO: rename
    },

    # Banking System: Loans Repaid by Sectors (prev2)
    '1.17.1': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_perdagangan_borong_dan_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_sektor_harta_benda_yang_luas_jumlah_broad_property_sector_total',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_jumlah_consumption_credit_total',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_lain_lain_others': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_format_terdahulu_banking_system_loans_repaid_by_sector_previous_format_kredit_penggunaan_lain_lain_others',  # TODO: rename
        'total_loans_approved': 'total_loans_approved',  # TODO: rename
    },

    # Banking System: Loan/Financing Repaid by Type
    '1.17.2': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_total': 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'foreign_currency_loans_financing': 'foreign_currency_loans_financing',  # TODO: rename
        'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_loan_financing_repaid_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_loan_financing_repaid': 'total_loan_financing_repaid',  # TODO: rename
    },

    # Banking System: Loans Repaid by Sector (prev)
    '1.17a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_hotels': 'restaurants_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'sistem_perbankan_pinjaman_yang_dibayar_mengikut_sektor_banking_system_loans_repaid_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'renting_business_activities': 'renting_business_activities',  # TODO: rename
        'research_development': 'research_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'total_loans_repaid': 'total_loans_repaid',  # TODO: rename
    },

    # Banking System: Loan/Financing by Type
    '1.18': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_loan_financing_by_type_rm_million_term_loans_financing_total': 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'up_to_one_year': 'up_to_one_year',  # TODO: rename
        'more_than_one_year': 'more_than_one_year',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'foreign_currency_loans_financing': 'foreign_currency_loans_financing',  # TODO: rename
        'banking_system_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Type
    '1.18.1': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'islamic_banking_system_financing_by_type_rm_million_term_financing_total': 'islamic_banking_system_financing_by_type_rm_million_term_financing_total',  # TODO: rename
        'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_total': 'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_others': 'islamic_banking_system_financing_by_type_rm_million_term_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_financing': 'bridging_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_financing': 'personal_financing',  # TODO: rename
        'housing_financing': 'housing_financing',  # TODO: rename
        'other_term_financing': 'other_term_financing',  # TODO: rename
        'up_to_one_year': 'up_to_one_year',  # TODO: rename
        'more_than_one_year': 'more_than_one_year',  # TODO: rename
        'bill_financing': 'bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'foreign_currency_financing': 'foreign_currency_financing',  # TODO: rename
        'islamic_banking_system_financing_by_type_rm_million_term_financing_lain_lain_others': 'islamic_banking_system_financing_by_type_rm_million_term_financing_lain_lain_others',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Type (prev)
    '1.18.1a': {
        'ibs_of_investment_merchant_banks': 'ibs_of_investment_merchant_banks',  # TODO: rename
        'overdraft': 'overdraft',  # TODO: rename
        'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_sewa_beli_hire_purchase_jumlah_total': 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_sewa_beli_hire_purchase_jumlah_total',  # TODO: rename
        'of_which_passenger_cars': 'of_which_passenger_cars',  # TODO: rename
        'leasing': 'leasing',  # TODO: rename
        'block_discounting': 'block_discounting',  # TODO: rename
        'bridging_financing': 'bridging_financing',  # TODO: rename
        'syndicated_financing': 'syndicated_financing',  # TODO: rename
        'factoring': 'factoring',  # TODO: rename
        'personal_financing': 'personal_financing',  # TODO: rename
        'housing_financing': 'housing_financing',  # TODO: rename
        'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_lain_lain_others': 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_pembiayaan_berjangka_term_financing_lain_lain_others',  # TODO: rename
        'up_to_one_year': 'up_to_one_year',  # TODO: rename
        'more_than_one_year': 'more_than_one_year',  # TODO: rename
        'bill_financing': 'bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'foreign_currency_financing': 'foreign_currency_financing',  # TODO: rename
        'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_lain_lain_others': 'sistem_perbankan_islam_pembiayaan_mengikut_jenis_islamic_banking_system_financing_by_type_lain_lain_others',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Shariah Contract
    '1.18.2': {
        'industry': 'industry',  # TODO: rename
        'bai_inah': 'bai_inah',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_total',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_total',  # TODO: rename
        'ijarah_thumma_al_bai': 'ijarah_thumma_al_bai',  # TODO: rename
        'ijarah_mawsufah_fi_zimmah': 'ijarah_mawsufah_fi_zimmah',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_ijarah_muntahiyah_bit_tamlik_others',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_lain_lain_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_ijarah_financing_lain_lain_others',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_total',  # TODO: rename
        'parallel_istisna': 'parallel_istisna',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_lain_lain_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_istisna_lain_lain_others',  # TODO: rename
        'mudarabah_venture': 'mudarabah_venture',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_total',  # TODO: rename
        'murabahah_to_the_purchase_orderer': 'murabahah_to_the_purchase_orderer',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_lain_lain_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_murabahah_lain_lain_others',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_total',  # TODO: rename
        'musyarakah_mutanaqisah': 'musyarakah_mutanaqisah',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_lain_lain_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_musyarakah_financing_lain_lain_others',  # TODO: rename
        'musyarakah_venture': 'musyarakah_venture',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_total': 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_total',  # TODO: rename
        'qard_standalone': 'qard_standalone',  # TODO: rename
        'qard_with_rahn': 'qard_with_rahn',  # TODO: rename
        'qard_with_ujrah': 'qard_with_ujrah',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others': 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others',  # TODO: rename
        'tawarruq': 'tawarruq',  # TODO: rename
        'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others_1': 'islamic_banking_system_financing_by_shariah_contract_rm_million_qard_lain_lain_others_1',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Concept (prev)
    '1.18.2a': {
        'ibs_of_investment_merchant_banks': 'ibs_of_investment_merchant_banks',  # TODO: rename
        'bai_bithaman_ajil': 'bai_bithaman_ajil',  # TODO: rename
        'ijarah': 'ijarah',  # TODO: rename
        'ijarah_thumma_al_bai': 'ijarah_thumma_al_bai',  # TODO: rename
        'murabahah': 'murabahah',  # TODO: rename
        'musyarakah': 'musyarakah',  # TODO: rename
        'mudharabah': 'mudharabah',  # TODO: rename
        'istisna': 'istisna',  # TODO: rename
        'sistem_perbankan_islam_pembiayaan_mengikut_konsep_islamic_banking_system_financing_by_concept_lain_lain_others': 'sistem_perbankan_islam_pembiayaan_mengikut_konsep_islamic_banking_system_financing_by_concept_lain_lain_others',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Banking System: Loan/Financing by Location
    '1.18.3': {
        'location': 'location',  # TODO: rename
        'banking_system_loan_financing_by_location_rm_million_inside_malaysia_jumlah_total': 'banking_system_loan_financing_by_location_rm_million_inside_malaysia_jumlah_total',  # TODO: rename
        'johor': 'johor',  # TODO: rename
        'kedah': 'kedah',  # TODO: rename
        'kelantan': 'kelantan',  # TODO: rename
        'melaka': 'melaka',  # TODO: rename
        'negeri_sembilan': 'negeri_sembilan',  # TODO: rename
        'pahang': 'pahang',  # TODO: rename
        'pulau_pinang': 'pulau_pinang',  # TODO: rename
        'perak': 'perak',  # TODO: rename
        'perlis': 'perlis',  # TODO: rename
        'sabah': 'sabah',  # TODO: rename
        'sarawak': 'sarawak',  # TODO: rename
        'selangor': 'selangor',  # TODO: rename
        'terengganu': 'terengganu',  # TODO: rename
        'wilayah_persekutuan_kuala_lumpur': 'wilayah_persekutuan_kuala_lumpur',  # TODO: rename
        'wilayah_persekutuan_labuan': 'wilayah_persekutuan_labuan',  # TODO: rename
        'wilayah_persekutuan_putrajaya': 'wilayah_persekutuan_putrajaya',  # TODO: rename
        'outside_malaysia': 'outside_malaysia',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Banking System: Classification of Loans by Type (prev)
    '1.18a': {
        'merchant_banks': 'merchant_banks',  # TODO: rename
        'overdraft': 'overdraft',  # TODO: rename
        'total': 'total',  # TODO: rename
        'of_which_passenger_cars': 'of_which_passenger_cars',  # TODO: rename
        'leasing': 'leasing',  # TODO: rename
        'block_discounting': 'block_discounting',  # TODO: rename
        'bridging_loans': 'bridging_loans',  # TODO: rename
        'syndicated_loans': 'syndicated_loans',  # TODO: rename
        'factoring': 'factoring',  # TODO: rename
        'personal_loans': 'personal_loans',  # TODO: rename
        'housing_loans': 'housing_loans',  # TODO: rename
        'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_pinjaman_berjangka_term_loans_lain_lain_others': 'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_pinjaman_berjangka_term_loans_lain_lain_others',  # TODO: rename
        'up_to_one_year': 'up_to_one_year',  # TODO: rename
        'more_than_one_year': 'more_than_one_year',  # TODO: rename
        'trade_bills': 'trade_bills',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'spi_loans': 'spi_loans',  # TODO: rename
        'foreign_currency_loans': 'foreign_currency_loans',  # TODO: rename
        'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_lain_lain_others': 'sistem_perbankan_pinjaman_mengikut_jenis_banking_system_classification_of_loans_by_type_lain_lain_others',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Loan/Financing by Purpose
    '1.19': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total',  # TODO: rename
        'cost_300k': 'cost_300k',  # TODO: rename
        'cost_300k_to_500k': 'cost_300k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'of_which_housing_loan_financing_sold_to_cagamas': 'of_which_housing_loan_financing_sold_to_cagamas',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'purchase_of_industrial_building_factories': 'purchase_of_industrial_building_factories',  # TODO: rename
        'purchase_of_land_only': 'purchase_of_land_only',  # TODO: rename
        'purchase_of_commercial_complexes': 'purchase_of_commercial_complexes',  # TODO: rename
        'purchase_of_shophouses_shoplots': 'purchase_of_shophouses_shoplots',  # TODO: rename
        'purchase_of_other_non_residential_property': 'purchase_of_other_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total': 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Purpose and Sectors
    '1.19.1': {
        'industry': 'industry',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_total': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_total': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_lain_lain_others': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_purpose_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'pembinaan_construction': 'pembinaan_construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'jumlah_pembiayaan_total_financing': 'jumlah_pembiayaan_total_financing',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'personal_uses_pembinaan_construction': 'personal_uses_pembinaan_construction',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_finance_insurance_real_estate_and_business_activities_total': 'islamic_banking_system_financing_by_purpose_and_sector_rm_million_sector_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'finance_insurance_real_estate_and_business_activities_jumlah_pembiayaan_total_financing': 'finance_insurance_real_estate_and_business_activities_jumlah_pembiayaan_total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by Purpose and Sectors (prev)
    '1.19.1a': {
        'ibs_of_investment_merchant_banks': 'ibs_of_investment_merchant_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'sistem_perbankan_islam_pembiayaan_mengikut_tujuan_dan_sektor_islamic_banking_system_financing_by_purpose_and_sectors_purpose_pembelian_kenderaan_pengangkutan_purchase_of_transport_vehicles_jumlah_total': 'sistem_perbankan_islam_pembiayaan_mengikut_tujuan_dan_sektor_islamic_banking_system_financing_by_purpose_and_sectors_purpose_pembelian_kenderaan_pengangkutan_purchase_of_transport_vehicles_jumlah_total',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_use': 'personal_use',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'purchase_of_consumer_durables': 'purchase_of_consumer_durables',  # TODO: rename
        'pembinaan_construction': 'pembinaan_construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'sector_pembinaan_construction': 'sector_pembinaan_construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_activities': 'finance_insurance_and_business_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
    },

    # Islamic Banking: Loans by Purpose and Sector (prev)
    '1.19.2': {
        'akhir_tempoh_end_of_period_1': 'akhir_tempoh_end_of_period_1',  # TODO: rename
        'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_purpose_and_sector': 'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_purpose_and_sector',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_use': 'personal_use',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'purchase_of_consumer_durables': 'purchase_of_consumer_durables',  # TODO: rename
        'pembinaan_construction': 'pembinaan_construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'loans_by_sector_pembinaan_construction': 'loans_by_sector_pembinaan_construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_activities': 'finance_insurance_and_business_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'sector': 'sector',  # TODO: rename
    },

    # Islamic Banking: Loans by Type and Sector (prev)
    '1.19.3': {
        'akhir_tempoh_as_at_end_of_1': 'akhir_tempoh_as_at_end_of_1',  # TODO: rename
        'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector': 'banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector',  # TODO: rename
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_and_water': 'electricity_gas_and_water',  # TODO: rename
        'wholesale_retail_hotels_and_restaurants': 'wholesale_retail_hotels_and_restaurants',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'residential_property': 'residential_property',  # TODO: rename
        'non_residential_property': 'non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'financial_insurance_and_business_services': 'financial_insurance_and_business_services',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'sistem_perbankan_skim_perbankan_islam1_2_format_terdahulu_pinjaman_mengikut_jenis_dan_sektor_banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector_pembiayaan_mengikut_sektor_financing_by_sector_lain_lain_others': 'sistem_perbankan_skim_perbankan_islam1_2_format_terdahulu_pinjaman_mengikut_jenis_dan_sektor_banking_system_previous_format_islamic_banking_scheme1_2_loans_by_type_and_sector_pembiayaan_mengikut_sektor_financing_by_sector_lain_lain_others',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
        'overdrafts': 'overdrafts',  # TODO: rename
        'term_financing': 'term_financing',  # TODO: rename
        'bill_financing': 'bill_financing',  # TODO: rename
        'other_financing': 'other_financing',  # TODO: rename
    },

    # Commercial & Islamic Banks: Loans/Financing by Purpose
    '1.19.4': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_tujuan_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Investment Banks: Classification of Loans by Purpose
    '1.19.5': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_tujuan_merchant_banks_investment_banks_classification_of_loans_by_purpose_purpose_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Household Loan/Financing by Purpose
    '1.19.6': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total': 'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total',  # TODO: rename
        'cost_300k': 'cost_300k',  # TODO: rename
        'cost_300k_to_500k': 'cost_300k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Banking System: Household Loan/Financing by Purpose (prev)
    '1.19.6a': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total': 'banking_system_household_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total',  # TODO: rename
        'cost_250k': 'cost_250k',  # TODO: rename
        'cost_250k_to_500k': 'cost_250k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Banking System: Loans by Purpose (prev)
    '1.19a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_use': 'personal_use',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'purchase_of_consumer_durables': 'purchase_of_consumer_durables',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Loans by Purpose (prev2)
    '1.19b': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'sistem_perbankan_pengelasan_pinjaman_mengikut_tujuan1_banking_system_classification_of_loans_by_purpose1_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_use': 'personal_use',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'purchase_of_consumer_durables': 'purchase_of_consumer_durables',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Loan/Financing by Purpose (prev3)
    '1.19c': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total',  # TODO: rename
        'cost_250k': 'cost_250k',  # TODO: rename
        'cost_250k_to_500k': 'cost_250k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'of_which_housing_loan_financing_sold_to_cagamas': 'of_which_housing_loan_financing_sold_to_cagamas',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total': 'banking_system_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total',  # TODO: rename
        'purchase_of_industrial_building_factories': 'purchase_of_industrial_building_factories',  # TODO: rename
        'purchase_of_land_only': 'purchase_of_land_only',  # TODO: rename
        'purchase_of_commercial_complexes': 'purchase_of_commercial_complexes',  # TODO: rename
        'purchase_of_shophouses_shoplots': 'purchase_of_shophouses_shoplots',  # TODO: rename
        'purchase_of_other_non_residential_property': 'purchase_of_other_non_residential_property',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_personal_uses_total': 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Currency in Circulation by Denomination
    '1.2': {
        'currency_in_circulation_by_denomination': 'currency_in_circulation_by_denomination',  # TODO: rename
        'mata_wang_dalam_edaran_currency_in_circulation': 'mata_wang_dalam_edaran_currency_in_circulation',  # TODO: rename
        'rm1': 'rm1',  # TODO: rename
        'rm2': 'rm2',  # TODO: rename
        'rm5': 'rm5',  # TODO: rename
        'rm10': 'rm10',  # TODO: rename
        'rm20': 'rm20',  # TODO: rename
        'rm50': 'rm50',  # TODO: rename
        'rm100': 'rm100',  # TODO: rename
        'rm5002': 'rm5002',  # TODO: rename
        'rm10002': 'rm10002',  # TODO: rename
        'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_notes_currency_in_circulation_others': 'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_notes_currency_in_circulation_others',  # TODO: rename
        '1_sen': '1_sen',  # TODO: rename
        '5_sen': '5_sen',  # TODO: rename
        '10_sen': '10_sen',  # TODO: rename
        '20_sen': '20_sen',  # TODO: rename
        '50_sen': '50_sen',  # TODO: rename
        'rm14': 'rm14',  # TODO: rename
        'coins_currency_in_circulation': 'coins_currency_in_circulation',  # TODO: rename
        'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_rm_million_others': 'mata_wang_dalam_edaran_mengikut_jenis_nilai_currency_in_circulation_by_denomination_rm_million_others',  # TODO: rename
    },

    # Banking System: Loan/Financing by Sector
    '1.20': {
        'sector': 'sector',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_jumlah_total',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_total': 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_total',  # TODO: rename
        'growing_of_oil_palm': 'growing_of_oil_palm',  # TODO: rename
        'growing_of_cocoa': 'growing_of_cocoa',  # TODO: rename
        'growing_of_rubber_trees': 'growing_of_rubber_trees',  # TODO: rename
        'animal_production': 'animal_production',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_others': 'banking_system_loan_financing_by_sector_rm_million_agriculture_forestry_and_fishing_crops_and_animal_production_hunting_and_related_service_activities_others',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fishing_and_aquaculture': 'fishing_and_aquaculture',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_jumlah_total',  # TODO: rename
        'extraction_of_crude_petroleum_and_natural_gas': 'extraction_of_crude_petroleum_and_natural_gas',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_total': 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_total',  # TODO: rename
        'mining_of_tin_ores': 'mining_of_tin_ores',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_others': 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_mining_of_metal_ores_others',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_lain_lain_others': 'banking_system_loan_financing_by_sector_rm_million_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_jumlah_total',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_total': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_total',  # TODO: rename
        'palm_oil_processing': 'palm_oil_processing',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_others': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_food_products_others',  # TODO: rename
        'beverages': 'beverages',  # TODO: rename
        'tobacco_products': 'tobacco_products',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_reproduction_of_recorded_media': 'printing_and_reproduction_of_recorded_media',  # TODO: rename
        'chemicals_and_chemical_products': 'chemicals_and_chemical_products',  # TODO: rename
        'rubber_and_plastic_products': 'rubber_and_plastic_products',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_total': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_total',  # TODO: rename
        'basic_iron_and_steel': 'basic_iron_and_steel',  # TODO: rename
        'tin_smelting': 'tin_smelting',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_others': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_basic_metals_others',  # TODO: rename
        'fabricated_metal_products': 'fabricated_metal_products',  # TODO: rename
        'electrical_machinery_and_apparatus_n_e_c': 'electrical_machinery_and_apparatus_n_e_c',  # TODO: rename
        'machinery_and_equipment_n_e_c': 'machinery_and_equipment_n_e_c',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_manufacturing_lain_lain_others': 'banking_system_loan_financing_by_sector_rm_million_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_construction_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_construction_jumlah_total',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_total': 'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_total',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'non_residential': 'non_residential',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_others': 'banking_system_loan_financing_by_sector_rm_million_construction_construction_of_buildings_others',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'specialised_construction_activities': 'specialised_construction_activities',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_jumlah_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'banking_system_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_jumlah_total': 'banking_system_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_jumlah_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loan_financing': 'total_loan_financing',  # TODO: rename
    },

    # Commercial & Islamic Banks: Loans/Financing by Sector
    '1.20.1': {
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'manufacture_of_rubber_and_plastic_products': 'manufacture_of_rubber_and_plastic_products',  # TODO: rename
        'manufacturing_timah_tin': 'manufacturing_timah_tin',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'of_which_palm_oil_processing': 'of_which_palm_oil_processing',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_publishing_and_allied_industries': 'printing_and_publishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_pembinaan_construction_lain_lain_others',  # TODO: rename
        'real_estates': 'real_estates',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'business_activities': 'business_activities',  # TODO: rename
        'research_and_development': 'research_and_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Commercial & Islamic Banks: Loans by Sector (prev)
    '1.20.2': {
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'rubber_processing_and_rubber_products': 'rubber_processing_and_rubber_products',  # TODO: rename
        'manufacturing_timah_tin': 'manufacturing_timah_tin',  # TODO: rename
        'palm_oil_processing': 'palm_oil_processing',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_pulishing_and_allied_industries': 'printing_and_pulishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'plastic_products': 'plastic_products',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'building_materials': 'building_materials',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'industrial_buldings_and_factories': 'industrial_buldings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'kompleks_perniagaan_commercial_complexes': 'kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes': 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'real_estates': 'real_estates',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pengelasan_pinjaman_pembiayaan_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_classification_of_loans_financing_by_sector_previous_format_sector_lain_lain_others',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
        'of_which_loans_to_government': 'of_which_loans_to_government',  # TODO: rename
    },

    # Investment Banks: Classification of Loans by Sector
    '1.20.3': {
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pertanian_primer_primary_agriculture_lain_lain_others',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'manufacture_of_rubber_and_plastic_products': 'manufacture_of_rubber_and_plastic_products',  # TODO: rename
        'manufacturing_timah_tin': 'manufacturing_timah_tin',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'of_which_palm_oil_processing': 'of_which_palm_oil_processing',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_publishing_and_allied_industries': 'printing_and_publishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_lain_lain_others': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_lain_lain_others': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_pembinaan_construction_lain_lain_others',  # TODO: rename
        'real_estates': 'real_estates',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'bank_saudagar_bank_pelaburan_pengelasan_pinjaman_mengikut_sektor_merchant_banks_investment_banks_classification_of_loans_by_sector_sectors_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'business_activities': 'business_activities',  # TODO: rename
        'research_and_development': 'research_and_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Merchant Banks: Loans by Sector (prev)
    '1.20.4': {
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'rubber_processing_and_rubber_products': 'rubber_processing_and_rubber_products',  # TODO: rename
        'manufacturing_timah_tin': 'manufacturing_timah_tin',  # TODO: rename
        'palm_oil_processing': 'palm_oil_processing',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_publishing_and_allied_industries': 'printing_and_publishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'plastic_products': 'plastic_products',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'building_materials': 'building_materials',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories': 'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'kompleks_perniagaan_commercial_complexes': 'kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories': 'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes': 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'real_estates': 'real_estates',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_lain_lain_others': 'bank_saudagar_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_merchant_bank_classification_of_loans_by_sector_previous_format_sector_lain_lain_others',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
        'of_which_loans_to_government': 'of_which_loans_to_government',  # TODO: rename
    },

    # Finance Companies: Loans by Sector (prev)
    '1.20.5': {
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pertanian_ternakan_perhutanan_dan_perikanan_agriculture_hunting_forestry_and_fishing_lain_lain_others',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'rubber_processing_and_rubber_products': 'rubber_processing_and_rubber_products',  # TODO: rename
        'manufacturing_timah_tin': 'manufacturing_timah_tin',  # TODO: rename
        'palm_oil_processing': 'palm_oil_processing',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_publishing_and_allied_industries': 'printing_and_publishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'plastic_products': 'plastic_products',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'building_materials': 'building_materials',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories': 'bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'kompleks_perniagaan_commercial_complexes': 'kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembinaan_construction_lain_lain_others',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_kediaman_purchase_of_residential_property_jumlah_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150k_to_250k': '150k_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'housing_loans_sold_to_cagamas': 'housing_loans_sold_to_cagamas',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories': 'purchase_of_non_residential_property_bangunan_kilang_dan_perusahaan_industrial_buildings_and_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes': 'purchase_of_non_residential_property_kompleks_perniagaan_commercial_complexes',  # TODO: rename
        'shophouses': 'shophouses',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_pembelian_harta_bukan_kediaman_purchase_of_non_residential_property_lain_lain_others',  # TODO: rename
        'real_estates': 'real_estates',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_services': 'financial_services',  # TODO: rename
        'insurance': 'insurance',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'community_social_and_personal_services': 'community_social_and_personal_services',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_format_terdahulu_finance_companies_classification_of_loans_by_sector_previous_format_sector_lain_lain_others',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
        'of_which_loans_to_government': 'of_which_loans_to_government',  # TODO: rename
    },

    # Finance Companies: Loans by Sector (historical)
    '1.20.6': {
        'sector_pertanian_agriculture_jumlah_total': 'sector_pertanian_agriculture_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries_and_livestock': 'fisheries_and_livestock',  # TODO: rename
        'other_agriculture': 'other_agriculture',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'tin': 'tin',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'other_minerals': 'other_minerals',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_jumlah_total',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'textiles_and_wearing_apparel': 'textiles_and_wearing_apparel',  # TODO: rename
        'wood_and_woods_products': 'wood_and_woods_products',  # TODO: rename
        'printing_publishing_paper_etc': 'printing_publishing_paper_etc',  # TODO: rename
        'metal_and_metal_products': 'metal_and_metal_products',  # TODO: rename
        'machinery_appliances_and_transport_equipment': 'machinery_appliances_and_transport_equipment',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perkilangan_manufacturing_lain_lain_others',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perdagangan_am_general_commerce_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_perdagangan_am_general_commerce_jumlah_total',  # TODO: rename
        'import_export_and_wholesale_trade': 'import_export_and_wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_jumlah_total',  # TODO: rename
        'housing': 'housing',  # TODO: rename
        'consumption_credit': 'consumption_credit',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_lain_lain_others': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_orang_orang_perseorangan_private_individuals_lain_lain_others',  # TODO: rename
        'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_pelbagai_hal_miscellaneous_jumlah_total': 'syarikat_kewangan_pengelasan_pinjaman_mengikut_sektor_terdahulu_finance_companies_classification_of_loans_by_sector_historical_sector_pelbagai_hal_miscellaneous_jumlah_total',  # TODO: rename
        'transport_and_storage': 'transport_and_storage',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'business_services': 'business_services',  # TODO: rename
        'all_other': 'all_other',  # TODO: rename
        'jumlah_pinjaman_total_loans': 'jumlah_pinjaman_total_loans',  # TODO: rename
        'foreign_loans': 'foreign_loans',  # TODO: rename
        'rm_juta_rm_million_jumlah_pinjaman_total_loans': 'rm_juta_rm_million_jumlah_pinjaman_total_loans',  # TODO: rename
    },

    # Banking System: Loans by Sector (prev)
    '1.20a': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_restaurants_and_hotels': 'wholesale_retail_restaurants_and_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'financing_insurance_and_business_services': 'financing_insurance_and_business_services',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Loans by Sector (prev2)
    '1.20b': {
        'merchant_or_investment_banks': 'merchant_or_investment_banks',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_jumlah_total',  # TODO: rename
        'rubber': 'rubber',  # TODO: rename
        'oil_palm': 'oil_palm',  # TODO: rename
        'cocoa': 'cocoa',  # TODO: rename
        'livestock': 'livestock',  # TODO: rename
        'forestry_and_logging': 'forestry_and_logging',  # TODO: rename
        'fisheries': 'fisheries',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_lain_lain_others': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pertanian_primer_primary_agriculture_lain_lain_others',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_jumlah_total',  # TODO: rename
        'timah_tin': 'timah_tin',  # TODO: rename
        'crude_petroleum_and_natural_gas': 'crude_petroleum_and_natural_gas',  # TODO: rename
        'quarrying': 'quarrying',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perlombongan_dan_kuari_mining_and_quarrying_lain_lain_others',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_jumlah_total',  # TODO: rename
        'manufacture_of_rubber_and_plastic_products': 'manufacture_of_rubber_and_plastic_products',  # TODO: rename
        'manufacturing_including_agro_based_timah_tin': 'manufacturing_including_agro_based_timah_tin',  # TODO: rename
        'food_beverages_and_tobacco': 'food_beverages_and_tobacco',  # TODO: rename
        'of_which_palm_oil_processing': 'of_which_palm_oil_processing',  # TODO: rename
        'textiles_wearing_apparel_and_leather': 'textiles_wearing_apparel_and_leather',  # TODO: rename
        'wood_and_wood_products_incl_furniture': 'wood_and_wood_products_incl_furniture',  # TODO: rename
        'paper_and_paper_products': 'paper_and_paper_products',  # TODO: rename
        'printing_and_publishing_and_allied_industries': 'printing_and_publishing_and_allied_industries',  # TODO: rename
        'industrial_chemicals': 'industrial_chemicals',  # TODO: rename
        'non_metallic_mineral_products': 'non_metallic_mineral_products',  # TODO: rename
        'iron_and_steel_products': 'iron_and_steel_products',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'machinery_non_electrical': 'machinery_non_electrical',  # TODO: rename
        'electrical_machinery_and_appliances': 'electrical_machinery_and_appliances',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_lain_lain_others': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkilangan_termasuk_asas_tani_manufacturing_including_agro_based_lain_lain_others',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perdagangan_borong_dan_runcit_restoran_dan_hotel_wholesale_retail_restaurants_and_hotels_jumlah_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurants_and_hotels': 'restaurants_and_hotels',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_jumlah_total',  # TODO: rename
        'civil_engineering': 'civil_engineering',  # TODO: rename
        'industrial_buildings_and_factories': 'industrial_buildings_and_factories',  # TODO: rename
        'infrastructure': 'infrastructure',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'residential': 'residential',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_lain_lain_others': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_pembinaan_construction_lain_lain_others',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total': 'sistem_perbankan_pengelasan_pinjaman_mengikut_sektor_banking_system_classification_of_loans_by_sector_perkhidmatan_kewangan_insurans_dan_perniagaan_financing_insurance_and_business_services_jumlah_total',  # TODO: rename
        'financial_intermediation': 'financial_intermediation',  # TODO: rename
        'business_activities': 'business_activities',  # TODO: rename
        'research_and_development': 'research_and_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_loans': 'total_loans',  # TODO: rename
    },

    # Banking System: Loans by MFRS 9 Stages and Provisions
    '1.21': {
        'industry': 'industry',  # TODO: rename
        'banking_system_total_loan_financing_by_malaysian_financial_reporting_standards_9_mfrs_9_stages_and_total_provisions_rm_million_total_loan_financing_jumlah_total': 'banking_system_total_loan_financing_by_malaysian_financial_reporting_standards_9_mfrs_9_stages_and_total_provisions_rm_million_total_loan_financing_jumlah_total',  # TODO: rename
        '12_months_expected_credit_losses_stage_1': '12_months_expected_credit_losses_stage_1',  # TODO: rename
        'lifetime_expected_credit_losses_not_credit_impaired_stage_2': 'lifetime_expected_credit_losses_not_credit_impaired_stage_2',  # TODO: rename
        'lifetime_expected_credit_losses_credit_impaired_stage_3': 'lifetime_expected_credit_losses_credit_impaired_stage_3',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_gross_impaired_loan_financing_to_gross_total_financing': 'ratio_of_gross_impaired_loan_financing_to_gross_total_financing',  # TODO: rename
        'ratio_of_net_impaired_financing_to_net_total_financing': 'ratio_of_net_impaired_financing_to_net_total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing by MFRS 9 Stages and Provisions
    '1.21.1': {
        'industry': 'industry',  # TODO: rename
        'islamic_banking_system_total_financing_by_mfrs_9_stages_and_total_provisions_rm_million_total_financing_jumlah_total': 'islamic_banking_system_total_financing_by_mfrs_9_stages_and_total_provisions_rm_million_total_financing_jumlah_total',  # TODO: rename
        '12_months_expected_credit_losses_stage_1': '12_months_expected_credit_losses_stage_1',  # TODO: rename
        'lifetime_expected_credit_losses_not_credit_impaired_stage_2': 'lifetime_expected_credit_losses_not_credit_impaired_stage_2',  # TODO: rename
        'lifetime_expected_credit_losses_credit_impaired_stage_3': 'lifetime_expected_credit_losses_credit_impaired_stage_3',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_gross_impaired_financing_to_gross_total_financing': 'ratio_of_gross_impaired_financing_to_gross_total_financing',  # TODO: rename
        'ratio_of_net_impaired_financing_to_net_total_financing': 'ratio_of_net_impaired_financing_to_net_total_financing',  # TODO: rename
    },

    # Islamic Banking: NPL/Impaired and Provisions (prev)
    '1.21.1a': {
        'ibs_of_investment_merchant_banks': 'ibs_of_investment_merchant_banks',  # TODO: rename
        'non_performing_financing_impaired_financing': 'non_performing_financing_impaired_financing',  # TODO: rename
        'pendapatan_tergantung_income_in_suspense': 'pendapatan_tergantung_income_in_suspense',  # TODO: rename
        'peruntukan_jejas_nilai_individu_individual_impairment_provisions': 'peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        'collective_impairment_provisions': 'collective_impairment_provisions',  # TODO: rename
        'pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing': 'pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing',  # TODO: rename
        'pembiayaan_bersih_net_total_financing': 'pembiayaan_bersih_net_total_financing',  # TODO: rename
        'nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing': 'nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing',  # TODO: rename
        'ratio_of_total_provisions_impairment_provisions_to_net_non_performing_financing_impaired_financing': 'ratio_of_total_provisions_impairment_provisions_to_net_non_performing_financing_impaired_financing',  # TODO: rename
        'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing': 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing',  # TODO: rename
        'impaired_financing': 'impaired_financing',  # TODO: rename
        '6_months_pendapatan_tergantung_income_in_suspense': '6_months_pendapatan_tergantung_income_in_suspense',  # TODO: rename
        '6_months_peruntukan_jejas_nilai_individu_individual_impairment_provisions': '6_months_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        'general_provisions_collective_impairment_provisions': 'general_provisions_collective_impairment_provisions',  # TODO: rename
        '6_months_pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing': '6_months_pembiayaan_tak_berbayar_bersih_pembiayaan_terjejas_bersih_net_impaired_financing',  # TODO: rename
        '6_months_pembiayaan_bersih_net_total_financing': '6_months_pembiayaan_bersih_net_total_financing',  # TODO: rename
        '6_months_nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing': '6_months_nisbah_pembiayaan_tak_berbayar_bersih_pembiayaan_jejas_nilai_kepada_jumlah_pembiayaan_besih_ratio_of_net_non_performing_financing_impaired_financing_to_net_total_financing',  # TODO: rename
        'impairment_provisions_to_net_non_performing_financing_impaired_financing': 'impairment_provisions_to_net_non_performing_financing_impaired_financing',  # TODO: rename
        '6_months_nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing': '6_months_nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pembiayaan_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_financing',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Impaired Financing and Provisions (prev)
    '1.21.1b': {
        'islamic_banking_scheme_ibs': 'islamic_banking_scheme_ibs',  # TODO: rename
        'impaired_financing': 'impaired_financing',  # TODO: rename
        'individual_impairment_provisions': 'individual_impairment_provisions',  # TODO: rename
        'collective_impairment_provisions': 'collective_impairment_provisions',  # TODO: rename
        'ratio_of_net_impaired_financing_to_net_total_financing': 'ratio_of_net_impaired_financing_to_net_total_financing',  # TODO: rename
        'ratio_of_total_impairment_provisions_to_total_impaired_financing': 'ratio_of_total_impairment_provisions_to_total_impaired_financing',  # TODO: rename
        'ratio_of_collective_impairment_provisions_to_net_total_financing': 'ratio_of_collective_impairment_provisions_to_net_total_financing',  # TODO: rename
    },

    # Islamic Banking: Impaired Financing and Provisions (prev2)
    '1.21.1c': {
        'industry': 'industry',  # TODO: rename
        'impaired_financing': 'impaired_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_financing_to_net_total_financing': 'ratio_of_net_impaired_financing_to_net_total_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_financing': 'ratio_of_total_provisions_to_total_financing',  # TODO: rename
    },

    # Islamic Banking: Impaired Financing and Provisions (prev3)
    '1.21.1d': {
        'industry': 'industry',  # TODO: rename
        'impaired_loan_financing': 'impaired_loan_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing': 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_loan_financing': 'ratio_of_total_provisions_to_total_loan_financing',  # TODO: rename
    },

    # Commercial & Islamic Banks: NPL/Impaired Loans
    '1.21.2': {
        'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': 'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        'faedah_tergantung_interest_in_suspense': 'faedah_tergantung_interest_in_suspense',  # TODO: rename
        'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
        '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        '6_months_faedah_tergantung_interest_in_suspense': '6_months_faedah_tergantung_interest_in_suspense',  # TODO: rename
        '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
    },

    # Commercial & Islamic Banks: Impaired Loans (prev)
    '1.21.2a': {
        'impaired_loans': 'impaired_loans',  # TODO: rename
        'individual_impairment_provisions': 'individual_impairment_provisions',  # TODO: rename
        'collective_impairment_provisions': 'collective_impairment_provisions',  # TODO: rename
        'ratio_of_net_impaired_loans_to_net_total_loans': 'ratio_of_net_impaired_loans_to_net_total_loans',  # TODO: rename
        'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans': 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans',  # TODO: rename
    },

    # Commercial & Islamic Banks: Impaired Loans (prev2)
    '1.21.2b': {
        'impaired_loan_financing': 'impaired_loan_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing': 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_loan_financing': 'ratio_of_total_provisions_to_total_loan_financing',  # TODO: rename
    },

    # Investment Banks: NPL/Impaired Loans
    '1.21.3': {
        'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': 'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        'faedah_tergantung_interest_in_suspense': 'faedah_tergantung_interest_in_suspense',  # TODO: rename
        'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
        '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        '6_months_faedah_tergantung_interest_in_suspense': '6_months_faedah_tergantung_interest_in_suspense',  # TODO: rename
        '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
    },

    # Investment Banks: Impaired Loans (prev)
    '1.21.3a': {
        'impaired_loans': 'impaired_loans',  # TODO: rename
        'individual_impairment_provisions': 'individual_impairment_provisions',  # TODO: rename
        'collective_impairment_provisions': 'collective_impairment_provisions',  # TODO: rename
        'ratio_of_net_impaired_loans_to_net_total_loans': 'ratio_of_net_impaired_loans_to_net_total_loans',  # TODO: rename
        'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans': 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans',  # TODO: rename
    },

    # Investment Banks: Impaired Loans (prev2)
    '1.21.3b': {
        'impaired_loan_financing': 'impaired_loan_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing': 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_loan_financing': 'ratio_of_total_provisions_to_total_loan_financing',  # TODO: rename
    },

    # Finance Companies: Loan Provisions and NPL
    '1.21.4': {
        'pinjaman_tak_berbayar_non_performing_loans': 'pinjaman_tak_berbayar_non_performing_loans',  # TODO: rename
        'faedah_tergantung_interest_in_suspense': 'faedah_tergantung_interest_in_suspense',  # TODO: rename
        'peruntukan_khas_specific_provisions': 'peruntukan_khas_specific_provisions',  # TODO: rename
        'peruntukan_am_general_provisions': 'peruntukan_am_general_provisions',  # TODO: rename
        'jumlah_pinjaman1_3_total_loans1_3': 'jumlah_pinjaman1_3_total_loans1_3',  # TODO: rename
        'pinjaman_tak_berbayar4_non_performing_loans4': 'pinjaman_tak_berbayar4_non_performing_loans4',  # TODO: rename
        'jumlah_pinjaman_bersih2_net_total_loans2': 'jumlah_pinjaman_bersih2_net_total_loans2',  # TODO: rename
        '6_months_pinjaman_tak_berbayar_non_performing_loans': '6_months_pinjaman_tak_berbayar_non_performing_loans',  # TODO: rename
        '6_months_faedah_tergantung_interest_in_suspense': '6_months_faedah_tergantung_interest_in_suspense',  # TODO: rename
        '6_months_peruntukan_khas_specific_provisions': '6_months_peruntukan_khas_specific_provisions',  # TODO: rename
        '6_months_peruntukan_am_general_provisions': '6_months_peruntukan_am_general_provisions',  # TODO: rename
        '6_months_jumlah_pinjaman1_3_total_loans1_3': '6_months_jumlah_pinjaman1_3_total_loans1_3',  # TODO: rename
        '6_months_pinjaman_tak_berbayar4_non_performing_loans4': '6_months_pinjaman_tak_berbayar4_non_performing_loans4',  # TODO: rename
        'rm_million_jumlah_pinjaman_bersih2_net_total_loans2': 'rm_million_jumlah_pinjaman_bersih2_net_total_loans2',  # TODO: rename
    },

    # Banking System: NPL/Impaired Loans and Provisions (prev)
    '1.21a': {
        'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': 'pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        'faedah_tergantung_interest_in_suspense': 'faedah_tergantung_interest_in_suspense',  # TODO: rename
        'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': 'peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_jejas_nilai_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': 'nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'nisbah_peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
        '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans': '6_months_pinjaman_tak_berbayar_pinjaman_terjejas_non_performing_loan_impaired_loans',  # TODO: rename
        '6_months_faedah_tergantung_interest_in_suspense': '6_months_faedah_tergantung_interest_in_suspense',  # TODO: rename
        '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions': '6_months_peruntukan_khas_peruntukan_jejas_nilai_individu_individual_impairment_provisions',  # TODO: rename
        '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions': '6_months_peruntukan_am_peruntukan_jejas_nilai_kolektif_collective_impairment_provisions',  # TODO: rename
        'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans': 'nisbah_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_kepada_jumlah_pinjaman_bersih_ratio_of_net_non_performing_loans_impaired_loans_to_net_total_loans',  # TODO: rename
        '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans': '6_months_nisbah_jumlah_peruntukan_peruntukan_jejas_nilai_kepada_pinjaman_tak_berbayar_bersih_pinjaman_terjejas_ratio_of_total_provisions_impairment_provisions_to_net_non_performing_loans_impaired_loans',  # TODO: rename
        'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans': 'peruntukan_am_peruntukan_jejas_nilai_kolektif_kepada_jumlah_pinjaman_bersih_ratio_of_general_provisions_collective_impairment_provisions_to_net_total_loans',  # TODO: rename
    },

    # Banking System: Impaired Loans and Provisions (prev)
    '1.21b': {
        'impaired_loans': 'impaired_loans',  # TODO: rename
        'individual_impairment_provisions': 'individual_impairment_provisions',  # TODO: rename
        'collective_impairment_provisions': 'collective_impairment_provisions',  # TODO: rename
        'ratio_of_net_impaired_loans_to_net_total_loans': 'ratio_of_net_impaired_loans_to_net_total_loans',  # TODO: rename
        'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans': 'ratio_of_individual_and_collective_impairment_provisions_to_total_impaired_loans',  # TODO: rename
    },

    # Banking System: Impaired Loans and Provisions (prev2)
    '1.21c': {
        'impaired_loan_financing': 'impaired_loan_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing': 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_loan_financing': 'ratio_of_total_provisions_to_total_loan_financing',  # TODO: rename
    },

    # Banking System: Impaired Loans and Provisions (prev3)
    '1.21d': {
        'industry': 'industry',  # TODO: rename
        'impaired_loan_financing': 'impaired_loan_financing',  # TODO: rename
        'total_provisions': 'total_provisions',  # TODO: rename
        'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing': 'ratio_of_net_impaired_loan_financing_to_net_total_loan_financing',  # TODO: rename
        'ratio_of_total_provisions_to_total_loan_financing': 'ratio_of_total_provisions_to_total_loan_financing',  # TODO: rename
    },

    # Banking System: Impaired Loan/Financing by Purpose
    '1.22': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_jumlah_total',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_jumlah_total',  # TODO: rename
        'cost_300k': 'cost_300k',  # TODO: rename
        'cost_300k_to_500k': 'cost_300k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_jumlah_total',  # TODO: rename
        'purchase_of_industrial_building_factories': 'purchase_of_industrial_building_factories',  # TODO: rename
        'purchase_of_land_only': 'purchase_of_land_only',  # TODO: rename
        'purchase_of_commercial_complexes': 'purchase_of_commercial_complexes',  # TODO: rename
        'purchase_of_shophouses_shoplots': 'purchase_of_shophouses_shoplots',  # TODO: rename
        'purchase_of_other_non_residential_property': 'purchase_of_other_non_residential_property',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_jumlah_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_impaired_loan_financing': 'total_impaired_loan_financing',  # TODO: rename
    },

    # Commercial & Islamic Banks: NPL by Purpose
    '1.22.1': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150_to_250k': '150_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total',  # TODO: rename
        'industrial_building_factories': 'industrial_building_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouse': 'shophouse',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Investment Banks: NPL/Impaired Loans by Purpose
    '1.22.2': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total': 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150_to_250k': '150_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total': 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total',  # TODO: rename
        'industrial_building_factories': 'industrial_building_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouse': 'shophouse',  # TODO: rename
        'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others': 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_investment_banks_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Banking System: NPL/Impaired Loans by Purpose (prev)
    '1.22a': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Banking System: NPL/Impaired Loans by Purpose (prev2)
    '1.22b': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicle': 'purchase_of_transport_vehicle',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total': 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_kediaman_jumlah_purchase_of_residential_property_total',  # TODO: rename
        '25k': '25k',  # TODO: rename
        '25k_to_60k': '25k_to_60k',  # TODO: rename
        '60k_to_100k': '60k_to_100k',  # TODO: rename
        '100k_to_150k': '100k_to_150k',  # TODO: rename
        '150_to_250k': '150_to_250k',  # TODO: rename
        '250k': '250k',  # TODO: rename
        'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total': 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_jumlah_purchase_of_non_residential_property_total',  # TODO: rename
        'industrial_building_factories': 'industrial_building_factories',  # TODO: rename
        'land': 'land',  # TODO: rename
        'commercial_complexes': 'commercial_complexes',  # TODO: rename
        'shophouse': 'shophouse',  # TODO: rename
        'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others': 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_tujuan_banking_system_non_performing_impaired_loans_by_purpose_pembelian_harta_bukan_kediaman_lain_lain_others',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_uses': 'personal_uses',  # TODO: rename
        'credit_cards': 'credit_cards',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Banking System: Impaired Loans by Purpose (prev)
    '1.22c': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_residential_property_total',  # TODO: rename
        'cost_250k': 'cost_250k',  # TODO: rename
        'cost_250k_to_500k': 'cost_250k_to_500k',  # TODO: rename
        'cost_500k_to_1m': 'cost_500k_to_1m',  # TODO: rename
        'cost_1m': 'cost_1m',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_purchase_of_non_residential_property_total',  # TODO: rename
        'purchase_of_industrial_building_factories': 'purchase_of_industrial_building_factories',  # TODO: rename
        'purchase_of_land_only': 'purchase_of_land_only',  # TODO: rename
        'purchase_of_commercial_complexes': 'purchase_of_commercial_complexes',  # TODO: rename
        'purchase_of_shophouses_shoplots': 'purchase_of_shophouses_shoplots',  # TODO: rename
        'purchase_of_other_non_residential_property': 'purchase_of_other_non_residential_property',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_total': 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_total',  # TODO: rename
        'purchase_of_consumer_durable_goods': 'purchase_of_consumer_durable_goods',  # TODO: rename
        'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others': 'banking_system_impaired_loan_financing_by_purpose_rm_million_personal_uses_lain_lain_others',  # TODO: rename
        'credit_card': 'credit_card',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'total_impaired_loan_financing': 'total_impaired_loan_financing',  # TODO: rename
    },

    # Banking System: Impaired Loan/Financing by Sector
    '1.23': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others': 'banking_system_impaired_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_lain_lain_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_and_storage': 'transportation_and_storage',  # TODO: rename
        'information_and_communication': 'information_and_communication',  # TODO: rename
        'banking_system_impaired_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total': 'banking_system_impaired_loan_financing_by_sector_rm_million_finance_insurance_real_estate_and_business_activities_total',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_impaired_loan_financing': 'total_impaired_loan_financing',  # TODO: rename
    },

    # Commercial & Islamic Banks: NPL by Sector
    '1.23.1': {
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurant_hotels': 'restaurant_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_commercial_banks_and_islamic_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_imtermediation': 'financial_imtermediation',  # TODO: rename
        'real_estate_renting_and_business_activities': 'real_estate_renting_and_business_activities',  # TODO: rename
        'reseach_development': 'reseach_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Commercial & Islamic Banks: NPL by Sector (prev)
    '1.23.2': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'consump_tion_credit': 'consump_tion_credit',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tidak_berbayar_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_non_performing_loans_by_sector_previous_format_purpose_or_group_borrowers_lain_lain_others': 'bank_bank_perdagangan_dan_bank_bank_islam_pinjaman_tidak_berbayar_mengikut_sektor_format_terdahulu_commercial_banks_and_islamic_banks_non_performing_loans_by_sector_previous_format_purpose_or_group_borrowers_lain_lain_others',  # TODO: rename
        'total_non_performing_loans': 'total_non_performing_loans',  # TODO: rename
    },

    # Investment Banks: NPL/Impaired Loans by Sector
    '1.23.3': {
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurant_hotels': 'restaurant_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'bank_bank_pelaburan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_investment_banks_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_imtermediation': 'financial_imtermediation',  # TODO: rename
        'real_estate_renting_and_business_activities': 'real_estate_renting_and_business_activities',  # TODO: rename
        'reseach_development': 'reseach_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Merchant Banks: NPL by Sector (prev)
    '1.23.4': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufac_turing': 'manufac_turing',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'construc_tion': 'construc_tion',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'consump_tion_credit': 'consump_tion_credit',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'bank_saudagar_pinjaman_tidak_berbayar_mengikut_sektor_merchant_bank_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others': 'bank_saudagar_pinjaman_tidak_berbayar_mengikut_sektor_merchant_bank_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others',  # TODO: rename
        'total_non_performing_loans': 'total_non_performing_loans',  # TODO: rename
    },

    # Finance Companies: Non-Performing Loans by Sector
    '1.23.5': {
        'agriculture_hunting_forestry_and_fishing': 'agriculture_hunting_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufactu_ring': 'manufactu_ring',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'construc_tion': 'construc_tion',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_services': 'finance_insurance_and_business_services',  # TODO: rename
        'consump_tion_credit': 'consump_tion_credit',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'purchase_of_transport_vehicles': 'purchase_of_transport_vehicles',  # TODO: rename
        'syarikat_kewangan_pinjaman_tidak_berbayar_mengikut_sektor_finance_companies_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others': 'syarikat_kewangan_pinjaman_tidak_berbayar_mengikut_sektor_finance_companies_non_performing_loans_by_sector_purpose_or_group_borrowers_lain_lain_others',  # TODO: rename
        'total_non_performing_loans': 'total_non_performing_loans',  # TODO: rename
    },

    # Banking System: Impaired Loan/Financing by Type
    '1.23.6': {
        'type': 'type',  # TODO: rename
        'overdraft_facilities': 'overdraft_facilities',  # TODO: rename
        'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_total': 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_total',  # TODO: rename
        'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total': 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others': 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_hire_purchase_receivables_others',  # TODO: rename
        'leasing_receivables': 'leasing_receivables',  # TODO: rename
        'block_discounting_receivables': 'block_discounting_receivables',  # TODO: rename
        'bridging_loans_financing': 'bridging_loans_financing',  # TODO: rename
        'factoring_receivables': 'factoring_receivables',  # TODO: rename
        'personal_loans_financing': 'personal_loans_financing',  # TODO: rename
        'housing_loans_financing': 'housing_loans_financing',  # TODO: rename
        'other_term_loans_financing': 'other_term_loans_financing',  # TODO: rename
        'trade_bills_bill_financing': 'trade_bills_bill_financing',  # TODO: rename
        'trust_receipts': 'trust_receipts',  # TODO: rename
        'revolving_credit': 'revolving_credit',  # TODO: rename
        'credit_charge_card': 'credit_charge_card',  # TODO: rename
        'foreign_currency_loans_financing': 'foreign_currency_loans_financing',  # TODO: rename
        'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others': 'banking_system_impaired_loan_financing_by_type_rm_million_term_loans_financing_lain_lain_others',  # TODO: rename
        'total_impaired_loan_financing': 'total_impaired_loan_financing',  # TODO: rename
    },

    # Banking System: NPL/Impaired Loans by Sector (prev)
    '1.23a': {
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_restaurants_hotels': 'wholesale_retail_trade_and_restaurants_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'finance_insurance_and_business_activities': 'finance_insurance_and_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Banking System: NPL/Impaired Loans by Sector (prev2)
    '1.23b': {
        'sector': 'sector',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total': 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_perdagangan_borong_runcit_restoran_dan_hotel_jumlah_wholesale_retail_trade_and_restaurants_hotels_total',  # TODO: rename
        'wholesale_trade': 'wholesale_trade',  # TODO: rename
        'retail_trade': 'retail_trade',  # TODO: rename
        'restaurant_hotels': 'restaurant_hotels',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'transport_storage_and_communication': 'transport_storage_and_communication',  # TODO: rename
        'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total': 'sistem_perbankan_pinjaman_tak_berbayar_pinjaman_terjejas_mengikut_sektor_banking_system_non_performing_impaired_loans_by_sector_aktiviti_kewangan_insurans_dan_perniagaan_jumlah_finance_insurance_and_business_activities_total',  # TODO: rename
        'financial_imtermediation': 'financial_imtermediation',  # TODO: rename
        'real_estate_renting_and_business_activities': 'real_estate_renting_and_business_activities',  # TODO: rename
        'reseach_development': 'reseach_development',  # TODO: rename
        'other_business_activities': 'other_business_activities',  # TODO: rename
        'education_health_others': 'education_health_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
        'impaired_loans': 'impaired_loans',  # TODO: rename
    },

    # Banking System: Total Deposits by Type
    '1.24': {
        'demand_deposits': 'demand_deposits',  # TODO: rename
        'fixed_deposits_special_investment_account_and_general_investment_account': 'fixed_deposits_special_investment_account_and_general_investment_account',  # TODO: rename
        'saving_deposits': 'saving_deposits',  # TODO: rename
        'negotiable_instruments_of_deposits_issued': 'negotiable_instruments_of_deposits_issued',  # TODO: rename
        'foreign_currency_deposit': 'foreign_currency_deposit',  # TODO: rename
        'tawarruq_fixed_deposits': 'tawarruq_fixed_deposits',  # TODO: rename
        'others_deposit_accepted': 'others_deposit_accepted',  # TODO: rename
        'banking_system_total_deposits_by_type_and_repurchase_agreements_rm_million_total_deposit_total': 'banking_system_total_deposits_by_type_and_repurchase_agreements_rm_million_total_deposit_total',  # TODO: rename
        'repurchase_agreements': 'repurchase_agreements',  # TODO: rename
        'total_deposits_and_repurchase_agreements': 'total_deposits_and_repurchase_agreements',  # TODO: rename
    },

    # Islamic Banking: Deposits by Type
    '1.24.1': {
        'islamic_banking_system_deposits_by_type_discontinued': 'islamic_banking_system_deposits_by_type_discontinued',  # TODO: rename
        'rm_special_investment_deposits': 'rm_special_investment_deposits',  # TODO: rename
        'fx_special_investment_deposits': 'fx_special_investment_deposits',  # TODO: rename
        'rm_general_investment_deposits': 'rm_general_investment_deposits',  # TODO: rename
        'fx_general_investment_deposits': 'fx_general_investment_deposits',  # TODO: rename
        'rm_demand_deposits': 'rm_demand_deposits',  # TODO: rename
        'fx_demand_deposits': 'fx_demand_deposits',  # TODO: rename
        'rm_saving_deposits': 'rm_saving_deposits',  # TODO: rename
        'fx_saving_deposits': 'fx_saving_deposits',  # TODO: rename
        'negotiable_instruments_of_deposits_issued': 'negotiable_instruments_of_deposits_issued',  # TODO: rename
        'rm_tawarruq_fixed_deposits': 'rm_tawarruq_fixed_deposits',  # TODO: rename
        'fx_tawarruq_fixed_deposits': 'fx_tawarruq_fixed_deposits',  # TODO: rename
        'rm_others_deposit_accepted': 'rm_others_deposit_accepted',  # TODO: rename
        'fx_others_deposit_accepted': 'fx_others_deposit_accepted',  # TODO: rename
        'islamic_banking_system_deposits_by_type_discontinued_rm_million_total': 'islamic_banking_system_deposits_by_type_discontinued_rm_million_total',  # TODO: rename
    },

    # Islamic Banking: Deposits by Type & Holder
    '1.24.2': {
        'islamic_banking_system_deposits_by_type_and_holder': 'islamic_banking_system_deposits_by_type_and_holder',  # TODO: rename
        'kerajaan_persekutuan_federal_government': 'kerajaan_persekutuan_federal_government',  # TODO: rename
        'kerajaan_negeri_state_government': 'kerajaan_negeri_state_government',  # TODO: rename
        'badan_berkanun_statutory_agency': 'badan_berkanun_statutory_agency',  # TODO: rename
        'institusi_kewangan_financial_institution': 'institusi_kewangan_financial_institution',  # TODO: rename
        'perusahaan_perniagaan_business_enterprises': 'perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'individu_individuals': 'individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_khusus_rm_special_investment_deposits_jumlah_total',  # TODO: rename
        'fx_special_investment_deposits_kerajaan_persekutuan_federal_government': 'fx_special_investment_deposits_kerajaan_persekutuan_federal_government',  # TODO: rename
        'fx_special_investment_deposits_kerajaan_negeri_state_government': 'fx_special_investment_deposits_kerajaan_negeri_state_government',  # TODO: rename
        'fx_special_investment_deposits_badan_berkanun_statutory_agency': 'fx_special_investment_deposits_badan_berkanun_statutory_agency',  # TODO: rename
        'fx_special_investment_deposits_institusi_kewangan_financial_institution': 'fx_special_investment_deposits_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_special_investment_deposits_perusahaan_perniagaan_business_enterprises': 'fx_special_investment_deposits_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'fx_special_investment_deposits_individu_individuals': 'fx_special_investment_deposits_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_khusus_fx_special_investment_deposits_jumlah_total',  # TODO: rename
        'rm_general_investment_deposits_kerajaan_persekutuan_federal_government': 'rm_general_investment_deposits_kerajaan_persekutuan_federal_government',  # TODO: rename
        'rm_general_investment_deposits_kerajaan_negeri_state_government': 'rm_general_investment_deposits_kerajaan_negeri_state_government',  # TODO: rename
        'rm_general_investment_deposits_badan_berkanun_statutory_agency': 'rm_general_investment_deposits_badan_berkanun_statutory_agency',  # TODO: rename
        'rm_general_investment_deposits_institusi_kewangan_financial_institution': 'rm_general_investment_deposits_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_general_investment_deposits_perusahaan_perniagaan_business_enterprises': 'rm_general_investment_deposits_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'rm_general_investment_deposits_individu_individuals': 'rm_general_investment_deposits_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_pelaburan_am_rm_general_investment_deposits_jumlah_total',  # TODO: rename
        'fx_general_investment_deposits_kerajaan_persekutuan_federal_government': 'fx_general_investment_deposits_kerajaan_persekutuan_federal_government',  # TODO: rename
        'fx_general_investment_deposits_kerajaan_negeri_state_government': 'fx_general_investment_deposits_kerajaan_negeri_state_government',  # TODO: rename
        'fx_general_investment_deposits_badan_berkanun_statutory_agency': 'fx_general_investment_deposits_badan_berkanun_statutory_agency',  # TODO: rename
        'fx_general_investment_deposits_institusi_kewangan_financial_institution': 'fx_general_investment_deposits_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_general_investment_deposits_perusahaan_perniagaan_business_enterprises': 'fx_general_investment_deposits_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'fx_general_investment_deposits_individu_individuals': 'fx_general_investment_deposits_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_pelaburan_am_fx_general_investment_deposits_jumlah_total',  # TODO: rename
        'rm_demand_deposits_by_customer_kerajaan_persekutuan_federal_government': 'rm_demand_deposits_by_customer_kerajaan_persekutuan_federal_government',  # TODO: rename
        'rm_demand_deposits_by_customer_kerajaan_negeri_state_government': 'rm_demand_deposits_by_customer_kerajaan_negeri_state_government',  # TODO: rename
        'rm_demand_deposits_by_customer_badan_berkanun_statutory_agency': 'rm_demand_deposits_by_customer_badan_berkanun_statutory_agency',  # TODO: rename
        'rm_demand_deposits_by_customer_institusi_kewangan_financial_institution': 'rm_demand_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises': 'rm_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'rm_demand_deposits_by_customer_individu_individuals': 'rm_demand_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_permintaan_mengikut_penyimpan_rm_demand_deposits_by_customer_jumlah_total',  # TODO: rename
        'fx_demand_deposits_by_customer_kerajaan_persekutuan_federal_government': 'fx_demand_deposits_by_customer_kerajaan_persekutuan_federal_government',  # TODO: rename
        'fx_demand_deposits_by_customer_kerajaan_negeri_state_government': 'fx_demand_deposits_by_customer_kerajaan_negeri_state_government',  # TODO: rename
        'fx_demand_deposits_by_customer_badan_berkanun_statutory_agency': 'fx_demand_deposits_by_customer_badan_berkanun_statutory_agency',  # TODO: rename
        'fx_demand_deposits_by_customer_institusi_kewangan_financial_institution': 'fx_demand_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises': 'fx_demand_deposits_by_customer_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'fx_demand_deposits_by_customer_individu_individuals': 'fx_demand_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_permintaan_mengikut_penyimpan_fx_demand_deposits_by_customer_jumlah_total',  # TODO: rename
        'rm_saving_deposits_by_customer_institusi_kewangan_financial_institution': 'rm_saving_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_saving_deposits_by_customer_individu_individuals': 'rm_saving_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tabungan_mengikut_penyimpan_rm_saving_deposits_by_customer_jumlah_total',  # TODO: rename
        'fx_saving_deposits_by_customer_institusi_kewangan_financial_institution': 'fx_saving_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_saving_deposits_by_customer_individu_individuals': 'fx_saving_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tabungan_mengikut_penyimpan_fx_saving_deposits_by_customer_jumlah_total',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_persekutuan_federal_government': 'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_persekutuan_federal_government',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_negeri_state_government': 'rm_negotiable_instruments_of_deposits_issued_by_customer_kerajaan_negeri_state_government',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_badan_berkanun_statutory_agency': 'rm_negotiable_instruments_of_deposits_issued_by_customer_badan_berkanun_statutory_agency',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_institusi_kewangan_financial_institution': 'rm_negotiable_instruments_of_deposits_issued_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_perusahaan_perniagaan_business_enterprises': 'rm_negotiable_instruments_of_deposits_issued_by_customer_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'rm_negotiable_instruments_of_deposits_issued_by_customer_individu_individuals': 'rm_negotiable_instruments_of_deposits_issued_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_instrumen_deposit_boleh_niaga_mengikut_penyimpan_rm_negotiable_instruments_of_deposits_issued_by_customer_jumlah_total',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government': 'rm_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government': 'rm_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency': 'rm_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution': 'rm_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises': 'rm_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'rm_tawarruq_fixed_deposits_by_customer_individu_individuals': 'rm_tawarruq_fixed_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_deposit_tetap_tawarruq_mengikut_penyimpan_rm_tawarruq_fixed_deposits_by_customer_jumlah_total',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government': 'fx_tawarruq_fixed_deposits_by_customer_kerajaan_persekutuan_federal_government',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government': 'fx_tawarruq_fixed_deposits_by_customer_kerajaan_negeri_state_government',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency': 'fx_tawarruq_fixed_deposits_by_customer_badan_berkanun_statutory_agency',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution': 'fx_tawarruq_fixed_deposits_by_customer_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises': 'fx_tawarruq_fixed_deposits_by_customer_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'fx_tawarruq_fixed_deposits_by_customer_individu_individuals': 'fx_tawarruq_fixed_deposits_by_customer_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_deposit_tetap_tawarruq_mengikut_penyimpan_fx_tawarruq_fixed_deposits_by_customer_jumlah_total',  # TODO: rename
        'rm_others_deposits_kerajaan_persekutuan_federal_government': 'rm_others_deposits_kerajaan_persekutuan_federal_government',  # TODO: rename
        'rm_others_deposits_kerajaan_negeri_state_government': 'rm_others_deposits_kerajaan_negeri_state_government',  # TODO: rename
        'rm_others_deposits_badan_berkanun_statutory_agency': 'rm_others_deposits_badan_berkanun_statutory_agency',  # TODO: rename
        'rm_others_deposits_institusi_kewangan_financial_institution': 'rm_others_deposits_institusi_kewangan_financial_institution',  # TODO: rename
        'rm_others_deposits_perusahaan_perniagaan_business_enterprises': 'rm_others_deposits_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'rm_others_deposits_individu_individuals': 'rm_others_deposits_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_rm_lain_lain_deposit_rm_others_deposits_jumlah_total',  # TODO: rename
        'fx_others_deposits_kerajaan_persekutuan_federal_government': 'fx_others_deposits_kerajaan_persekutuan_federal_government',  # TODO: rename
        'fx_others_deposits_kerajaan_negeri_state_government': 'fx_others_deposits_kerajaan_negeri_state_government',  # TODO: rename
        'fx_others_deposits_badan_berkanun_statutory_agency': 'fx_others_deposits_badan_berkanun_statutory_agency',  # TODO: rename
        'fx_others_deposits_institusi_kewangan_financial_institution': 'fx_others_deposits_institusi_kewangan_financial_institution',  # TODO: rename
        'fx_others_deposits_perusahaan_perniagaan_business_enterprises': 'fx_others_deposits_perusahaan_perniagaan_business_enterprises',  # TODO: rename
        'fx_others_deposits_individu_individuals': 'fx_others_deposits_individu_individuals',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_lain_lain_others': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_lain_lain_others',  # TODO: rename
        'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_jumlah_total': 'islamic_banking_system_deposits_by_type_and_holder_rm_million_fx_lain_lain_deposit_fx_others_deposits_jumlah_total',  # TODO: rename
    },

    # Islamic Banking: Deposits by Type and Holder (prev)
    '1.24.3': {
        'akhir_tempoh_as_at_end_of_1': 'akhir_tempoh_as_at_end_of_1',  # TODO: rename
        'banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder': 'banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder',  # TODO: rename
        'kerajaan_government': 'kerajaan_government',  # TODO: rename
        'institusi_kewangan_financial_institutions': 'institusi_kewangan_financial_institutions',  # TODO: rename
        'badan_perniagaan_business_enterprises': 'badan_perniagaan_business_enterprises',  # TODO: rename
        'individu_individuals': 'individu_individuals',  # TODO: rename
        'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_permintaan_demand_deposits_jumlah_total': 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_permintaan_demand_deposits_jumlah_total',  # TODO: rename
        'investment_deposits_kerajaan_government': 'investment_deposits_kerajaan_government',  # TODO: rename
        'investment_deposits_institusi_kewangan_financial_institutions': 'investment_deposits_institusi_kewangan_financial_institutions',  # TODO: rename
        'investment_deposits_badan_perniagaan_business_enterprises': 'investment_deposits_badan_perniagaan_business_enterprises',  # TODO: rename
        'investment_deposits_individu_individuals': 'investment_deposits_individu_individuals',  # TODO: rename
        'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_pelaburan_investment_deposits_jumlah_total': 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_deposit_pelaburan_investment_deposits_jumlah_total',  # TODO: rename
        'saving_deposits_institusi_kewangan_financial_institutions': 'saving_deposits_institusi_kewangan_financial_institutions',  # TODO: rename
        'saving_deposits_individu_individuals': 'saving_deposits_individu_individuals',  # TODO: rename
        'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_rm_million_jumlah_total': 'sistem_perbankan_format_terdahulu_skim_perbankan_islam_deposit_mengikut_jenis_dan_penyimpan_banking_system_previous_format_islamic_banking_scheme_deposits_by_type_and_holder_rm_million_jumlah_total',  # TODO: rename
    },

    # Banking System: Total Deposits by Holder
    '1.25': {
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_others': 'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_others',  # TODO: rename
        'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_total': 'banking_system_total_deposits_and_repurchase_agreement_by_holder_rm_million_total',  # TODO: rename
    },

    # Banking System: Demand Deposits by Holder
    '1.25.1': {
        'holder': 'holder',  # TODO: rename
        'banking_system_demand_deposits_by_holder': 'banking_system_demand_deposits_by_holder',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_others': 'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_others',  # TODO: rename
        'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_total': 'banking_system_demand_deposits_by_holder_rm_million_demand_deposits_by_customer_total',  # TODO: rename
    },

    # Banking System: Savings and Fixed Deposits by Holder
    '1.25.2': {
        'holder': 'holder',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_financial_institution': 'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_individuals': 'fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_individuals',  # TODO: rename
        'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_others': 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_others',  # TODO: rename
        'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_total': 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_fixed_deposits_tawarruq_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_customer_total',  # TODO: rename
        'saving_deposit_by_customer_financial_institution': 'saving_deposit_by_customer_financial_institution',  # TODO: rename
        'saving_deposit_by_customer_individuals': 'saving_deposit_by_customer_individuals',  # TODO: rename
        'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_others': 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_others',  # TODO: rename
        'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_total': 'banking_system_savings_and_fixed_deposits_tawarruq_fixed_deposits_special_and_general_investment_deposits²_by_holder_rm_million_saving_deposit_by_customer_total',  # TODO: rename
    },

    # Banking System: Repurchase Agreements by Holder
    '1.25.3': {
        'holder': 'holder',  # TODO: rename
        'banking_system_repurchase_agreements_by_holder': 'banking_system_repurchase_agreements_by_holder',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_others': 'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_others',  # TODO: rename
        'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_total': 'banking_system_repurchase_agreements_by_holder_rm_million_repurchase_agreements_by_customer_total',  # TODO: rename
    },

    # Banking System: NIDs by Holder
    '1.25.4': {
        'holder': 'holder',  # TODO: rename
        'banking_system_negotiable_instruments_of_deposits_by_holder': 'banking_system_negotiable_instruments_of_deposits_by_holder',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_others': 'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_others',  # TODO: rename
        'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_total': 'banking_system_negotiable_instruments_of_deposits_by_holder_rm_million_negotiable_instruments_of_deposits_issued_by_customer_total',  # TODO: rename
    },

    # Banking System: Foreign Currency and Other Deposits by Holder
    '1.25.5': {
        'holder': 'holder',  # TODO: rename
        'banking_system_foreign_currency_and_other_deposits_by_holder': 'banking_system_foreign_currency_and_other_deposits_by_holder',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'state_government': 'state_government',  # TODO: rename
        'statutory_agency': 'statutory_agency',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_others': 'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_others',  # TODO: rename
        'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_total': 'banking_system_foreign_currency_and_other_deposits_by_holder_rm_million_foreign_currency_deposits_by_customer_total',  # TODO: rename
        'other_deposits_accepted': 'other_deposits_accepted',  # TODO: rename
        'total_deposits': 'total_deposits',  # TODO: rename
    },

    # Banking System: Fixed Deposits by Original Maturity
    '1.25.6': {
        'original_maturity': 'original_maturity',  # TODO: rename
        'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity': 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity',  # TODO: rename
        'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_total': 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_total',  # TODO: rename
        'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_up_to_1_year_in_months_total': 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_up_to_1_year_in_months_total',  # TODO: rename
        'le_1_month': 'le_1_month',  # TODO: rename
        'gt_1_month_to_3_months': 'gt_1_month_to_3_months',  # TODO: rename
        'gt_3_months_to_6_months': 'gt_3_months_to_6_months',  # TODO: rename
        'gt_6_months_to_9_months': 'gt_6_months_to_9_months',  # TODO: rename
        'gt_9_months_to_12_months': 'gt_9_months_to_12_months',  # TODO: rename
        'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_exceeding_1_year_in_years_total': 'banking_system_fixed_deposits_special_investment_deposits_and_general_investment_deposits_by_original_maturity_rm_million_deposits_exceeding_1_year_in_years_total',  # TODO: rename
        'gt_1_year_to_3_years': 'gt_1_year_to_3_years',  # TODO: rename
        'gt_3_years_to_4_years': 'gt_3_years_to_4_years',  # TODO: rename
        'gt_4_years_to_5_years': 'gt_4_years_to_5_years',  # TODO: rename
        'gt_5_years': 'gt_5_years',  # TODO: rename
    },

    # Statutory Reserve Requirement and Liquidity Ratio
    '1.26': {
    },

    # Statutory Reserve and Liquid Asset Requirement
    '1.27': {
        'rizab_berkanun_statutory_reserve': 'rizab_berkanun_statutory_reserve',  # TODO: rename
        'tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities': 'tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities',  # TODO: rename
        'islamic_banks_rizab_berkanun_statutory_reserve': 'islamic_banks_rizab_berkanun_statutory_reserve',  # TODO: rename
        'islamic_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities': 'islamic_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities',  # TODO: rename
        'investment_banks_rizab_berkanun_statutory_reserve': 'investment_banks_rizab_berkanun_statutory_reserve',  # TODO: rename
        'investment_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities': 'investment_banks_tanggungan_yang_layak_dalam_rm_rm_eligible_liabilities',  # TODO: rename
    },

    # New Liquidity Framework
    '1.28': {
        'keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'lebihan_pematuhan_bersih_net_compliance_surplus': 'lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
        'maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus': 'maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
        'tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'islamic_banks_tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'islamic_banks_tempoh_matang_kurang_daripada_1_minggu_maturity_le_1_week_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'maturity_le_1_week_lebihan_pematuhan_bersih_net_compliance_surplus': 'maturity_le_1_week_lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
        'islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'rm_million_islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'rm_million_islamic_banks_tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus': 'tempoh_matang_lebih_daripada_1_minggu_hingga_1_bulan_maturity_gt_1_week_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
        'maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'tempoh_matang_kurang_daripada_3_hari_maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'tempoh_matang_kurang_daripada_3_hari_maturity_le_3_days_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'maturity_le_3_days_lebihan_pematuhan_bersih_net_compliance_surplus': 'maturity_le_3_days_lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
        'maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'tempoh_matang_lebih_daripada_3_hari_hingga_1_bulan_maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm': 'tempoh_matang_lebih_daripada_3_hari_hingga_1_bulan_maturity_gt_3_days_to_1_month_keperluan_pematuhan_seperti_yang_dipersetujui_dengan_bnm_compliance_requirement_as_agreed_with_bnm',  # TODO: rename
        'maturity_gt_3_days_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus': 'maturity_gt_3_days_to_1_month_lebihan_pematuhan_bersih_net_compliance_surplus',  # TODO: rename
    },

    # Liquidity Coverage Ratio
    '1.28a': {
        'nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio': 'nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio',  # TODO: rename
        'aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets': 'aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets',  # TODO: rename
        'aliran_keluar_tunai_bersih²_net_cash_outflows²': 'aliran_keluar_tunai_bersih²_net_cash_outflows²',  # TODO: rename
        'commercial_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio': 'commercial_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio',  # TODO: rename
        'commercial_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets': 'commercial_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets',  # TODO: rename
        'commercial_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²': 'commercial_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²',  # TODO: rename
        'islamic_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio': 'islamic_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio',  # TODO: rename
        'islamic_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets': 'islamic_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets',  # TODO: rename
        'islamic_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²': 'islamic_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²',  # TODO: rename
        'investment_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio': 'investment_banks_nisbah_perlindungan_mudah_tunai_liquidity_coverage_ratio',  # TODO: rename
        'investment_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets': 'investment_banks_aset_cair_berkualiti_tinggi_stok_hqla_stock_of_high_quality_liquid_assets',  # TODO: rename
        'investment_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²': 'investment_banks_aliran_keluar_tunai_bersih²_net_cash_outflows²',  # TODO: rename
    },

    # Banking System: Constituents of Capital
    '1.29': {
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'tier_2_capital': 'tier_2_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital': 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital',  # TODO: rename
        'capital_base': 'capital_base',  # TODO: rename
        'aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1': 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1',  # TODO: rename
        'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2': 'sistem_perbankan_komponen_modal_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'risk_weighted_capital_ratio': 'risk_weighted_capital_ratio',  # TODO: rename
        'core_capital_ratio': 'core_capital_ratio',  # TODO: rename
    },

    # Islamic Banking System: Constituents of Capital
    '1.29.1': {
        'akhir_tempoh_as_at_end_of_1': 'akhir_tempoh_as_at_end_of_1',  # TODO: rename
        'ibs_of_investment_merchant_banks': 'ibs_of_investment_merchant_banks',  # TODO: rename
        'core_capital': 'core_capital',  # TODO: rename
        'tier_2_capital': 'tier_2_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital': 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital',  # TODO: rename
        'capital_base': 'capital_base',  # TODO: rename
        'aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1': 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1',  # TODO: rename
        'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2': 'sistem_perbankan_islam_komponen_modal_islamic_banking_system_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'risk_weighted_capital_ratio': 'risk_weighted_capital_ratio',  # TODO: rename
        'core_capital_ratio': 'core_capital_ratio',  # TODO: rename
    },

    # Islamic Banking System: Constituents of Capital (v2)
    '1.29.1a': {
        'islamic_banking_scheme_ibs': 'islamic_banking_scheme_ibs',  # TODO: rename
        'cet1_capital': 'cet1_capital',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'cet1_capital_ratio': 'cet1_capital_ratio',  # TODO: rename
        'tier_1_capital_ratio': 'tier_1_capital_ratio',  # TODO: rename
        'total_capital_ratio': 'total_capital_ratio',  # TODO: rename
    },

    # Commercial & Islamic Banks: Constituents of Capital
    '1.29.2': {
        'akhir_tempoh_end_of_period_1': 'akhir_tempoh_end_of_period_1',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'tier_2_capital': 'tier_2_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital': 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital',  # TODO: rename
        'capital_base': 'capital_base',  # TODO: rename
        'aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1': 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2': 'bank_bank_perdagangan_dan_bank_bank_islam_komponen_modal_commercial_banks_and_islamic_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'capital_ratio': 'capital_ratio',  # TODO: rename
        'core_capital_ratio': 'core_capital_ratio',  # TODO: rename
    },

    # Commercial & Islamic Banks: Capital (prev)
    '1.29.2a': {
        'cet1_capital': 'cet1_capital',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'cet1_capital_ratio': 'cet1_capital_ratio',  # TODO: rename
        'tier_1_capital_ratio': 'tier_1_capital_ratio',  # TODO: rename
        'total_capital_ratio': 'total_capital_ratio',  # TODO: rename
    },

    # Finance Companies: Constituents of Capital
    '1.29.3': {
        'akhir_tempoh_end_of_period_1': 'akhir_tempoh_end_of_period_1',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'tier_2_capital': 'tier_2_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital': 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital',  # TODO: rename
        'capital_base': 'capital_base',  # TODO: rename
        'aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1': 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1',  # TODO: rename
        'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2': 'syarikat_kewangan_komponen_modal_finance_companies_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'risk_weighted_capital_ratio': 'risk_weighted_capital_ratio',  # TODO: rename
        'core_capital_ratio': 'core_capital_ratio',  # TODO: rename
    },

    # Investment Banks: Constituents of Capital
    '1.29.4': {
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'tier_2_capital': 'tier_2_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital': 'investment_in_subsidiaries_and_holdings_in_other_banking_institutions_capital',  # TODO: rename
        'capital_base': 'capital_base',  # TODO: rename
        'aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight': 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight',  # TODO: rename
        'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1': 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_1',  # TODO: rename
        'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2': 'bank_bank_pelaburan_komponen_modal_investment_banks_constituents_of_capital_aset_mengikut_wajaran_risiko_assets_by_risk_weight_2',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'risk_weighted_capital_ratio': 'risk_weighted_capital_ratio',  # TODO: rename
        'core_capital_ratio': 'core_capital_ratio',  # TODO: rename
    },

    # Investment Banks: Constituents of Capital (prev)
    '1.29.4a': {
        'cet1_capital': 'cet1_capital',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'cet1_capital_ratio': 'cet1_capital_ratio',  # TODO: rename
        'tier_1_capital_ratio': 'tier_1_capital_ratio',  # TODO: rename
        'total_capital_ratio': 'total_capital_ratio',  # TODO: rename
    },

    # Banking System: Constituents of Capital (v2)
    '1.29a': {
        'bank_pelaburan_investment_banks': 'bank_pelaburan_investment_banks',  # TODO: rename
        'cet1_capital': 'cet1_capital',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'cet1_capital_ratio': 'cet1_capital_ratio',  # TODO: rename
        'tier_1_capital_ratio': 'tier_1_capital_ratio',  # TODO: rename
        'total_capital_ratio': 'total_capital_ratio',  # TODO: rename
    },

    # Banking System: Constituents of Capital (prev)
    '1.29b': {
        'cet1_capital': 'cet1_capital',  # TODO: rename
        'tier_1_capital': 'tier_1_capital',  # TODO: rename
        'total_capital': 'total_capital',  # TODO: rename
        'total_risk_weighted_assets': 'total_risk_weighted_assets',  # TODO: rename
        'cet1_capital_ratio': 'cet1_capital_ratio',  # TODO: rename
        'tier_1_capital_ratio': 'tier_1_capital_ratio',  # TODO: rename
        'total_capital_ratio': 'total_capital_ratio',  # TODO: rename
    },

    # Monetary Aggregates: M1, M2 and M3
    '1.3': {
        'monetary_aggregates_m1_m2_and_m': 'monetary_aggregates_m1_m2_and_m',  # TODO: rename
        'total_m': 'total_m',  # TODO: rename
        'jumlah_total_m': 'jumlah_total_m',  # TODO: rename
        'm_jumlah_total_m': 'm_jumlah_total_m',  # TODO: rename
        'currency_m': 'currency_m',  # TODO: rename
        'demand_m': 'demand_m',  # TODO: rename
        'narrow_qm': 'narrow_qm',  # TODO: rename
        'savings_deposits': 'savings_deposits',  # TODO: rename
        'fixed_deposits': 'fixed_deposits',  # TODO: rename
        'nids': 'nids',  # TODO: rename
        'repos': 'repos',  # TODO: rename
        'fx_deposits': 'fx_deposits',  # TODO: rename
        'other_deposits': 'other_deposits',  # TODO: rename
        'deposits_placed_with_other_banking_institutions': 'deposits_placed_with_other_banking_institutions',  # TODO: rename
    },

    # Broad Money, M3
    '1.3.1': {
        'wang_secara_luas_m_broad_money_m_m_jumlah_total': 'wang_secara_luas_m_broad_money_m_m_jumlah_total',  # TODO: rename
        'wang_secara_luas_m_broad_money_m_m_baki_urus_niaga_transaction_balances_jumlah_total': 'wang_secara_luas_m_broad_money_m_m_baki_urus_niaga_transaction_balances_jumlah_total',  # TODO: rename
        'currency_in_circulation': 'currency_in_circulation',  # TODO: rename
        'demand_deposits': 'demand_deposits',  # TODO: rename
        'wang_secara_luas_m_broad_money_m_m_separuh_wang_secara_luas_broad_quasi_money_jumlah_total': 'wang_secara_luas_m_broad_money_m_m_separuh_wang_secara_luas_broad_quasi_money_jumlah_total',  # TODO: rename
        'savings_deposits': 'savings_deposits',  # TODO: rename
        'fixed_deposits': 'fixed_deposits',  # TODO: rename
        'nids': 'nids',  # TODO: rename
        'repos': 'repos',  # TODO: rename
        'foreign_currency_deposits': 'foreign_currency_deposits',  # TODO: rename
        'other_deposits': 'other_deposits',  # TODO: rename
    },

    # Factors Affecting M3
    '1.3.2': {
        'faktor_penentu_m_factors_affecting_m_jumlah_total': 'faktor_penentu_m_factors_affecting_m_jumlah_total',  # TODO: rename
        'faktor_penentu_m_factors_affecting_m_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total': 'faktor_penentu_m_factors_affecting_m_tuntutan_bersih_ke_atas_kerajaan_net_claims_on_government_jumlah_total',  # TODO: rename
        'claims_on_government': 'claims_on_government',  # TODO: rename
        'government_deposits': 'government_deposits',  # TODO: rename
        'faktor_penentu_m_factors_affecting_m_tuntutan_ke_atas_sektor_swasta_claims_on_the_private_sector_jumlah_total': 'faktor_penentu_m_factors_affecting_m_tuntutan_ke_atas_sektor_swasta_claims_on_the_private_sector_jumlah_total',  # TODO: rename
        'loans': 'loans',  # TODO: rename
        'securities': 'securities',  # TODO: rename
        'faktor_penentu_m_factors_affecting_m_aset_asing_bersih_net_foreign_assets_jumlah_total': 'faktor_penentu_m_factors_affecting_m_aset_asing_bersih_net_foreign_assets_jumlah_total',  # TODO: rename
        'bnm': 'bnm',  # TODO: rename
        'banking_system': 'banking_system',  # TODO: rename
        'other_influences': 'other_influences',  # TODO: rename
    },

    # Credit Card Operations in Malaysia
    '1.30': {
        'no_of_card_transactions¹': 'no_of_card_transactions¹',  # TODO: rename
        'in_malaysia_local_cardholders²': 'in_malaysia_local_cardholders²',  # TODO: rename
        'in_malaysia_foreign_cardholders³': 'in_malaysia_foreign_cardholders³',  # TODO: rename
        'abroad_local_cardholders²': 'abroad_local_cardholders²',  # TODO: rename
        'total_cash_advances_in_malaysia_local_cardholders²': 'total_cash_advances_in_malaysia_local_cardholders²',  # TODO: rename
        'total_cash_advances_in_malaysia_foreign_cardholders³': 'total_cash_advances_in_malaysia_foreign_cardholders³',  # TODO: rename
        'total_cash_advances_abroad_local_cardholders²': 'total_cash_advances_abroad_local_cardholders²',  # TODO: rename
        'principal_cards': 'principal_cards',  # TODO: rename
        'supplementary_cards': 'supplementary_cards',  # TODO: rename
        'amount_of_credit_line_extended': 'amount_of_credit_line_extended',  # TODO: rename
        'current_balances': 'current_balances',  # TODO: rename
        '3_months': '3_months',  # TODO: rename
        '3_to_6_months': '3_to_6_months',  # TODO: rename
        '6_months': '6_months',  # TODO: rename
    },

    # Debit Card Transactions
    '1.30.1': {
        'number_of_card_transactions': 'number_of_card_transactions',  # TODO: rename
        'total_purchases_in_malaysia': 'total_purchases_in_malaysia',  # TODO: rename
        'total_purchases_abroad': 'total_purchases_abroad',  # TODO: rename
        'total_cash_withdrawals_via_pos_terminal_in_malaysia': 'total_cash_withdrawals_via_pos_terminal_in_malaysia',  # TODO: rename
        'total_cash_withdrawals_via_pos_terminal_abroad': 'total_cash_withdrawals_via_pos_terminal_abroad',  # TODO: rename
        'total_fund_transfer_in_malaysia': 'total_fund_transfer_in_malaysia',  # TODO: rename
        'total_cash_withdrawals_via_atm_in_malaysia': 'total_cash_withdrawals_via_atm_in_malaysia',  # TODO: rename
        'rm_million_unit_million_abroad': 'rm_million_unit_million_abroad',  # TODO: rename
    },

    # Banking System: Loan to Fund Ratio and Liquidity
    '1.31': {
        'deposit_rm_billion': 'deposit_rm_billion',  # TODO: rename
        'debt': 'debt',  # TODO: rename
        'equity': 'equity',  # TODO: rename
        'loan': 'loan',  # TODO: rename
        'loan_to_fund_ratio': 'loan_to_fund_ratio',  # TODO: rename
        'loan_to_fund_and_equity_ratio': 'loan_to_fund_and_equity_ratio',  # TODO: rename
        'money_market_borrowings_excluding_repos_rm_billion': 'money_market_borrowings_excluding_repos_rm_billion',  # TODO: rename
        'repo': 'repo',  # TODO: rename
        'bnm_debt_securities': 'bnm_debt_securities',  # TODO: rename
        'srr': 'srr',  # TODO: rename
        'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_lain_lain_others': 'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_lain_lain_others',  # TODO: rename
        'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_jumlah_total': 'sistem_perbankan_nisbah_pinjaman_kepada_dana_nisbah_pinjaman_kepada_dana_dan_ekuiti_dan_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_banking_system_loan_to_fund_ratio_loan_to_fund_and_equity_ratio_and_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_mudah_tunai_ringgit_terkumpul_di_bank_negara_malaysia_outstanding_ringgit_liquidity_placed_with_bank_negara_malaysia_jumlah_total',  # TODO: rename
    },

    # Islamic Banking: Total Investment Account by Type and Holder
    '1.32': {
        'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_restricted_investment_account¹_total': 'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_restricted_investment_account¹_total',  # TODO: rename
        'financial_institution': 'financial_institution',  # TODO: rename
        'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_unrestricted_investment_account¹_total': 'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_unrestricted_investment_account¹_total',  # TODO: rename
        'business_enterprises': 'business_enterprises',  # TODO: rename
        'individuals': 'individuals',  # TODO: rename
        'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_jumlah_total': 'islamic_banking_system_total_investment_account¹_by_type_and_holder_rm_million_jumlah_total',  # TODO: rename
    },

    # Islamic Banking: Assets funded through Investment Account
    '1.32.1': {
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'amount_due_from_designated_financial_institutions': 'amount_due_from_designated_financial_institutions',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Islamic Banking: Financing through Investment Account by Type
    '1.32.2': {
        'syndicated_financing': 'syndicated_financing',  # TODO: rename
        'housing_financing': 'housing_financing',  # TODO: rename
        'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others': 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others',  # TODO: rename
        'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others_1': 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_type_rm_million_term_financing_others_1',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing through Investment Account by Concept
    '1.32.3': {
        'bai_bithaman_ajil': 'bai_bithaman_ajil',  # TODO: rename
        'murabahah': 'murabahah',  # TODO: rename
        'islamic_banking_system_total_financing_funded_through_investment_account¹_by_concept_rm_million_others': 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_concept_rm_million_others',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
    },

    # Islamic Banking: Financing through Investment Account by Purpose
    '1.32.4': {
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'islamic_banking_system_total_financing_funded_through_investment_account¹_by_purpose_and_sectors_rm_million_purpose_purchase_of_transport_vehicles_total': 'islamic_banking_system_total_financing_funded_through_investment_account¹_by_purpose_and_sectors_rm_million_purpose_purchase_of_transport_vehicles_total',  # TODO: rename
        'of_which_purchase_of_passenger_cars': 'of_which_purchase_of_passenger_cars',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'purchase_of_fixed_assets_other_than_land_and_building': 'purchase_of_fixed_assets_other_than_land_and_building',  # TODO: rename
        'personal_use': 'personal_use',  # TODO: rename
        'pembinaan_construction': 'pembinaan_construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purpose': 'other_purpose',  # TODO: rename
        'total_financing': 'total_financing',  # TODO: rename
        'primary_agriculture': 'primary_agriculture',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing_including_agro_based': 'manufacturing_including_agro_based',  # TODO: rename
        'electricity_gas_and_water_supply': 'electricity_gas_and_water_supply',  # TODO: rename
        'wholesale_retail_trade_and_hotels_restaurants': 'wholesale_retail_trade_and_hotels_restaurants',  # TODO: rename
        'sector_pembinaan_construction': 'sector_pembinaan_construction',  # TODO: rename
        'real_estate': 'real_estate',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'finance_insurance_and_business_activities': 'finance_insurance_and_business_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'household_sector': 'household_sector',  # TODO: rename
        'other_sector_n_e_c': 'other_sector_n_e_c',  # TODO: rename
    },

    # Islamic Banking: Total Investment Account by Original Maturity
    '1.32.5': {
        'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_jumlah_total': 'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_jumlah_total',  # TODO: rename
        'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_up_to_1_year_in_months_total': 'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_up_to_1_year_in_months_total',  # TODO: rename
        'le_1_month': 'le_1_month',  # TODO: rename
        'gt_1_month_to_3_months': 'gt_1_month_to_3_months',  # TODO: rename
        'gt_3_months_to_6_months': 'gt_3_months_to_6_months',  # TODO: rename
        'gt_6_months_to_9_months': 'gt_6_months_to_9_months',  # TODO: rename
        'gt_9_months_to_12_months': 'gt_9_months_to_12_months',  # TODO: rename
        'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_exceeding_1_year_in_years_total': 'islamic_banking_system_total_investment_account¹_by_original_maturity_rm_million_investment_account_exceeding_1_year_in_years_total',  # TODO: rename
        'gt_1_year_to_3_years': 'gt_1_year_to_3_years',  # TODO: rename
        'gt_3_years_to_4_years': 'gt_3_years_to_4_years',  # TODO: rename
        'gt_4_years_to_5_years': 'gt_4_years_to_5_years',  # TODO: rename
        'gt_5_years': 'gt_5_years',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing by Sector
    '1.33': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_sektor_financial_institution_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'total_outstanding_loan_financing': 'total_outstanding_loan_financing',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing Applied by Sector
    '1.33.1': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dipohon_mengikut_sektor_financial_institution_sme_loan_financing_applied_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'financing_applied': 'financing_applied',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing Approved by Sector
    '1.33.2': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_diluluskan_mengikut_sektor_financial_institution_sme_loan_financing_approved_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'financing_approved': 'financing_approved',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing Disbursed by Sector
    '1.33.3': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dikeluarkan_mengikut_sektor_financial_institution_sme_loan_financing_disbursed_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'financing_disbursed': 'financing_disbursed',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing Repaid by Sector
    '1.33.4': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_yang_dibayar_balik_mengikut_sektor_financial_institution_sme_loan_financing_repaid_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'financing_repaid': 'financing_repaid',  # TODO: rename
    },

    # Financial Institution: Impaired SME Loan/Financing by Sector
    '1.33.5': {
        'sector': 'sector',  # TODO: rename
        'agriculture_forestry_and_fishing': 'agriculture_forestry_and_fishing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'electricity_gas_steam_and_air_conditioning_supply': 'electricity_gas_steam_and_air_conditioning_supply',  # TODO: rename
        'water_supply_sewerage_waste_management_and_remediation_activities': 'water_supply_sewerage_waste_management_and_remediation_activities',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total': 'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_total',  # TODO: rename
        'wholesale_trade_except_of_motor_vehicles_and_motorcycles': 'wholesale_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'retail_trade_except_of_motor_vehicles_and_motorcycles': 'retail_trade_except_of_motor_vehicles_and_motorcycles',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others': 'institusi_kewangan_pinjaman_pembiayaan_terjejas_pks_mengikut_sektor_financial_institution_impaired_sme_loan_financing_by_sector_rm_million_wholesale_and_retail_trade_repair_of_motor_vehicles_and_motorcycles_others',  # TODO: rename
        'accommodation_and_food_service_activities': 'accommodation_and_food_service_activities',  # TODO: rename
        'transportation_storage': 'transportation_storage',  # TODO: rename
        'information_communication': 'information_communication',  # TODO: rename
        'financial_and_insurance_takaful_activities': 'financial_and_insurance_takaful_activities',  # TODO: rename
        'real_estate_activities': 'real_estate_activities',  # TODO: rename
        'professional_scientific_and_technical_activities': 'professional_scientific_and_technical_activities',  # TODO: rename
        'administrative_and_support_service_activities': 'administrative_and_support_service_activities',  # TODO: rename
        'education_health_and_others': 'education_health_and_others',  # TODO: rename
        'other_sector': 'other_sector',  # TODO: rename
        'financing': 'financing',  # TODO: rename
    },

    # Financial Institutions: SME Loan/Financing by Purpose
    '1.34': {
        'purpose': 'purpose',  # TODO: rename
        'purchase_of_securities': 'purchase_of_securities',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_total',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_total',  # TODO: rename
        'purchase_of_passenger_cars': 'purchase_of_passenger_cars',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_purchase_of_transport_vehicles_others',  # TODO: rename
        'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others': 'institusi_kewangan_pinjaman_pembiayaan_pks_mengikut_tujuan_financial_institutions_sme_loan_financing_by_purpose_rm_million_purchase_of_fixed_assets_other_than_land_and_building_lain_lain_others',  # TODO: rename
        'purchase_of_residential_property': 'purchase_of_residential_property',  # TODO: rename
        'purchase_of_non_residential_property': 'purchase_of_non_residential_property',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'working_capital': 'working_capital',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'financing': 'financing',  # TODO: rename
        'memo_item_credit_card': 'memo_item_credit_card',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing by SME Size
    '1.35': {
        'sme_size': 'sme_size',  # TODO: rename
        'individual_for_business': 'individual_for_business',  # TODO: rename
        'micro': 'micro',  # TODO: rename
        'small': 'small',  # TODO: rename
        'medium': 'medium',  # TODO: rename
        'financing': 'financing',  # TODO: rename
    },

    # Financial Institution: SME Loans Applied and Approved by Size
    '1.35.1': {
        'sme_size': 'sme_size',  # TODO: rename
        'individu_bagi_tujuan_perniagaan_individual_for_business': 'individu_bagi_tujuan_perniagaan_individual_for_business',  # TODO: rename
        'mikro_micro': 'mikro_micro',  # TODO: rename
        'kecil_small': 'kecil_small',  # TODO: rename
        'sederhana_medium': 'sederhana_medium',  # TODO: rename
        'financing_applied': 'financing_applied',  # TODO: rename
        'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business': 'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business',  # TODO: rename
        'rm_million_mikro_micro': 'rm_million_mikro_micro',  # TODO: rename
        'rm_million_kecil_small': 'rm_million_kecil_small',  # TODO: rename
        'rm_million_sederhana_medium': 'rm_million_sederhana_medium',  # TODO: rename
        'financing_approved': 'financing_approved',  # TODO: rename
    },

    # Financial Institution: SME Loans Disbursed and Repaid by Size
    '1.35.2': {
        'sme_size': 'sme_size',  # TODO: rename
        'individu_bagi_tujuan_perniagaan_individual_for_business': 'individu_bagi_tujuan_perniagaan_individual_for_business',  # TODO: rename
        'mikro_micro': 'mikro_micro',  # TODO: rename
        'kecil_small': 'kecil_small',  # TODO: rename
        'sederhana_medium': 'sederhana_medium',  # TODO: rename
        'financing_disbursed': 'financing_disbursed',  # TODO: rename
        'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business': 'rm_million_individu_bagi_tujuan_perniagaan_individual_for_business',  # TODO: rename
        'rm_million_mikro_micro': 'rm_million_mikro_micro',  # TODO: rename
        'rm_million_kecil_small': 'rm_million_kecil_small',  # TODO: rename
        'rm_million_sederhana_medium': 'rm_million_sederhana_medium',  # TODO: rename
        'financing_repaid': 'financing_repaid',  # TODO: rename
    },

    # Financial Institution: Impaired SME Loans by Size
    '1.35.3': {
        'sme_size': 'sme_size',  # TODO: rename
        'individual_for_business': 'individual_for_business',  # TODO: rename
        'micro': 'micro',  # TODO: rename
        'small': 'small',  # TODO: rename
        'medium': 'medium',  # TODO: rename
        'financing': 'financing',  # TODO: rename
    },

    # Financial Institution: SME Loan/Financing by Loan Size
    '1.36': {
        'loan_size': 'loan_size',  # TODO: rename
        'rm': 'rm',  # TODO: rename
        'rm1_million': 'rm1_million',  # TODO: rename
        'rm1_juta_hingga_rm5_juta_rm5_million': 'rm1_juta_hingga_rm5_juta_rm5_million',  # TODO: rename
        'rm5_juta_rm5_million': 'rm5_juta_rm5_million',  # TODO: rename
        'total_outstanding_loan_financing': 'total_outstanding_loan_financing',  # TODO: rename
    },

    # BNM: Statement of Assets
    '1.4': {
        'pada_akhir_tempoh_end_of_period_1': 'pada_akhir_tempoh_end_of_period_1',  # TODO: rename
        'bank_negara_malaysia_statement_of_assets': 'bank_negara_malaysia_statement_of_assets',  # TODO: rename
        'gold_and_foreign_exchange': 'gold_and_foreign_exchange',  # TODO: rename
        'imf_reserve_tranche_position': 'imf_reserve_tranche_position',  # TODO: rename
        'holdings_of_special_drawing_rights': 'holdings_of_special_drawing_rights',  # TODO: rename
        'malaysian_government_papers': 'malaysian_government_papers',  # TODO: rename
        'bills_discounted': 'bills_discounted',  # TODO: rename
        'deposits_with_financial_institutions': 'deposits_with_financial_institutions',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'deferred_expenditure': 'deferred_expenditure',  # TODO: rename
        'properties_land_and_buildings': 'properties_land_and_buildings',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # BNM: Statement of Capital and Liabilities
    '1.5': {
        'bank_negara_malaysia_statement_of_capital_and_liabilities': 'bank_negara_malaysia_statement_of_capital_and_liabilities',  # TODO: rename
        'paid_up_capital': 'paid_up_capital',  # TODO: rename
        'reserves': 'reserves',  # TODO: rename
        'currency_in_circulation': 'currency_in_circulation',  # TODO: rename
        'financial_institutions': 'financial_institutions',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'bank_negara_malaysia_penyata_modal_dan_liabiliti_bank_negara_malaysia_statement_of_capital_and_liabilities_deposit_deposits_lain_lain_others': 'bank_negara_malaysia_penyata_modal_dan_liabiliti_bank_negara_malaysia_statement_of_capital_and_liabilities_deposit_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_bills_and_bonds': 'bank_negara_bills_and_bonds',  # TODO: rename
        'allocation_of_special_drawing_rights': 'allocation_of_special_drawing_rights',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_liabilities': 'total_liabilities',  # TODO: rename
    },

    # BNM: Statement of Capital and Liabilities (prev)
    '1.5.1': {
        'bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format': 'bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format',  # TODO: rename
        'paid_up_capital': 'paid_up_capital',  # TODO: rename
        'general_reserve_fund': 'general_reserve_fund',  # TODO: rename
        'other_reserves': 'other_reserves',  # TODO: rename
        'currency_in_circulation': 'currency_in_circulation',  # TODO: rename
        'financial_institutions': 'financial_institutions',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'bank_negara_malaysia_penyata_modal_dan_liabiliti_format_terdahulu_bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format_deposit_deposits_lain_lain_others': 'bank_negara_malaysia_penyata_modal_dan_liabiliti_format_terdahulu_bank_negara_malaysia_statement_of_capital_and_liabilities_previous_format_deposit_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_bills_and_bonds': 'bank_negara_bills_and_bonds',  # TODO: rename
        'allocation_of_special_drawing_rights': 'allocation_of_special_drawing_rights',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_liabilities': 'total_liabilities',  # TODO: rename
    },

    # Banking System: Statement of Assets
    '1.7': {
        'assets': 'assets',  # TODO: rename
        'wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents': 'wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents',  # TODO: rename
        'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia': 'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos': 'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos',  # TODO: rename
        'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia': 'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'residents_bank_negara_malaysia': 'residents_bank_negara_malaysia',  # TODO: rename
        'residents_commercial_banks': 'residents_commercial_banks',  # TODO: rename
        'residents_islamic_banks': 'residents_islamic_banks',  # TODO: rename
        'residents_investment_banks': 'residents_investment_banks',  # TODO: rename
        'residents_other_banking_institutions': 'residents_other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions': 'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held': 'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held',  # TODO: rename
        'bil_perbendaha_raan_treasury_bills': 'bil_perbendaha_raan_treasury_bills',  # TODO: rename
        'sekuriti_kerajaan_¹_government_securities_¹': 'sekuriti_kerajaan_¹_government_securities_¹',  # TODO: rename
        'sekuriti_lain_other_securities': 'sekuriti_lain_other_securities',  # TODO: rename
        'pinjaman_dan_pendahuluan_loans_and_advances': 'pinjaman_dan_pendahuluan_loans_and_advances',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain_other_assets': 'aset_lain_other_assets',  # TODO: rename
        'jumlah_aset_total_assets': 'jumlah_aset_total_assets',  # TODO: rename
        'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents': 'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents',  # TODO: rename
        'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia': 'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos': 'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos',  # TODO: rename
        'deposits_placed_and_reverse_repos_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia': 'deposits_placed_and_reverse_repos_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia': 'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_commercial_banks': 'amount_due_from_designated_financial_institutions_residents_commercial_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_islamic_banks': 'amount_due_from_designated_financial_institutions_residents_islamic_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_investment_banks': 'amount_due_from_designated_financial_institutions_residents_investment_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_other_banking_institutions': 'amount_due_from_designated_financial_institutions_residents_other_banking_institutions',  # TODO: rename
        'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents': 'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents',  # TODO: rename
        'amount_due_from_designated_financial_institutions_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions': 'amount_due_from_designated_financial_institutions_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'amount_due_from_designated_financial_institutions_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held': 'amount_due_from_designated_financial_institutions_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held',  # TODO: rename
        'malaysian_securities_bil_perbendaha_raan_treasury_bills': 'malaysian_securities_bil_perbendaha_raan_treasury_bills',  # TODO: rename
        'malaysian_securities_sekuriti_kerajaan_¹_government_securities_¹': 'malaysian_securities_sekuriti_kerajaan_¹_government_securities_¹',  # TODO: rename
        'malaysian_securities_sekuriti_lain_other_securities': 'malaysian_securities_sekuriti_lain_other_securities',  # TODO: rename
        'malaysian_securities_pinjaman_dan_pendahuluan_loans_and_advances': 'malaysian_securities_pinjaman_dan_pendahuluan_loans_and_advances',  # TODO: rename
        'malaysian_securities_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'malaysian_securities_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'malaysian_securities_aset_lain_other_assets': 'malaysian_securities_aset_lain_other_assets',  # TODO: rename
        'malaysian_securities_jumlah_aset_total_assets': 'malaysian_securities_jumlah_aset_total_assets',  # TODO: rename
        'rm_million_jumlah_aset_total_assets': 'rm_million_jumlah_aset_total_assets',  # TODO: rename
    },

    # Islamic Banking System: Statement of Assets
    '1.7.1': {
        'assets': 'assets',  # TODO: rename
        'cash_and_cash_equivalents': 'cash_and_cash_equivalents',  # TODO: rename
        'balances_in_current_account_with_bank_negara_malaysia': 'balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'other_deposits_placed_and_reverse_repos': 'other_deposits_placed_and_reverse_repos',  # TODO: rename
        'statutory_deposits_with_bank_negara_malaysia': 'statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'non_residents': 'non_residents',  # TODO: rename
        'investment_account_due_from_designated_financial_institutions': 'investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'negotiable_instrument_deposits_held': 'negotiable_instrument_deposits_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities¹': 'government_securities¹',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'property_plant_and_equipment': 'property_plant_and_equipment',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Commercial & Islamic Banks: Statement of Assets
    '1.7.2': {
        'cash_and_cash_equivalents': 'cash_and_cash_equivalents',  # TODO: rename
        'balances_in_current_account_with_bank_negara_malaysia': 'balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'other_deposits_placed_and_reverse_repos': 'other_deposits_placed_and_reverse_repos',  # TODO: rename
        'statutory_deposits_with_bank_negara_malaysia': 'statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'non_residents': 'non_residents',  # TODO: rename
        'investment_account_due_from_designated_financial_institutions': 'investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'negotiable_instrument_deposits_held': 'negotiable_instrument_deposits_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities_¹': 'government_securities_¹',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'property_plant_and_equipment': 'property_plant_and_equipment',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Commercial & Islamic Banks: Assets (prev)
    '1.7.2.1': {
    },

    # Commercial & Islamic Banks: Domestic & Foreign Assets
    '1.7.3': {
        'wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents': 'wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents',  # TODO: rename
        'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia': 'baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos': 'deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos',  # TODO: rename
        'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia': 'simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'residents_bank_negara_malaysia': 'residents_bank_negara_malaysia',  # TODO: rename
        'residents_commercial_banks': 'residents_commercial_banks',  # TODO: rename
        'residents_islamic_banks': 'residents_islamic_banks',  # TODO: rename
        'residents_investment_banks': 'residents_investment_banks',  # TODO: rename
        'residents_other_banking_institutions': 'residents_other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions': 'jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held': 'instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held',  # TODO: rename
        'bil_perbendaha_raan_treasury_bills': 'bil_perbendaha_raan_treasury_bills',  # TODO: rename
        'sekuriti_kerajaan1_government_securities1': 'sekuriti_kerajaan1_government_securities1',  # TODO: rename
        'sekuriti_lain_other_securities': 'sekuriti_lain_other_securities',  # TODO: rename
        'pinjaman_dan_pendahuluan_loans_and_advances': 'pinjaman_dan_pendahuluan_loans_and_advances',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain_other_assets': 'aset_lain_other_assets',  # TODO: rename
        'jumlah_aset_total_assets': 'jumlah_aset_total_assets',  # TODO: rename
        'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents': 'bank_asing_foreign_banks_wang_tunai_dan_kesamaan_tunai_cash_and_cash_equivalents',  # TODO: rename
        'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia': 'deposits_placed_and_reverse_repos_baki_akaun_semasa_dengan_bank_negara_malaysia_balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos': 'deposits_placed_and_reverse_repos_deposit_lain_yang_disimpan_dan_repo_berbalik_other_deposits_placed_and_reverse_repos',  # TODO: rename
        'bank_asing_foreign_banks_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia': 'bank_asing_foreign_banks_simpanan_berkanun_dengan_bank_negara_malaysia_statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia': 'amount_due_from_designated_financial_institutions_residents_bank_negara_malaysia',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_commercial_banks': 'amount_due_from_designated_financial_institutions_residents_commercial_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_islamic_banks': 'amount_due_from_designated_financial_institutions_residents_islamic_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_investment_banks': 'amount_due_from_designated_financial_institutions_residents_investment_banks',  # TODO: rename
        'amount_due_from_designated_financial_institutions_residents_other_banking_institutions': 'amount_due_from_designated_financial_institutions_residents_other_banking_institutions',  # TODO: rename
        'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents': 'amount_due_from_designated_financial_institutions_bukan_pemastautin_non_residents',  # TODO: rename
        'bank_asing_foreign_banks_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions': 'bank_asing_foreign_banks_jumlah_akaun_pelaburan_yang_akan_diterima_daripada_institusi_kewangan_tertentu_investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'bank_asing_foreign_banks_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held': 'bank_asing_foreign_banks_instrumen_deposit_boleh_niaga_yang_dipegang_negotiable_instrument_deposits_held',  # TODO: rename
        'malaysian_securities_bil_perbendaha_raan_treasury_bills': 'malaysian_securities_bil_perbendaha_raan_treasury_bills',  # TODO: rename
        'malaysian_securities_sekuriti_kerajaan1_government_securities1': 'malaysian_securities_sekuriti_kerajaan1_government_securities1',  # TODO: rename
        'bank_asing_foreign_banks_sekuriti_lain_other_securities': 'bank_asing_foreign_banks_sekuriti_lain_other_securities',  # TODO: rename
        'bank_asing_foreign_banks_pinjaman_dan_pendahuluan_loans_and_advances': 'bank_asing_foreign_banks_pinjaman_dan_pendahuluan_loans_and_advances',  # TODO: rename
        'bank_asing_foreign_banks_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'bank_asing_foreign_banks_harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'bank_asing_foreign_banks_aset_lain_other_assets': 'bank_asing_foreign_banks_aset_lain_other_assets',  # TODO: rename
        'bank_asing_foreign_banks_jumlah_aset_total_assets': 'bank_asing_foreign_banks_jumlah_aset_total_assets',  # TODO: rename
    },

    # Commercial & Islamic Banks: Domestic & Foreign Assets (prev)
    '1.7.3.1': {
        'cash': 'cash',  # TODO: rename
        'balances_with_the_central_bank_of_malaysia': 'balances_with_the_central_bank_of_malaysia',  # TODO: rename
        'statutory_reserve_with_the_central_bank_of_malaysia': 'statutory_reserve_with_the_central_bank_of_malaysia',  # TODO: rename
        'money_at_call_in_malaysia': 'money_at_call_in_malaysia',  # TODO: rename
        'other_banks': 'other_banks',  # TODO: rename
        'finance_companies': 'finance_companies',  # TODO: rename
        'merchant_banks': 'merchant_banks',  # TODO: rename
        'outside_malaysia': 'outside_malaysia',  # TODO: rename
        'negotiable_instruments_of_deposit_held': 'negotiable_instruments_of_deposit_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities': 'government_securities',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'overdrafts_and_other_advances': 'overdrafts_and_other_advances',  # TODO: rename
        'more_than_1_year_to_4_years': 'more_than_1_year_to_4_years',  # TODO: rename
        'more_than_4_years': 'more_than_4_years',  # TODO: rename
        'of_which_outside_malaysia': 'of_which_outside_malaysia',  # TODO: rename
        'bankers_acceptances': 'bankers_acceptances',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_bil_bil_perdagangan_trade_bills_kena_bayar_di_malaysia_payable_in_malaysia_lain_lain_other': 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_bil_bil_perdagangan_trade_bills_kena_bayar_di_malaysia_payable_in_malaysia_lain_lain_other',  # TODO: rename
        'payable_outside_malaysia': 'payable_outside_malaysia',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_aset_tempatan_dan_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_assets_of_domestic_and_foreign_banks_previous_format_pinjaman_dan_pendahuluan_loans_and_advances_jumlah_total',  # TODO: rename
        'cheques_purchased': 'cheques_purchased',  # TODO: rename
        'fixed_and_other_assets_in_malaysia': 'fixed_and_other_assets_in_malaysia',  # TODO: rename
        'other_foreign_assets': 'other_foreign_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Investment Banks: Statement of Assets
    '1.7.4': {
        'cash_and_cash_equivalents': 'cash_and_cash_equivalents',  # TODO: rename
        'balances_in_current_account_with_bank_negara_malaysia': 'balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'other_deposits_placed_and_reverse_repos': 'other_deposits_placed_and_reverse_repos',  # TODO: rename
        'statutory_deposits_with_bank_negara_malaysia': 'statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'non_residents': 'non_residents',  # TODO: rename
        'negotiable_instrument_deposits_held': 'negotiable_instrument_deposits_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities': 'government_securities',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'property_plant_and_equipment': 'property_plant_and_equipment',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Finance Companies: Statement of Assets
    '1.7.5': {
        'cash': 'cash',  # TODO: rename
        'balances_with_bank_negara_malaysia': 'balances_with_bank_negara_malaysia',  # TODO: rename
        'statutory_reserves_with_bank_negara_malaysia': 'statutory_reserves_with_bank_negara_malaysia',  # TODO: rename
        'other_deposits_placed_and_reverse_repos': 'other_deposits_placed_and_reverse_repos',  # TODO: rename
        'money_at_call_in_malaysia': 'money_at_call_in_malaysia',  # TODO: rename
        'central_bank_of_malaysia': 'central_bank_of_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'finance_companies': 'finance_companies',  # TODO: rename
        'merchant_banks': 'merchant_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'di_luar_malaysia_outside_malaysia': 'di_luar_malaysia_outside_malaysia',  # TODO: rename
        'negotiable_instruments_of_deposit_held': 'negotiable_instruments_of_deposit_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities': 'government_securities',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'fixed_assets': 'fixed_assets',  # TODO: rename
        'in_malaysia': 'in_malaysia',  # TODO: rename
        'in_malaysia_di_luar_malaysia_outside_malaysia': 'in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Banking System: Statement of Assets (prev)
    '1.7a': {
        'assets': 'assets',  # TODO: rename
        'cash_and_cash_equivalents': 'cash_and_cash_equivalents',  # TODO: rename
        'balances_in_current_account_with_bank_negara_malaysia': 'balances_in_current_account_with_bank_negara_malaysia',  # TODO: rename
        'other_deposits_placed_and_reverse_repos': 'other_deposits_placed_and_reverse_repos',  # TODO: rename
        'statutory_deposits_with_bank_negara_malaysia': 'statutory_deposits_with_bank_negara_malaysia',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'non_residents': 'non_residents',  # TODO: rename
        'investment_account_due_from_designated_financial_institutions': 'investment_account_due_from_designated_financial_institutions',  # TODO: rename
        'negotiable_instrument_deposits_held': 'negotiable_instrument_deposits_held',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities_¹': 'government_securities_¹',  # TODO: rename
        'other_securities': 'other_securities',  # TODO: rename
        'loans_and_advances': 'loans_and_advances',  # TODO: rename
        'property_plant_and_equipment': 'property_plant_and_equipment',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
    },

    # Banking System: Statement of Capital and Liabilities
    '1.9': {
        'equities_and_liabilities': 'equities_and_liabilities',  # TODO: rename
        'modal_dan_rizab_total_equities': 'modal_dan_rizab_total_equities',  # TODO: rename
        'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund': 'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund',  # TODO: rename
        'akaun_deposit_khas_special_deposit_account': 'akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'banking_system_statement_of_equities_and_liabilities_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others': 'banking_system_statement_of_equities_and_liabilities_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'residents_bank_negara_malaysia': 'residents_bank_negara_malaysia',  # TODO: rename
        'residents_commercial_banks': 'residents_commercial_banks',  # TODO: rename
        'residents_islamic_banks': 'residents_islamic_banks',  # TODO: rename
        'residents_investment_banks': 'residents_investment_banks',  # TODO: rename
        'residents_other_banking_institutions': 'residents_other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'akaun_pelaburan_dari_pengguna_investment_account_of_customers': 'akaun_pelaburan_dari_pengguna_investment_account_of_customers',  # TODO: rename
        'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions': 'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'penerimaan_belum_bayar_acceptances_payable': 'penerimaan_belum_bayar_acceptances_payable',  # TODO: rename
        'pemastautin_residents': 'pemastautin_residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'tanggungan_lain_other_liabilities': 'tanggungan_lain_other_liabilities',  # TODO: rename
        'bank_tempatan_domestic_banks_total_equities_and_liabilities': 'bank_tempatan_domestic_banks_total_equities_and_liabilities',  # TODO: rename
        'bank_asing_foreign_banks_modal_dan_rizab_total_equities': 'bank_asing_foreign_banks_modal_dan_rizab_total_equities',  # TODO: rename
        'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund': 'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund',  # TODO: rename
        'total_deposits_akaun_deposit_khas_special_deposit_account': 'total_deposits_akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'banking_system_statement_of_equities_and_liabilities_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others': 'banking_system_statement_of_equities_and_liabilities_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia': 'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_commercial_banks': 'amount_due_to_designated_financial_institutions_residents_commercial_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_islamic_banks': 'amount_due_to_designated_financial_institutions_residents_islamic_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_investment_banks': 'amount_due_to_designated_financial_institutions_residents_investment_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_other_banking_institutions': 'amount_due_to_designated_financial_institutions_residents_other_banking_institutions',  # TODO: rename
        'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents': 'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents',  # TODO: rename
        'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers': 'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers',  # TODO: rename
        'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions': 'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'total_investment_account_penerimaan_belum_bayar_acceptances_payable': 'total_investment_account_penerimaan_belum_bayar_acceptances_payable',  # TODO: rename
        'bills_payable_pemastautin_residents': 'bills_payable_pemastautin_residents',  # TODO: rename
        'total_liabilities_bills_payable_bukan_pemastautin_non_residents': 'total_liabilities_bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'bills_payable_tanggungan_lain_other_liabilities': 'bills_payable_tanggungan_lain_other_liabilities',  # TODO: rename
        'bank_asing_foreign_banks_total_equities_and_liabilities': 'bank_asing_foreign_banks_total_equities_and_liabilities',  # TODO: rename
        'rm_million_total_equities_and_liabilities': 'rm_million_total_equities_and_liabilities',  # TODO: rename
    },

    # Islamic Banking System: Statement of Capital & Liabilities
    '1.9.1': {
        'equities_and_liabilities': 'equities_and_liabilities',  # TODO: rename
        'total_equities': 'total_equities',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'islamic_banking_system_statement_of_equities_and_liabilities_rm_million_total_liabilities_total_deposits_lain_lain_others': 'islamic_banking_system_statement_of_equities_and_liabilities_rm_million_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'investment_account_of_customers': 'investment_account_of_customers',  # TODO: rename
        'investment_account_due_to_designated_financial_institutions': 'investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'miscellaneous_borrowing': 'miscellaneous_borrowing',  # TODO: rename
        'miscellaneous_debt_securities_issued': 'miscellaneous_debt_securities_issued',  # TODO: rename
        'acceptances_payable': 'acceptances_payable',  # TODO: rename
        'residents': 'residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_equities_and_liabilities': 'total_equities_and_liabilities',  # TODO: rename
    },

    # Commercial & Islamic Banks: Statement of Liabilities
    '1.9.2': {
        'total_equities': 'total_equities',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others': 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'investment_account_of_customers': 'investment_account_of_customers',  # TODO: rename
        'investment_account_due_to_designated_financial_institutions': 'investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'acceptances_payable': 'acceptances_payable',  # TODO: rename
        'residents': 'residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_equities_and_liabilities': 'total_equities_and_liabilities',  # TODO: rename
    },

    # Commercial & Islamic Banks: Liabilities (prev)
    '1.9.2.1': {
        'capital_and_reserves': 'capital_and_reserves',  # TODO: rename
        'demand': 'demand',  # TODO: rename
        'fixed': 'fixed',  # TODO: rename
        'savings': 'savings',  # TODO: rename
        'bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_previous_format_deposit_deposits_jumlah_total': 'bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_previous_format_deposit_deposits_jumlah_total',  # TODO: rename
        'negotiable_instruments_of_deposits_issued': 'negotiable_instruments_of_deposits_issued',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'other_banks': 'other_banks',  # TODO: rename
        'finance_companies': 'finance_companies',  # TODO: rename
        'merchant_banks': 'merchant_banks',  # TODO: rename
        'di_luar_malaysia_outside_malaysia': 'di_luar_malaysia_outside_malaysia',  # TODO: rename
        'bankers_acceptances_outstanding': 'bankers_acceptances_outstanding',  # TODO: rename
        'di_malaysia_in_malaysia': 'di_malaysia_in_malaysia',  # TODO: rename
        'in_malaysia_di_luar_malaysia_outside_malaysia': 'in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'other_liabilities_di_malaysia_in_malaysia': 'other_liabilities_di_malaysia_in_malaysia',  # TODO: rename
        'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia': 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'total_liabilities': 'total_liabilities',  # TODO: rename
    },

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities
    '1.9.3': {
        'modal_dan_rizab_total_equities': 'modal_dan_rizab_total_equities',  # TODO: rename
        'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund': 'deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund',  # TODO: rename
        'akaun_deposit_khas_special_deposit_account': 'akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others': 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_tempatan_domestic_banks_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'residents_bank_negara_malaysia': 'residents_bank_negara_malaysia',  # TODO: rename
        'residents_commercial_banks': 'residents_commercial_banks',  # TODO: rename
        'residents_islamic_banks': 'residents_islamic_banks',  # TODO: rename
        'residents_investment_banks': 'residents_investment_banks',  # TODO: rename
        'residents_other_banking_institutions': 'residents_other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'akaun_pelaburan_dari_pengguna_investment_account_of_customers': 'akaun_pelaburan_dari_pengguna_investment_account_of_customers',  # TODO: rename
        'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions': 'jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'penerimaan_belum_bayar_acceptances_payable': 'penerimaan_belum_bayar_acceptances_payable',  # TODO: rename
        'pemastautin_residents': 'pemastautin_residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'tanggungan_lain_other_liabilities': 'tanggungan_lain_other_liabilities',  # TODO: rename
        'jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities': 'jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities',  # TODO: rename
        'bank_asing_foreign_banks_modal_dan_rizab_total_equities': 'bank_asing_foreign_banks_modal_dan_rizab_total_equities',  # TODO: rename
        'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund': 'total_deposits_deposit_dalam_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investment_fund',  # TODO: rename
        'total_deposits_akaun_deposit_khas_special_deposit_account': 'total_deposits_akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others': 'commercial_banks_and_islamic_banks_statement_of_equities_and_liabilities_of_domestic_and_foreign_banks_discontinued_rm_million_bank_asing_foreign_banks_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia': 'amount_due_to_designated_financial_institutions_residents_bank_negara_malaysia',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_commercial_banks': 'amount_due_to_designated_financial_institutions_residents_commercial_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_islamic_banks': 'amount_due_to_designated_financial_institutions_residents_islamic_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_investment_banks': 'amount_due_to_designated_financial_institutions_residents_investment_banks',  # TODO: rename
        'amount_due_to_designated_financial_institutions_residents_other_banking_institutions': 'amount_due_to_designated_financial_institutions_residents_other_banking_institutions',  # TODO: rename
        'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents': 'amount_due_to_designated_financial_institutions_bukan_pemastautin_non_residents',  # TODO: rename
        'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers': 'total_investment_account_akaun_pelaburan_dari_pengguna_investment_account_of_customers',  # TODO: rename
        'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions': 'total_investment_account_jumlah_akaun_pelaburan_yang_akan_dibayar_kepada_institusi_kewangan_tertentu_investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'total_liabilities_penerimaan_belum_bayar_acceptances_payable': 'total_liabilities_penerimaan_belum_bayar_acceptances_payable',  # TODO: rename
        'bills_payable_pemastautin_residents': 'bills_payable_pemastautin_residents',  # TODO: rename
        'total_liabilities_bills_payable_bukan_pemastautin_non_residents': 'total_liabilities_bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'total_liabilities_tanggungan_lain_other_liabilities': 'total_liabilities_tanggungan_lain_other_liabilities',  # TODO: rename
        'total_liabilities_jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities': 'total_liabilities_jumlah_ekuiti_dan_liabiliti_total_equities_and_liabilities',  # TODO: rename
    },

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities (prev)
    '1.9.3.1': {
        'capital_and_reserves': 'capital_and_reserves',  # TODO: rename
        'permintaan_demand': 'permintaan_demand',  # TODO: rename
        'tetap_fixed': 'tetap_fixed',  # TODO: rename
        'tabungan_savings': 'tabungan_savings',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_deposits_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_deposits_jumlah_total',  # TODO: rename
        'instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued': 'instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued',  # TODO: rename
        'deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds': 'deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds',  # TODO: rename
        'akaun_deposit_khas_special_deposit_account': 'akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'bank_bank_lain_other_banks': 'bank_bank_lain_other_banks',  # TODO: rename
        'syarikat_kewangan_finance_companies': 'syarikat_kewangan_finance_companies',  # TODO: rename
        'bank_saudagar_merchant_banks': 'bank_saudagar_merchant_banks',  # TODO: rename
        'di_luar_malaysia_outside_malaysia': 'di_luar_malaysia_outside_malaysia',  # TODO: rename
        'penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding': 'penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding',  # TODO: rename
        'di_malaysia_in_malaysia': 'di_malaysia_in_malaysia',  # TODO: rename
        'in_malaysia_di_luar_malaysia_outside_malaysia': 'in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'other_liabilities_di_malaysia_in_malaysia': 'other_liabilities_di_malaysia_in_malaysia',  # TODO: rename
        'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia': 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'jumlah_tanggungan_total_liabilities': 'jumlah_tanggungan_total_liabilities',  # TODO: rename
        'bank_asing_foreign_banks': 'bank_asing_foreign_banks',  # TODO: rename
        'deposits_permintaan_demand': 'deposits_permintaan_demand',  # TODO: rename
        'in_malaysia_tetap_fixed': 'in_malaysia_tetap_fixed',  # TODO: rename
        'in_malaysia_tabungan_savings': 'in_malaysia_tabungan_savings',  # TODO: rename
        'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_amounts_due_to_deposits_in_malaysia_jumlah_total': 'bank_bank_perdagangan_dan_bank_bank_islam_penyata_liabiliti_bank_tempatan_dan_bank_asing_format_terdahulu_commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_amounts_due_to_deposits_in_malaysia_jumlah_total',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued': 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_instrumen_deposit_boleh_niaga_yang_dikeluarkan_negotiable_instruments_of_deposits_issued',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds': 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_deposit_dibawah_kumpulan_wang_pelaburan_baru_deposits_under_the_new_investments_funds',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_akaun_deposit_khas_special_deposit_account': 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_akaun_deposit_khas_special_deposit_account',  # TODO: rename
        'in_malaysia_bank_bank_lain_other_banks': 'in_malaysia_bank_bank_lain_other_banks',  # TODO: rename
        'in_malaysia_syarikat_kewangan_finance_companies': 'in_malaysia_syarikat_kewangan_finance_companies',  # TODO: rename
        'in_malaysia_bank_saudagar_merchant_banks': 'in_malaysia_bank_saudagar_merchant_banks',  # TODO: rename
        'amounts_due_to_di_luar_malaysia_outside_malaysia': 'amounts_due_to_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding': 'commercial_banks_and_islamic_banks_statement_of_liabilities_of_domestic_and_foreign_banks_previous_format_penerimaan_penerimaan_jurubank_yang_belum_dijelaskan_bankers_acceptances_outstanding',  # TODO: rename
        'bills_payable_di_malaysia_in_malaysia': 'bills_payable_di_malaysia_in_malaysia',  # TODO: rename
        'bills_payable_in_malaysia_di_luar_malaysia_outside_malaysia': 'bills_payable_in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'tanggungan_lain_other_liabilities_di_malaysia_in_malaysia': 'tanggungan_lain_other_liabilities_di_malaysia_in_malaysia',  # TODO: rename
        'amounts_due_to_other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia': 'amounts_due_to_other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'rm_juta_rm_million_jumlah_tanggungan_total_liabilities': 'rm_juta_rm_million_jumlah_tanggungan_total_liabilities',  # TODO: rename
    },

    # Investment Banks: Statement of Liabilities
    '1.9.4': {
        'total_equities': 'total_equities',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'merchant_banks_investment_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others': 'merchant_banks_investment_banks_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'acceptances_payable': 'acceptances_payable',  # TODO: rename
        'residents': 'residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_equities_and_liabilities': 'total_equities_and_liabilities',  # TODO: rename
    },

    # Finance Companies: Statement of Liabilities
    '1.9.5': {
        'capital_and_reserves': 'capital_and_reserves',  # TODO: rename
        'total_deposits': 'total_deposits',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposits_account': 'special_deposits_account',  # TODO: rename
        'central_bank_of_malaysia': 'central_bank_of_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'finance_companies': 'finance_companies',  # TODO: rename
        'merchant_banks': 'merchant_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'di_luar_malaysia_outside_malaysia': 'di_luar_malaysia_outside_malaysia',  # TODO: rename
        'bankers_acceptances_outstanding': 'bankers_acceptances_outstanding',  # TODO: rename
        'di_malaysia_in_malaysia': 'di_malaysia_in_malaysia',  # TODO: rename
        'in_malaysia_di_luar_malaysia_outside_malaysia': 'in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'other_liabilities_di_malaysia_in_malaysia': 'other_liabilities_di_malaysia_in_malaysia',  # TODO: rename
        'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia': 'other_liabilities_in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'total_liabilities': 'total_liabilities',  # TODO: rename
    },

    # Finance Companies: Assets and Liabilities (prev)
    '1.9.5.1': {
        'cash': 'cash',  # TODO: rename
        'statutory_reserve_with_bnm': 'statutory_reserve_with_bnm',  # TODO: rename
        'money_at_call': 'money_at_call',  # TODO: rename
        'demand': 'demand',  # TODO: rename
        'tetap_fixed': 'tetap_fixed',  # TODO: rename
        'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_dengan_bank_deposits_with_banks_di_malaysia_in_malaysia_jumlah_total': 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_dengan_bank_deposits_with_banks_di_malaysia_in_malaysia_jumlah_total',  # TODO: rename
        'di_luar_malaysia_outside_malaysia': 'di_luar_malaysia_outside_malaysia',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'government_securities': 'government_securities',  # TODO: rename
        'subsidiary_and_other_companies': 'subsidiary_and_other_companies',  # TODO: rename
        'loans_to_financial_institutions': 'loans_to_financial_institutions',  # TODO: rename
        'hire_purchase': 'hire_purchase',  # TODO: rename
        'leasing': 'leasing',  # TODO: rename
        'housing': 'housing',  # TODO: rename
        'other_purposes': 'other_purposes',  # TODO: rename
        'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_pelannggan_lain_other_customer_jumlah_total': 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_pelannggan_lain_other_customer_jumlah_total',  # TODO: rename
        'receivables_under_refinancing': 'receivables_under_refinancing',  # TODO: rename
        'fixed_and_other_assets': 'fixed_and_other_assets',  # TODO: rename
        'total_assets_liabilities': 'total_assets_liabilities',  # TODO: rename
        'capital_and_reserves': 'capital_and_reserves',  # TODO: rename
        'deposits_of_customers_other_than_banks_tetap_fixed': 'deposits_of_customers_other_than_banks_tetap_fixed',  # TODO: rename
        'savings': 'savings',  # TODO: rename
        'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_pelanggan_selain_bank_other_customer_deposits_of_customers_other_than_banks_in_malaysia_jumlah_total': 'syarikat_kewangan_penyata_aset_dan_liabiliti_format_terdahulu_finance_companies_statement_of_assets_and_liabilities_previous_format_harta_harta_assets_deposit_pelanggan_selain_bank_other_customer_deposits_of_customers_other_than_banks_in_malaysia_jumlah_total',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'in_malaysia': 'in_malaysia',  # TODO: rename
        'in_malaysia_di_luar_malaysia_outside_malaysia': 'in_malaysia_di_luar_malaysia_outside_malaysia',  # TODO: rename
        'liabilities_under_refinancing': 'liabilities_under_refinancing',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
    },

    # Banking System: External Assets and Liabilities
    '1.9.6': {
        'amount_due_from_designated_financial_institutions': 'amount_due_from_designated_financial_institutions',  # TODO: rename
        'stock_and_shares': 'stock_and_shares',  # TODO: rename
        'investments': 'investments',  # TODO: rename
        'loans_financing_and_advances': 'loans_financing_and_advances',  # TODO: rename
        'other_external_assets': 'other_external_assets',  # TODO: rename
        'banking_system_external_assets_and_external_liabilities_rm_million_total_external_assets_total': 'banking_system_external_assets_and_external_liabilities_rm_million_total_external_assets_total',  # TODO: rename
        'amount_due_to_designated_financial_institutions': 'amount_due_to_designated_financial_institutions',  # TODO: rename
        'deposits_accepted': 'deposits_accepted',  # TODO: rename
        'bills_payable': 'bills_payable',  # TODO: rename
        'other_external_liabilities': 'other_external_liabilities',  # TODO: rename
        'banking_system_external_assets_and_external_liabilities_rm_million_total_external_liabilities_total': 'banking_system_external_assets_and_external_liabilities_rm_million_total_external_liabilities_total',  # TODO: rename
        'net_external_liabilities': 'net_external_liabilities',  # TODO: rename
    },

    # Banking System: Capital and Liabilities (prev)
    '1.9a': {
        'equities_and_liabilities': 'equities_and_liabilities',  # TODO: rename
        'total_equities': 'total_equities',  # TODO: rename
        'deposits_under_the_new_investment_fund': 'deposits_under_the_new_investment_fund',  # TODO: rename
        'special_deposit_account': 'special_deposit_account',  # TODO: rename
        'banking_system_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others': 'banking_system_statement_of_equities_and_liabilities_discontinued_rm_million_total_liabilities_total_deposits_lain_lain_others',  # TODO: rename
        'bank_negara_malaysia': 'bank_negara_malaysia',  # TODO: rename
        'commercial_banks': 'commercial_banks',  # TODO: rename
        'islamic_banks': 'islamic_banks',  # TODO: rename
        'investment_banks': 'investment_banks',  # TODO: rename
        'other_banking_institutions': 'other_banking_institutions',  # TODO: rename
        'bukan_pemastautin_non_residents': 'bukan_pemastautin_non_residents',  # TODO: rename
        'investment_account_of_customers': 'investment_account_of_customers',  # TODO: rename
        'investment_account_due_to_designated_financial_institutions': 'investment_account_due_to_designated_financial_institutions',  # TODO: rename
        'acceptances_payable': 'acceptances_payable',  # TODO: rename
        'residents': 'residents',  # TODO: rename
        'bills_payable_bukan_pemastautin_non_residents': 'bills_payable_bukan_pemastautin_non_residents',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
        'total_equities_and_liabilities': 'total_equities_and_liabilities',  # TODO: rename
    },

    # Interest Rates: Banking Institutions
    '2.1': {
        'interest_rates_banking_institutions': 'interest_rates_banking_institutions',  # TODO: rename
        'fixed_deposit_rates_period_in_months': 'fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'weighted_average_fixed_deposit_rates_period_in_months': 'weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_commercial_banks_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'savings_deposit_rate': 'savings_deposit_rate',  # TODO: rename
        'weighted_average_savings_deposit_rate': 'weighted_average_savings_deposit_rate',  # TODO: rename
        'base_rate2_br': 'base_rate2_br',  # TODO: rename
        'weighted_average_br': 'weighted_average_br',  # TODO: rename
        'base_lending_rate_blr': 'base_lending_rate_blr',  # TODO: rename
        'weighted_average_blr': 'weighted_average_blr',  # TODO: rename
        'kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans': 'kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans',  # TODO: rename
        'weighted_alr_on_outstanding_loans': 'weighted_alr_on_outstanding_loans',  # TODO: rename
        'investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_1': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_1',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_2': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_investment_banks_kadar_deposit_tetap_fixed_deposit_rates_period_in_months_2',  # TODO: rename
        'percent_per_annum_kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans': 'percent_per_annum_kadar_pinjaman_purata_bagi_pinjaman_terkumpul_average_lending_rate_alr_on_outstanding_loans',  # TODO: rename
    },

    # Funds Raised in Capital Market (by Private Sector)
    '2.10': {
        'initial_public_offers': 'initial_public_offers',  # TODO: rename
        'rights_issues': 'rights_issues',  # TODO: rename
        'restricted_offer_for_sale': 'restricted_offer_for_sale',  # TODO: rename
        'special_issues': 'special_issues',  # TODO: rename
        'preference_shares': 'preference_shares',  # TODO: rename
        'warrants': 'warrants',  # TODO: rename
        'new_issues_of_shares_war_rants': 'new_issues_of_shares_war_rants',  # TODO: rename
        'straight_bonds': 'straight_bonds',  # TODO: rename
        'bonds_with_war_rants': 'bonds_with_war_rants',  # TODO: rename
        'conver_tible_bonds': 'conver_tible_bonds',  # TODO: rename
        'islamic_bonds': 'islamic_bonds',  # TODO: rename
        'asset_backed_bonds': 'asset_backed_bonds',  # TODO: rename
        'medium_term_notes': 'medium_term_notes',  # TODO: rename
        'bon_cagamas_cagamas_bonds': 'bon_cagamas_cagamas_bonds',  # TODO: rename
        'new_issues_of_corporate_bond_and_or_sukuk': 'new_issues_of_corporate_bond_and_or_sukuk',  # TODO: rename
        'corporate_bond_and_or_sukuk': 'corporate_bond_and_or_sukuk',  # TODO: rename
        'redemptions_bon_cagamas_cagamas_bonds': 'redemptions_bon_cagamas_cagamas_bonds',  # TODO: rename
        'net_issues_of_corporate_bond_and_or_sukuk': 'net_issues_of_corporate_bond_and_or_sukuk',  # TODO: rename
        'net_funds_raised_by_the_private_sector': 'net_funds_raised_by_the_private_sector',  # TODO: rename
    },

    # New Issues of Corporate Bond and/or Sukuk
    '2.11': {
        'agriculture_foresty_and_fishing': 'agriculture_foresty_and_fishing',  # TODO: rename
        'construction': 'construction',  # TODO: rename
        'electricity_gas_and_water': 'electricity_gas_and_water',  # TODO: rename
        'finance_insurance_real_estate_and_business_services': 'finance_insurance_real_estate_and_business_services',  # TODO: rename
        'government_and_other_services': 'government_and_other_services',  # TODO: rename
        'manufacturing': 'manufacturing',  # TODO: rename
        'mining_and_quarrying': 'mining_and_quarrying',  # TODO: rename
        'transport_storage_and_communications': 'transport_storage_and_communications',  # TODO: rename
        'wholesale_retail_trade_hotels_and_restaurants': 'wholesale_retail_trade_hotels_and_restaurants',  # TODO: rename
        'terbitan_baru_bon_korporat_dan_atau_sukuk1_kecuali_bon_cagamas_mengikut_sektor_new_issues_of_corporate_bond_and_or_sukuk1_excluding_cagamas_bonds_by_sector_rm_million_jumlah_total': 'terbitan_baru_bon_korporat_dan_atau_sukuk1_kecuali_bon_cagamas_mengikut_sektor_new_issues_of_corporate_bond_and_or_sukuk1_excluding_cagamas_bonds_by_sector_rm_million_jumlah_total',  # TODO: rename
    },

    # Turnover of Conventional and Islamic Money Market
    '2.14': {
        'antara_bank_interbank': 'antara_bank_interbank',  # TODO: rename
        'korporat_corporate': 'korporat_corporate',  # TODO: rename
        'banker_s_acceptance_antara_bank_interbank': 'banker_s_acceptance_antara_bank_interbank',  # TODO: rename
        'banker_s_acceptance_korporat_corporate': 'banker_s_acceptance_korporat_corporate',  # TODO: rename
        'negotiable_instrument_of_deposit_antara_bank_interbank': 'negotiable_instrument_of_deposit_antara_bank_interbank',  # TODO: rename
        'negotiable_instrument_of_deposit_korporat_corporate': 'negotiable_instrument_of_deposit_korporat_corporate',  # TODO: rename
        'mudharabah_deposits_antara_bank_interbank': 'mudharabah_deposits_antara_bank_interbank',  # TODO: rename
        'mudharabah_deposits_korporat_corporate': 'mudharabah_deposits_korporat_corporate',  # TODO: rename
        'commodity_murabahah_deposits_antara_bank_interbank': 'commodity_murabahah_deposits_antara_bank_interbank',  # TODO: rename
        'commodity_murabahah_deposits_korporat_corporate': 'commodity_murabahah_deposits_korporat_corporate',  # TODO: rename
        'wakalah_deposits_antara_bank_interbank': 'wakalah_deposits_antara_bank_interbank',  # TODO: rename
        'wakalah_deposits_korporat_corporate': 'wakalah_deposits_korporat_corporate',  # TODO: rename
        'other_deposit_antara_bank_interbank': 'other_deposit_antara_bank_interbank',  # TODO: rename
        'other_deposit_korporat_corporate': 'other_deposit_korporat_corporate',  # TODO: rename
        'islamic_bankers_acceptance_antara_bank_interbank': 'islamic_bankers_acceptance_antara_bank_interbank',  # TODO: rename
        'islamic_bankers_acceptance_korporat_corporate': 'islamic_bankers_acceptance_korporat_corporate',  # TODO: rename
        'islamic_negotiable_instrument_of_deposit_antara_bank_interbank': 'islamic_negotiable_instrument_of_deposit_antara_bank_interbank',  # TODO: rename
        'rm_million_equivalent_korporat_corporate': 'rm_million_equivalent_korporat_corporate',  # TODO: rename
    },

    # Turnover of Derivatives Transactions
    '2.15': {
        'warrants': 'warrants',  # TODO: rename
        'opsyen_options': 'opsyen_options',  # TODO: rename
        'klibor_futures': 'klibor_futures',  # TODO: rename
        'swap': 'swap',  # TODO: rename
        'interest_rate_related_opsyen_options': 'interest_rate_related_opsyen_options',  # TODO: rename
        'futures': 'futures',  # TODO: rename
        'credit_default_swap': 'credit_default_swap',  # TODO: rename
        'pusing_ganti_derivatif_turnover_of_derivatives_transactions_konvensional_conventional_lain_lain_others': 'pusing_ganti_derivatif_turnover_of_derivatives_transactions_konvensional_conventional_lain_lain_others',  # TODO: rename
        'profit_rate_swap': 'profit_rate_swap',  # TODO: rename
    },

    # Turnover of Debt Securities and Sukuk
    '2.16': {
        'turnover_of_debt_securities_and_sukuk': 'turnover_of_debt_securities_and_sukuk',  # TODO: rename
        'bank_negara_monetary_note': 'bank_negara_monetary_note',  # TODO: rename
        'malaysian_treasury_bills': 'malaysian_treasury_bills',  # TODO: rename
        'malaysian_government_securities': 'malaysian_government_securities',  # TODO: rename
        'bank_negara_monetary_note_islamic': 'bank_negara_monetary_note_islamic',  # TODO: rename
        'malaysian_islamic_treasury_bills': 'malaysian_islamic_treasury_bills',  # TODO: rename
        'government_investment_issues': 'government_investment_issues',  # TODO: rename
        'government_housing_sukuk': 'government_housing_sukuk',  # TODO: rename
        'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_conventional_jumlah_total': 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_conventional_jumlah_total',  # TODO: rename
        'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_sukuk_jumlah_total': 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_private_sector_sukuk_jumlah_total',  # TODO: rename
        'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_rm_million_equivalent_jumlah_total': 'pusing_ganti_sekuriti_hutang_dan_sukuk_turnover_of_debt_securities_and_sukuk_rm_million_equivalent_jumlah_total',  # TODO: rename
    },

    # Turnover of Foreign Currency Market Transactions
    '2.17': {
        'fx_spot': 'fx_spot',  # TODO: rename
        'fx_swap': 'fx_swap',  # TODO: rename
        'fx_forward': 'fx_forward',  # TODO: rename
        'fx_options': 'fx_options',  # TODO: rename
    },

    # Credit to the Private Non-Financial Sector
    '2.18': {
        'outstanding_rm_million': 'outstanding_rm_million',  # TODO: rename
        'of_which_household_a': 'of_which_household_a',  # TODO: rename
        'of_which_business_b': 'of_which_business_b',  # TODO: rename
        'credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c': 'credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c',  # TODO: rename
        'total_credit_to_the_private_non_financial_sector_total_a_b_c': 'total_credit_to_the_private_non_financial_sector_total_a_b_c',  # TODO: rename
        'of_which_credit_to_businesses_b_c': 'of_which_credit_to_businesses_b_c',  # TODO: rename
        'annual_growth': 'annual_growth',  # TODO: rename
        'outstanding_loans_to_the_private_non_financial_sector_of_which_household_a': 'outstanding_loans_to_the_private_non_financial_sector_of_which_household_a',  # TODO: rename
        'outstanding_loans_to_the_private_non_financial_sector_of_which_business_b': 'outstanding_loans_to_the_private_non_financial_sector_of_which_business_b',  # TODO: rename
        'kredit_kepada_sektor_swasta_bukan_kewangan_credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c': 'kredit_kepada_sektor_swasta_bukan_kewangan_credit_to_the_private_non_financial_sector_outstanding_corporate_bonds_issued_by_the_private_non_financial_sector_c',  # TODO: rename
        'credit_to_the_private_non_financial_sector_total_credit_to_the_private_non_financial_sector_total_a_b_c': 'credit_to_the_private_non_financial_sector_total_credit_to_the_private_non_financial_sector_total_a_b_c',  # TODO: rename
        'total_credit_to_the_private_non_financial_sector_of_which_credit_to_businesses_b_c': 'total_credit_to_the_private_non_financial_sector_of_which_credit_to_businesses_b_c',  # TODO: rename
    },

    # Net Financing through Banking, DFIs and Corporate Bonds (prev)
    '2.18a': {
        'outstanding_rm_million': 'outstanding_rm_million',  # TODO: rename
        'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds': 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds',  # TODO: rename
        'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing': 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing',  # TODO: rename
        'monthly_change_rm_million': 'monthly_change_rm_million',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing',  # TODO: rename
        'pertumbuhan_tahunan_annual_growth': 'pertumbuhan_tahunan_annual_growth',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds_1': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_corporate_bonds_1',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_1': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_1',  # TODO: rename
        'net_financing_pertumbuhan_tahunan_annual_growth': 'net_financing_pertumbuhan_tahunan_annual_growth',  # TODO: rename
        'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth': 'net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_1': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_1',  # TODO: rename
        'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_2': 'pembiayaan_bersih_melalui_sistem_perbankan_institusi_kewangan_pembangunan_ikp_dan_bon_korporat_net_financing_through_the_banking_system_development_financial_institutions_dfis_and_corporate_bonds_cb_net_financing_pertumbuhan_tahunan_annual_growth_2',  # TODO: rename
    },

    # Interest Rates: Banking Institutions (prev)
    '2.1a': {
        'interest_rates_banking_institutions_discontinued': 'interest_rates_banking_institutions_discontinued',  # TODO: rename
        'tempoh_dalam_bulan_period_in_months': 'tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'fixed_deposits_tempoh_dalam_bulan_period_in_months': 'fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'interest_rates_banking_institutions_discontinued_commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'interest_rates_banking_institutions_discontinued_commercial_banks_deposit_tetap1_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'savings_deposit': 'savings_deposit',  # TODO: rename
        'weighted_base_rate': 'weighted_base_rate',  # TODO: rename
        'base_lending_rate': 'base_lending_rate',  # TODO: rename
        'kadar_berian_pinjaman_purata2_average_lending_rate': 'kadar_berian_pinjaman_purata2_average_lending_rate',  # TODO: rename
        'weighted_average_lending_rate': 'weighted_average_lending_rate',  # TODO: rename
        'deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months',  # TODO: rename
        'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months_1': 'kadar_faedah_institusi_perbankan_interest_rates_banking_institutions_discontinued_investment_banks_deposit_tetap_fixed_deposits_tempoh_dalam_bulan_period_in_months_1',  # TODO: rename
        'kadar_berian_pinjaman_purata_average_lending_rate': 'kadar_berian_pinjaman_purata_average_lending_rate',  # TODO: rename
    },

    # Islamic Banking: Financing and Profit Rates
    '2.2': {
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders',  # TODO: rename
        'fixed_deposit_rates_period_in_months': 'fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'weighted_average_fixed_deposit_rates_period_in_months': 'weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_kadar_deposit_tetap_purata_berwajaran_weighted_average_fixed_deposit_rates_period_in_months',  # TODO: rename
        'investment_account_period_in_months': 'investment_account_period_in_months',  # TODO: rename
        'akaun_pelaburan_investment_account_period_in_months': 'akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'savings_deposit_rate': 'savings_deposit_rate',  # TODO: rename
        'weighted_average_savings_deposit_rate': 'weighted_average_savings_deposit_rate',  # TODO: rename
        'base_rate': 'base_rate',  # TODO: rename
        'weighted_average_base_rate_br': 'weighted_average_base_rate_br',  # TODO: rename
        'base_financing_rate': 'base_financing_rate',  # TODO: rename
        'weighted_average_base_financing_rate_bfr': 'weighted_average_base_financing_rate_bfr',  # TODO: rename
        'average_financing_rate_on_outstanding_financing': 'average_financing_rate_on_outstanding_financing',  # TODO: rename
        'weighted_average_financing_rate_afr_on_outstanding_financing': 'weighted_average_financing_rate_afr_on_outstanding_financing',  # TODO: rename
        'investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months': 'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_bank_bank_pelaburan_spi_investment_banks_ibs_kadar_deposit_tetap_fixed_deposit_rates_period_in_months',  # TODO: rename
        'percent_per_annum': 'percent_per_annum',  # TODO: rename
    },

    # Islamic Banking: Financing and Profit Rates (prev)
    '2.2a': {
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued',  # TODO: rename
        'investment_deposit_tawarruq_fixed_deposits_period_in_months': 'investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'investment_account_period_in_months': 'investment_account_period_in_months',  # TODO: rename
        'akaun_pelaburan_investment_account_period_in_months': 'akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_islam_dan_bank_bank_perdagangan_spi_islamic_banks_and_commercial_banks_ibs_akaun_pelaburan_investment_account_period_in_months',  # TODO: rename
        'savings_deposit': 'savings_deposit',  # TODO: rename
        'base_rate': 'base_rate',  # TODO: rename
        'base_financing_rate': 'base_financing_rate',  # TODO: rename
        'average_financing_rate': 'average_financing_rate',  # TODO: rename
        'investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months': 'sistem_perbankan_islam_kadar_pembiayaan_kadar_keuntungan_kepada_pendeposit_dan_kadar_pulangan_kepada_pemegang_akaun_pelaburan_islamic_banking_system_financing_rate_profit_rate_to_depositors_and_rate_of_return_to_investment_account_holders_discontinued_bank_bank_pelaburan_spi_investment_banks_ibs_deposit_pelaburan_deposit_tetap_tawarruq_investment_deposit_tawarruq_fixed_deposits_period_in_months',  # TODO: rename
        'percent_per_annum': 'percent_per_annum',  # TODO: rename
    },

    # Interest Rates: Interbank Money Market
    '2.3': {
        'tempoh_period_1': 'tempoh_period_1',  # TODO: rename
        'interest_rates_interbank_money_market': 'interest_rates_interbank_money_market',  # TODO: rename
        'as_at_period_end': 'as_at_period_end',  # TODO: rename
        'julat_range': 'julat_range',  # TODO: rename
        'overnight_money_julat_range': 'overnight_money_julat_range',  # TODO: rename
        'wang_semalaman_overnight_money_julat_range': 'wang_semalaman_overnight_money_julat_range',  # TODO: rename
        'purata_avg': 'purata_avg',  # TODO: rename
        '1_week_julat_range': '1_week_julat_range',  # TODO: rename
        '1_minggu_1_week_julat_range': '1_minggu_1_week_julat_range',  # TODO: rename
        'weighted_average_interbank_rates_1_minggu_1_week_julat_range': 'weighted_average_interbank_rates_1_minggu_1_week_julat_range',  # TODO: rename
        '1_week_purata_avg': '1_week_purata_avg',  # TODO: rename
        '1_month_julat_range': '1_month_julat_range',  # TODO: rename
        '1_bulan_1_month_julat_range': '1_bulan_1_month_julat_range',  # TODO: rename
        'weighted_average_interbank_rates_1_bulan_1_month_julat_range': 'weighted_average_interbank_rates_1_bulan_1_month_julat_range',  # TODO: rename
        '1_month_purata_avg': '1_month_purata_avg',  # TODO: rename
        '3_month_julat_range': '3_month_julat_range',  # TODO: rename
        '3_bulan_3_month_julat_range': '3_bulan_3_month_julat_range',  # TODO: rename
        'weighted_average_interbank_rates_3_bulan_3_month_julat_range': 'weighted_average_interbank_rates_3_bulan_3_month_julat_range',  # TODO: rename
        '3_month_purata_avg': '3_month_purata_avg',  # TODO: rename
        '6_month_julat_range': '6_month_julat_range',  # TODO: rename
        '6_bulan_6_month_julat_range': '6_bulan_6_month_julat_range',  # TODO: rename
        'weighted_average_interbank_rates_6_bulan_6_month_julat_range': 'weighted_average_interbank_rates_6_bulan_6_month_julat_range',  # TODO: rename
        '6_month_purata_avg': '6_month_purata_avg',  # TODO: rename
        '12_month_julat_range': '12_month_julat_range',  # TODO: rename
        '12_bulan_12_month_julat_range': '12_bulan_12_month_julat_range',  # TODO: rename
        'weighted_average_interbank_rates_12_bulan_12_month_julat_range': 'weighted_average_interbank_rates_12_bulan_12_month_julat_range',  # TODO: rename
        'percent_per_annum_purata_avg': 'percent_per_annum_purata_avg',  # TODO: rename
        '12_month_purata_avg': '12_month_purata_avg',  # TODO: rename
    },

    # Interest Rates: Treasury Bills and Bank Negara Bills
    '2.4': {
        'interest_rates_treasury_bills_and_bank_negara_bills': 'interest_rates_treasury_bills_and_bank_negara_bills',  # TODO: rename
        'average_discount_rate_on_treasury_bills_period_in_months': 'average_discount_rate_on_treasury_bills_period_in_months',  # TODO: rename
        'kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months': 'kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months',  # TODO: rename
        'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months': 'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months',  # TODO: rename
        'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months': 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_perbendaharaan_average_discount_rate_on_treasury_bills_period_in_months',  # TODO: rename
        'average_discount_rate_on_bank_negara_bills_period_in_months': 'average_discount_rate_on_bank_negara_bills_period_in_months',  # TODO: rename
        'kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months': 'kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months',  # TODO: rename
        'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months': 'interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months',  # TODO: rename
        'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months': 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months',  # TODO: rename
        'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months_1': 'kadar_faedah_bil_perbendaharaan_dan_bil_bank_negara_interest_rates_treasury_bills_and_bank_negara_bills_kadar_diskaun_purata_bil_bank_negara_average_discount_rate_on_bank_negara_bills_period_in_months_1',  # TODO: rename
        'percent_per_annum': 'percent_per_annum',  # TODO: rename
    },

    # Treasury Bills, MGS and Khazanah Bonds: Tender Results
    '2.4.1': {
    },

    # Market Indicative Yield: Malaysian Government Securities
    '2.5': {
        'market_indicative_yield1_malaysian_government_securities': 'market_indicative_yield1_malaysian_government_securities',  # TODO: rename
        'market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity': 'market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_1': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_1',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_2': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_2',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_3': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_3',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_4': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_4',  # TODO: rename
        'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_5': 'hasil_indikatif_pasaran1_sekuriti_kerajaan_malaysia_market_indicative_yield1_malaysian_government_securities_tahun_sebelum_kematangan_remaining_years_to_maturity_5',  # TODO: rename
        'percent_per_annum': 'percent_per_annum',  # TODO: rename
    },

    # Exchange Rates: Malaysian Ringgit
    '2.6': {
        'exchange_rates_malaysian_ringgit': 'exchange_rates_malaysian_ringgit',  # TODO: rename
        'end_of_period': 'end_of_period',  # TODO: rename
        'rm_per_unit_of_usd': 'rm_per_unit_of_usd',  # TODO: rename
        'rm_per_unit_of_gbp': 'rm_per_unit_of_gbp',  # TODO: rename
        'rm_per_unit_of_euro': 'rm_per_unit_of_euro',  # TODO: rename
        'rm_per_unit_of_100_sf': 'rm_per_unit_of_100_sf',  # TODO: rename
        'rm_per_unit_of_100_hkd': 'rm_per_unit_of_100_hkd',  # TODO: rename
        'rm_per_unit_of_100_jpy': 'rm_per_unit_of_100_jpy',  # TODO: rename
        'rm_per_unit_of_cny': 'rm_per_unit_of_cny',  # TODO: rename
        'rm_per_unit_of_sgd': 'rm_per_unit_of_sgd',  # TODO: rename
        'rm_per_unit_of_100_idr': 'rm_per_unit_of_100_idr',  # TODO: rename
        'rm_per_unit_of_100_thb': 'rm_per_unit_of_100_thb',  # TODO: rename
        'average_for_period': 'average_for_period',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_usd': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_usd',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_gbp': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_gbp',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_euro': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_euro',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_sf': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_sf',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_hkd': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_hkd',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_jpy': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_jpy',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_cny': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_cny',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_sgd': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_sgd',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_idr': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_idr',  # TODO: rename
        'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_thb': 'exchange_rates_malaysian_ringgit_rm_per_unit_of_100_thb',  # TODO: rename
    },

    # Exchange Rates: Malaysian Ringgit (Daily)
    '2.6.1': {
        'tempoh_period_1': 'tempoh_period_1',  # TODO: rename
        'june': 'june',  # TODO: rename
        'sdr': 'sdr',  # TODO: rename
        'end_of_period': 'end_of_period',  # TODO: rename
        'gbp': 'gbp',  # TODO: rename
        'eur': 'eur',  # TODO: rename
        'sf': 'sf',  # TODO: rename
        '100_hkd': '100_hkd',  # TODO: rename
        '100_jpy': '100_jpy',  # TODO: rename
        'cny': 'cny',  # TODO: rename
        'sgd': 'sgd',  # TODO: rename
        '100_idr': '100_idr',  # TODO: rename
        '100_thb': '100_thb',  # TODO: rename
    },

    # Volume of Transaction in Interbank Money Market
    '2.7': {
        'volume_of_transactions_in_interbank_money_market': 'volume_of_transactions_in_interbank_money_market',  # TODO: rename
        'overnight': 'overnight',  # TODO: rename
        'weekend': 'weekend',  # TODO: rename
        '1_week': '1_week',  # TODO: rename
        '1_month': '1_month',  # TODO: rename
        '2_months': '2_months',  # TODO: rename
        '3_months': '3_months',  # TODO: rename
        '6_months': '6_months',  # TODO: rename
        '1_year': '1_year',  # TODO: rename
        'jumlah_dana_diniagakan_dalam_pasaran_wang_antara_bank_volume_of_transactions_in_interbank_money_market_deposit_antara_bank_interbank_deposit_lain_lain_others': 'jumlah_dana_diniagakan_dalam_pasaran_wang_antara_bank_volume_of_transactions_in_interbank_money_market_deposit_antara_bank_interbank_deposit_lain_lain_others',  # TODO: rename
        'jumlah_kecil_sub_total': 'jumlah_kecil_sub_total',  # TODO: rename
        'malaysian_government_securities': 'malaysian_government_securities',  # TODO: rename
        'khazanah_bonds': 'khazanah_bonds',  # TODO: rename
        'cagamas_bonds': 'cagamas_bonds',  # TODO: rename
        'malaysian_treasury_bills': 'malaysian_treasury_bills',  # TODO: rename
        'bank_negara_bills': 'bank_negara_bills',  # TODO: rename
        'cagamas_notes': 'cagamas_notes',  # TODO: rename
        'negotiable_instrument_of_deposit': 'negotiable_instrument_of_deposit',  # TODO: rename
        'banker_s_acceptance': 'banker_s_acceptance',  # TODO: rename
        'money_market_instrument_jumlah_kecil_sub_total': 'money_market_instrument_jumlah_kecil_sub_total',  # TODO: rename
        'grand_total': 'grand_total',  # TODO: rename
    },

    # Volume of Interbank Transactions in KL FX Market
    '2.8': {
        'usd_rm_spot': 'usd_rm_spot',  # TODO: rename
        'usd_rm_swap': 'usd_rm_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_rm_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_rm_jumlah_total',  # TODO: rename
        'usd_sgd_spot': 'usd_sgd_spot',  # TODO: rename
        'usd_sgd_swap': 'usd_sgd_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_sgd_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_sgd_jumlah_total',  # TODO: rename
        'usd_jpy_spot': 'usd_jpy_spot',  # TODO: rename
        'usd_jpy_swap': 'usd_jpy_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_jpy_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_usd_jpy_jumlah_total',  # TODO: rename
        'gbp_usd_spot': 'gbp_usd_spot',  # TODO: rename
        'gbp_usd_swap': 'gbp_usd_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_gbp_usd_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_gbp_usd_jumlah_total',  # TODO: rename
        'eur_usd_spot': 'eur_usd_spot',  # TODO: rename
        'eur_usd_swap': 'eur_usd_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_eur_usd_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_eur_usd_jumlah_total',  # TODO: rename
        'usd_chf_spot': 'usd_chf_spot',  # TODO: rename
        'usd_chf_swap': 'usd_chf_swap',  # TODO: rename
        'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_rm_juta_rm_million_jumlah_total': 'jumlah_urus_niaga_antara_bank_dalam_pasaran_pertukaran_asing_kuala_lumpur_volume_of_interbank_transactions_in_the_kuala_lumpur_foreign_exchange_market_rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Funds Raised in Capital Market (by Public Sector)
    '2.9': {
        'funds_raised_in_the_capital_market_by_public_sector': 'funds_raised_in_the_capital_market_by_public_sector',  # TODO: rename
        'malaysian_government_securities_mgs': 'malaysian_government_securities_mgs',  # TODO: rename
        'mgs_advanced_subscriptions': 'mgs_advanced_subscriptions',  # TODO: rename
        'khazanah_bonds_kb': 'khazanah_bonds_kb',  # TODO: rename
        'malaysian_government_investment_issues_mgii': 'malaysian_government_investment_issues_mgii',  # TODO: rename
        'bon_simpanan_savings_bonds': 'bon_simpanan_savings_bonds',  # TODO: rename
        'sukuk_perumahan_kerajaan_government_housing_sukuk': 'sukuk_perumahan_kerajaan_government_housing_sukuk',  # TODO: rename
        'new_issues_of_debt_securities': 'new_issues_of_debt_securities',  # TODO: rename
        'mgs': 'mgs',  # TODO: rename
        'kb': 'kb',  # TODO: rename
        'mgii': 'mgii',  # TODO: rename
        'redemptions_bon_simpanan_savings_bonds': 'redemptions_bon_simpanan_savings_bonds',  # TODO: rename
        'redemptions_sukuk_perumahan_kerajaan_government_housing_sukuk': 'redemptions_sukuk_perumahan_kerajaan_government_housing_sukuk',  # TODO: rename
        'less_government_holdings': 'less_government_holdings',  # TODO: rename
        'net_funds_raised_by_the_public_sector': 'net_funds_raised_by_the_public_sector',  # TODO: rename
    },

    # Federal Government Finance
    '3.1': {
        'federal_government_finance': 'federal_government_finance',  # TODO: rename
        'revenue': 'revenue',  # TODO: rename
        'operating_expenditure': 'operating_expenditure',  # TODO: rename
        'kurangan_deficit': 'kurangan_deficit',  # TODO: rename
        'gross_development_expenditure': 'gross_development_expenditure',  # TODO: rename
        'less_loan_recoveries': 'less_loan_recoveries',  # TODO: rename
        'net_development_expenditure': 'net_development_expenditure',  # TODO: rename
        'covid_19_fund': 'covid_19_fund',  # TODO: rename
        'kurangan_keseluruhan_deficit': 'kurangan_keseluruhan_deficit',  # TODO: rename
        'gross_domestic_borrowing': 'gross_domestic_borrowing',  # TODO: rename
        'less_domestic_repayment': 'less_domestic_repayment',  # TODO: rename
        'net_domestic_borrowing': 'net_domestic_borrowing',  # TODO: rename
        'gross_foreign_borrowing': 'gross_foreign_borrowing',  # TODO: rename
        'less_foreign_repayment': 'less_foreign_repayment',  # TODO: rename
        'net_foreign_borrowing': 'net_foreign_borrowing',  # TODO: rename
        'use_of_assets': 'use_of_assets',  # TODO: rename
    },

    # Federal Government Revenue
    '3.1.1': {
        'hasil_kerajaan_persekutuan_federal_government_revenue_jumlah_total': 'hasil_kerajaan_persekutuan_federal_government_revenue_jumlah_total',  # TODO: rename
        'jumlah_kecil_sub_total': 'jumlah_kecil_sub_total',  # TODO: rename
        'companies_income_tax': 'companies_income_tax',  # TODO: rename
        'petroleum_income_tax': 'petroleum_income_tax',  # TODO: rename
        'individuals_income_tax': 'individuals_income_tax',  # TODO: rename
        'stamp_duties': 'stamp_duties',  # TODO: rename
        'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_langsung_direct_taxes_lain_lain_others': 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_langsung_direct_taxes_lain_lain_others',  # TODO: rename
        'indirect_taxes_jumlah_kecil_sub_total': 'indirect_taxes_jumlah_kecil_sub_total',  # TODO: rename
        'export_duties': 'export_duties',  # TODO: rename
        'import_duties': 'import_duties',  # TODO: rename
        'excise_duties': 'excise_duties',  # TODO: rename
        'goods_and_services_tax': 'goods_and_services_tax',  # TODO: rename
        'sales_tax': 'sales_tax',  # TODO: rename
        'service_tax': 'service_tax',  # TODO: rename
        'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_tidak_langsung_indirect_taxes_lain_lain_others': 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_cukai_tax_revenue_cukai_tidak_langsung_indirect_taxes_lain_lain_others',  # TODO: rename
        'non_tax_revenue_jumlah_kecil_sub_total': 'non_tax_revenue_jumlah_kecil_sub_total',  # TODO: rename
        'licences_and_permits': 'licences_and_permits',  # TODO: rename
        'petroleum_royalty': 'petroleum_royalty',  # TODO: rename
        'interest_and_returns_on_investment': 'interest_and_returns_on_investment',  # TODO: rename
        'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_bukan_cukai_tax_revenue_non_tax_revenue_indirect_taxes_lain_lain_others': 'hasil_kerajaan_persekutuan_federal_government_revenue_hasil_bukan_cukai_tax_revenue_non_tax_revenue_indirect_taxes_lain_lain_others',  # TODO: rename
        'non_revenue_receipts': 'non_revenue_receipts',  # TODO: rename
    },

    # Federal Government Operating Expenditure by Object
    '3.1.2': {
        'perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_jumlah_total': 'perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_jumlah_total',  # TODO: rename
        'emoluments': 'emoluments',  # TODO: rename
        'retirement_charges': 'retirement_charges',  # TODO: rename
        'perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_bayaran_khidmat_hutang_debt_service_charges_jumlah_total': 'perbelanjaan_mengurus_kerajaan_persekutuan_mengikut_objek¹_federal_government_operating_expenditure_by_object¹_bayaran_khidmat_hutang_debt_service_charges_jumlah_total',  # TODO: rename
        'domestic': 'domestic',  # TODO: rename
        'external': 'external',  # TODO: rename
        'supplies_and_services': 'supplies_and_services',  # TODO: rename
        'subsidies_and_social_assistance': 'subsidies_and_social_assistance',  # TODO: rename
        'asset_acquisition': 'asset_acquisition',  # TODO: rename
        'grants_and_transfers': 'grants_and_transfers',  # TODO: rename
        'other_expenditure': 'other_expenditure',  # TODO: rename
    },

    # Federal Government Development Expenditure
    '3.1.3': {
        'perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_jumlah_total': 'perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_jumlah_total',  # TODO: rename
        'defence_and_security': 'defence_and_security',  # TODO: rename
        'jumlah_kecil_sub_total': 'jumlah_kecil_sub_total',  # TODO: rename
        'agriculture_and_rural_development': 'agriculture_and_rural_development',  # TODO: rename
        'trade_and_industry': 'trade_and_industry',  # TODO: rename
        'transport': 'transport',  # TODO: rename
        'public_utilities': 'public_utilities',  # TODO: rename
        'perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_perkhidmatan_ekonomi_economic_services_lain_lain_others': 'perbelanjaan_pembangunan_kerajaan_persekutuan_pengkelasan_mengikut_fungsi_federal_government_development_expenditure_a_functional_classification_perkhidmatan_ekonomi_economic_services_lain_lain_others',  # TODO: rename
        'social_services_jumlah_kecil_sub_total': 'social_services_jumlah_kecil_sub_total',  # TODO: rename
        'education': 'education',  # TODO: rename
        'health': 'health',  # TODO: rename
        'housing': 'housing',  # TODO: rename
        'social_and_community_services': 'social_and_community_services',  # TODO: rename
        'general_administration': 'general_administration',  # TODO: rename
    },

    # Federal Government Debt by Remaining Maturity
    '3.1.4': {
        'hutang_kerajaan_persekutuan_pengkelasan_mengikut_tempoh_baki_matang_federal_government_debt_classification_by_remaining_maturity_jumlah_total': 'hutang_kerajaan_persekutuan_pengkelasan_mengikut_tempoh_baki_matang_federal_government_debt_classification_by_remaining_maturity_jumlah_total',  # TODO: rename
        'jumlah_kecil_sub_total': 'jumlah_kecil_sub_total',  # TODO: rename
        'treasury_bills': 'treasury_bills',  # TODO: rename
        'malaysian_government_investment_issues_jumlah_kecil_sub_total': 'malaysian_government_investment_issues_jumlah_kecil_sub_total',  # TODO: rename
        'kurang_dari_3_tahun_less_than_3_years': 'kurang_dari_3_tahun_less_than_3_years',  # TODO: rename
        '5_tahun_5_years': '5_tahun_5_years',  # TODO: rename
        '10_tahun_10_years': '10_tahun_10_years',  # TODO: rename
        '15_tahun_15_years': '15_tahun_15_years',  # TODO: rename
        'malaysian_government_investment_issues_15_tahun_15_years': 'malaysian_government_investment_issues_15_tahun_15_years',  # TODO: rename
        'malaysian_government_securities_jumlah_kecil_sub_total': 'malaysian_government_securities_jumlah_kecil_sub_total',  # TODO: rename
        'malaysian_government_securities_kurang_dari_3_tahun_less_than_3_years': 'malaysian_government_securities_kurang_dari_3_tahun_less_than_3_years',  # TODO: rename
        'malaysian_government_securities_5_tahun_5_years': 'malaysian_government_securities_5_tahun_5_years',  # TODO: rename
        'malaysian_government_securities_10_tahun_10_years': 'malaysian_government_securities_10_tahun_10_years',  # TODO: rename
        'malaysian_government_securities_15_tahun_15_years': 'malaysian_government_securities_15_tahun_15_years',  # TODO: rename
        'sekuriti_kerajaan_malaysia_malaysian_government_securities_15_tahun_15_years': 'sekuriti_kerajaan_malaysia_malaysian_government_securities_15_tahun_15_years',  # TODO: rename
        'other_loans': 'other_loans',  # TODO: rename
        'external_debt4_jumlah_kecil_sub_total': 'external_debt4_jumlah_kecil_sub_total',  # TODO: rename
        'non_resident_holdings_of_rm_denominated_debt': 'non_resident_holdings_of_rm_denominated_debt',  # TODO: rename
        'market_loans': 'market_loans',  # TODO: rename
        'project_loans': 'project_loans',  # TODO: rename
    },

    # Federal Government Domestic Debt by Holder
    '3.1.5': {
        'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_jumlah_total': 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_jumlah_total',  # TODO: rename
        'jumlah_kecil_sub_total': 'jumlah_kecil_sub_total',  # TODO: rename
        'bank_negara_malaysia_central_bank_of_malaysia': 'bank_negara_malaysia_central_bank_of_malaysia',  # TODO: rename
        'institusi_perbankan_banking_institutions': 'institusi_perbankan_banking_institutions',  # TODO: rename
        'pemilik_pemilik_asing_foreign_holders': 'pemilik_pemilik_asing_foreign_holders',  # TODO: rename
        'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_bil_bil_perbendaharaan_treasury_bills_lain_lain_other': 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_bil_bil_perbendaharaan_treasury_bills_lain_lain_other',  # TODO: rename
        'malaysia_government_investment_issues_jumlah_kecil_sub_total': 'malaysia_government_investment_issues_jumlah_kecil_sub_total',  # TODO: rename
        'kumpulan_wang_simpanan_pekerja_employees_provident_fund': 'kumpulan_wang_simpanan_pekerja_employees_provident_fund',  # TODO: rename
        'kumpulan_wang_amanah_persaraan_kwap': 'kumpulan_wang_amanah_persaraan_kwap',  # TODO: rename
        'syarikat_syarikat_insurans_insurance_companies': 'syarikat_syarikat_insurans_insurance_companies',  # TODO: rename
        'financial_sector_bank_negara_malaysia_central_bank_of_malaysia': 'financial_sector_bank_negara_malaysia_central_bank_of_malaysia',  # TODO: rename
        'financial_sector_institusi_perbankan_banking_institutions': 'financial_sector_institusi_perbankan_banking_institutions',  # TODO: rename
        'institusi_kewangan_pembangunan_development_financial_institutions': 'institusi_kewangan_pembangunan_development_financial_institutions',  # TODO: rename
        'lain_lain_institusi_bukan_kewangan_non_bank_financial_institutions': 'lain_lain_institusi_bukan_kewangan_non_bank_financial_institutions',  # TODO: rename
        'malaysia_government_investment_issues_pemilik_pemilik_asing_foreign_holders': 'malaysia_government_investment_issues_pemilik_pemilik_asing_foreign_holders',  # TODO: rename
        'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_terbitan_pelaburan_kerajaan_malaysia_malaysia_government_investment_issues_lain_lain_other': 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_terbitan_pelaburan_kerajaan_malaysia_malaysia_government_investment_issues_lain_lain_other',  # TODO: rename
        'malaysian_government_securities_jumlah_kecil_sub_total': 'malaysian_government_securities_jumlah_kecil_sub_total',  # TODO: rename
        'social_security_institutions_kumpulan_wang_simpanan_pekerja_employees_provident_fund': 'social_security_institutions_kumpulan_wang_simpanan_pekerja_employees_provident_fund',  # TODO: rename
        'social_security_institutions_kumpulan_wang_amanah_persaraan_kwap': 'social_security_institutions_kumpulan_wang_amanah_persaraan_kwap',  # TODO: rename
        'malaysian_government_securities_syarikat_syarikat_insurans_insurance_companies': 'malaysian_government_securities_syarikat_syarikat_insurans_insurance_companies',  # TODO: rename
        'sektor_kewangan_financial_sector_bank_negara_malaysia_central_bank_of_malaysia': 'sektor_kewangan_financial_sector_bank_negara_malaysia_central_bank_of_malaysia',  # TODO: rename
        'sektor_kewangan_financial_sector_institusi_perbankan_banking_institutions': 'sektor_kewangan_financial_sector_institusi_perbankan_banking_institutions',  # TODO: rename
        'financial_sector_institusi_kewangan_pembangunan_development_financial_institutions': 'financial_sector_institusi_kewangan_pembangunan_development_financial_institutions',  # TODO: rename
        'lain_lain_institusi_kewangan_non_bank_financial_institutions': 'lain_lain_institusi_kewangan_non_bank_financial_institutions',  # TODO: rename
        'malaysian_government_securities_pemilik_pemilik_asing_foreign_holders': 'malaysian_government_securities_pemilik_pemilik_asing_foreign_holders',  # TODO: rename
        'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_sekuriti_kerajaan_malaysia_malaysian_government_securities_lain_lain_other': 'hutang_kerajaan_persekutuan_yang_diterbitkan_dalam_negeri_pengkelasan_mengikut_pemilik_federal_government_debt_issued_domestically_classification_by_holder_sekuriti_kerajaan_malaysia_malaysian_government_securities_lain_lain_other',  # TODO: rename
        'other_loans': 'other_loans',  # TODO: rename
    },

    # Federal Government Debt by Currency and Remaining Maturity
    '3.1.6': {
        'federal_government_debt_classification_by_currency_and_remaining_maturity': 'federal_government_debt_classification_by_currency_and_remaining_maturity',  # TODO: rename
        'total_rm_million_equivalent': 'total_rm_million_equivalent',  # TODO: rename
        'rm': 'rm',  # TODO: rename
        'usd': 'usd',  # TODO: rename
        'yen': 'yen',  # TODO: rename
        'hutang_kerajaan_persekutuan_pengkelasan_mengikut_matawang_dan_tempoh_baki_matang_federal_government_debt_classification_by_currency_and_remaining_maturity_hutang_yang_belum_dijelaskan_kerajaan_persekutuan_mengikut_matawang_outstanding_federal_government_debt_by_currency_lain_lain_others': 'hutang_kerajaan_persekutuan_pengkelasan_mengikut_matawang_dan_tempoh_baki_matang_federal_government_debt_classification_by_currency_and_remaining_maturity_hutang_yang_belum_dijelaskan_kerajaan_persekutuan_mengikut_matawang_outstanding_federal_government_debt_by_currency_lain_lain_others',  # TODO: rename
        'others_rm_million_equivalent': 'others_rm_million_equivalent',  # TODO: rename
    },

    # RENTAS: Foreign Holdings in Debt Securities and Sukuk
    '3.2': {
        'rentas_foreign_holdings_in_debt_securities_and_sukuk': 'rentas_foreign_holdings_in_debt_securities_and_sukuk',  # TODO: rename
        'bank_negara_monetary_note': 'bank_negara_monetary_note',  # TODO: rename
        'malaysian_treasury_bills': 'malaysian_treasury_bills',  # TODO: rename
        'malaysian_government_securities': 'malaysian_government_securities',  # TODO: rename
        'bank_negara_monetary_note_islamic': 'bank_negara_monetary_note_islamic',  # TODO: rename
        'malaysian_islamic_treasury_bills': 'malaysian_islamic_treasury_bills',  # TODO: rename
        'bank_negara_malaysia_sukuk_ijarah': 'bank_negara_malaysia_sukuk_ijarah',  # TODO: rename
        'malaysian_government_investment_issues': 'malaysian_government_investment_issues',  # TODO: rename
        'government_housing_sukuk': 'government_housing_sukuk',  # TODO: rename
        'corporate_bonds': 'corporate_bonds',  # TODO: rename
        'sukuk': 'sukuk',  # TODO: rename
        'denominated_debt_securities': 'denominated_debt_securities',  # TODO: rename
        'denominasi_sekuriti_hutang_denominated_debt_securities': 'denominasi_sekuriti_hutang_denominated_debt_securities',  # TODO: rename
    },

    # Labour Market Indicators for the Financial Services Sector
    '3.5.12a': {
        'labour_market_indicators_for_the_financial_services_sector': 'labour_market_indicators_for_the_financial_services_sector',  # TODO: rename
        'total_number_of_employees': 'total_number_of_employees',  # TODO: rename
        'number_of_job_vacancies': 'number_of_job_vacancies',  # TODO: rename
        'new_job_created': 'new_job_created',  # TODO: rename
        'new_hires_and_recalls': 'new_hires_and_recalls',  # TODO: rename
        'penunjuk_pasaran_pekerja_bagi_sektor_perkhidmatan_kewangan_labour_market_indicators_for_the_financial_services_sector_separations_total': 'penunjuk_pasaran_pekerja_bagi_sektor_perkhidmatan_kewangan_labour_market_indicators_for_the_financial_services_sector_separations_total',  # TODO: rename
        'quits_and_resignation_except_retirement': 'quits_and_resignation_except_retirement',  # TODO: rename
        'layoffs_and_discharges': 'layoffs_and_discharges',  # TODO: rename
        'other_separations': 'other_separations',  # TODO: rename
    },

    # Selected Statistics on Cheques Cleared and Returned
    '3.5.14': {
        'no_million': 'no_million',  # TODO: rename
        'rm_billion': 'rm_billion',  # TODO: rename
        'no_000_no_000': 'no_000_no_000',  # TODO: rename
        'rm_milion_rm_million': 'rm_milion_rm_million',  # TODO: rename
        'of_which_returned_cheques_due_to_insufficient_funds_no_000_no_000': 'of_which_returned_cheques_due_to_insufficient_funds_no_000_no_000',  # TODO: rename
        'of_which_returned_cheques_due_to_insufficient_funds_rm_milion_rm_million': 'of_which_returned_cheques_due_to_insufficient_funds_rm_milion_rm_million',  # TODO: rename
    },

    # Selected Statistics on Dishonoured Cheques (prev)
    '3.5.14a': {
        'no': 'no',  # TODO: rename
        'annual_change': 'annual_change',  # TODO: rename
        'no_million': 'no_million',  # TODO: rename
        'rm_bilion_rm_billion': 'rm_bilion_rm_billion',  # TODO: rename
        'cheques_cleared_rm_bilion_rm_billion': 'cheques_cleared_rm_bilion_rm_billion',  # TODO: rename
    },

    # Banking System: Cross-Border Position vs Non-Resident
    '3.6.19': {
        'pinjaman_dan_deposit_loans_and_deposits': 'pinjaman_dan_deposit_loans_and_deposits',  # TODO: rename
        'sekuriti_hutang_debt_securities': 'sekuriti_hutang_debt_securities',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_lain_lain_others': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_lain_lain_others',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_jumlah_total': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_aset_assets_jumlah_total',  # TODO: rename
        'liabilities_pinjaman_dan_deposit_loans_and_deposits': 'liabilities_pinjaman_dan_deposit_loans_and_deposits',  # TODO: rename
        'liabilities_sekuriti_hutang_debt_securities': 'liabilities_sekuriti_hutang_debt_securities',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_lain_lain_others': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_lain_lain_others',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_jumlah_total': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_perbankan_bukan_pemastautin_non_resident_banking_sector_liabiliti_liabilities_jumlah_total',  # TODO: rename
        'assets_pinjaman_dan_deposit_loans_and_deposits': 'assets_pinjaman_dan_deposit_loans_and_deposits',  # TODO: rename
        'assets_sekuriti_hutang_debt_securities': 'assets_sekuriti_hutang_debt_securities',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_lain_lain_others': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_lain_lain_others',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_jumlah_total': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_aset_assets_jumlah_total',  # TODO: rename
        'liabiliti_liabilities_pinjaman_dan_deposit_loans_and_deposits': 'liabiliti_liabilities_pinjaman_dan_deposit_loans_and_deposits',  # TODO: rename
        'liabiliti_liabilities_sekuriti_hutang_debt_securities': 'liabiliti_liabilities_sekuriti_hutang_debt_securities',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_liabiliti_liabilities_lain_lain_others': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_sektor_bukan_bank_bukan_pemastautin_non_resident_non_bank_sector_liabiliti_liabilities_lain_lain_others',  # TODO: rename
        '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_rm_million_jumlah_total': '3_6_19_sistem_perbankan_kedudukan_rentas_sempadan_berhubung_dengan_bukan_pemastautin_mengikut_sektor_rakan_niaga_dan_instrumen_banking_system_cross_border_position_vis_à_vis_non_resident_by_counterparty_sector_and_instrument_labuan_as_resident_rm_million_jumlah_total',  # TODO: rename
    },

    # Gross Imports by Economic Function
    '3.6.7': {
        'food': 'food',  # TODO: rename
        'consumer_durables': 'consumer_durables',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_lain_lain_others': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_lain_lain_others',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_jumlah_total': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_penggunaan_consumption_goods_jumlah_total',  # TODO: rename
        'machinery': 'machinery',  # TODO: rename
        'transport_equipment': 'transport_equipment',  # TODO: rename
        'metal_products': 'metal_products',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_lain_lain_others': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_lain_lain_others',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_jumlah_total': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pelaburan_investment_goods_jumlah_total',  # TODO: rename
        'for_manufacturing': 'for_manufacturing',  # TODO: rename
        'for_construction': 'for_construction',  # TODO: rename
        'for_agriculture': 'for_agriculture',  # TODO: rename
        'crude_petroleum': 'crude_petroleum',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_lain_lain_others': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_lain_lain_others',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_jumlah_total': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_barang_pengantara_intermediate_goods_jumlah_total',  # TODO: rename
        'retained_imports': 'retained_imports',  # TODO: rename
        'imports_for_re_exports': 'imports_for_re_exports',  # TODO: rename
        'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_rm_million_jumlah_total': 'import_kasar_mengikut_fungsi_ekonomi_gross_imports_by_economic_function_rm_million_jumlah_total',  # TODO: rename
    },

    # External Debt
    '3.7': {
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_jumlah_total': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_jumlah_total',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_peminjaman_luar_pesisir2_offshore_borrowing_jumlah_total': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_peminjaman_luar_pesisir2_offshore_borrowing_jumlah_total',  # TODO: rename
        'federal_government': 'federal_government',  # TODO: rename
        'public_enterprise': 'public_enterprise',  # TODO: rename
        'sektor_perbankan_banking_sector': 'sektor_perbankan_banking_sector',  # TODO: rename
        'sektor_bukan_bank_non_bank_sector': 'sektor_bukan_bank_non_bank_sector',  # TODO: rename
        'short_term_sektor_perbankan_banking_sector': 'short_term_sektor_perbankan_banking_sector',  # TODO: rename
        'private_sector_sektor_bukan_bank_non_bank_sector': 'private_sector_sektor_bukan_bank_non_bank_sector',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_jumlah_total': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_jumlah_total',  # TODO: rename
        'sekuriti_kerajaan_government_securities': 'sekuriti_kerajaan_government_securities',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_sederhana_dan_panjang_medium_and_long_term_lain_lain_others': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_sederhana_dan_panjang_medium_and_long_term_lain_lain_others',  # TODO: rename
        'short_term_sekuriti_kerajaan_government_securities': 'short_term_sekuriti_kerajaan_government_securities',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_pendek_short_term_lain_lain_others': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_pemegangan_sekuriti_hutang_dalam_denominasi_ringgit_oleh_bukan_pemastautin_non_resident_holdings_of_ringgit_denominated_debt_securities_short_term_jangka_pendek_short_term_lain_lain_others',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_deposit_bukan_pemastautin_non_resident_deposits_jumlah_total': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_deposit_bukan_pemastautin_non_resident_deposits_jumlah_total',  # TODO: rename
        'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_lain_lain_others_jumlah_total': 'hutang_luar_negeri_definisi_semula_external_debt_redefined_external_debt_outstanding_lain_lain_others_jumlah_total',  # TODO: rename
        'medium_and_long_term': 'medium_and_long_term',  # TODO: rename
        'term': 'term',  # TODO: rename
        'debt_service_ratio7': 'debt_service_ratio7',  # TODO: rename
        'medium_and_long_term_debt': 'medium_and_long_term_debt',  # TODO: rename
        'term_debt': 'term_debt',  # TODO: rename
    },

    # External Reserves
    '3.8': {
        'external_reserves': 'external_reserves',  # TODO: rename
        'rizab_luar_negeri_external_reserves_central_bank_of_malaysia_gross_international_reserves_jumlah_total': 'rizab_luar_negeri_external_reserves_central_bank_of_malaysia_gross_international_reserves_jumlah_total',  # TODO: rename
        'special_drawing_rights': 'special_drawing_rights',  # TODO: rename
        'imf_reserves_position': 'imf_reserves_position',  # TODO: rename
        'gold_and_foreign_exchange': 'gold_and_foreign_exchange',  # TODO: rename
        'external_liabilities': 'external_liabilities',  # TODO: rename
        'net_international_reserves': 'net_international_reserves',  # TODO: rename
        'other_official_reserves': 'other_official_reserves',  # TODO: rename
        'net_official_reserves': 'net_official_reserves',  # TODO: rename
    },

    # Life/General Insurance and Takaful Funds: Statement of Assets
    '4.1': {
        'number_of_life_family_and_general_insurance_takaful_funds': 'number_of_life_family_and_general_insurance_takaful_funds',  # TODO: rename
        'total_assets': 'total_assets',  # TODO: rename
        'property_plant_and_equipment': 'property_plant_and_equipment',  # TODO: rename
        'investment_properties': 'investment_properties',  # TODO: rename
        'loans_financing': 'loans_financing',  # TODO: rename
        'malaysian_government_papers2_guaranteed_loans': 'malaysian_government_papers2_guaranteed_loans',  # TODO: rename
        'corporate_debt_securities': 'corporate_debt_securities',  # TODO: rename
        'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_lain_lain_others': 'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_lain_lain_others',  # TODO: rename
        'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_jumlah_total': 'kumpulan_wang_insurans_hayat_am_dan_takaful_keluarga_am_langsung_penyata_aset_life_general_insurance_and_direct_family_general_takaful_funds_statement_of_assets_pelaburan_jumlah_total',  # TODO: rename
        'foreign_assets': 'foreign_assets',  # TODO: rename
        'cash_and_deposits': 'cash_and_deposits',  # TODO: rename
        'other_assets': 'other_assets',  # TODO: rename
    },

    # Insurance Key Indicators
    '4.10': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # Life Insurance Business: Valuation Result and Surplus Distribution
    '4.10.1': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # Takaful Key Indicators
    '4.11': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # Insurance Broking Business: Operating Results
    '4.12': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # Insurance Broking Business: Total Premiums Transacted
    '4.12.1': {
        'marine_aviation_and_transit_direct_premiums_rm_million': 'marine_aviation_and_transit_direct_premiums_rm_million',  # TODO: rename
        'general_marine_aviation_and_transit_direct_premiums_rm_million': 'general_marine_aviation_and_transit_direct_premiums_rm_million',  # TODO: rename
        'fire': 'fire',  # TODO: rename
        'fire_direct_premiums_rm_million': 'fire_direct_premiums_rm_million',  # TODO: rename
        'motor': 'motor',  # TODO: rename
        'motor_direct_premiums_rm_million': 'motor_direct_premiums_rm_million',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'miscellaneous_direct_premiums_rm_million': 'miscellaneous_direct_premiums_rm_million',  # TODO: rename
        'life': 'life',  # TODO: rename
        'life_miscellaneous_direct_premiums_rm_million': 'life_miscellaneous_direct_premiums_rm_million',  # TODO: rename
        'table_4_12_insurance_broking_total_premiums_transacted_total': 'table_4_12_insurance_broking_total_premiums_transacted_total',  # TODO: rename
        'total_miscellaneous_direct_premiums_rm_million': 'total_miscellaneous_direct_premiums_rm_million',  # TODO: rename
    },

    # Loss Adjusting Business: Operating Results
    '4.13': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # Loss Adjusting Business: Cases Handled by Adjusters
    '4.13.1': {
        'motor_no': 'motor_no',  # TODO: rename
        'cases_handled_by_adjusters_motor_no': 'cases_handled_by_adjusters_motor_no',  # TODO: rename
        'motor_change': 'motor_change',  # TODO: rename
        'cases_handled_by_adjusters_motor_change': 'cases_handled_by_adjusters_motor_change',  # TODO: rename
        'motor_share': 'motor_share',  # TODO: rename
        'cases_handled_by_adjusters_motor_share': 'cases_handled_by_adjusters_motor_share',  # TODO: rename
        'non_motor_no': 'non_motor_no',  # TODO: rename
        'cases_handled_by_adjusters_non_motor_no': 'cases_handled_by_adjusters_non_motor_no',  # TODO: rename
        'non_motor_change': 'non_motor_change',  # TODO: rename
        'cases_handled_by_adjusters_non_motor_change': 'cases_handled_by_adjusters_non_motor_change',  # TODO: rename
        'non_motor_share': 'non_motor_share',  # TODO: rename
        'cases_handled_by_adjusters_non_motor_share': 'cases_handled_by_adjusters_non_motor_share',  # TODO: rename
        'total_no': 'total_no',  # TODO: rename
        'cases_handled_by_adjusters_total_no': 'cases_handled_by_adjusters_total_no',  # TODO: rename
        'total_change': 'total_change',  # TODO: rename
        'cases_handled_by_adjusters_total_change': 'cases_handled_by_adjusters_total_change',  # TODO: rename
    },

    # Insurance: Assets and Liabilities
    '4.2': {
        'penanggung_insurans_hayat_langsung_life_direct_insurers': 'penanggung_insurans_hayat_langsung_life_direct_insurers',  # TODO: rename
        'modal_berbayar_paid_up_capital': 'modal_berbayar_paid_up_capital',  # TODO: rename
        'akaun_premium_saham_share_premium_account': 'akaun_premium_saham_share_premium_account',  # TODO: rename
        'rizab_reserves': 'rizab_reserves',  # TODO: rename
        'keuntungan_kerugian_tertahan_retained_profit_loss': 'keuntungan_kerugian_tertahan_retained_profit_loss',  # TODO: rename
        'ekuiti_pemegang_syer_shareholders_equity_jumlah_total': 'ekuiti_pemegang_syer_shareholders_equity_jumlah_total',  # TODO: rename
        'rizab_penilaian_semula_aset_assets_revaluation_reserves': 'rizab_penilaian_semula_aset_assets_revaluation_reserves',  # TODO: rename
        'liabiliti_lain_other_liabilities': 'liabiliti_lain_other_liabilities',  # TODO: rename
        'jumlah_liabiliti_total_liabilities': 'jumlah_liabiliti_total_liabilities',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'pinjaman_loans': 'pinjaman_loans',  # TODO: rename
        'malaysian_government_papers_guaranteed_loans': 'malaysian_government_papers_guaranteed_loans',  # TODO: rename
        'corporate_debt_securities': 'corporate_debt_securities',  # TODO: rename
        'pelaburan_lain_other_investments': 'pelaburan_lain_other_investments',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'harta_benda_pelaburan_investment_properties': 'harta_benda_pelaburan_investment_properties',  # TODO: rename
        'wang_tunai_dan_simpanan_cash_and_deposits': 'wang_tunai_dan_simpanan_cash_and_deposits',  # TODO: rename
        'aset_lain1_other_assets': 'aset_lain1_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'jumlah_aset_total_assets': 'jumlah_aset_total_assets',  # TODO: rename
    },

    # Takaful: Assets and Liabilities
    '4.3': {
        'pengendali_takaful_keluarga_langsung_family_direct_takaful_operators': 'pengendali_takaful_keluarga_langsung_family_direct_takaful_operators',  # TODO: rename
        'modal_berbayar_paid_up_capital': 'modal_berbayar_paid_up_capital',  # TODO: rename
        'akaun_premium_saham_share_premium_account': 'akaun_premium_saham_share_premium_account',  # TODO: rename
        'rizab_reserves': 'rizab_reserves',  # TODO: rename
        'keuntungan_kerugian_tertahan_retained_profit_loss': 'keuntungan_kerugian_tertahan_retained_profit_loss',  # TODO: rename
        'ekuiti_pemegang_syer_shareholders_equity_jumlah_total': 'ekuiti_pemegang_syer_shareholders_equity_jumlah_total',  # TODO: rename
        'rizab_penilaian_semula_aset_assets_revaluation_reserves': 'rizab_penilaian_semula_aset_assets_revaluation_reserves',  # TODO: rename
        'liabiliti_lain_other_liabilities': 'liabiliti_lain_other_liabilities',  # TODO: rename
        'jumlah_liabiliti_total_liabilities': 'jumlah_liabiliti_total_liabilities',  # TODO: rename
        'wang_tunai_dan_simpanan_cash_and_deposits': 'wang_tunai_dan_simpanan_cash_and_deposits',  # TODO: rename
        'government_islamic_papers_malaysian_government_guaranteed_financing': 'government_islamic_papers_malaysian_government_guaranteed_financing',  # TODO: rename
        'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities': 'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities',  # TODO: rename
        'pelaburan_lain_other_investments': 'pelaburan_lain_other_investments',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'pelaburan_harta_benda_investment_properties': 'pelaburan_harta_benda_investment_properties',  # TODO: rename
        'pembiayaan_financing': 'pembiayaan_financing',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain_other_assets': 'aset_lain_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'jumlah_aset_total_assets': 'jumlah_aset_total_assets',  # TODO: rename
    },

    # Insurance: Capital Adequacy Ratio
    '4.4': {
        'penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available': 'penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available',  # TODO: rename
        'penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required': 'penanggung_insurans_hayat_life_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required',  # TODO: rename
        'penanggung_insurans_hayat_life_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio': 'penanggung_insurans_hayat_life_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'penanggung_insurans_am_general_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available': 'penanggung_insurans_am_general_insurance_companies_jumlah_modal_sedia_ada3_total_capital_available',  # TODO: rename
        'penanggung_insurans_am_general_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required': 'penanggung_insurans_am_general_insurance_companies_jumlah_modal_dikehendaki3_total_capital_required',  # TODO: rename
        'penanggung_insurans_am_general_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio': 'penanggung_insurans_am_general_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'jumlah_modal_sedia_ada4_total_capital_available': 'jumlah_modal_sedia_ada4_total_capital_available',  # TODO: rename
        'jumlah_modal_dikehendaki4_total_capital_required': 'jumlah_modal_dikehendaki4_total_capital_required',  # TODO: rename
        'penanggung_insurans_komposit2_composite2_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio': 'penanggung_insurans_komposit2_composite2_insurance_companies_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'jumlah_modal_sedia_ada_total_capital_available': 'jumlah_modal_sedia_ada_total_capital_available',  # TODO: rename
        'jumlah_modal_dikehendaki_total_capital_required': 'jumlah_modal_dikehendaki_total_capital_required',  # TODO: rename
        'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio': 'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
    },

    # Takaful: Capital Adequacy Ratio
    '4.5': {
        'pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_sedia_ada_total_capital_available': 'pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_sedia_ada_total_capital_available',  # TODO: rename
        'pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_dikehendaki_total_capital_required': 'pengendali_takaful_keluarga_family_takaful_operators_jumlah_modal_dikehendaki_total_capital_required',  # TODO: rename
        'pengendali_takaful_keluarga_family_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio': 'pengendali_takaful_keluarga_family_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'pengendali_takaful_am_general_takaful_operators_jumlah_modal_sedia_ada_total_capital_available': 'pengendali_takaful_am_general_takaful_operators_jumlah_modal_sedia_ada_total_capital_available',  # TODO: rename
        'pengendali_takaful_am_general_takaful_operators_jumlah_modal_dikehendaki_total_capital_required': 'pengendali_takaful_am_general_takaful_operators_jumlah_modal_dikehendaki_total_capital_required',  # TODO: rename
        'pengendali_takaful_am_general_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio': 'pengendali_takaful_am_general_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'jumlah_modal_sedia_ada3_total_capital_available': 'jumlah_modal_sedia_ada3_total_capital_available',  # TODO: rename
        'jumlah_modal_dikehendaki3_total_capital_required': 'jumlah_modal_dikehendaki3_total_capital_required',  # TODO: rename
        'pengendali_takaful_komposit2_composite2_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio': 'pengendali_takaful_komposit2_composite2_takaful_operators_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
        'keseluruhan_industri_consolidated_industry_jumlah_modal_sedia_ada_total_capital_available': 'keseluruhan_industri_consolidated_industry_jumlah_modal_sedia_ada_total_capital_available',  # TODO: rename
        'keseluruhan_industri_consolidated_industry_jumlah_modal_dikehendaki_total_capital_required': 'keseluruhan_industri_consolidated_industry_jumlah_modal_dikehendaki_total_capital_required',  # TODO: rename
        'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio': 'rm_juta_rm_million_nisbah_kecukupan_modal_capital_adequacy_ratio',  # TODO: rename
    },

    # Life Insurance: New Business and Business in Force
    '4.6': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'nilai_diinsuranskan_sums_insured_rm_juta_rm_million': 'nilai_diinsuranskan_sums_insured_rm_juta_rm_million',  # TODO: rename
        'tahunan_annual': 'tahunan_annual',  # TODO: rename
        'tunggal_single': 'tunggal_single',  # TODO: rename
        'jumlah_total': 'jumlah_total',  # TODO: rename
        'unit_unit': 'unit_unit',  # TODO: rename
        'perniagaan_berkuat_kuasa_business_in_force_nilai_diinsuranskan_sums_insured_rm_juta_rm_million': 'perniagaan_berkuat_kuasa_business_in_force_nilai_diinsuranskan_sums_insured_rm_juta_rm_million',  # TODO: rename
        'premium_tahunan_annual_premium': 'premium_tahunan_annual_premium',  # TODO: rename
    },

    # Life Insurance: No. of New Business Policies
    '4.6.1': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'seumur_hidup_whole_life_jumlah_total': 'seumur_hidup_whole_life_jumlah_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total': 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total',  # TODO: rename
        'anuiti_annuity_individu_individual': 'anuiti_annuity_individu_individual',  # TODO: rename
        'anuiti_annuity_lain_lain_others_kumpulan_group': 'anuiti_annuity_lain_lain_others_kumpulan_group',  # TODO: rename
        'anuiti_annuity_lain_lain_others_jumlah_total': 'anuiti_annuity_lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'jumlah_total_lain_lain_others_jumlah_total': 'jumlah_total_lain_lain_others_jumlah_total',  # TODO: rename
    },

    # Life Insurance: No. of Policies in Force
    '4.6.2': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'seumur_hidup_whole_life_jumlah_total': 'seumur_hidup_whole_life_jumlah_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total': 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total',  # TODO: rename
        'anuiti_annuity_individu_individual': 'anuiti_annuity_individu_individual',  # TODO: rename
        'anuiti_annuity_lain_lain_others_kumpulan_group': 'anuiti_annuity_lain_lain_others_kumpulan_group',  # TODO: rename
        'anuiti_annuity_lain_lain_others_jumlah_total': 'anuiti_annuity_lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'unit_unit_jumlah_total': 'unit_unit_jumlah_total',  # TODO: rename
    },

    # Life Insurance: No. of Policies Terminated
    '4.6.3': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'cukup_tempoh_maturity_individu_individual': 'cukup_tempoh_maturity_individu_individual',  # TODO: rename
        'cukup_tempoh_maturity_kumpulan_group': 'cukup_tempoh_maturity_kumpulan_group',  # TODO: rename
        'cukup_tempoh_maturity_jumlah_total': 'cukup_tempoh_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'unit_unit_jumlah_total': 'unit_unit_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Distribution of New Business Premiums
    '4.6.4': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_seumur_hidup_whole_life_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_seumur_hidup_whole_life_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_endowmen_endowment_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_endowmen_endowment_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_sementara_temporary_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_sementara_temporary_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_lain_lain_others_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_hayat_biasa_ordinary_life_lain_lain_others_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_berkaitan_pelaburan_investment_linked_lain_lain_others_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_berkaitan_pelaburan_investment_linked_lain_lain_others_total',  # TODO: rename
        'anuiti_annuity_individu_individual': 'anuiti_annuity_individu_individual',  # TODO: rename
        'anuiti_annuity_lain_lain_others_kumpulan_group': 'anuiti_annuity_lain_lain_others_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_anuiti_annuity_lain_lain_others_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_anuiti_annuity_lain_lain_others_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_rm_juta_rm_million_total': 'insurans_hayat1_agihan_premium_perniagaan_baharu_penanggung_insurans_langsung_life1_insurance_distribution_of_new_business_premiums_of_direct_insurers_rm_juta_rm_million_total',  # TODO: rename
    },

    # Life Insurance: Distribution of Annual Premiums in Force
    '4.6.5': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'seumur_hidup_whole_life_jumlah_total': 'seumur_hidup_whole_life_jumlah_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total': 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Distribution of New Sums Insured
    '4.6.6': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'seumur_hidup_whole_life_jumlah_total': 'seumur_hidup_whole_life_jumlah_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total': 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total',  # TODO: rename
        'anuiti_annuity_individu_individual': 'anuiti_annuity_individu_individual',  # TODO: rename
        'anuiti_annuity_lain_lain_others_kumpulan_group': 'anuiti_annuity_lain_lain_others_kumpulan_group',  # TODO: rename
        'anuiti_annuity_lain_lain_others_jumlah_total': 'anuiti_annuity_lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Distribution of Sums Insured in Force
    '4.6.7': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'seumur_hidup_whole_life_kumpulan_group': 'seumur_hidup_whole_life_kumpulan_group',  # TODO: rename
        'seumur_hidup_whole_life_jumlah_total': 'seumur_hidup_whole_life_jumlah_total',  # TODO: rename
        'endowmen_endowment_individu_individual': 'endowmen_endowment_individu_individual',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group': 'berkaitan_pelaburan_investment_linked_lain_lain_others_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total': 'berkaitan_pelaburan_investment_linked_lain_lain_others_jumlah_total',  # TODO: rename
        'anuiti_annuity_individu_individual': 'anuiti_annuity_individu_individual',  # TODO: rename
        'anuiti_annuity_lain_lain_others_kumpulan_group': 'anuiti_annuity_lain_lain_others_kumpulan_group',  # TODO: rename
        'anuiti_annuity_lain_lain_others_jumlah_total': 'anuiti_annuity_lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_lain_lain_others_kumpulan_group': 'jumlah_total_lain_lain_others_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Terminations of Annual Premiums
    '4.6.8': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'kematangan_maturity_individu_individual': 'kematangan_maturity_individu_individual',  # TODO: rename
        'kematangan_maturity_kumpulan_group': 'kematangan_maturity_kumpulan_group',  # TODO: rename
        'kematangan_maturity_jumlah_total': 'kematangan_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total',  # TODO: rename
        'other_causes_including_expiry_individu_individual': 'other_causes_including_expiry_individu_individual',  # TODO: rename
        'other_causes_including_expiry_kumpulan_group': 'other_causes_including_expiry_kumpulan_group',  # TODO: rename
        'other_causes_including_expiry_jumlah_total': 'other_causes_including_expiry_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Terminations of Sums Insured
    '4.6.9': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'cukup_tempoh_maturity_individu_individual': 'cukup_tempoh_maturity_individu_individual',  # TODO: rename
        'cukup_tempoh_maturity_kumpulan_group': 'cukup_tempoh_maturity_kumpulan_group',  # TODO: rename
        'cukup_tempoh_maturity_jumlah_total': 'cukup_tempoh_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_individu_individual',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_kumpulan_group',  # TODO: rename
        'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total': 'perlucutan_hak_tolak_pengaktifan_semula_forfeiture_less_revivals_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Life Insurance: Income and Outgo
    '4.6.a': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'pendapatan_pelaburan_bersih_net_investment_income': 'pendapatan_pelaburan_bersih_net_investment_income',  # TODO: rename
        'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income': 'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income',  # TODO: rename
        'pendapatan_income_jumlah_total': 'pendapatan_income_jumlah_total',  # TODO: rename
        'faedah_polisi_bersih_net_policy_benefits': 'faedah_polisi_bersih_net_policy_benefits',  # TODO: rename
        'imbuhan_agensi_agency_remuneration': 'imbuhan_agensi_agency_remuneration',  # TODO: rename
        'perbelanjaan_pengurusan_management_expenses': 'perbelanjaan_pengurusan_management_expenses',  # TODO: rename
        'kerugian_dari_pelupusan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo': 'kerugian_dari_pelupusan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo',  # TODO: rename
        'perbelanjaan_outgo_jumlah_total': 'perbelanjaan_outgo_jumlah_total',  # TODO: rename
        'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo': 'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo',  # TODO: rename
    },

    # Life Insurance: Assets of Life Insurance Funds
    '4.6.b': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kertas_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_guaranteed_loans': 'kertas_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_guaranteed_loans',  # TODO: rename
        'sekuriti_hutang_korporat_corporate_debt_securities': 'sekuriti_hutang_korporat_corporate_debt_securities',  # TODO: rename
        'pelaburan_investments_lain_lain_others': 'pelaburan_investments_lain_lain_others',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'pelaburan_harta_benda_investment_properties': 'pelaburan_harta_benda_investment_properties',  # TODO: rename
        'gadai_janji_mortgages': 'gadai_janji_mortgages',  # TODO: rename
        'polisi_policy': 'polisi_policy',  # TODO: rename
        'pinjaman_loans_lain_lain_others': 'pinjaman_loans_lain_lain_others',  # TODO: rename
        'pinjaman_loans_jumlah_total': 'pinjaman_loans_jumlah_total',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain2_other_assets': 'aset_lain2_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Premium Income
    '4.7': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'premium_langsung_kasar_gross_direct_premiums': 'premium_langsung_kasar_gross_direct_premiums',  # TODO: rename
        'premium_bersih_net_premiums': 'premium_bersih_net_premiums',  # TODO: rename
        'nisbah_bendungan_retention_ratio': 'nisbah_bendungan_retention_ratio',  # TODO: rename
    },

    # General Insurance: Distribution of Gross Direct Premiums
    '4.7.1': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'general1_insurance_distribution_of_gross_direct_premiums_jumlah_total': 'general1_insurance_distribution_of_gross_direct_premiums_jumlah_total',  # TODO: rename
    },

    # General Insurance: Claims Ratio
    '4.7.10': {
        'col': 'col',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'perniagaan_dalam_malaysia_business_within_malaysia_jumlah_total': 'perniagaan_dalam_malaysia_business_within_malaysia_jumlah_total',  # TODO: rename
    },

    # General Insurance: Claims Ratio for Direct Insurers
    '4.7.10.a': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'insurans_am1_nisbah_tuntutan2_penanggung_insurans_am_langsung_jumlah_total': 'insurans_am1_nisbah_tuntutan2_penanggung_insurans_am_langsung_jumlah_total',  # TODO: rename
    },

    # General Insurance: Reinsurance Accepted Premiums
    '4.7.11': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Premiums for Professional Reinsurers
    '4.7.12': {
        'marin_udara_dan_transit_marine_aviation_and_transit': 'marin_udara_dan_transit_marine_aviation_and_transit',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Claims Ratio for Professional Reinsurers
    '4.7.13': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'general1_insurance_claims_ratio2_for_professional_general_reinsurers_jumlah_total': 'general1_insurance_claims_ratio2_for_professional_general_reinsurers_jumlah_total',  # TODO: rename
    },

    # General Insurance: Earned Premium Income
    '4.7.14': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Gross Claims Paid for Direct Business
    '4.7.15': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Gross Claims Paid for Reinsurance Accepted
    '4.7.16': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Claim Recoveries from Licensed Insurers
    '4.7.17': {
        'marin_udara_dan_transit_marine_aviation_and_transit': 'marin_udara_dan_transit_marine_aviation_and_transit',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Claim Recoveries from Foreign Insurers
    '4.7.18': {
        'marin_udara_dan_transit_marine_aviation_and_transit': 'marin_udara_dan_transit_marine_aviation_and_transit',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Claims Paid
    '4.7.19': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Distribution of Net Premiums
    '4.7.2': {
        'marin_udara_dan_transit_marine_aviation_and_transit': 'marin_udara_dan_transit_marine_aviation_and_transit',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Claims Incurred
    '4.7.20': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Combined Net Retention Ratio
    '4.7.3': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'general1_insurance_combined_direct_insurers_and_professional_reinsurers_net_retention_ratio_jumlah_total': 'general1_insurance_combined_direct_insurers_and_professional_reinsurers_net_retention_ratio_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Retention Ratio for Direct Insurers
    '4.7.4': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'general1_insurance_net_retention_ratio_for_direct_insurers_jumlah_total': 'general1_insurance_net_retention_ratio_for_direct_insurers_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Retention Ratio for Reinsurers
    '4.7.5': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'contractor_s_all_risk_and_engineering': 'contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'general1_insurance_net_retention_ratio_for_professional_reinsurers_jumlah_total': 'general1_insurance_net_retention_ratio_for_professional_reinsurers_jumlah_total',  # TODO: rename
    },

    # General Insurance: Reinsurance Position for Premiums Ceded
    '4.7.6': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo': 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'miscellaneous': 'miscellaneous',  # TODO: rename
        'general1_insurance_reinsurance_position_for_premiums_ceded_and_retroceded_overseas_jumlah_total': 'general1_insurance_reinsurance_position_for_premiums_ceded_and_retroceded_overseas_jumlah_total',  # TODO: rename
    },

    # General Insurance: Reinsurance Claims Recoveries
    '4.7.7': {
        'marin_dan_penerbangan_udara_marine_and_aviation_hull': 'marin_dan_penerbangan_udara_marine_and_aviation_hull',  # TODO: rename
        'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo': 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Reinsurance Profit Commissions
    '4.7.8': {
        'marin_dan_penerbangan_udara_marine_and_aviation_hull': 'marin_dan_penerbangan_udara_marine_and_aviation_hull',  # TODO: rename
        'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo': 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Net Reinsurance Position
    '4.7.9': {
        'aliran_masuk_bersih_atau_aliran_keluar_bersih_net_inflow_or_outflow': 'aliran_masuk_bersih_atau_aliran_keluar_bersih_net_inflow_or_outflow',  # TODO: rename
        'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo': 'marin_penerbangan_udara_dan_kargo_transit_marine_aviation_and_transit_cargo',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_million_jumlah_total': 'rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Underwriting and Operating Results
    '4.7.a': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'tuntutan_bersih_kena_dibayar_net_claims_incurred': 'tuntutan_bersih_kena_dibayar_net_claims_incurred',  # TODO: rename
        'commissions': 'commissions',  # TODO: rename
        'management_expenses': 'management_expenses',  # TODO: rename
        'underwriting_profit': 'underwriting_profit',  # TODO: rename
        'investment_income': 'investment_income',  # TODO: rename
        'capital_gains': 'capital_gains',  # TODO: rename
        'pendapatan_lain_other_income': 'pendapatan_lain_other_income',  # TODO: rename
        'capital_losses': 'capital_losses',  # TODO: rename
        'other_outgo': 'other_outgo',  # TODO: rename
        'operating_profit': 'operating_profit',  # TODO: rename
    },

    # General Insurance: Assets of General Insurance Funds
    '4.7.b': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'amaun_tertunggak_daripada_pelanggan_pengantara_penanggung_insurans_semula_amount_due_from_clients_intermediaries_reinsurers': 'amaun_tertunggak_daripada_pelanggan_pengantara_penanggung_insurans_semula_amount_due_from_clients_intermediaries_reinsurers',  # TODO: rename
        'kertas_dan_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_and_guaranteed_loans': 'kertas_dan_pinjaman_dijamin_kerajaan_malaysia_malaysia_government_papers_and_guaranteed_loans',  # TODO: rename
        'sekuriti_dan_hutang_korporat_corporate_debt_and_securities': 'sekuriti_dan_hutang_korporat_corporate_debt_and_securities',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'pelaburan_harta_benda_investment_properties': 'pelaburan_harta_benda_investment_properties',  # TODO: rename
        'pinjaman_loans': 'pinjaman_loans',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain2_other_assets': 'aset_lain2_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Insurance: Technical Reserves
    '4.7.c': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'liabiliti_premium_premium_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium': 'liabiliti_premium_premium_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium',  # TODO: rename
        'liabiliti_tuntutan_claims_liabilities_rm_juta_rm_million': 'liabiliti_tuntutan_claims_liabilities_rm_juta_rm_million',  # TODO: rename
        'liabiliti_tuntutan_claims_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium': 'liabiliti_tuntutan_claims_liabilities_peratusan_daripada_premium_bersih_percentage_of_net_premium',  # TODO: rename
        'rizab_teknikal_technical_reserves_rm_juta_rm_million': 'rizab_teknikal_technical_reserves_rm_juta_rm_million',  # TODO: rename
        'rizab_teknikal_technical_reserves_peratusan_daripada_premium_bersih_percentage_of_net_premium': 'rizab_teknikal_technical_reserves_peratusan_daripada_premium_bersih_percentage_of_net_premium',  # TODO: rename
    },

    # Family Takaful: New Business and Business in Force
    '4.8': {
        'bilangan_sijil_no_of_certificates_unit_unit': 'bilangan_sijil_no_of_certificates_unit_unit',  # TODO: rename
        'jumlah_penyertaan_sum_participated_rm_juta_rm_million': 'jumlah_penyertaan_sum_participated_rm_juta_rm_million',  # TODO: rename
        'tunggal_single': 'tunggal_single',  # TODO: rename
        'tahunan_annual': 'tahunan_annual',  # TODO: rename
        'jumlah_total': 'jumlah_total',  # TODO: rename
        'perniagaan_berkuat_kuasa_business_in_force_bilangan_sijil_no_of_certificates_unit_unit': 'perniagaan_berkuat_kuasa_business_in_force_bilangan_sijil_no_of_certificates_unit_unit',  # TODO: rename
        'perniagaan_berkuat_kuasa_business_in_force_jumlah_penyertaan_sum_participated_rm_juta_rm_million': 'perniagaan_berkuat_kuasa_business_in_force_jumlah_penyertaan_sum_participated_rm_juta_rm_million',  # TODO: rename
        'caruman_contributions': 'caruman_contributions',  # TODO: rename
    },

    # Family Takaful: No. of New Business Certificates
    '4.8.1': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'keluarga_biasa_ordinary_family_group': 'keluarga_biasa_ordinary_family_group',  # TODO: rename
        'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_keluarga_biasa_ordinary_family_total': 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_keluarga_biasa_ordinary_family_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individual': 'berkaitan_pelaburan_investment_linked_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_group': 'berkaitan_pelaburan_investment_linked_group',  # TODO: rename
        'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_berkaitan_pelaburan_investment_linked_total': 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_berkaitan_pelaburan_investment_linked_total',  # TODO: rename
        'anuiti_annuity_individual': 'anuiti_annuity_individual',  # TODO: rename
        'anuiti_annuity_group': 'anuiti_annuity_group',  # TODO: rename
        'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_anuiti_annuity_total': 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_anuiti_annuity_total',  # TODO: rename
        'jumlah_total_individual': 'jumlah_total_individual',  # TODO: rename
        'jumlah_total_group': 'jumlah_total_group',  # TODO: rename
        'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_jumlah_total_total': 'takaful_keluarga1_bilangan_sijil_perniagaan_baharu_pengendali_takaful_langsung_family1_takaful_no_of_new_business_certificates_of_direct_takaful_operators_bilangan_sijil_no_of_certificates_jumlah_total_total',  # TODO: rename
    },

    # Family Takaful: Annual Contributions of Terminated Certificates
    '4.8.10': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'kematangan_maturity_individu_individual': 'kematangan_maturity_individu_individual',  # TODO: rename
        'kematangan_maturity_kumpulan_group': 'kematangan_maturity_kumpulan_group',  # TODO: rename
        'kematangan_maturity_jumlah_total': 'kematangan_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'other_causes_including_expiry_individu_individual': 'other_causes_including_expiry_individu_individual',  # TODO: rename
        'other_causes_including_expiry_kumpulan_group': 'other_causes_including_expiry_kumpulan_group',  # TODO: rename
        'other_causes_including_expiry_jumlah_total': 'other_causes_including_expiry_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Distribution of Sum Participated of New Business
    '4.8.2': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'keluarga_biasa_ordinary_family_group': 'keluarga_biasa_ordinary_family_group',  # TODO: rename
        'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_keluarga_biasa_ordinary_family_total': 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_keluarga_biasa_ordinary_family_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individual': 'berkaitan_pelaburan_investment_linked_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_group': 'berkaitan_pelaburan_investment_linked_group',  # TODO: rename
        'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_berkaitan_pelaburan_investment_linked_total': 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_berkaitan_pelaburan_investment_linked_total',  # TODO: rename
        'anuiti_annuity_individual': 'anuiti_annuity_individual',  # TODO: rename
        'anuiti_annuity_group': 'anuiti_annuity_group',  # TODO: rename
        'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_anuiti_annuity_total': 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_jumlah_penyertaan_sum_participated_anuiti_annuity_total',  # TODO: rename
        'jumlah_total_individual': 'jumlah_total_individual',  # TODO: rename
        'jumlah_total_group': 'jumlah_total_group',  # TODO: rename
        'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_rm_juta_rm_million_total': 'takaful_keluarga1_agihan_jumlah_penyertaan_bagi_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_sum_participated_of_new_business_of_direct_takaful_operators_rm_juta_rm_million_total',  # TODO: rename
    },

    # Family Takaful: Distribution of New Business Contributions
    '4.8.3': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'keluarga_biasa_ordinary_family_group': 'keluarga_biasa_ordinary_family_group',  # TODO: rename
        'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_keluarga_biasa_ordinary_family_total': 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_keluarga_biasa_ordinary_family_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individual': 'berkaitan_pelaburan_investment_linked_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_group': 'berkaitan_pelaburan_investment_linked_group',  # TODO: rename
        'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_berkaitan_pelaburan_investment_linked_total': 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_berkaitan_pelaburan_investment_linked_total',  # TODO: rename
        'anuiti_annuity_individual': 'anuiti_annuity_individual',  # TODO: rename
        'anuiti_annuity_group': 'anuiti_annuity_group',  # TODO: rename
        'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_anuiti_annuity_total': 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_caruman_contributions_anuiti_annuity_total',  # TODO: rename
        'jumlah_total_individual': 'jumlah_total_individual',  # TODO: rename
        'jumlah_total_group': 'jumlah_total_group',  # TODO: rename
        'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_rm_juta_rm_million_total': 'takaful_keluarga1_agihan_caruman_perniagaan_baharu_pengendali_takaful_langsung_family_takaful1_distribution_of_new_business_contribution_of_direct_takaful_operators_rm_juta_rm_million_total',  # TODO: rename
    },

    # Family Takaful: Distribution of New Business Contributions by Plan
    '4.8.4': {
        'pendidikan_education': 'pendidikan_education',  # TODO: rename
        'endowmen_endowment_lain_lain_others': 'endowmen_endowment_lain_lain_others',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'gadai_janji_mortgage': 'gadai_janji_mortgage',  # TODO: rename
        'sementara_temporary_lain_lain_others': 'sementara_temporary_lain_lain_others',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'perubatan_dan_kesihatan_medical_and_health': 'perubatan_dan_kesihatan_medical_and_health',  # TODO: rename
        'keluarga_biasa_ordinary_family_lain_lain_others': 'keluarga_biasa_ordinary_family_lain_lain_others',  # TODO: rename
        'keluarga_biasa_ordinary_family_jumlah_total': 'keluarga_biasa_ordinary_family_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked': 'berkaitan_pelaburan_investment_linked',  # TODO: rename
        'anuiti_annuity': 'anuiti_annuity',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: No. of Certificates In Force
    '4.8.5': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'keluarga_biasa_ordinary_family_jumlah_total': 'keluarga_biasa_ordinary_family_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group': 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total': 'berkaitan_pelaburan_investment_linked_jumlah_total',  # TODO: rename
        'annuiti_annuity_individu_individual': 'annuiti_annuity_individu_individual',  # TODO: rename
        'annuiti_annuity_jumlah_total_kumpulan_group': 'annuiti_annuity_jumlah_total_kumpulan_group',  # TODO: rename
        'annuiti_annuity_jumlah_total': 'annuiti_annuity_jumlah_total',  # TODO: rename
        'bilangan_sijil_no_of_certificates_jumlah_total_individu_individual': 'bilangan_sijil_no_of_certificates_jumlah_total_individu_individual',  # TODO: rename
        'bilangan_sijil_no_of_certificates_jumlah_total_kumpulan_group': 'bilangan_sijil_no_of_certificates_jumlah_total_kumpulan_group',  # TODO: rename
        'unit_unit_jumlah_total': 'unit_unit_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Distribution of Sum Participated In Force
    '4.8.6': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'keluarga_biasa_ordinary_family_jumlah_total': 'keluarga_biasa_ordinary_family_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group': 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total': 'berkaitan_pelaburan_investment_linked_jumlah_total',  # TODO: rename
        'annuiti_annuity_individu_individual': 'annuiti_annuity_individu_individual',  # TODO: rename
        'annuiti_annuity_jumlah_total_kumpulan_group': 'annuiti_annuity_jumlah_total_kumpulan_group',  # TODO: rename
        'annuiti_annuity_jumlah_total': 'annuiti_annuity_jumlah_total',  # TODO: rename
        'jumlah_penyertaan_sum_participated_jumlah_total_individu_individual': 'jumlah_penyertaan_sum_participated_jumlah_total_individu_individual',  # TODO: rename
        'jumlah_penyertaan_sum_participated_jumlah_total_kumpulan_group': 'jumlah_penyertaan_sum_participated_jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Distribution of Annual Contributions In Force
    '4.8.7': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'endowmen_endowment_kumpulan_group': 'endowmen_endowment_kumpulan_group',  # TODO: rename
        'endowmen_endowment_jumlah_total': 'endowmen_endowment_jumlah_total',  # TODO: rename
        'sementara_temporary_individu_individual': 'sementara_temporary_individu_individual',  # TODO: rename
        'sementara_temporary_kumpulan_group': 'sementara_temporary_kumpulan_group',  # TODO: rename
        'sementara_temporary_jumlah_total': 'sementara_temporary_jumlah_total',  # TODO: rename
        'lain_lain_others_individu_individual': 'lain_lain_others_individu_individual',  # TODO: rename
        'lain_lain_others_kumpulan_group': 'lain_lain_others_kumpulan_group',  # TODO: rename
        'lain_lain_others_jumlah_total': 'lain_lain_others_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'keluarga_biasa_ordinary_family_jumlah_total': 'keluarga_biasa_ordinary_family_jumlah_total',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_individu_individual': 'berkaitan_pelaburan_investment_linked_individu_individual',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group': 'berkaitan_pelaburan_investment_linked_jumlah_total_kumpulan_group',  # TODO: rename
        'berkaitan_pelaburan_investment_linked_jumlah_total': 'berkaitan_pelaburan_investment_linked_jumlah_total',  # TODO: rename
        'annuiti_annuity_individu_individual': 'annuiti_annuity_individu_individual',  # TODO: rename
        'annuiti_annuity_jumlah_total_kumpulan_group': 'annuiti_annuity_jumlah_total_kumpulan_group',  # TODO: rename
        'annuiti_annuity_jumlah_total': 'annuiti_annuity_jumlah_total',  # TODO: rename
        'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_individu_individual': 'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_individu_individual',  # TODO: rename
        'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_kumpulan_group': 'family_takaful1_distribution_of_annual_contributions_of_business_in_force_of_direct_takaful_operators_jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: No. of Certificates Terminated
    '4.8.8': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'kematangan_maturity_individu_individual': 'kematangan_maturity_individu_individual',  # TODO: rename
        'kematangan_maturity_kumpulan_group': 'kematangan_maturity_kumpulan_group',  # TODO: rename
        'kematangan_maturity_jumlah_total': 'kematangan_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'unit_unit_jumlah_total': 'unit_unit_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Sum Participated of Terminated Certificates
    '4.8.9': {
        'kematian_death_individu_individual': 'kematian_death_individu_individual',  # TODO: rename
        'kematian_death_kumpulan_group': 'kematian_death_kumpulan_group',  # TODO: rename
        'kematian_death_jumlah_total': 'kematian_death_jumlah_total',  # TODO: rename
        'kematangan_maturity_individu_individual': 'kematangan_maturity_individu_individual',  # TODO: rename
        'kematangan_maturity_kumpulan_group': 'kematangan_maturity_kumpulan_group',  # TODO: rename
        'kematangan_maturity_jumlah_total': 'kematangan_maturity_jumlah_total',  # TODO: rename
        'serahan_surrender_individu_individual': 'serahan_surrender_individu_individual',  # TODO: rename
        'serahan_surrender_kumpulan_group': 'serahan_surrender_kumpulan_group',  # TODO: rename
        'serahan_surrender_jumlah_total': 'serahan_surrender_jumlah_total',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_individu_individual',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_kumpulan_group',  # TODO: rename
        'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total': 'sebab_lain_termasuk_tamat_tempoh_other_causes_including_expiry_jumlah_total',  # TODO: rename
        'jumlah_total_individu_individual': 'jumlah_total_individu_individual',  # TODO: rename
        'jumlah_total_kumpulan_group': 'jumlah_total_kumpulan_group',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Income and Outgo
    '4.8.a': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'pendapatan_pelaburan_bersih_net_investment_income': 'pendapatan_pelaburan_bersih_net_investment_income',  # TODO: rename
        'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income': 'keuntungan_atas_jualan_aset_dan_pendapatan_pelbagai_profit_on_sale_of_assets_and_miscellaneous_income',  # TODO: rename
        'pendapatan_income_jumlah_total': 'pendapatan_income_jumlah_total',  # TODO: rename
        'manfaat_sijil_bersih_net_certificate_benefits': 'manfaat_sijil_bersih_net_certificate_benefits',  # TODO: rename
        'komisen_bersih_net_commissions': 'komisen_bersih_net_commissions',  # TODO: rename
        'perbelanjaan_pengurusan2_management_expenses': 'perbelanjaan_pengurusan2_management_expenses',  # TODO: rename
        'kerugian_atas_jualan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo': 'kerugian_atas_jualan_aset_dan_perbelanjaan_lain_loss_on_disposal_of_assets_and_other_outgo',  # TODO: rename
        'perbelanjaan_outgo_jumlah_total': 'perbelanjaan_outgo_jumlah_total',  # TODO: rename
        'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo': 'lebihan_pendapatan_daripada_perbelanjaan_excess_of_income_over_outgo',  # TODO: rename
    },

    # Family Takaful: Assets of Family Takaful Funds
    '4.8.b': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market': 'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market',  # TODO: rename
        'sekuriti_islam_kerajaan_government_islamic_papers': 'sekuriti_islam_kerajaan_government_islamic_papers',  # TODO: rename
        'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities': 'sekuriti_hutang_swasta_islam_dan_ekuiti_islamic_private_debt_securities_and_equities',  # TODO: rename
        'pelaburan_lain_other_investments': 'pelaburan_lain_other_investments',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'pelaburan_harta_benda_investment_properties': 'pelaburan_harta_benda_investment_properties',  # TODO: rename
        'pembiayaan_financing': 'pembiayaan_financing',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain_other_assets': 'aset_lain_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # Family Takaful: Valuation Result
    '4.8.c': {
        'indicator': 'indicator',  # TODO: rename
        'value': 'value',  # TODO: rename
    },

    # General Takaful: Distribution of Gross Contributions
    '4.9': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Distribution of Net Contributions
    '4.9.1': {
        'marin_udara_dan_transit_marine_aviation_and_transit': 'marin_udara_dan_transit_marine_aviation_and_transit',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident': 'perbelanjaan_perubatan_dan_kemalangan_diri_medical_expenses_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Domestic Retention
    '4.9.2': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'general_takaful1_domestic_retention_ratio_of_direct_takaful_operators_business_jumlah_total': 'general_takaful1_domestic_retention_ratio_of_direct_takaful_operators_business_jumlah_total',  # TODO: rename
    },

    # General Takaful: Gross Claims Paid
    '4.9.3': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Net Claims Paid
    '4.9.4': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Claims Ratio
    '4.9.5': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'general_takaful1_claims_ratio_of_direct_takaful_operators_jumlah_total': 'general_takaful1_claims_ratio_of_direct_takaful_operators_jumlah_total',  # TODO: rename
    },

    # General Takaful: Earned Contribution Income
    '4.9.6': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Net Claims Incurred
    '4.9.7': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering': 'semua_risiko_kontraktor_dan_kejuruteraan_contractor_s_all_risk_and_engineering',  # TODO: rename
        'kebakaran_fire': 'kebakaran_fire',  # TODO: rename
        'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident': 'perubatan_dan_kesihatan_kemalangan_diri_medical_and_health_and_personal_accident',  # TODO: rename
        'perlindungan_akta_act_cover': 'perlindungan_akta_act_cover',  # TODO: rename
        'lain_lain_others': 'lain_lain_others',  # TODO: rename
        'motor_motor_jumlah_total': 'motor_motor_jumlah_total',  # TODO: rename
        'liabiliti_liability': 'liabiliti_liability',  # TODO: rename
        'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability': 'pampasan_pekerja_dan_liabiliti_majikan_workmen_s_compensation_and_employers_liability',  # TODO: rename
        'pelbagai_miscellaneous': 'pelbagai_miscellaneous',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Underwriting and Operating Results
    '4.9.a': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'tuntutan_bersih_kena_dibayar_net_claims_incurred': 'tuntutan_bersih_kena_dibayar_net_claims_incurred',  # TODO: rename
        'komisen_bersih_net_commissions': 'komisen_bersih_net_commissions',  # TODO: rename
        'perbelanjaan_pengurusan2_management_expenses': 'perbelanjaan_pengurusan2_management_expenses',  # TODO: rename
        'keuntungan_pengunderaitan_underwriting_profit': 'keuntungan_pengunderaitan_underwriting_profit',  # TODO: rename
        'keuntungan_pelaburan_investment_income': 'keuntungan_pelaburan_investment_income',  # TODO: rename
        'keuntungan_modal_capital_gains': 'keuntungan_modal_capital_gains',  # TODO: rename
        'pendapatan_lain_other_income': 'pendapatan_lain_other_income',  # TODO: rename
        'kerugian_modal_capital_losses': 'kerugian_modal_capital_losses',  # TODO: rename
        'perbelanjaan_lain_other_outgo': 'perbelanjaan_lain_other_outgo',  # TODO: rename
        'keuntungan_kendalian_operating_profit': 'keuntungan_kendalian_operating_profit',  # TODO: rename
    },

    # General Takaful: Assets of General Takaful Funds
    '4.9.b': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market': 'akaun_pelaburan_dan_pasaran_wang_islam_investment_accounts_and_islamic_money_market',  # TODO: rename
        'sekuriti_islam_kerajaan_government_islamic_papers': 'sekuriti_islam_kerajaan_government_islamic_papers',  # TODO: rename
        'sekuriti_hutang_swasta_dan_ekuiti_islam_islamic_private_debt_securities_and_equities': 'sekuriti_hutang_swasta_dan_ekuiti_islam_islamic_private_debt_securities_and_equities',  # TODO: rename
        'pelaburan_lain_other_investments': 'pelaburan_lain_other_investments',  # TODO: rename
        'pelaburan_investments_jumlah_total': 'pelaburan_investments_jumlah_total',  # TODO: rename
        'pelaburan_harta_benda_investment_properties': 'pelaburan_harta_benda_investment_properties',  # TODO: rename
        'pembiayaan_financing': 'pembiayaan_financing',  # TODO: rename
        'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment': 'harta_benda_loji_dan_kelengkapan_property_plant_and_equipment',  # TODO: rename
        'aset_lain_other_assets': 'aset_lain_other_assets',  # TODO: rename
        'aset_asing_foreign_assets': 'aset_asing_foreign_assets',  # TODO: rename
        'rm_juta_rm_million_jumlah_total': 'rm_juta_rm_million_jumlah_total',  # TODO: rename
    },

    # General Takaful: Technical Reserves
    '4.9.c': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'rizab_caruman_tidak_diperoleh_unearned_contributions_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions': 'rizab_caruman_tidak_diperoleh_unearned_contributions_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions',  # TODO: rename
        'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_rm_juta_rm_million': 'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_rm_juta_rm_million',  # TODO: rename
        'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_peratusan_daripada_caruman_bersih_percentage_of_net_contributions': 'peruntukan_tuntutan_belum_dibayar_provision_for_outstanding_claims_peratusan_daripada_caruman_bersih_percentage_of_net_contributions',  # TODO: rename
        'rizab_teknikal_technical_reserves_rm_juta_rm_million': 'rizab_teknikal_technical_reserves_rm_juta_rm_million',  # TODO: rename
        'rizab_teknikal_technical_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions': 'rizab_teknikal_technical_reserves_peratusan_daripada_caruman_bersih_percentage_of_net_contributions',  # TODO: rename
    },

    # General Takaful: Contributions Income
    '4.9.d': {
        'perniagaan_dalam_malaysia_business_within_malaysia': 'perniagaan_dalam_malaysia_business_within_malaysia',  # TODO: rename
        'caruman_langsung_kasar_gross_direct_contributions': 'caruman_langsung_kasar_gross_direct_contributions',  # TODO: rename
        'caruman_bersih_net_contributions': 'caruman_bersih_net_contributions',  # TODO: rename
        'nisbah_bendungan_retention_ratio': 'nisbah_bendungan_retention_ratio',  # TODO: rename
    },

    # List of Banking Institutions
    '5.1': {
    },

    # Leasing and Factoring Companies: Statement of Assets and Liabilities
    '5.2': {
        'cash_and_bank_balances': 'cash_and_bank_balances',  # TODO: rename
        'investments': 'investments',  # TODO: rename
        'leasing_factoring': 'leasing_factoring',  # TODO: rename
        'syarikat_pemajakan1_dan_pemfaktoran2_penyata_aset_dan_tanggungan_leasing1_and_factoring2_companies_statement_of_assets_and_liabilities_harta_assets_akan_diterima_receivables_lain_lain_others': 'syarikat_pemajakan1_dan_pemfaktoran2_penyata_aset_dan_tanggungan_leasing1_and_factoring2_companies_statement_of_assets_and_liabilities_harta_assets_akan_diterima_receivables_lain_lain_others',  # TODO: rename
        'syarikat_pemajakan_leasing_companies': 'syarikat_pemajakan_leasing_companies',  # TODO: rename
        'total_assets_liabilities': 'total_assets_liabilities',  # TODO: rename
        'capital_reserves_and_retained_earnings': 'capital_reserves_and_retained_earnings',  # TODO: rename
        'borrowings_from_financial_institutions': 'borrowings_from_financial_institutions',  # TODO: rename
        'inter_company_borrowings': 'inter_company_borrowings',  # TODO: rename
        'other_liabilities': 'other_liabilities',  # TODO: rename
    },

}

METADATA: dict[str, dict] = {
    # Reserve Money
    '1.1': {},

    # Banking System: Loan/Financing Applied by Purpose
    '1.10': {},

    # Banking System: Loans Applied by Purpose (prev)
    '1.10a': {},

    # Banking System: Loan/Financing Applied by Sector
    '1.11': {},

    # Banking System: Loan/Financing Applied by Type
    '1.11.1': {},

    # Banking System: Loans Applied by Sector (prev)
    '1.11a': {},

    # Banking System: Loan/Financing Approved
    '1.12': {},

    # Banking System: Loans Approved by Purpose (prev)
    '1.12a': {},

    # Banking System: Loan/Financing Approved by Sector
    '1.13': {},

    # Banking System: Loans Approved by Sector (prev2)
    '1.13.1': {},

    # Banking System: Loan/Financing Approved by Type
    '1.13.2': {},

    # Banking System: Loans Approved by Sector (prev)
    '1.13a': {},

    # Banking System: Loan/Financing Disbursed by Purpose
    '1.14': {},

    # Banking System: Loans Disbursed by Purpose (prev)
    '1.14a': {},

    # Banking System: Loan/Financing Disbursed by Sector
    '1.15': {},

    # Banking System: Loans Disbursed by Sectors (prev2)
    '1.15.1': {},

    # Banking System: Loan/Financing Disbursed by Type
    '1.15.2': {},

    # Banking System: Loans Disbursed by Sector (prev)
    '1.15a': {},

    # Banking System: Loan/Financing Repaid by Purpose
    '1.16': {},

    # Banking System: Loans Repaid by Purpose (prev)
    '1.16a': {},

    # Banking System: Loan/Financing Repaid by Sector
    '1.17': {},

    # Banking System: Loans Repaid by Sectors (prev2)
    '1.17.1': {},

    # Banking System: Loan/Financing Repaid by Type
    '1.17.2': {},

    # Banking System: Loans Repaid by Sector (prev)
    '1.17a': {},

    # Banking System: Loan/Financing by Type
    '1.18': {},

    # Islamic Banking: Financing by Type
    '1.18.1': {},

    # Islamic Banking: Financing by Type (prev)
    '1.18.1a': {},

    # Islamic Banking: Financing by Shariah Contract
    '1.18.2': {},

    # Islamic Banking: Financing by Concept (prev)
    '1.18.2a': {},

    # Banking System: Loan/Financing by Location
    '1.18.3': {},

    # Banking System: Classification of Loans by Type (prev)
    '1.18a': {},

    # Banking System: Loan/Financing by Purpose
    '1.19': {},

    # Islamic Banking: Financing by Purpose and Sectors
    '1.19.1': {},

    # Islamic Banking: Financing by Purpose and Sectors (prev)
    '1.19.1a': {},

    # Islamic Banking: Loans by Purpose and Sector (prev)
    '1.19.2': {},

    # Islamic Banking: Loans by Type and Sector (prev)
    '1.19.3': {},

    # Commercial & Islamic Banks: Loans/Financing by Purpose
    '1.19.4': {},

    # Investment Banks: Classification of Loans by Purpose
    '1.19.5': {},

    # Banking System: Household Loan/Financing by Purpose
    '1.19.6': {},

    # Banking System: Household Loan/Financing by Purpose (prev)
    '1.19.6a': {},

    # Banking System: Loans by Purpose (prev)
    '1.19a': {},

    # Banking System: Loans by Purpose (prev2)
    '1.19b': {},

    # Banking System: Loan/Financing by Purpose (prev3)
    '1.19c': {},

    # Currency in Circulation by Denomination
    '1.2': {},

    # Banking System: Loan/Financing by Sector
    '1.20': {},

    # Commercial & Islamic Banks: Loans/Financing by Sector
    '1.20.1': {},

    # Commercial & Islamic Banks: Loans by Sector (prev)
    '1.20.2': {},

    # Investment Banks: Classification of Loans by Sector
    '1.20.3': {},

    # Merchant Banks: Loans by Sector (prev)
    '1.20.4': {},

    # Finance Companies: Loans by Sector (prev)
    '1.20.5': {},

    # Finance Companies: Loans by Sector (historical)
    '1.20.6': {},

    # Banking System: Loans by Sector (prev)
    '1.20a': {},

    # Banking System: Loans by Sector (prev2)
    '1.20b': {},

    # Banking System: Loans by MFRS 9 Stages and Provisions
    '1.21': {},

    # Islamic Banking: Financing by MFRS 9 Stages and Provisions
    '1.21.1': {},

    # Islamic Banking: NPL/Impaired and Provisions (prev)
    '1.21.1a': {},

    # Islamic Banking: Impaired Financing and Provisions (prev)
    '1.21.1b': {},

    # Islamic Banking: Impaired Financing and Provisions (prev2)
    '1.21.1c': {},

    # Islamic Banking: Impaired Financing and Provisions (prev3)
    '1.21.1d': {},

    # Commercial & Islamic Banks: NPL/Impaired Loans
    '1.21.2': {},

    # Commercial & Islamic Banks: Impaired Loans (prev)
    '1.21.2a': {},

    # Commercial & Islamic Banks: Impaired Loans (prev2)
    '1.21.2b': {},

    # Investment Banks: NPL/Impaired Loans
    '1.21.3': {},

    # Investment Banks: Impaired Loans (prev)
    '1.21.3a': {},

    # Investment Banks: Impaired Loans (prev2)
    '1.21.3b': {},

    # Finance Companies: Loan Provisions and NPL
    '1.21.4': {},

    # Banking System: NPL/Impaired Loans and Provisions (prev)
    '1.21a': {},

    # Banking System: Impaired Loans and Provisions (prev)
    '1.21b': {},

    # Banking System: Impaired Loans and Provisions (prev2)
    '1.21c': {},

    # Banking System: Impaired Loans and Provisions (prev3)
    '1.21d': {},

    # Banking System: Impaired Loan/Financing by Purpose
    '1.22': {},

    # Commercial & Islamic Banks: NPL by Purpose
    '1.22.1': {},

    # Investment Banks: NPL/Impaired Loans by Purpose
    '1.22.2': {},

    # Banking System: NPL/Impaired Loans by Purpose (prev)
    '1.22a': {},

    # Banking System: NPL/Impaired Loans by Purpose (prev2)
    '1.22b': {},

    # Banking System: Impaired Loans by Purpose (prev)
    '1.22c': {},

    # Banking System: Impaired Loan/Financing by Sector
    '1.23': {},

    # Commercial & Islamic Banks: NPL by Sector
    '1.23.1': {},

    # Commercial & Islamic Banks: NPL by Sector (prev)
    '1.23.2': {},

    # Investment Banks: NPL/Impaired Loans by Sector
    '1.23.3': {},

    # Merchant Banks: NPL by Sector (prev)
    '1.23.4': {},

    # Finance Companies: Non-Performing Loans by Sector
    '1.23.5': {},

    # Banking System: Impaired Loan/Financing by Type
    '1.23.6': {},

    # Banking System: NPL/Impaired Loans by Sector (prev)
    '1.23a': {},

    # Banking System: NPL/Impaired Loans by Sector (prev2)
    '1.23b': {},

    # Banking System: Total Deposits by Type
    '1.24': {},

    # Islamic Banking: Deposits by Type
    '1.24.1': {},

    # Islamic Banking: Deposits by Type & Holder
    '1.24.2': {},

    # Islamic Banking: Deposits by Type and Holder (prev)
    '1.24.3': {},

    # Banking System: Total Deposits by Holder
    '1.25': {},

    # Banking System: Demand Deposits by Holder
    '1.25.1': {},

    # Banking System: Savings and Fixed Deposits by Holder
    '1.25.2': {},

    # Banking System: Repurchase Agreements by Holder
    '1.25.3': {},

    # Banking System: NIDs by Holder
    '1.25.4': {},

    # Banking System: Foreign Currency and Other Deposits by Holder
    '1.25.5': {},

    # Banking System: Fixed Deposits by Original Maturity
    '1.25.6': {},

    # Statutory Reserve Requirement and Liquidity Ratio
    '1.26': {},

    # Statutory Reserve and Liquid Asset Requirement
    '1.27': {},

    # New Liquidity Framework
    '1.28': {},

    # Liquidity Coverage Ratio
    '1.28a': {},

    # Banking System: Constituents of Capital
    '1.29': {},

    # Islamic Banking System: Constituents of Capital
    '1.29.1': {},

    # Islamic Banking System: Constituents of Capital (v2)
    '1.29.1a': {},

    # Commercial & Islamic Banks: Constituents of Capital
    '1.29.2': {},

    # Commercial & Islamic Banks: Capital (prev)
    '1.29.2a': {},

    # Finance Companies: Constituents of Capital
    '1.29.3': {},

    # Investment Banks: Constituents of Capital
    '1.29.4': {},

    # Investment Banks: Constituents of Capital (prev)
    '1.29.4a': {},

    # Banking System: Constituents of Capital (v2)
    '1.29a': {},

    # Banking System: Constituents of Capital (prev)
    '1.29b': {},

    # Monetary Aggregates: M1, M2 and M3
    '1.3': {},

    # Broad Money, M3
    '1.3.1': {},

    # Factors Affecting M3
    '1.3.2': {},

    # Credit Card Operations in Malaysia
    '1.30': {},

    # Debit Card Transactions
    '1.30.1': {},

    # Banking System: Loan to Fund Ratio and Liquidity
    '1.31': {},

    # Islamic Banking: Total Investment Account by Type and Holder
    '1.32': {},

    # Islamic Banking: Assets funded through Investment Account
    '1.32.1': {},

    # Islamic Banking: Financing through Investment Account by Type
    '1.32.2': {},

    # Islamic Banking: Financing through Investment Account by Concept
    '1.32.3': {},

    # Islamic Banking: Financing through Investment Account by Purpose
    '1.32.4': {},

    # Islamic Banking: Total Investment Account by Original Maturity
    '1.32.5': {},

    # Financial Institution: SME Loan/Financing by Sector
    '1.33': {},

    # Financial Institution: SME Loan/Financing Applied by Sector
    '1.33.1': {},

    # Financial Institution: SME Loan/Financing Approved by Sector
    '1.33.2': {},

    # Financial Institution: SME Loan/Financing Disbursed by Sector
    '1.33.3': {},

    # Financial Institution: SME Loan/Financing Repaid by Sector
    '1.33.4': {},

    # Financial Institution: Impaired SME Loan/Financing by Sector
    '1.33.5': {},

    # Financial Institutions: SME Loan/Financing by Purpose
    '1.34': {},

    # Financial Institution: SME Loan/Financing by SME Size
    '1.35': {},

    # Financial Institution: SME Loans Applied and Approved by Size
    '1.35.1': {},

    # Financial Institution: SME Loans Disbursed and Repaid by Size
    '1.35.2': {},

    # Financial Institution: Impaired SME Loans by Size
    '1.35.3': {},

    # Financial Institution: SME Loan/Financing by Loan Size
    '1.36': {},

    # BNM: Statement of Assets
    '1.4': {},

    # BNM: Statement of Capital and Liabilities
    '1.5': {},

    # BNM: Statement of Capital and Liabilities (prev)
    '1.5.1': {},

    # Banking System: Statement of Assets
    '1.7': {},

    # Islamic Banking System: Statement of Assets
    '1.7.1': {},

    # Commercial & Islamic Banks: Statement of Assets
    '1.7.2': {},

    # Commercial & Islamic Banks: Assets (prev)
    '1.7.2.1': {},

    # Commercial & Islamic Banks: Domestic & Foreign Assets
    '1.7.3': {},

    # Commercial & Islamic Banks: Domestic & Foreign Assets (prev)
    '1.7.3.1': {},

    # Investment Banks: Statement of Assets
    '1.7.4': {},

    # Finance Companies: Statement of Assets
    '1.7.5': {},

    # Banking System: Statement of Assets (prev)
    '1.7a': {},

    # Banking System: Statement of Capital and Liabilities
    '1.9': {},

    # Islamic Banking System: Statement of Capital & Liabilities
    '1.9.1': {},

    # Commercial & Islamic Banks: Statement of Liabilities
    '1.9.2': {},

    # Commercial & Islamic Banks: Liabilities (prev)
    '1.9.2.1': {},

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities
    '1.9.3': {},

    # Commercial & Islamic Banks: Domestic & Foreign Liabilities (prev)
    '1.9.3.1': {},

    # Investment Banks: Statement of Liabilities
    '1.9.4': {},

    # Finance Companies: Statement of Liabilities
    '1.9.5': {},

    # Finance Companies: Assets and Liabilities (prev)
    '1.9.5.1': {},

    # Banking System: External Assets and Liabilities
    '1.9.6': {},

    # Banking System: Capital and Liabilities (prev)
    '1.9a': {},

    # Interest Rates: Banking Institutions
    '2.1': {},

    # Funds Raised in Capital Market (by Private Sector)
    '2.10': {},

    # New Issues of Corporate Bond and/or Sukuk
    '2.11': {},

    # Turnover of Conventional and Islamic Money Market
    '2.14': {},

    # Turnover of Derivatives Transactions
    '2.15': {},

    # Turnover of Debt Securities and Sukuk
    '2.16': {},

    # Turnover of Foreign Currency Market Transactions
    '2.17': {},

    # Credit to the Private Non-Financial Sector
    '2.18': {},

    # Net Financing through Banking, DFIs and Corporate Bonds (prev)
    '2.18a': {},

    # Interest Rates: Banking Institutions (prev)
    '2.1a': {},

    # Islamic Banking: Financing and Profit Rates
    '2.2': {},

    # Islamic Banking: Financing and Profit Rates (prev)
    '2.2a': {},

    # Interest Rates: Interbank Money Market
    '2.3': {},

    # Interest Rates: Treasury Bills and Bank Negara Bills
    '2.4': {},

    # Treasury Bills, MGS and Khazanah Bonds: Tender Results
    '2.4.1': {},

    # Market Indicative Yield: Malaysian Government Securities
    '2.5': {},

    # Exchange Rates: Malaysian Ringgit
    '2.6': {},

    # Exchange Rates: Malaysian Ringgit (Daily)
    '2.6.1': {},

    # Volume of Transaction in Interbank Money Market
    '2.7': {},

    # Volume of Interbank Transactions in KL FX Market
    '2.8': {},

    # Funds Raised in Capital Market (by Public Sector)
    '2.9': {},

    # Federal Government Finance
    '3.1': {},

    # Federal Government Revenue
    '3.1.1': {},

    # Federal Government Operating Expenditure by Object
    '3.1.2': {},

    # Federal Government Development Expenditure
    '3.1.3': {},

    # Federal Government Debt by Remaining Maturity
    '3.1.4': {},

    # Federal Government Domestic Debt by Holder
    '3.1.5': {},

    # Federal Government Debt by Currency and Remaining Maturity
    '3.1.6': {},

    # RENTAS: Foreign Holdings in Debt Securities and Sukuk
    '3.2': {},

    # Labour Market Indicators for the Financial Services Sector
    '3.5.12a': {},

    # Selected Statistics on Cheques Cleared and Returned
    '3.5.14': {},

    # Selected Statistics on Dishonoured Cheques (prev)
    '3.5.14a': {},

    # Banking System: Cross-Border Position vs Non-Resident
    '3.6.19': {},

    # Gross Imports by Economic Function
    '3.6.7': {},

    # External Debt
    '3.7': {},

    # External Reserves
    '3.8': {},

    # Life/General Insurance and Takaful Funds: Statement of Assets
    '4.1': {},

    # Insurance Key Indicators
    '4.10': {},

    # Life Insurance Business: Valuation Result and Surplus Distribution
    '4.10.1': {},

    # Takaful Key Indicators
    '4.11': {},

    # Insurance Broking Business: Operating Results
    '4.12': {},

    # Insurance Broking Business: Total Premiums Transacted
    '4.12.1': {},

    # Loss Adjusting Business: Operating Results
    '4.13': {},

    # Loss Adjusting Business: Cases Handled by Adjusters
    '4.13.1': {},

    # Insurance: Assets and Liabilities
    '4.2': {},

    # Takaful: Assets and Liabilities
    '4.3': {},

    # Insurance: Capital Adequacy Ratio
    '4.4': {},

    # Takaful: Capital Adequacy Ratio
    '4.5': {},

    # Life Insurance: New Business and Business in Force
    '4.6': {},

    # Life Insurance: No. of New Business Policies
    '4.6.1': {},

    # Life Insurance: No. of Policies in Force
    '4.6.2': {},

    # Life Insurance: No. of Policies Terminated
    '4.6.3': {},

    # Life Insurance: Distribution of New Business Premiums
    '4.6.4': {},

    # Life Insurance: Distribution of Annual Premiums in Force
    '4.6.5': {},

    # Life Insurance: Distribution of New Sums Insured
    '4.6.6': {},

    # Life Insurance: Distribution of Sums Insured in Force
    '4.6.7': {},

    # Life Insurance: Terminations of Annual Premiums
    '4.6.8': {},

    # Life Insurance: Terminations of Sums Insured
    '4.6.9': {},

    # Life Insurance: Income and Outgo
    '4.6.a': {},

    # Life Insurance: Assets of Life Insurance Funds
    '4.6.b': {},

    # General Insurance: Premium Income
    '4.7': {},

    # General Insurance: Distribution of Gross Direct Premiums
    '4.7.1': {},

    # General Insurance: Claims Ratio
    '4.7.10': {},

    # General Insurance: Claims Ratio for Direct Insurers
    '4.7.10.a': {},

    # General Insurance: Reinsurance Accepted Premiums
    '4.7.11': {},

    # General Insurance: Net Premiums for Professional Reinsurers
    '4.7.12': {},

    # General Insurance: Claims Ratio for Professional Reinsurers
    '4.7.13': {},

    # General Insurance: Earned Premium Income
    '4.7.14': {},

    # General Insurance: Gross Claims Paid for Direct Business
    '4.7.15': {},

    # General Insurance: Gross Claims Paid for Reinsurance Accepted
    '4.7.16': {},

    # General Insurance: Claim Recoveries from Licensed Insurers
    '4.7.17': {},

    # General Insurance: Claim Recoveries from Foreign Insurers
    '4.7.18': {},

    # General Insurance: Net Claims Paid
    '4.7.19': {},

    # General Insurance: Distribution of Net Premiums
    '4.7.2': {},

    # General Insurance: Net Claims Incurred
    '4.7.20': {},

    # General Insurance: Combined Net Retention Ratio
    '4.7.3': {},

    # General Insurance: Net Retention Ratio for Direct Insurers
    '4.7.4': {},

    # General Insurance: Net Retention Ratio for Reinsurers
    '4.7.5': {},

    # General Insurance: Reinsurance Position for Premiums Ceded
    '4.7.6': {},

    # General Insurance: Reinsurance Claims Recoveries
    '4.7.7': {},

    # General Insurance: Reinsurance Profit Commissions
    '4.7.8': {},

    # General Insurance: Net Reinsurance Position
    '4.7.9': {},

    # General Insurance: Underwriting and Operating Results
    '4.7.a': {},

    # General Insurance: Assets of General Insurance Funds
    '4.7.b': {},

    # General Insurance: Technical Reserves
    '4.7.c': {},

    # Family Takaful: New Business and Business in Force
    '4.8': {},

    # Family Takaful: No. of New Business Certificates
    '4.8.1': {},

    # Family Takaful: Annual Contributions of Terminated Certificates
    '4.8.10': {},

    # Family Takaful: Distribution of Sum Participated of New Business
    '4.8.2': {},

    # Family Takaful: Distribution of New Business Contributions
    '4.8.3': {},

    # Family Takaful: Distribution of New Business Contributions by Plan
    '4.8.4': {},

    # Family Takaful: No. of Certificates In Force
    '4.8.5': {},

    # Family Takaful: Distribution of Sum Participated In Force
    '4.8.6': {},

    # Family Takaful: Distribution of Annual Contributions In Force
    '4.8.7': {},

    # Family Takaful: No. of Certificates Terminated
    '4.8.8': {},

    # Family Takaful: Sum Participated of Terminated Certificates
    '4.8.9': {},

    # Family Takaful: Income and Outgo
    '4.8.a': {},

    # Family Takaful: Assets of Family Takaful Funds
    '4.8.b': {},

    # Family Takaful: Valuation Result
    '4.8.c': {},

    # General Takaful: Distribution of Gross Contributions
    '4.9': {},

    # General Takaful: Distribution of Net Contributions
    '4.9.1': {},

    # General Takaful: Domestic Retention
    '4.9.2': {},

    # General Takaful: Gross Claims Paid
    '4.9.3': {},

    # General Takaful: Net Claims Paid
    '4.9.4': {},

    # General Takaful: Claims Ratio
    '4.9.5': {},

    # General Takaful: Earned Contribution Income
    '4.9.6': {},

    # General Takaful: Net Claims Incurred
    '4.9.7': {},

    # General Takaful: Underwriting and Operating Results
    '4.9.a': {},

    # General Takaful: Assets of General Takaful Funds
    '4.9.b': {},

    # General Takaful: Technical Reserves
    '4.9.c': {},

    # General Takaful: Contributions Income
    '4.9.d': {},

    # List of Banking Institutions
    '5.1': {},

    # Leasing and Factoring Companies: Statement of Assets and Liabilities
    '5.2': {},

}
