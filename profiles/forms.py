from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')

# 
# class TestForm(forms.Form):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     url = forms.URLField(required=False)
#     comment = forms.CharField(required=True, widget=forms.Textarea)
# 
#     @property
#     def helper(self):
#         helper = FormHelper()
#         helper.form_tag = False # don't render form DOM element
#         helper.render_unmentioned_fields = True # render all fields
#         helper.label_class = 'col-md-2'
#         helper.field_class = 'col-md-10'
#         return helper
# 
