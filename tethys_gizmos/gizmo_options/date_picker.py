"""
********************************************************************************
* Name: date_picker.py
* Author: Nathan Swain and Ezra Rice
* Created On: May 2015
* Copyright: (c) Brigham Young University 2015
* License: BSD 2-Clause
********************************************************************************
"""
from .base import TethysGizmoOptions

__all__ = ['DatePicker']


class DatePicker(TethysGizmoOptions):
    """
    Date pickers are used to make the input of dates streamlined and easy. Rather than typing the date, the user is presented with a calendar to select the date. This date picker was implemented using `Bootstrap Datepicker <http://bootstrap-datepicker.readthedocs.org/en/release/index.html>`_.

    Attributes:
        name (str, required): Name of the input element that will be used for form submission.
        display_text (str): Display text for the label that accompanies date picker.
        autoclose (bool): Set whether datepicker auto closes when a date is selected.
        calendar_weeks (bool): Set whether calendar week numbers are shown on the left of the datepicker.
        clear_button (bool): Set whether the clear button is displayed or not.
        days_of_week_disabled (str): Days of the week that are disabled 0-6 with 0 being Sunday and 6 being Saturday. Multiple days are comma separated (e.g.: '0,6').
        end_date (str): Last date that can be selected. All other dates after this date are shown as disabled.
        format (str): String representing date format. For valid formats see Bootstrap Datepicker documentation `here <http://bootstrap-datepicker.readthedocs.org/en/release/options.html#format>`_.
        min_view_mode (str): Set the minimum view mode. Possible values are 'days', 'months', 'years'.
        multidate (int): Enables multi-selection of dates up to the number given.
        start_date (str): First date that can be selected. All other dates before this date are shown as disabled.
        start_view (str): View the date picker starts on. Valid values include 'month', 'year', and 'decade'.
        today_button (bool): Set whether a today button is displayed or not.
        today_highlight (bool): Set whether to highlight the current date.
        week_start (int): Set the day the week starts on 0-6, where 0 is Sunday and 6 is Saturday.
        initial (str): Initial date to appear in date picker.
        disabled (bool): Disabled state of the date picker.
        error (str): Error message for form validation.
        attributes(dict): A dictionary representing additional HTML attributes to add to the primary element (e.g. {"onclick": "run_me();"}).
        classes(str): Additional classes to add to the primary HTML element (e.g. "example-class another-class").

    Example

    ::

        # CONTROLLER

        from tethys_sdk.gizmos import DatePickerOptions

        # Date Picker Options
        date_picker = DatePicker(name='date1',
                                 display_text='Date',
                                 autoclose=True,
                                 format='MM d, yyyy',
                                 start_date='2/15/2014',
                                 start_view='decade',
                                 today_button=True,
                                 initial='February 15, 2014')

        date_picker_error = DatePicker(name='data2',
                                       display_text='Date',
                                       initial='10/2/2013',
                                       disabled=True,
                                       error='Here is my error text.')

        # TEMPLATE

        {% gizmo date_picker date_picker %}
        {% gizmo date_picker date_picker_error %}

    """

    def __init__(self, name, display_text='', autoclose=False, calendar_weeks=False, clear_button=False,
                 days_of_week_disabled='', end_date='', format='', min_view_mode='days', multidate=1, start_date='',
                 start_view='month', today_button=False, today_highlight=False, week_start=0, initial='',
                 disabled=False, error='', attributes={}, classes=''):
        """
        Constructor
        """
        # Initialize super class
        super(DatePicker, self).__init__(attributes=attributes, classes=classes)

        self.name = name
        self.display_text = display_text
        self.autoclose = autoclose
        self.calendar_weeks = calendar_weeks
        self.clear_button = clear_button
        self.days_of_week_disabled = days_of_week_disabled
        self.end_date = end_date
        self.format = format
        self.min_view_mode = min_view_mode
        self.multidate = multidate
        self.start_date = start_date
        self.start_view = start_view
        self.today_button = today_button
        self.today_highlight = today_highlight
        self.week_start = week_start
        self.initial = initial
        self.disabled = disabled
        self.error = error





