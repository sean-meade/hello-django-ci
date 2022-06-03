from django.test import TestCase
from .forms import ItemForm

# Name must begin with Test
class TestItemForm(TestCase):

    # Use descriptive names for tests for when they fail
    # name must begin with test_
    # self refers to the classs (TestItemForm in this case) which has
    # a bunch of pre-built methods and functionality you can use
    def test_item_name_is_required(self):
        # Simulate a form with no name
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # Check to see if there is a 'name' key in the errors
        self.assertIn('name', form.errors.keys())
        # Check to see if the error is = 'This field is required.'
        # String has to match exactly
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # Check to see the only fields that display in the form are:
        self.assertEqual(form.Meta.fields, ['name', 'done'])

