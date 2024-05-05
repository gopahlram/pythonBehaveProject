from behave import *

from features.pages.HomePage import HomePage


@given(u'A user click search jobs in Career section.')
def step_impl(context):
    home_page = HomePage(context.driver)
    context.career_page = home_page.click_on_careers_tab()
    context.job_listing_page = context.career_page.click_search_button()


@given(u'Navigate to job listing page.')
def step_impl(context):
    context.job_listing_page.navigate_to_job_listing_page()
    expected_text = "What Will You Make Possible?"
    assert expected_text.__eq__(context.job_listing_page.verify_job_listing_page())


@when(u'Upload user profile "{user_profile}" in job listing page.')
def step_impl(context, user_profile):
    file_name = user_profile
    assert context.job_listing_page.upload_file(file_name).__eq__(True)


@when(u'Search for the "{job}" Job and check requirement id "{id}".')
def step_impl(context, job, id):
    context.job_listing_page.search_job(job)
    expected_id = id
    assert expected_id.__eq__(context.job_listing_page.validate_requirement_id())


@when(u'Apply for the Selected Job.')
def step_impl(context):
    context.submit_form_page = context.job_listing_page.apply_job()


@then(u'Submit the application without mandatory fields and check error message "{error_message}".')
def step_impl(context, error_message):
    context.submit_form_page.click_submit_button()
    assert error_message.__eq__(context.submit_form_page.verify_mandatory_error_message())


@then('Submit the form without mandatory fields and check error message "{error_message}".')
def step_impl(context, error_message):
    context.submit_form_page.click_submit_button()
    assert error_message.__eq__(context.submit_form_page.verify_mandatory_error_message())
