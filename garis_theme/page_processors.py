# from django import forms
# from django.http import HttpResponseRedirect
# from mezzanine.pages.page_processors import processor_for

# from django.core.mail import send_mail
# from garis_theme.models import (
#     ContactPage,
#     PortfolioPage,
# )

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import (
#     Submit,
#     Reset,
#     Layout, 
#     Field,
#     Div,
# )
# from crispy_forms.bootstrap import (
#     FormActions,
# )
#from captcha.fields import CaptchaField
# from simplemathcaptcha.fields import MathCaptchaField
# from simplemathcaptcha.widgets import MathCaptchaWidget


# class ContactForm(forms.Form):

#     name = forms.CharField()
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea())
#     captcha = MathCaptchaField(
#         error_messages={
#             'invalid': 'Fel svar var god försök igen.',
#             'invalid_number': 'Var god ange heltal endast.',
#             'required': 'Fyll i Captcha fältet', 
#         },
#         widget=MathCaptchaWidget(
#             attrs={'class': 'form-control'},
#             question_tmpl = ('Vad är %(num1)i %(operator)s %(num2)i?')
#         )
#     )

    # helper = FormHelper()
    # helper.form_tag = False
    # helper.form_show_labels = False
    # helper.layout = Layout(
    #     Div(Field('name', placeholder="Namn"), css_class="row"),
    #     Div(Field('email', placeholder="Email"), css_class="row"),
    #     Div(Field('subject', placeholder="Rubrik"), css_class="row"),
    #     Div(Field('message', rows=10), css_class="row"),
    #     Div(Field('captcha'), css_class="row"),
    #     Div(
    #         FormActions(
    #             Submit('Skicka', 'submit', css_class='btn btn-dark big'),
    #             Reset('Ångra', 'reset', css_class='btn btn-dark big')
    #         ),
    #         css_class="row",
    #     ),
    # )


# @processor_for(ContactPage)
# def author_form(request, page):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Form processing goes here.
#             message = "{name} / {email} said: ".format(
#                 name=form.cleaned_data.get('name', ''),
#                 email=form.cleaned_data.get('email', '')
#             )
#             message += "\n\n{0}".format(form.cleaned_data.get('message', ''))
#             send_mail(
#                 subject=form.cleaned_data.get('subject', '').strip(),
#                 message=message,
#                 from_email='contact-form@myapp.com',
#                 recipient_list=['jonatan.doherty.work@gmail.com'],
#             )

#             redirect = request.path + "?submitted=true"
#             return HttpResponseRedirect(redirect)
#     return {"form": form}


