

class Locators:
    css_lastname_placeholder = "input[placeholder='Last Name']"
    css_firstname_placeholder = "input[placeholder='First Name']"
    xpath_address = "//form[@id='basicBootstrapForm']//div//div//textarea"
    css_email_type = "input[type='email']"
    css_phone_type = "input[type='tel']"
    css_male_gender_value = "input[value='Male']"
    css_female_gender_value = "input[value='FeMale']"
    id_hobbies_cricket = "checkbox1"
    id_hobbies_movies = "checkbox2"
    id_hobbies_hockey = "checkbox3"

    #Languages
    language_box_xpath = "//div[@id='msdd']"
    language_options_xpath = "//section[@id='section']//li//a"

    #Skill
    id_skills_ddw = "Skills"



class Locators_Itera:
    txbx_id_name = "name"
    txbx_id_phone = "phone"
    txbx_id_email = "email"
    txbx_id_password = "password"
    txbx_id_address = "address"
    bttn_css_submit = "submit"
    rd_id_male_gender = "male"
    rd_id_female_gender = "female"

    #days
    days_xpath = "(//input[@type='checkbox' and @class='form-check-input'])"

    #DD
    ddw_class_country = "custom-select"

    #Years of Experience
    rd_years_xpath = "//*[contains(@for,'year')]"